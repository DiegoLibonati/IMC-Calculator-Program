from src.constants import messages


class TestMessages:
    def test_message_thin_is_string(self) -> None:
        assert isinstance(messages.MESSAGE_THIN, str)

    def test_message_normal_is_string(self) -> None:
        assert isinstance(messages.MESSAGE_NORMAL, str)

    def test_message_overweight_is_string(self) -> None:
        assert isinstance(messages.MESSAGE_OVERWEIGHT, str)

    def test_message_obesity_is_string(self) -> None:
        assert isinstance(messages.MESSAGE_OBESITY, str)

    def test_message_error_app_is_string(self) -> None:
        assert isinstance(messages.MESSAGE_ERROR_APP, str)

    def test_message_not_valid_fields_is_string(self) -> None:
        assert isinstance(messages.MESSAGE_NOT_VALID_FIELDS, str)

    def test_message_not_found_dialog_type_is_string(self) -> None:
        assert isinstance(messages.MESSAGE_NOT_FOUND_DIALOG_TYPE, str)

    def test_message_thin_value(self) -> None:
        assert messages.MESSAGE_THIN == "You are thin."

    def test_message_normal_value(self) -> None:
        assert messages.MESSAGE_NORMAL == "You have a normal weight."

    def test_message_overweight_value(self) -> None:
        assert messages.MESSAGE_OVERWEIGHT == "You are overweight."

    def test_message_obesity_value(self) -> None:
        assert messages.MESSAGE_OBESITY == "Obesity status."

    def test_message_not_valid_fields_value(self) -> None:
        assert messages.MESSAGE_NOT_VALID_FIELDS == "The fields entered are invalid."

    def test_message_error_app_is_not_empty(self) -> None:
        assert len(messages.MESSAGE_ERROR_APP) > 0

    def test_message_not_found_dialog_type_is_not_empty(self) -> None:
        assert len(messages.MESSAGE_NOT_FOUND_DIALOG_TYPE) > 0
