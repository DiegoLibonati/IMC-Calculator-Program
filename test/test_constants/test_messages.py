from src.constants.messages import (
    MESSAGE_ERROR_INVALID_VALUES,
    MESSAGE_NORMAL,
    MESSAGE_OBESITY,
    MESSAGE_OVERWEIGHT,
    MESSAGE_THIN,
)


class TestMessages:
    def test_message_error_invalid_values_is_string(self) -> None:
        assert isinstance(MESSAGE_ERROR_INVALID_VALUES, str)

    def test_message_error_invalid_values_is_not_empty(self) -> None:
        assert len(MESSAGE_ERROR_INVALID_VALUES) > 0

    def test_message_thin_is_string(self) -> None:
        assert isinstance(MESSAGE_THIN, str)

    def test_message_thin_is_not_empty(self) -> None:
        assert len(MESSAGE_THIN) > 0

    def test_message_normal_is_string(self) -> None:
        assert isinstance(MESSAGE_NORMAL, str)

    def test_message_normal_is_not_empty(self) -> None:
        assert len(MESSAGE_NORMAL) > 0

    def test_message_overweight_is_string(self) -> None:
        assert isinstance(MESSAGE_OVERWEIGHT, str)

    def test_message_overweight_is_not_empty(self) -> None:
        assert len(MESSAGE_OVERWEIGHT) > 0

    def test_message_obesity_is_string(self) -> None:
        assert isinstance(MESSAGE_OBESITY, str)

    def test_message_obesity_is_not_empty(self) -> None:
        assert len(MESSAGE_OBESITY) > 0
