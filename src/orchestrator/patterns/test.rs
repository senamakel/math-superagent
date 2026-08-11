//! Unit tests for the deterministic sequence-analysis tools.
#![allow(clippy::expect_used)]

use super::{Frac, analyze, detect_periodicity, difference_table, find_recurrence, render_recurrence};

#[test]
fn constant_differences_identify_a_polynomial() {
    let table = difference_table(&[1, 4, 9, 16, 25, 36]);
    assert_eq!(table[0], vec![3, 5, 7, 9, 11]);
    assert!(table[1].windows(2).all(|pair| pair[0] == pair[1]));
    assert_eq!(table[1][0], 2);
}

#[test]
fn fibonacci_recurrence_is_recovered_exactly() {
    let fib = [1_i128, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144];
    let found = find_recurrence(&fib, 6).expect("fibonacci has an order-2 recurrence");
    assert_eq!(found.len(), 2);
    assert_eq!(found[0], Frac::integer(1));
    assert_eq!(found[1], Frac::integer(1));
    assert!(render_recurrence(&found).contains("a(n-1)"));
}

#[test]
fn geometric_sequences_are_order_one() {
    let powers = [1_i128, 3, 9, 27, 81, 243, 729];
    let found = find_recurrence(&powers, 4).expect("powers of three are order one");
    assert_eq!(found.len(), 1);
    assert_eq!(found[0], Frac::integer(3));
}

#[test]
fn a_sequence_with_no_linear_recurrence_reports_none() {
    let factorials = [1_i128, 1, 2, 6, 24, 120, 720, 5040];
    assert!(find_recurrence(&factorials, 3).is_none());
}

#[test]
fn periodicity_is_detected_in_residues() {
    let (modulus, period) = detect_periodicity(&[1, 2, 3, 4, 5, 6, 7, 8]).expect("parity repeats");
    assert_eq!(modulus, 2);
    assert_eq!(period, 2);
}

#[test]
fn rational_arithmetic_reduces_and_rejects_zero_denominators() {
    assert!(Frac::new(1, 0).is_none());
    let half = Frac::new(2, 4).expect("2/4 is valid");
    assert_eq!(half.render(), "1/2");
    let sum = half.add(half).expect("1/2 + 1/2");
    assert_eq!(sum, Frac::integer(1));
}

#[test]
fn analysis_never_claims_a_pattern_is_proved() {
    let report = analyze(&[1, 4, 9, 16, 25]);
    assert!(report.contains("degree-2"));
    assert!(report.to_lowercase().contains("not a proof"));
}
