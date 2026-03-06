from tkinter import StringVar
from unittest.mock import MagicMock, patch

import pytest

from src.ui.views.main_view import MainView


@pytest.fixture
def main_view(mock_root: MagicMock, mock_styles: MagicMock, mock_on_calculate: MagicMock) -> MainView:
    with (
        patch("src.ui.views.main_view.Frame.__init__", return_value=None),
        patch("src.ui.views.main_view.LabeledEntry"),
        patch("src.ui.views.main_view.Button"),
        patch("src.ui.views.main_view.Label"),
        patch("src.ui.views.main_view.StringVar"),
        patch.object(MainView, "columnconfigure"),
    ):
        instance: MainView = MainView.__new__(MainView)
        instance._styles = mock_styles
        instance._on_calculate = mock_on_calculate
        instance._entry_result = MagicMock(spec=StringVar)
        instance._label_result = MagicMock(spec=StringVar)
        instance.entry_weight = MagicMock(spec=StringVar)
        instance.entry_height = MagicMock(spec=StringVar)
        return instance


class TestMainViewInit:
    def test_stores_styles(self, main_view: MainView, mock_styles: MagicMock) -> None:
        assert main_view._styles == mock_styles

    def test_stores_on_calculate(self, main_view: MainView, mock_on_calculate: MagicMock) -> None:
        assert main_view._on_calculate == mock_on_calculate

    def test_four_string_vars_are_created(self, mock_root: MagicMock, mock_styles: MagicMock, mock_on_calculate: MagicMock) -> None:
        with (
            patch("src.ui.views.main_view.Frame.__init__", return_value=None),
            patch("src.ui.views.main_view.LabeledEntry") as mock_labeled_entry,
            patch("src.ui.views.main_view.Button") as mock_button,
            patch("src.ui.views.main_view.Label") as mock_label,
            patch("src.ui.views.main_view.StringVar") as mock_string_var,
            patch.object(MainView, "columnconfigure"),
        ):
            mock_labeled_entry.return_value.grid = MagicMock()
            mock_button.return_value.grid = MagicMock()
            mock_label.return_value.grid = MagicMock()
            instance: MainView = MainView.__new__(MainView)
            instance._styles = mock_styles
            MainView.__init__(instance, root=mock_root, styles=mock_styles, on_calculate=mock_on_calculate)

        assert mock_string_var.call_count == 4

    def test_labeled_entry_created_for_weight(self, mock_root: MagicMock, mock_styles: MagicMock, mock_on_calculate: MagicMock) -> None:
        with (
            patch("src.ui.views.main_view.Frame.__init__", return_value=None),
            patch("src.ui.views.main_view.LabeledEntry") as mock_labeled_entry,
            patch("src.ui.views.main_view.Button") as mock_button,
            patch("src.ui.views.main_view.Label") as mock_label,
            patch("src.ui.views.main_view.StringVar"),
            patch.object(MainView, "columnconfigure"),
        ):
            mock_labeled_entry.return_value.grid = MagicMock()
            mock_button.return_value.grid = MagicMock()
            mock_label.return_value.grid = MagicMock()
            instance: MainView = MainView.__new__(MainView)
            instance._styles = mock_styles
            MainView.__init__(instance, root=mock_root, styles=mock_styles, on_calculate=mock_on_calculate)

        calls: list[str | None] = [call.kwargs.get("label_text") for call in mock_labeled_entry.call_args_list]
        assert "Weight:" in calls

    def test_labeled_entry_created_for_height(self, mock_root: MagicMock, mock_styles: MagicMock, mock_on_calculate: MagicMock) -> None:
        with (
            patch("src.ui.views.main_view.Frame.__init__", return_value=None),
            patch("src.ui.views.main_view.LabeledEntry") as mock_labeled_entry,
            patch("src.ui.views.main_view.Button") as mock_button,
            patch("src.ui.views.main_view.Label") as mock_label,
            patch("src.ui.views.main_view.StringVar"),
            patch.object(MainView, "columnconfigure"),
        ):
            mock_labeled_entry.return_value.grid = MagicMock()
            mock_button.return_value.grid = MagicMock()
            mock_label.return_value.grid = MagicMock()
            instance: MainView = MainView.__new__(MainView)
            instance._styles = mock_styles
            MainView.__init__(instance, root=mock_root, styles=mock_styles, on_calculate=mock_on_calculate)

        calls: list[str | None] = [call.kwargs.get("label_text") for call in mock_labeled_entry.call_args_list]
        assert "Height in CM:" in calls

    def test_labeled_entry_created_for_imc_result(self, mock_root: MagicMock, mock_styles: MagicMock, mock_on_calculate: MagicMock) -> None:
        with (
            patch("src.ui.views.main_view.Frame.__init__", return_value=None),
            patch("src.ui.views.main_view.LabeledEntry") as mock_labeled_entry,
            patch("src.ui.views.main_view.Button") as mock_button,
            patch("src.ui.views.main_view.Label") as mock_label,
            patch("src.ui.views.main_view.StringVar"),
            patch.object(MainView, "columnconfigure"),
        ):
            mock_labeled_entry.return_value.grid = MagicMock()
            mock_button.return_value.grid = MagicMock()
            mock_label.return_value.grid = MagicMock()
            instance: MainView = MainView.__new__(MainView)
            instance._styles = mock_styles
            MainView.__init__(instance, root=mock_root, styles=mock_styles, on_calculate=mock_on_calculate)

        calls: list[str | None] = [call.kwargs.get("label_text") for call in mock_labeled_entry.call_args_list]
        assert "YOUR IMC:" in calls

    def test_button_command_is_on_calculate(self, mock_root: MagicMock, mock_styles: MagicMock, mock_on_calculate: MagicMock) -> None:
        with (
            patch("src.ui.views.main_view.Frame.__init__", return_value=None),
            patch("src.ui.views.main_view.LabeledEntry") as mock_labeled_entry,
            patch("src.ui.views.main_view.Button") as mock_button,
            patch("src.ui.views.main_view.Label") as mock_label,
            patch("src.ui.views.main_view.StringVar"),
            patch.object(MainView, "columnconfigure"),
        ):
            mock_labeled_entry.return_value.grid = MagicMock()
            mock_button.return_value.grid = MagicMock()
            mock_label.return_value.grid = MagicMock()
            instance: MainView = MainView.__new__(MainView)
            instance._styles = mock_styles
            MainView.__init__(instance, root=mock_root, styles=mock_styles, on_calculate=mock_on_calculate)

        _, kwargs = mock_button.call_args
        assert kwargs.get("command") == mock_on_calculate

    def test_button_text_is_calculate(self, mock_root: MagicMock, mock_styles: MagicMock, mock_on_calculate: MagicMock) -> None:
        with (
            patch("src.ui.views.main_view.Frame.__init__", return_value=None),
            patch("src.ui.views.main_view.LabeledEntry") as mock_labeled_entry,
            patch("src.ui.views.main_view.Button") as mock_button,
            patch("src.ui.views.main_view.Label") as mock_label,
            patch("src.ui.views.main_view.StringVar"),
            patch.object(MainView, "columnconfigure"),
        ):
            mock_labeled_entry.return_value.grid = MagicMock()
            mock_button.return_value.grid = MagicMock()
            mock_label.return_value.grid = MagicMock()
            instance: MainView = MainView.__new__(MainView)
            instance._styles = mock_styles
            MainView.__init__(instance, root=mock_root, styles=mock_styles, on_calculate=mock_on_calculate)

        _, kwargs = mock_button.call_args
        assert kwargs.get("text") == "Calculate"

    def test_columnconfigure_is_called(self, mock_root: MagicMock, mock_styles: MagicMock, mock_on_calculate: MagicMock) -> None:
        with (
            patch("src.ui.views.main_view.Frame.__init__", return_value=None),
            patch("src.ui.views.main_view.LabeledEntry") as mock_labeled_entry,
            patch("src.ui.views.main_view.Button") as mock_button,
            patch("src.ui.views.main_view.Label") as mock_label,
            patch("src.ui.views.main_view.StringVar"),
            patch.object(MainView, "columnconfigure") as mock_columnconfigure,
        ):
            mock_labeled_entry.return_value.grid = MagicMock()
            mock_button.return_value.grid = MagicMock()
            mock_label.return_value.grid = MagicMock()
            instance: MainView = MainView.__new__(MainView)
            instance._styles = mock_styles
            MainView.__init__(instance, root=mock_root, styles=mock_styles, on_calculate=mock_on_calculate)

        mock_columnconfigure.assert_called_once_with(0, weight=1)


class TestMainViewSetResult:
    def test_set_result_updates_entry_result(self, main_view: MainView) -> None:
        main_view.set_result("22.86")
        main_view._entry_result.set.assert_called_once_with("22.86")

    def test_set_result_with_empty_string(self, main_view: MainView) -> None:
        main_view.set_result("")
        main_view._entry_result.set.assert_called_once_with("")


class TestMainViewSetMessage:
    def test_set_message_updates_label_result(self, main_view: MainView) -> None:
        main_view.set_message("You have a normal weight.")
        main_view._label_result.set.assert_called_once_with("You have a normal weight.")

    def test_set_message_with_empty_string(self, main_view: MainView) -> None:
        main_view.set_message("")
        main_view._label_result.set.assert_called_once_with("")

    def test_set_message_with_error(self, main_view: MainView) -> None:
        main_view.set_message("YOU NEED TO INPUT CORRECT VALUES.")
        main_view._label_result.set.assert_called_once_with("YOU NEED TO INPUT CORRECT VALUES.")
