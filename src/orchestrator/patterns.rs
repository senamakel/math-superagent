//! Deterministic sequence-analysis tools for the pattern-recognition agent.
//!
//! These are calculators, not heuristics: every answer is exact integer or
//! rational arithmetic, and a claim is only made when it holds for every term
//! supplied. A model asked to "spot the pattern" by eye will confabulate a
//! closed form that fits the first few terms; these tools instead report what
//! is verifiably true of the whole sequence, which is what turns an observed
//! regularity into something worth trying to prove.

use std::fmt::Write as _;

use async_trait::async_trait;
use serde_json::{Value, json};

use crate::agent::{Result, Tool, ToolCall, ToolResult, ToolSchema};

/// Largest number of terms accepted, bounding the cubic elimination cost.
const MAX_TERMS: usize = 512;
/// Largest recurrence order searched by `find_linear_recurrence`.
const MAX_RECURRENCE_ORDER: usize = 12;
/// Largest modulus probed for periodicity.
const MAX_MODULUS: i128 = 24;

/// An exact rational over `i128`, reduced on construction.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
struct Frac {
    numerator: i128,
    denominator: i128,
}

impl Frac {
    fn new(numerator: i128, denominator: i128) -> Option<Self> {
        if denominator == 0 {
            return None;
        }
        let sign = if denominator < 0 { -1 } else { 1 };
        let divisor = gcd(numerator.abs(), denominator.abs()).max(1);
        Some(Self {
            numerator: sign * (numerator / divisor),
            denominator: sign * (denominator / divisor),
        })
    }

    fn integer(value: i128) -> Self {
        Self {
            numerator: value,
            denominator: 1,
        }
    }

    fn zero() -> Self {
        Self::integer(0)
    }

    fn is_zero(self) -> bool {
        self.numerator == 0
    }

    fn add(self, other: Self) -> Option<Self> {
        let numerator = self
            .numerator
            .checked_mul(other.denominator)?
            .checked_add(other.numerator.checked_mul(self.denominator)?)?;
        Self::new(numerator, self.denominator.checked_mul(other.denominator)?)
    }

    fn sub(self, other: Self) -> Option<Self> {
        self.add(Self {
            numerator: -other.numerator,
            denominator: other.denominator,
        })
    }

    fn mul(self, other: Self) -> Option<Self> {
        Self::new(
            self.numerator.checked_mul(other.numerator)?,
            self.denominator.checked_mul(other.denominator)?,
        )
    }

    fn div(self, other: Self) -> Option<Self> {
        if other.is_zero() {
            return None;
        }
        Self::new(
            self.numerator.checked_mul(other.denominator)?,
            self.denominator.checked_mul(other.numerator)?,
        )
    }

    fn render(self) -> String {
        if self.denominator == 1 {
            self.numerator.to_string()
        } else {
            format!("{}/{}", self.numerator, self.denominator)
        }
    }
}

fn gcd(a: i128, b: i128) -> i128 {
    let (mut a, mut b) = (a.abs(), b.abs());
    while b != 0 {
        let remainder = a % b;
        a = b;
        b = remainder;
    }
    a
}

/// Returns the forward-difference table until it becomes constant.
///
/// A sequence whose `d`-th differences are constant and non-trivial is a
/// polynomial of degree `d` in its index, which is the single most useful fact
/// about a counting sequence.
fn difference_table(terms: &[i128]) -> Vec<Vec<i128>> {
    let mut rows = Vec::new();
    let mut current = terms.to_vec();
    while current.len() > 1 && rows.len() < MAX_RECURRENCE_ORDER {
        let next: Vec<i128> = current
            .windows(2)
            .map(|pair| pair[1].saturating_sub(pair[0]))
            .collect();
        let constant = next.windows(2).all(|pair| pair[0] == pair[1]);
        rows.push(next.clone());
        if constant {
            break;
        }
        current = next;
    }
    rows
}

/// Returns the smallest modulus in `2..=MAX_MODULUS` under which the residues
/// repeat with a period shorter than the sequence, with that period.
fn detect_periodicity(terms: &[i128]) -> Option<(i128, usize)> {
    for modulus in 2..=MAX_MODULUS {
        let residues: Vec<i128> = terms.iter().map(|term| term.rem_euclid(modulus)).collect();
        for period in 1..=residues.len() / 2 {
            if residues
                .iter()
                .enumerate()
                .all(|(index, value)| *value == residues[index % period])
            {
                return Some((modulus, period));
            }
        }
    }
    None
}

/// Searches for the shortest linear recurrence with constant rational
/// coefficients satisfied by every supplied term.
///
/// Solves the exact linear system by Gaussian elimination over rationals, then
/// re-checks the candidate against every term. Returning only a verified
/// recurrence is the point: an unverified fit is a guess, and a guess is what
/// the agent would have produced without this tool.
fn find_recurrence(terms: &[i128], max_order: usize) -> Option<Vec<Frac>> {
    for order in 1..=max_order.min(terms.len() / 2) {
        let equations = terms.len() - order;
        if equations < order {
            continue;
        }
        let mut matrix: Vec<Vec<Frac>> = (0..equations)
            .map(|row| {
                let mut coefficients: Vec<Frac> = (0..order)
                    .map(|column| Frac::integer(terms[row + order - 1 - column]))
                    .collect();
                coefficients.push(Frac::integer(terms[row + order]));
                coefficients
            })
            .collect();

        if let Some(solution) = solve(&mut matrix, order)
            && verifies(terms, &solution)
        {
            return Some(solution);
        }
    }
    None
}

