from src.constants.messages import (
    MESSAGE_NORMAL,
    MESSAGE_NOT_VALID_FIELDS,
    MESSAGE_OBESITY,
    MESSAGE_OVERWEIGHT,
    MESSAGE_THIN,
)


def calculate_imc(weight: str, height: str) -> tuple[float | None, str]:
    try:
        weight_value = int(weight)
        height_value = int(height)

        height_in_mts = height_value / 100
        bmi = weight_value / (height_in_mts * height_in_mts)
        result = round(bmi, 2)

        return result, get_imc_status(result)

    except Exception:
        return None, MESSAGE_NOT_VALID_FIELDS


def get_imc_status(result: float) -> str:
    if result < 20:
        return MESSAGE_THIN
    elif 20 <= result <= 25:
        return MESSAGE_NORMAL
    elif 26 <= result <= 30:
        return MESSAGE_OVERWEIGHT
    return MESSAGE_OBESITY
