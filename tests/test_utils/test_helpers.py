import pytest

from src.constants.messages import (
    MESSAGE_NORMAL,
    MESSAGE_NOT_VALID_FIELDS,
    MESSAGE_OBESITY,
    MESSAGE_OVERWEIGHT,
    MESSAGE_THIN,
)
from src.utils.helpers import calculate_imc, get_imc_status


@pytest.mark.unit
class TestGetImcStatus:
    @pytest.mark.parametrize(
        "result,expected",
        [
            (19.9, MESSAGE_THIN),
            (0.0, MESSAGE_THIN),
            (20.0, MESSAGE_NORMAL),
            (22.5, MESSAGE_NORMAL),
            (25.0, MESSAGE_NORMAL),
            (26.0, MESSAGE_OVERWEIGHT),
            (28.0, MESSAGE_OVERWEIGHT),
            (30.0, MESSAGE_OVERWEIGHT),
            (30.1, MESSAGE_OBESITY),
            (40.0, MESSAGE_OBESITY),
        ],
    )
    def test_returns_correct_status(self, result: float, expected: str) -> None:
        assert get_imc_status(result) == expected


@pytest.mark.unit
class TestCalculateImc:
    def test_returns_normal_bmi_for_valid_input(self) -> None:
        result, message = calculate_imc("70", "170")

        assert result == pytest.approx(24.22)
        assert message == MESSAGE_NORMAL

    def test_returns_thin_status_for_low_weight(self) -> None:
        result, message = calculate_imc("50", "170")

        assert result is not None
        assert result < 20
        assert message == MESSAGE_THIN

    def test_returns_overweight_status_for_high_weight(self) -> None:
        result, message = calculate_imc("85", "170")

        assert result is not None
        assert 26 <= result <= 30
        assert message == MESSAGE_OVERWEIGHT

    def test_returns_obesity_status_for_very_high_weight(self) -> None:
        result, message = calculate_imc("100", "170")

        assert result is not None
        assert result > 30
        assert message == MESSAGE_OBESITY

    def test_returns_none_for_empty_weight(self) -> None:
        result, message = calculate_imc("", "170")

        assert result is None
        assert message == MESSAGE_NOT_VALID_FIELDS

    def test_returns_none_for_empty_height(self) -> None:
        result, message = calculate_imc("70", "")

        assert result is None
        assert message == MESSAGE_NOT_VALID_FIELDS

    def test_returns_none_for_non_numeric_weight(self) -> None:
        result, message = calculate_imc("abc", "170")

        assert result is None
        assert message == MESSAGE_NOT_VALID_FIELDS

    def test_returns_none_for_non_numeric_height(self) -> None:
        result, message = calculate_imc("70", "abc")

        assert result is None
        assert message == MESSAGE_NOT_VALID_FIELDS

    def test_returns_none_for_zero_height(self) -> None:
        result, message = calculate_imc("70", "0")

        assert result is None
        assert message == MESSAGE_NOT_VALID_FIELDS
