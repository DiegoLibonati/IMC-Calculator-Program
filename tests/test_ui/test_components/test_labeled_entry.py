import tkinter as tk

import pytest

from src.ui.components.labeled_entry import LabeledEntry
from src.ui.styles import Styles


@pytest.mark.unit
class TestLabeledEntry:
    def test_initializes_as_frame(self, root: tk.Tk) -> None:
        variable: tk.StringVar = tk.StringVar()

        entry: LabeledEntry = LabeledEntry(
            parent=root,
            styles=Styles(),
            label_text="Weight:",
            variable=variable,
        )

        assert isinstance(entry, tk.Frame)

    def test_initializes_with_default_show_empty(self, root: tk.Tk) -> None:
        variable: tk.StringVar = tk.StringVar()

        entry: LabeledEntry = LabeledEntry(
            parent=root,
            styles=Styles(),
            label_text="Field:",
            variable=variable,
        )

        assert isinstance(entry, tk.Frame)

    def test_initializes_with_custom_show(self, root: tk.Tk) -> None:
        variable: tk.StringVar = tk.StringVar()

        entry: LabeledEntry = LabeledEntry(
            parent=root,
            styles=Styles(),
            label_text="Password:",
            variable=variable,
            show="*",
        )

        assert isinstance(entry, tk.Frame)

    def test_variable_retains_value_after_creation(self, root: tk.Tk) -> None:
        variable: tk.StringVar = tk.StringVar(value="initial")

        LabeledEntry(
            parent=root,
            styles=Styles(),
            label_text="Weight:",
            variable=variable,
        )

        assert variable.get() == "initial"
