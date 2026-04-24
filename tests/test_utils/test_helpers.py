from src.constants.messages import (
    MESSAGE_NORMAL,
    MESSAGE_NOT_VALID_FIELDS,
    MESSAGE_OBESITY,
    MESSAGE_OVERWEIGHT,
    MESSAGE_THIN,
)
from src.utils.helpers import calculate_imc, get_imc_status


class TestCalculateImc:
    def test_returns_tuple(self) -> None:
        result: tuple[float | None, str] = calculate_imc("70", "170")
        assert isinstance(result, tuple)

    def test_valid_normal_weight(self) -> None:
        result: float | None
        message: str
        result, message = calculate_imc("70", "170")
        assert result == 24.22
        assert message == MESSAGE_NORMAL

    def test_valid_thin(self) -> None:
        result: float | None
        message: str
        result, message = calculate_imc("50", "170")
        assert result is not None
        assert message == MESSAGE_THIN

    def test_valid_overweight(self) -> None:
        result: float | None
        message: str
        result, message = calculate_imc("80", "170")
        assert result is not None
        assert message == MESSAGE_OVERWEIGHT

    def test_valid_obesity(self) -> None:
        result: float | None
        message: str
        result, message = calculate_imc("90", "170")
        assert result is not None
        assert message == MESSAGE_OBESITY

    def test_invalid_weight_string(self) -> None:
        result: float | None
        message: str
        result, message = calculate_imc("abc", "170")
        assert result is None
        assert message == MESSAGE_NOT_VALID_FIELDS

    def test_invalid_height_string(self) -> None:
        result: float | None
        message: str
        result, message = calculate_imc("70", "xyz")
        assert result is None
        assert message == MESSAGE_NOT_VALID_FIELDS

    def test_empty_weight(self) -> None:
        result: float | None
        message: str
        result, message = calculate_imc("", "170")
        assert result is None
        assert message == MESSAGE_NOT_VALID_FIELDS

    def test_empty_height(self) -> None:
        result: float | None
        message: str
        result, message = calculate_imc("70", "")
        assert result is None
        assert message == MESSAGE_NOT_VALID_FIELDS

    def test_zero_height(self) -> None:
        result: float | None
        message: str
        result, message = calculate_imc("70", "0")
        assert result is None
        assert message == MESSAGE_NOT_VALID_FIELDS

    def test_float_string_weight(self) -> None:
        result: float | None
        message: str
        result, message = calculate_imc("70.5", "170")
        assert result is None
        assert message == MESSAGE_NOT_VALID_FIELDS

    def test_result_is_rounded_to_two_decimals(self) -> None:
        result: float | None
        result, _ = calculate_imc("70", "170")
        assert result is not None
        assert result == round(result, 2)

    def test_negative_height_computes_valid_imc(self) -> None:
        result: float | None
        result, _ = calculate_imc("70", "-170")
        assert result is not None
        assert result > 0


class TestGetImcStatus:
    def test_thin_below_20(self) -> None:
        assert get_imc_status(15.0) == MESSAGE_THIN

    def test_thin_at_boundary(self) -> None:
        assert get_imc_status(19.99) == MESSAGE_THIN

    def test_normal_at_lower_boundary(self) -> None:
        assert get_imc_status(20.0) == MESSAGE_NORMAL

    def test_normal_at_upper_boundary(self) -> None:
        assert get_imc_status(25.0) == MESSAGE_NORMAL

    def test_normal_midrange(self) -> None:
        assert get_imc_status(22.5) == MESSAGE_NORMAL

    def test_overweight_at_lower_boundary(self) -> None:
        assert get_imc_status(26.0) == MESSAGE_OVERWEIGHT

    def test_overweight_at_upper_boundary(self) -> None:
        assert get_imc_status(30.0) == MESSAGE_OVERWEIGHT

    def test_obesity_above_30(self) -> None:
        assert get_imc_status(31.0) == MESSAGE_OBESITY

    def test_obesity_extreme(self) -> None:
        assert get_imc_status(50.0) == MESSAGE_OBESITY

    def test_gap_between_25_and_26_returns_obesity(self) -> None:
        assert get_imc_status(25.5) == MESSAGE_OBESITY
