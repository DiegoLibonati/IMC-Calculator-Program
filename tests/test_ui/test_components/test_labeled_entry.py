import tkinter as tk

import pytest

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

    @pytest.mark.parametrize("label_text", ["Weight:", "Height in CM:", "YOUR BMI:"])
    def test_instantiation_with_various_label_texts(self, root: tk.Tk, label_text: str) -> None:
        styles: Styles = Styles()
        variable: tk.StringVar = tk.StringVar(root)

        widget: LabeledEntry = LabeledEntry(
            parent=root,
            styles=styles,
            label_text=label_text,
            variable=variable,
        )

        assert widget is not None

    def test_is_frame_subclass(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        variable: tk.StringVar = tk.StringVar(root)

        widget: LabeledEntry = LabeledEntry(
            parent=root,
            styles=styles,
            label_text="Label:",
            variable=variable,
        )

        assert isinstance(widget, tk.Frame)

    def test_empty_show_param_does_not_affect_instantiation(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        variable: tk.StringVar = tk.StringVar(root)

        widget: LabeledEntry = LabeledEntry(
            parent=root,
            styles=styles,
            label_text="Field:",
            variable=variable,
            show="",
        )

        assert widget is not None
