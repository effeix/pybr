from .cnpj.cnpj import CNPJ
from .cpf.cpf import CPF

try:
    from ._version import __version__
except ImportError:
    # This handles the case where the code is run directly from source 
    # without being installed/built (e.g., during local dev without editable install)
    __version__ = "0.0.0+unknown"

# Now users can do: print(pybr.__version__)

__all__ = ["CPF", "CNPJ"]
