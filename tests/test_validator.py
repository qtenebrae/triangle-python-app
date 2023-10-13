from src.Validator import Validator


def test_validate_int():
    validator = Validator()
    assert validator.validate_int("123") == True
    assert validator.validate_int("abc") == False
    assert validator.validate_int("1.23") == False
