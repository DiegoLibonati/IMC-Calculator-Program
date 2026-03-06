from tkinter import Entry, Frame, Label, Misc, StringVar

from src.ui.styles import Styles


class LabeledEntry(Frame):
    def __init__(
        self,
        parent: Misc,
        styles: Styles,
        label_text: str,
        variable: StringVar,
        show: str = "",
    ) -> None:
        super().__init__(parent, bg=styles.PRIMARY_COLOR)
        self._styles = styles
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)

        Label(
            self,
            text=label_text,
            font=self._styles.FONT_TIMES_12,
            bg=self._styles.PRIMARY_COLOR,
            fg=self._styles.WHITE_COLOR,
        ).grid(row=0, column=0, padx=(0, 5), sticky="e")

        entry_config = {
            "width": 5,
            "bg": self._styles.WHITE_COLOR,
            "font": self._styles.FONT_TIMES_14,
            "textvariable": variable,
        }

        if show:
            entry_config["show"] = show

        Entry(self, **entry_config).grid(row=0, column=1, sticky="w")
