import tkinter as tk

from src.ui.components.labeled_entry import LabeledEntry
from src.ui.styles import Styles


class TestLabeledEntry:
    def test_instantiation(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        variable: tk.StringVar = tk.StringVar(root)
        widget: LabeledEntry = LabeledEntry(
            parent=root,
            styles=styles,
            label_text="Test:",
            variable=variable,
        )
        assert widget is not None

    def test_variable_initial_value_is_empty(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        variable: tk.StringVar = tk.StringVar(root)
        LabeledEntry(
            parent=root,
            styles=styles,
            label_text="Test:",
            variable=variable,
        )
        assert variable.get() == ""

    def test_variable_set_updates_value(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        variable: tk.StringVar = tk.StringVar(root)
        LabeledEntry(
            parent=root,
            styles=styles,
            label_text="Test:",
            variable=variable,
        )
        variable.set("hello")
        assert variable.get() == "hello"

    def test_background_matches_primary_color(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        variable: tk.StringVar = tk.StringVar(root)
        widget: LabeledEntry = LabeledEntry(
            parent=root,
            styles=styles,
            label_text="Test:",
            variable=variable,
        )
        assert widget.cget("bg") == styles.PRIMARY_COLOR

    def test_instantiation_with_show_param(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        variable: tk.StringVar = tk.StringVar(root)
        widget: LabeledEntry = LabeledEntry(
            parent=root,
            styles=styles,
            label_text="Password:",
            variable=variable,
            show="*",
        )
        assert widget is not None

    def test_different_label_texts(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        for label in ["Weight:", "Height in CM:", "YOUR BMI:"]:
            variable: tk.StringVar = tk.StringVar(root)
            widget: LabeledEntry = LabeledEntry(
                parent=root,
                styles=styles,
                label_text=label,
                variable=variable,
            )
            assert widget is not None