/// Solves an over-determined rational system by Gaussian elimination, returning
/// `None` when it is inconsistent or rank-deficient.
fn solve(matrix: &mut [Vec<Frac>], unknowns: usize) -> Option<Vec<Frac>> {
    let rows = matrix.len();
    let mut pivot_row = 0;
    let mut pivot_of_column = vec![None; unknowns];

    for column in 0..unknowns {
        let pivot = (pivot_row..rows).find(|row| !matrix[*row][column].is_zero())?;
        matrix.swap(pivot_row, pivot);
        let divisor = matrix[pivot_row][column];
        for value in &mut matrix[pivot_row][column..=unknowns] {
            *value = value.div(divisor)?;
        }
        for row in 0..rows {
            if row == pivot_row || matrix[row][column].is_zero() {
                continue;
            }
            let factor = matrix[row][column];
            let pivot_values: Vec<Frac> = matrix[pivot_row][column..=unknowns].to_vec();
            for (value, pivot_value) in matrix[row][column..=unknowns].iter_mut().zip(pivot_values)
            {
                *value = value.sub(pivot_value.mul(factor)?)?;
            }
        }
        pivot_of_column[column] = Some(pivot_row);
        pivot_row += 1;
        if pivot_row == rows {
            break;
        }
    }

    // Any all-zero coefficient row with a non-zero constant makes the system
    // inconsistent, so no recurrence of this order exists.
    for row in matrix.iter() {
        if row[..unknowns].iter().all(|value| value.is_zero()) && !row[unknowns].is_zero() {
            return None;
        }
    }

    pivot_of_column
        .into_iter()
        .map(|pivot| pivot.map(|row| matrix[row][unknowns]))
        .collect()
}

/// Confirms a candidate recurrence reproduces every term it should.
fn verifies(terms: &[i128], coefficients: &[Frac]) -> bool {
    let order = coefficients.len();
    (order..terms.len()).all(|index| {
        let predicted = coefficients.iter().enumerate().try_fold(
            Frac::zero(),
            |accumulator, (offset, coefficient)| {
                let term = Frac::integer(terms[index - 1 - offset]);
                accumulator.add(coefficient.mul(term)?)
            },
        );
        predicted == Some(Frac::integer(terms[index]))
    })
}

fn render_recurrence(coefficients: &[Frac]) -> String {
    let terms = coefficients
        .iter()
        .enumerate()
        .filter(|(_, coefficient)| !coefficient.is_zero())
        .map(|(offset, coefficient)| format!("({}) * a(n-{})", coefficient.render(), offset + 1))
        .collect::<Vec<_>>();
    if terms.is_empty() {
        "a(n) = 0".to_string()
    } else {
        format!("a(n) = {}", terms.join(" + "))
    }
}

/// The pattern tools exposed to the pattern-recognition agent.
#[derive(Clone, Copy, Debug)]
pub(super) enum PatternToolKind {
    /// Structural summary of a sequence.
    Analyze,
    /// Exact linear-recurrence search.
    Recurrence,
}

impl PatternToolKind {
    pub(super) const ALL: [Self; 2] = [Self::Analyze, Self::Recurrence];
}

/// A deterministic sequence-analysis tool.
#[derive(Clone, Copy, Debug)]
pub(super) struct PatternTool {
    kind: PatternToolKind,
}

impl PatternTool {
    pub(super) fn all() -> Vec<std::sync::Arc<dyn Tool<()>>> {
        PatternToolKind::ALL
            .into_iter()
            .map(|kind| std::sync::Arc::new(Self { kind }) as std::sync::Arc<dyn Tool<()>>)
            .collect()
    }
}

