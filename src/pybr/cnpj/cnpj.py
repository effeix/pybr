from pybr.common.base import BaseDocument

class CNPJ(BaseDocument):
    # Pre-calculated first digit weights (applied to first 12 chars)
    __WEIGHTS_1 = (5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)
    
    # Pre-calculated second digit weights (applied to first 13 chars)
    __WEIGHTS_2 = (6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)

    @staticmethod
    def clean(value: str) -> str:
        """
        Removes punctuation. Keeps alphanumeric characters (0-9, A-Z) (2026+ compatible).
        Forces uppercase for consistency.
        Returns empty string if input is None.
        """
        if not value:
            return ""

        return "".join(char for char in value.upper() if char.isalnum())

    @staticmethod
    def format(value: str) -> str | None:
        """
        Applies standard masking: XX.XXX.XXX/XXXX-XX
        Returns None if the cleaned value is not exactly 14 characters.
        """
        clean_value = CNPJ.clean(value)
        if len(clean_value) != 14:
            return None
        
        return (f"{clean_value[:2]}.{clean_value[2:5]}.{clean_value[5:8]}/"
                f"{clean_value[8:12]}-{clean_value[12:]}")

    @staticmethod 
    def is_valid(value: str) -> bool:
        """
        Validates CNPJ using the alphanumeric standard (2026+ compatible).

        Reference: https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/documentos-tecnicos/cnpj
        """
        cnpj = CNPJ.clean(value)

        if len(cnpj) != 14:
            return False

        if len(set(cnpj)) == 1:
            return False

        try:
            numbers = [ord(char) - 48 for char in cnpj]
        except ValueError:
            return False

        first_digit = CNPJ._calculate_digit(numbers[:12], CNPJ.__WEIGHTS_1)
        if first_digit != numbers[12]: 
            return False

        second_digit = CNPJ._calculate_digit(numbers[:13], CNPJ.__WEIGHTS_2)
        if second_digit != numbers[13]:
            return False

        return True

    @staticmethod
    def _calculate_digit(numbers: list[int], weights: tuple[int, ...]) -> int:
        """
        Optimized Mod11 calculation for CNPJ checksum digits.
        """
        total = sum(n * w for n, w in zip(numbers, weights))
        
        remainder = total % 11
        digit = 0 if remainder < 2 else 11 - remainder
        
        return digit