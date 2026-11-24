def required(value, label):
    value = str(value).strip()
    if not value:
        raise ValueError(f"{label} is required.")
    return value

def positive_number(value, label, allow_zero=False):
    try:
        number = float(value)
    except (TypeError, ValueError):
        raise ValueError(f"{label} must be a number.")
    if number < 0 or (number == 0 and not allow_zero):
        rule = "zero or greater" if allow_zero else "greater than zero"
        raise ValueError(f"{label} must be {rule}.")
    return number
