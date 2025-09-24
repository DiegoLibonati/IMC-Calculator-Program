import logging

import pytest

from src.utils.helpers import calculate_imc, get_imc_status
from src.utils.messages import (
    MESSAGE_ERROR_INVALID_VALUES,
    MESSAGE_NORMAL,
    MESSAGE_OBESITY,
    MESSAGE_OVERWEIGHT,
    MESSAGE_THIN,
)

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


@pytest.mark.parametrize(
    "weight, height, expected_status",
    [
        ("50", "180", MESSAGE_THIN),  # IMC < 20
        ("70", "175", MESSAGE_NORMAL),  # IMC normal
        ("85", "180", MESSAGE_OVERWEIGHT),  # IMC entre 26 y 30
        ("120", "170", MESSAGE_OBESITY),  # IMC > 30
    ],
)
def test_calculate_imc_valid_cases(weight, height, expected_status):
    result, message = calculate_imc(weight, height)
    assert isinstance(result, float)
    assert message == expected_status


def test_calculate_imc_invalid_values():
    result, message = calculate_imc("abc", "180")
    assert result is None
    assert message == MESSAGE_ERROR_INVALID_VALUES


def test_get_imc_status_ranges():
    assert get_imc_status(18) == MESSAGE_THIN
    assert get_imc_status(22) == MESSAGE_NORMAL
    assert get_imc_status(28) == MESSAGE_OVERWEIGHT
    assert get_imc_status(35) == MESSAGE_OBESITY
