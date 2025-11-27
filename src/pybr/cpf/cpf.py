from pybr.common.base import BaseDocument


class CPF(BaseDocument):
    
    @staticmethod
    def clean(value: str) -> str:
        """
        Removes all non-digit characters.
        Returns empty string if input is None.
        """
        if not value:
            return ""

        return "".join(filter(str.isdigit, value))

    @staticmethod
    def format(value: str) -> str | None:
        """
        Applies standard masking: XXX.XXX.XXX-XX
        Returns None if the cleaned value is not exactly 11 digits.
        """
        clean_value = CPF.clean(value)
        if len(clean_value) != 11:
            return None
        
        return f"{clean_value[:3]}.{clean_value[3:6]}.{clean_value[6:9]}-{clean_value[9:]}"

    @staticmethod
    def is_valid(value: str, allow_repeated: bool = False, **kwargs) -> bool:
        """
        Validates CPF using the Mod11 algorithm.
        1. Checks length (11 digits).
        2. Checks for known repeated sequences (111.111.111-11) by default. Can be overridden with allow_repeated=True.
        3. Validates checksum digits.
        """
        cpf = CPF.clean(value)

        if len(cpf) != 11:
            return False

        if not allow_repeated and len(set(cpf)) == 1:
            return False

        try:
            numbers = [int(digit) for digit in cpf]
        except ValueError:
            return False

        first_digit = CPF.__calculate_digit(numbers[:9])
        if first_digit != numbers[9]:
            return False

        second_digit = CPF.__calculate_digit(numbers[:10])
        if second_digit != numbers[10]:
            return False

        return True

    # We override the base method here to explicitly pass the allow_repeated flag.
    @classmethod
    def validate(cls, value: str, allow_repeated: bool = False, **kwargs) -> None:
        """
        Enforcement wrapper.
        Raises ValueError if invalid.
        """
        super().validate(value, allow_repeated=allow_repeated, **kwargs)

    @staticmethod
    def __calculate_digit(digits: list[int]) -> int:
        """
        Optimized Mod11 calculation for CPF checksum digits.
        """
        weight = len(digits) + 1
        
        total = sum(digit * (weight - idx) for idx, digit in enumerate(digits))
        
        remainder = total % 11
        return 0 if remainder < 2 else 11 - remainder