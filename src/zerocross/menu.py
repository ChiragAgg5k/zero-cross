"""Custom Tkinter module for UI."""
import tkinter as tk

import customtkinter as ctk


class Menu:
    """Menu class for the game."""

    def __init__(self, width: int, height: int, appearance: str, theme: str) -> None:
        """Initializes the Menu class.

        Args:
            width (int): Width of the window.
            height (int): Height of the window.
        """
        self.width = width
        self.height = height
        self.root = ctk.CTk()
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_heigth = self.root.winfo_screenheight()
        self.player_name = None

        ctk.set_appearance_mode(appearance)
        ctk.set_default_color_theme(theme)

        print("Screen Width:", self.screen_width)
        print("Screen Height:", self.screen_heigth)

        self.font = ctk.CTkFont(
            "Copperplate", 20, weight="bold", underline=0, overstrike=0
        )
        self.fontHeading = ctk.CTkFont(
            "Copperplate",
            size=(self.screen_width // 23),
            weight="bold",
            underline=1,
            overstrike=0,
        )

        self.name_entry = ctk.CTkEntry(
            self.root, font=self.font, width=self.screen_width // 5
        )

        self.heading = ctk.CTkLabel(
            self.root,
            text="Zero-Cross",
            font=self.fontHeading,
        )

        self.enter_details = ctk.CTkButton(
            self.root,
            text="Enter Username",
            font=self.font,
            height=self.screen_heigth // 20,
            width=self.screen_width // 5,
            command=self.name_button_pressed,
        )

        self.show_options = ctk.CTkButton(
            self.root,
            text="Options",
            font=self.font,
            height=self.screen_heigth // 20,
            width=self.screen_width // 5,
            command=self.options_button_pressed,
        )

    def center_window(self) -> None:
        """Function to center the window on the screen.

        Args:
            root (tk,ctk): CTkinter/Tkinter root object.
        """
        self.root.resizable(False, False)

        x_coord = int((self.screen_width / 2) - (self.width / 2))
        y_coord = int((self.screen_heigth / 2) - (self.height / 2))

        self.root.geometry(f"{self.width}x{self.height}+{x_coord}+{y_coord}")

    def name_button_pressed(self) -> bool:
        """Function to be called when the name button is pressed."""

        self.player_name = (
            self.name_entry.get() if self.name_entry.get() != "" else None
        )
        print("Player Name:", self.player_name)

        self.root.destroy()
        print("Main menu closed")

        return True

    def options_button_pressed(self):
        options = Options(self.root)
        options.display_options()

    def display_menu(self, title: str) -> None:
        """Displays the menu."""

        self.root.title(title)

        self.center_window()
        self.name_button_pressed

        self.heading.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)
        self.name_entry.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        self.enter_details.place(relx=0.5, rely=0.65, anchor=ctk.CENTER)
        self.show_options.place(relx=0.5, rely=0.8, anchor=ctk.CENTER)

        print("Main Menu Displayed")

        self.root.mainloop()


class Options:
    def __init__(self, root) -> None:
        self.root = root
        self.op_width = 400
        self.op_height = 400
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_heigth = self.root.winfo_screenheight()
        self.top = tk.Toplevel(self.root)

    def op_center_window(self) -> None:
        """Function to center the option window on the screen.

        Args:
            root (tk,ctk): CTkinter/Tkinter root object.
        """
        self.top.resizable(False, False)

        x_coord = int((self.screen_width / 2) - (self.op_width / 2))
        y_coord = int((self.screen_heigth / 2) - (self.op_height / 2))

        self.top.geometry(f"{self.op_width}x{self.op_height}+{x_coord}+{y_coord}")

    def change_theme(self, new_theme: str):
        ctk.set_appearance_mode(new_theme)
        self.top.update()

    def display_options(
        self,
    ):
        print("Options Displayed")
        self.top.title("Options")
        self.op_center_window()

        self.theme_options = ctk.CTkOptionMenu(
            self.top,
            values=["Dark", "Light", "System"],
            command=self.change_theme,
        )

        self.theme_options.pack(padx=10, pady=10)
        self.top.mainloop()
