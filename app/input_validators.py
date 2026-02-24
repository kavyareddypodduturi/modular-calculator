from app.exceptions import InvalidInputError


def validate_numbers(a: str, b: str):
    """
    Validate and convert input values to floats.
    Demonstrates both LBYL and EAFP.
    """

    # LBYL (Look Before You Leap)
    if not a or not b:
        raise InvalidInputError("Inputs cannot be empty")

    # EAFP (Easier to Ask Forgiveness than Permission)
    try:
        num1 = float(a)
        num2 = float(b)
    except ValueError:
        raise InvalidInputError("Inputs must be numeric")

    return num1, num2