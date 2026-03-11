from src.constants.messages import (
    MESSAGE_NORMAL,
    MESSAGE_NOT_VALID_FIELDS,
    MESSAGE_OBESITY,
    MESSAGE_OVERWEIGHT,
    MESSAGE_THIN,
)
from src.utils.helpers import calculate_imc, get_imc_status


class TestGetImcStatus:
    def test_returns_thin_when_imc_below_20(self) -> None:
        result: str = get_imc_status(18.0)
        assert result == MESSAGE_THIN

    def test_returns_thin_when_imc_is_19_99(self) -> None:
        result: str = get_imc_status(19.99)
        assert result == MESSAGE_THIN

    def test_returns_normal_when_imc_is_20(self) -> None:
        result: str = get_imc_status(20.0)
        assert result == MESSAGE_NORMAL

    def test_returns_normal_when_imc_is_25(self) -> None:
        result: str = get_imc_status(25.0)
        assert result == MESSAGE_NORMAL

    def test_returns_normal_when_imc_is_22(self) -> None:
        result: str = get_imc_status(22.5)
        assert result == MESSAGE_NORMAL

    def test_returns_overweight_when_imc_is_26(self) -> None:
        result: str = get_imc_status(26.0)
        assert result == MESSAGE_OVERWEIGHT

    def test_returns_overweight_when_imc_is_30(self) -> None:
        result: str = get_imc_status(30.0)
        assert result == MESSAGE_OVERWEIGHT

    def test_returns_obesity_when_imc_above_30(self) -> None:
        result: str = get_imc_status(31.0)
        assert result == MESSAGE_OBESITY

    def test_returns_obesity_when_imc_is_40(self) -> None:
        result: str = get_imc_status(40.0)
        assert result == MESSAGE_OBESITY


class TestCalculateImc:
    def test_returns_correct_imc_value(self) -> None:
        result, _ = calculate_imc("70", "175")
        assert result == round(70 / (1.75 * 1.75), 2)

    def test_returns_correct_message_for_normal_weight(self) -> None:
        _, message = calculate_imc("70", "175")
        assert message == MESSAGE_NORMAL

    def test_returns_correct_message_for_thin(self) -> None:
        _, message = calculate_imc("50", "175")
        assert message == MESSAGE_THIN

    def test_returns_correct_message_for_overweight(self) -> None:
        _, message = calculate_imc("85", "175")
        assert message == MESSAGE_OVERWEIGHT

    def test_returns_correct_message_for_obesity(self) -> None:
        _, message = calculate_imc("120", "175")
        assert message == MESSAGE_OBESITY

    def test_returns_none_result_when_weight_is_not_numeric(self) -> None:
        result, _ = calculate_imc("abc", "175")
        assert result is None

    def test_returns_none_result_when_height_is_not_numeric(self) -> None:
        result, _ = calculate_imc("70", "abc")
        assert result is None

    def test_returns_error_message_when_weight_is_not_numeric(self) -> None:
        _, message = calculate_imc("abc", "175")
        assert message == MESSAGE_NOT_VALID_FIELDS

    def test_returns_error_message_when_height_is_not_numeric(self) -> None:
        _, message = calculate_imc("70", "abc")
        assert message == MESSAGE_NOT_VALID_FIELDS

    def test_returns_none_result_when_both_inputs_are_empty(self) -> None:
        result, _ = calculate_imc("", "")
        assert result is None

    def test_returns_error_message_when_both_inputs_are_empty(self) -> None:
        _, message = calculate_imc("", "")
        assert message == MESSAGE_NOT_VALID_FIELDS

    def test_returns_none_result_when_height_is_zero(self) -> None:
        result, _ = calculate_imc("70", "0")
        assert result is None

    def test_returns_error_message_when_height_is_zero(self) -> None:
        _, message = calculate_imc("70", "0")
        assert message == MESSAGE_NOT_VALID_FIELDS

    def test_result_is_float(self) -> None:
        result, _ = calculate_imc("70", "175")
        assert isinstance(result, float)

    def test_result_is_rounded_to_two_decimals(self) -> None:
        result, _ = calculate_imc("70", "175")
        assert result is not None
        assert len(str(result).split(".")[-1]) <= 2
