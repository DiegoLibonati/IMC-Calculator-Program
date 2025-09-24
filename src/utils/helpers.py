from src.utils.messages import (
    MESSAGE_ERROR_INVALID_VALUES,
    MESSAGE_NORMAL,
    MESSAGE_OBESITY,
    MESSAGE_OVERWEIGHT,
    MESSAGE_THIN,
)


def calculate_imc(weight: str, height: str) -> tuple[float | None, str]:
    try:
        weight = int(weight)
        height = int(height)

        height_in_mts = height / 100
        imc = weight / (height_in_mts * height_in_mts)
        result = round(imc, 2)

        return result, get_imc_status(result)

    except Exception:
        return None, MESSAGE_ERROR_INVALID_VALUES


def get_imc_status(result: float) -> str:
    if result < 20:
        return MESSAGE_THIN
    elif 20 <= result <= 25:
        return MESSAGE_NORMAL
    elif 26 <= result <= 30:
        return MESSAGE_OVERWEIGHT
    return MESSAGE_OBESITY