#[async_trait]
impl Tool<()> for PatternTool {
    fn name(&self) -> &'static str {
        match self.kind {
            PatternToolKind::Analyze => "analyze_sequence",
            PatternToolKind::Recurrence => "find_linear_recurrence",
        }
    }

    fn description(&self) -> &'static str {
        match self.kind {
            PatternToolKind::Analyze => {
                "Reports exact structural facts about an integer sequence: forward differences and \
                 polynomial degree, growth ratios, common divisor, and periodicity of residues."
            }
            PatternToolKind::Recurrence => {
                "Finds the shortest constant-coefficient linear recurrence satisfied by every term, \
                 by exact rational elimination, or reports that none exists up to the order tried."
            }
        }
    }

    fn schema(&self) -> ToolSchema {
        let terms = json!({
            "type": "array",
            "description": "Integer terms in order, as numbers or decimal strings.",
            "items": { "type": ["integer", "string"] },
            "minItems": 3,
            "maxItems": MAX_TERMS
        });
        let parameters = match self.kind {
            PatternToolKind::Analyze => json!({
                "type": "object",
                "properties": { "terms": terms },
                "required": ["terms"],
                "additionalProperties": false
            }),
            PatternToolKind::Recurrence => json!({
                "type": "object",
                "properties": {
                    "terms": terms,
                    "max_order": {
                        "type": "integer",
                        "minimum": 1,
                        "maximum": MAX_RECURRENCE_ORDER,
                        "description": "Highest recurrence order to try."
                    }
                },
                "required": ["terms"],
                "additionalProperties": false
            }),
        };
        ToolSchema::new(self.name(), self.description(), parameters)
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        self.schema().validate_call(&call)?;
        let terms = parse_terms(&call.arguments)?;
        let report = match self.kind {
            PatternToolKind::Analyze => analyze(&terms),
            PatternToolKind::Recurrence => {
                let max_order = call
                    .arguments
                    .get("max_order")
                    .and_then(Value::as_u64)
                    .and_then(|value| usize::try_from(value).ok())
                    .unwrap_or(MAX_RECURRENCE_ORDER)
                    .min(MAX_RECURRENCE_ORDER);
                match find_recurrence(&terms, max_order) {
                    Some(coefficients) => format!(
                        "Verified linear recurrence of order {}:\n  {}\nIt reproduces every one of \
                         the {} supplied terms exactly. This is an observed regularity over the \
                         terms given, not a proof that it continues; prove it or derive it before \
                         relying on it.",
                        coefficients.len(),
                        render_recurrence(&coefficients),
                        terms.len()
                    ),
                    None => format!(
                        "No constant-coefficient linear recurrence of order {max_order} or less \
                         fits all {} terms. Consider a non-linear relation, polynomial \
                         coefficients, or a different indexing of the sequence.",
                        terms.len()
                    ),
                }
            }
        };
        Ok(ToolResult::text(call.id, self.name(), report))
    }
}

fn parse_terms(arguments: &Value) -> Result<Vec<i128>> {
    let raw = arguments
        .get("terms")
        .and_then(Value::as_array)
        .ok_or_else(|| {
            tinyagents::TinyAgentsError::Validation("terms must be an array".to_string())
        })?;
    if raw.len() > MAX_TERMS {
        return Err(tinyagents::TinyAgentsError::Validation(format!(
            "at most {MAX_TERMS} terms are accepted"
        )));
    }
    raw.iter()
        .map(|value| match value {
            Value::Number(number) => number.as_i64().map(i128::from).ok_or_else(|| {
                tinyagents::TinyAgentsError::Validation(format!(
                    "term `{number}` is not an integer"
                ))
            }),
            Value::String(text) => text.trim().parse::<i128>().map_err(|_| {
                tinyagents::TinyAgentsError::Validation(format!("term `{text}` is not an integer"))
            }),
            other => Err(tinyagents::TinyAgentsError::Validation(format!(
                "term `{other}` is not an integer"
            ))),
        })
        .collect()
}

fn analyze(terms: &[i128]) -> String {
    let mut report = format!("{} terms: {:?}\n", terms.len(), preview_terms(terms));

    let table = difference_table(terms);
    let polynomial_degree = table.iter().position(|row| {
        row.len() > 1 && row.windows(2).all(|pair| pair[0] == pair[1]) && row[0] != 0
    });
    match polynomial_degree {
        Some(index) => {
            let _ = writeln!(
                report,
                "Polynomial: the differences become constant at level {}, so the terms fit a \
                 degree-{} polynomial in the index (constant difference {}).",
                index + 1,
                index + 1,
                table[index][0]
            );
        }
        None => {
            let _ = writeln!(
                report,
                "Polynomial: differences do not become constant within {} levels, so this is not \
                 a low-degree polynomial.",
                table.len()
            );
        }
    }
    for (level, row) in table.iter().take(3).enumerate() {
        let _ = writeln!(
            report,
            "  level {} differences: {:?}",
            level + 1,
            preview_terms(row)
        );
    }

    let divisor = terms
        .iter()
        .fold(0, |accumulator, term| gcd(accumulator, *term));
    if divisor > 1 {
        let _ = writeln!(
            report,
            "Common divisor: every term is divisible by {divisor}."
        );
    }

    if let Some((modulus, period)) = detect_periodicity(terms) {
        let _ = writeln!(
            report,
            "Periodicity: residues modulo {modulus} repeat with period {period}."
        );
    }

    let ratios: Vec<String> = terms
        .windows(2)
        .take(5)
        .map(|pair| {
            if pair[0] == 0 {
                "undefined".to_string()
            } else {
                #[allow(clippy::cast_precision_loss)]
                let ratio = pair[1] as f64 / pair[0] as f64;
                format!("{ratio:.4}")
            }
        })
        .collect();
    let _ = writeln!(report, "Leading ratios: {}", ratios.join(", "));

    report.push_str(
        "\nEvery statement above is exact over the terms supplied. None of it is a proof that the \
         pattern continues; treat it as a conjecture to derive or refute.",
    );
    report
}

fn preview_terms(terms: &[i128]) -> Vec<i128> {
    terms.iter().copied().take(12).collect()
}

#[cfg(test)]
mod test;
