import logging
from pathlib import Path
from typing import Union

# Путь относительно текущего файла
current_dir = Path(__file__).parent  # Директория текущего скрипта
file_path = current_dir.parent / "logs" / "masks.log"  # Поднимаемся вверх и ищем файл

# Абсолютный путь
absolute_path = file_path.resolve()

logger = logging.getLogger("masks")  # Создание объекта логгера для модуля masks
file_handler = logging.FileHandler(filename=absolute_path, mode="w", encoding="UTF-8")  # Настраиваем хэндлер для файла
file_formatter = logging.Formatter(
    fmt="%(asctime)s %(filename)s, %(levelname)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)  # Настраиваем форматер
file_handler.setFormatter(file_formatter)  # Устанавливаем форматер
logger.addHandler(file_handler)  # Добавляем хэндлер в логер
logger.setLevel(logging.DEBUG)  # Устанавливаем уровень логирования


# Определяем функцию get_mask_card_number для маскирования номера карты
def get_mask_card_number(card_number: Union[str, int]) -> str:
    """Маскирует номера карты, оставляя видимыми первые 6 и последние 4 цифры номера карты"""
    card_number = str(card_number)
    clean_number = card_number.replace(" ", "")
    if len(clean_number) != 16 or not clean_number.isdigit():
        raise ValueError("Номер карты должен содержать 16 цифр")
    first_part: str = clean_number[:6]
    hidden_part: str = "** ****"
    last_part: str = clean_number[-4:]
    masked_number = f"{first_part[:4]} {first_part[4:6]}{hidden_part} {last_part}"
    return masked_number


# Определяем функцию get_mask_card_account для маскирования номера счёта
def get_mask_account(account_number: Union[str, int]) -> str:
    """Маскирует номера счёта, оставляя видимыми последние 4 цифры номера счёте и вставляет перед ними "**"."""
    account_number = str(account_number)
    if len(account_number) != 20 or not account_number.isdigit():
        raise ValueError("Номер карты должен содержать 20 цифр")
    hidden_part: str = "**"
    masked_number: str = f"{hidden_part}{account_number[-4:]}"
    return masked_number
