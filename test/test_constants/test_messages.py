from src.constants.messages import (
    MESSAGE_ERROR_APP,
    MESSAGE_NORMAL,
    MESSAGE_NOT_FOUND_DIALOG_TYPE,
    MESSAGE_NOT_VALID_FIELDS,
    MESSAGE_OBESITY,
    MESSAGE_OVERWEIGHT,
    MESSAGE_THIN,
)


class TestMessages:
    def test_thin_is_string(self) -> None:
        assert isinstance(MESSAGE_THIN, str)

    def test_thin_is_not_empty(self) -> None:
        assert len(MESSAGE_THIN) > 0

    def test_normal_is_string(self) -> None:
        assert isinstance(MESSAGE_NORMAL, str)

    def test_normal_is_not_empty(self) -> None:
        assert len(MESSAGE_NORMAL) > 0

    def test_overweight_is_string(self) -> None:
        assert isinstance(MESSAGE_OVERWEIGHT, str)

    def test_overweight_is_not_empty(self) -> None:
        assert len(MESSAGE_OVERWEIGHT) > 0

    def test_obesity_is_string(self) -> None:
        assert isinstance(MESSAGE_OBESITY, str)

    def test_obesity_is_not_empty(self) -> None:
        assert len(MESSAGE_OBESITY) > 0

    def test_error_app_is_string(self) -> None:
        assert isinstance(MESSAGE_ERROR_APP, str)

    def test_error_app_is_not_empty(self) -> None:
        assert len(MESSAGE_ERROR_APP) > 0

    def test_not_valid_fields_is_string(self) -> None:
        assert isinstance(MESSAGE_NOT_VALID_FIELDS, str)

    def test_not_valid_fields_is_not_empty(self) -> None:
        assert len(MESSAGE_NOT_VALID_FIELDS) > 0

    def test_not_found_dialog_type_is_string(self) -> None:
        assert isinstance(MESSAGE_NOT_FOUND_DIALOG_TYPE, str)

    def test_not_found_dialog_type_is_not_empty(self) -> None:
        assert len(MESSAGE_NOT_FOUND_DIALOG_TYPE) > 0

    def test_all_messages_are_unique(self) -> None:
        all_messages: list[str] = [
            MESSAGE_THIN,
            MESSAGE_NORMAL,
            MESSAGE_OVERWEIGHT,
            MESSAGE_OBESITY,
            MESSAGE_ERROR_APP,
            MESSAGE_NOT_VALID_FIELDS,
            MESSAGE_NOT_FOUND_DIALOG_TYPE,
        ]
        assert len(all_messages) == len(set(all_messages))
