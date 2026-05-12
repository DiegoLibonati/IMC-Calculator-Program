import tkinter as tk
from unittest.mock import MagicMock

import pytest

from src.ui.styles import Styles
from src.ui.views.main_view import MainView


@pytest.mark.unit
class TestMainView:
    def test_initializes_as_frame(self, root: tk.Tk) -> None:
        view: MainView = MainView(root=root, styles=Styles(), on_calculate=MagicMock())

        assert isinstance(view, tk.Frame)

    def test_entry_weight_is_string_var(self, root: tk.Tk) -> None:
        view: MainView = MainView(root=root, styles=Styles(), on_calculate=MagicMock())

        assert isinstance(view.entry_weight, tk.StringVar)

    def test_entry_height_is_string_var(self, root: tk.Tk) -> None:
        view: MainView = MainView(root=root, styles=Styles(), on_calculate=MagicMock())

        assert isinstance(view.entry_height, tk.StringVar)

    def test_set_result_updates_entry_result_var(self, root: tk.Tk) -> None:
        view: MainView = MainView(root=root, styles=Styles(), on_calculate=MagicMock())

        view.set_result("24.22")

        assert view._entry_result.get() == "24.22"

    def test_set_message_updates_label_result_var(self, root: tk.Tk) -> None:
        view: MainView = MainView(root=root, styles=Styles(), on_calculate=MagicMock())

        view.set_message("Normal weight")

        assert view._label_result.get() == "Normal weight"

    def test_on_calculate_callback_is_stored(self, root: tk.Tk) -> None:
        callback: MagicMock = MagicMock()

        view: MainView = MainView(root=root, styles=Styles(), on_calculate=callback)

        assert view._on_calculate is callback
