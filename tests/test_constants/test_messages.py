import pytest

from src.constants.messages import (
    MESSAGE_ERROR_APP,
    MESSAGE_NORMAL,
    MESSAGE_NOT_FOUND_DIALOG_TYPE,
    MESSAGE_NOT_VALID_FIELDS,
    MESSAGE_OBESITY,
    MESSAGE_OVERWEIGHT,
    MESSAGE_THIN,
)


@pytest.mark.unit
class TestMessages:
    @pytest.mark.parametrize(
        "message",
        [
            MESSAGE_THIN,
            MESSAGE_NORMAL,
            MESSAGE_OVERWEIGHT,
            MESSAGE_OBESITY,
            MESSAGE_ERROR_APP,
            MESSAGE_NOT_VALID_FIELDS,
            MESSAGE_NOT_FOUND_DIALOG_TYPE,
        ],
    )
    def test_message_is_non_empty_string(self, message: str) -> None:
        assert isinstance(message, str)
        assert len(message) > 0

    def test_all_messages_are_distinct(self) -> None:
        messages: list[str] = [
            MESSAGE_THIN,
            MESSAGE_NORMAL,
            MESSAGE_OVERWEIGHT,
            MESSAGE_OBESITY,
            MESSAGE_ERROR_APP,
            MESSAGE_NOT_VALID_FIELDS,
            MESSAGE_NOT_FOUND_DIALOG_TYPE,
        ]

        assert len(messages) == len(set(messages))
