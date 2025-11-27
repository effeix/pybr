from abc import ABC, abstractmethod
from typing import Optional

class BaseDocument(ABC):
    """
    Abstract Interface for all document validators.
    """

    @staticmethod
    @abstractmethod
    def clean(value: str) -> str:
        """
        Removes all characters not relevant to the validation logic.
        Must handle None/Empty strings by returning empty string.
        """
        ...

    @staticmethod
    @abstractmethod
    def format(value: str) -> Optional[str]:
        """
        Applies the standard display mask.
        Returns None if the value is structurally invalid (wrong length).
        """
        ...

    @staticmethod
    @abstractmethod
    def is_valid(value: str, **kwargs) -> bool:
        """
        Validates the document mathematically (checksums).
        Accepts **kwargs to allow document-specific flags (e.g., strict modes).
        """
        ...

    @classmethod
    def validate(cls, value: str, **kwargs) -> None:
        """
        Enforcement wrapper.
        Raises ValueError if invalid. 
        
        Subclasses do not need to override this unless they need custom exception logic.
        """
        if not cls.is_valid(value, **kwargs):
            raise ValueError(f"Invalid {cls.__name__}: {value}")