from .bot_start import dp
from .server_management import dp
from .error import dp # Все хендлеры ставим выше этого! Иначе он не будет их обрабатывать!
__all__ = ['dp']