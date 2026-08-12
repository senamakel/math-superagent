fn required_string(arguments: &Value, name: &str) -> Result<String> {
    string_value(arguments, name).and_then(|value| {
        if value.trim().is_empty() {
            Err(tinyagents::TinyAgentsError::Validation(format!(
                "{name} must be a non-empty string"
            )))
        } else {
            Ok(value)
        }
    })
}

fn string_value(arguments: &Value, name: &str) -> Result<String> {
    arguments
        .get(name)
        .and_then(Value::as_str)
        .map(ToOwned::to_owned)
        .ok_or_else(|| tinyagents::TinyAgentsError::Validation(format!("{name} must be a string")))
}

fn floor_char_boundary(text: &str, mut index: usize) -> usize {
    while index > 0 && !text.is_char_boundary(index) {
        index -= 1;
    }
    index
}

fn ceil_char_boundary(text: &str, mut index: usize) -> usize {
    while index < text.len() && !text.is_char_boundary(index) {
        index += 1;
    }
    index
}
