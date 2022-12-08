import tkinter as tk

import customtkinter as ctk


class Menu:
    def __init__(self, width: int, height: int) -> None:
        """Initializes the Menu class.

        Args:
            width (int): Width of the window.
            height (int): Height of the window.
        """
        self.width = width
        self.height = height
        self.root = ctk.CTk()
        self.SCREEN_WIDTH = self.root.winfo_screenwidth()
        self.SCREEN_HEIGHT = self.root.winfo_screenheight()

    def register(self) -> None:
        """Registers the user."""

        pass

    def center_window(self) -> None:
        """Function to center the window on the screen.

        Args:
            root (tk,ctk): CTkinter/Tkinter root object.
        """

        x = (self.SCREEN_WIDTH / 2) - (self.width / 2)
        y = (self.SCREEN_HEIGHT / 2) - (self.height / 2)

        self.root.geometry("%dx%d+%d+%d" % (self.width, self.height, x, y))

    def display_menu(self, title: str, appearance: str, theme: str) -> None:
        """Displays the menu."""

        self.root.title(title)
        ctk.set_appearance_mode(appearance)
        ctk.set_default_color_theme(theme)

        self.center_window()

        name_entry = ctk.CTkEntry(
            self.root, font=("Copperplate", 20), width=self.SCREEN_WIDTH // 5
        )
        enter_details = ctk.CTkButton(
            self.root,
            text="Enter Name",
            font=("Copperplate", 20),
            command=self.register,
            width=self.SCREEN_WIDTH // 5,
            height=self.SCREEN_HEIGHT // 20,
        )

        heading = ctk.CTkLabel(self.root, text="Zero-Cross", font=("Copperplate", 60))
        heading.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)
        name_entry.place(relx=0.5, rely=0.55, anchor=ctk.CENTER)
        enter_details.place(relx=0.5, rely=0.7, anchor=ctk.CENTER)

        self.root.mainloop()
