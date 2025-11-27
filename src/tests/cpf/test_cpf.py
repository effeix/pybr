import pytest
from pybr import CPF

class TestCPF:
    
    VALID_CPF_CASES = [
        "52998224725", 
        "06099629815", 
        "50025673807", 
    ]
    
    @pytest.mark.parametrize(
        "cpf, expected",
        [
            ("123.456.789-00", "12345678900"), # Standard case
            ("12345678900", "12345678900"),    # Already clean
            ("abc", ""),                       # No digits
            ("1a2b3c", "123"),                 # Mixed garbage
            ("", ""),                          # Empty string
            (None, ""),                        # None handling (critical for pipelines)
            ("   ", ""),                       # Whitespace
        ]
    )
    def test_clean_leaves_digits_only(self, cpf, expected):
        """Ensure inputs are stripped to digits only, handling None/Empty gracefully."""
        assert CPF.clean(cpf) == expected

    @pytest.mark.parametrize(
        "cpf, expected",
        [
            ("12345678900", "123.456.789-00"),    # Happy path
            ("123.456.789-00", "123.456.789-00"), # Idempotency (already formatted)
            ("123", None),                        # Too short
            ("123456789000", None),               # Too long
            (None, None),                         # None input
            ("abcdefghijk", None),                # Correct length, wrong content
        ]
    )
    def test_format(self, cpf, expected):
        """Ensure formatting adheres to standard mask or returns None."""
        assert CPF.format(cpf) == expected

    @pytest.mark.parametrize("cpf", VALID_CPF_CASES)
    def test_is_valid(self, cpf):
        """Test mathematically correct CPFs."""
        assert CPF.is_valid(cpf) is True
        
        assert CPF.is_valid(f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}") is True

    @pytest.mark.parametrize(
        "cpf",
        [
            "11111111111",   # Repeated digits
            "22222222222",   # Repeated digits
            "12345678900",   # Invalid Checksum (Math fail)
            "52998224720",   # Valid stem, wrong check digit
            "123",           # Too short
            "1234567890123", # Too long
            "",              # Empty
            None,            # None
            "abcdefghijk",   # Non-digit length 11
        ]
    )
    def test_is_valid_failures(self, cpf):
        """Test inputs that must fail strict validation."""
        assert CPF.is_valid(cpf) is False

    @pytest.mark.parametrize(
        "cpf, allow_repeated, expected",
        [
            ("11111111111", False, False), # Default secure behavior
            ("11111111111", True, True),   # Insecure toggle enabled (Checksum is valid for 111...)
        ]
    )
    def test_allow_repeated_toggle(self, cpf, allow_repeated, expected):
        """Ensure the repeated digit toggle functions correctly."""
        assert CPF.is_valid(cpf, allow_repeated=allow_repeated) is expected

    def test_validate_raises_error(self):
        """Ensure validate() raises ValueError on bad inputs."""
        with pytest.raises(ValueError) as excinfo:
            CPF.validate("123")
        
        assert "Invalid CPF" in str(excinfo.value)

    def test_validate_silent_success(self):
        """Ensure validate() returns None (no error) on good input."""
        valid_cpf = "52998224725"
        
        assert CPF.validate(valid_cpf) is None

    def test_unexpected_types(self):
        """
        How does the lib behave if a user passes an integer or object?
        
        Design Choice: 
        The current implementation expects strings/iterables in 'filter'.
        Passing an int (123456) to filter(str.isdigit, 123456) raises TypeError.
        We assert this happens to ensure we don't silently fail.
        """
        with pytest.raises(TypeError):
            CPF.clean(12345678900) # type: ignore 

        # However, is_valid catches ValueError during int conversion, 
        # but what about earlier steps?
        # If we pass an int to is_valid, it hits clean() -> TypeError.
        with pytest.raises(TypeError):
            CPF.is_valid(12345678900) # type: ignore