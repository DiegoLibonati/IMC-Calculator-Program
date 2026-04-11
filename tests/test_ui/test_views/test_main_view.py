import tkinter as tk
from unittest.mock import MagicMock

from src.ui.styles import Styles
from src.ui.views.main_view import MainView


class TestMainView:
    def test_instantiation(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        view: MainView = MainView(root=root, styles=styles, on_calculate=MagicMock())
        assert view is not None

    def test_entry_weight_initial_value(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        view: MainView = MainView(root=root, styles=styles, on_calculate=MagicMock())
        assert view.entry_weight.get() == ""

    def test_entry_height_initial_value(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        view: MainView = MainView(root=root, styles=styles, on_calculate=MagicMock())
        assert view.entry_height.get() == ""

    def test_entry_result_initial_value(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        view: MainView = MainView(root=root, styles=styles, on_calculate=MagicMock())
        assert view._entry_result.get() == ""

    def test_label_result_initial_value(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        view: MainView = MainView(root=root, styles=styles, on_calculate=MagicMock())
        assert view._label_result.get() == ""

    def test_set_result(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        view: MainView = MainView(root=root, styles=styles, on_calculate=MagicMock())
        view.set_result("24.22")
        assert view._entry_result.get() == "24.22"

    def test_set_message(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        view: MainView = MainView(root=root, styles=styles, on_calculate=MagicMock())
        view.set_message("You have a normal weight.")
        assert view._label_result.get() == "You have a normal weight."

    def test_set_result_overwrites_previous(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        view: MainView = MainView(root=root, styles=styles, on_calculate=MagicMock())
        view.set_result("17.30")
        view.set_result("24.22")
        assert view._entry_result.get() == "24.22"

    def test_set_message_overwrites_previous(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        view: MainView = MainView(root=root, styles=styles, on_calculate=MagicMock())
        view.set_message("first message")
        view.set_message("second message")
        assert view._label_result.get() == "second message"

    def test_on_calculate_callback_invoked(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        on_calculate: MagicMock = MagicMock()
        view: MainView = MainView(root=root, styles=styles, on_calculate=on_calculate)
        view._on_calculate()
        on_calculate.assert_called_once()

    def test_background_matches_primary_color(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        view: MainView = MainView(root=root, styles=styles, on_calculate=MagicMock())
        assert view.cget("bg") == styles.PRIMARY_COLOR

    def test_entry_weight_set_and_get(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        view: MainView = MainView(root=root, styles=styles, on_calculate=MagicMock())
        view.entry_weight.set("80")
        assert view.entry_weight.get() == "80"

    def test_entry_height_set_and_get(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        view: MainView = MainView(root=root, styles=styles, on_calculate=MagicMock())
        view.entry_height.set("175")
        assert view.entry_height.get() == "175"
