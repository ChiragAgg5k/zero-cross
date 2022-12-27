"""Custom Tkinter module for board UI."""
import customtkinter as ctk


class Board:
    """Board class for the game."""

    def __init__(self) -> None:
        self.window = ctk.CTk()
        self.window.title("Zero-Cross Board")
        self.width = 600
        self.height = 380
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_heigth = self.window.winfo_screenheight()
        self.board = [[None, None, None], [None, None, None], [None, None, None]]
        self.tile_font = ctk.CTkFont(
            "Copperplate", 50, weight="bold", underline=0, overstrike=0
        )

    def center_window(self) -> None:
        """Function to center the window on the screen.

        Args:
            root (tk,ctk): CTkinter/Tkinter root object.
        """
        self.window.resizable(False, False)

        x_coord = int((self.screen_width / 2) - (self.width / 2))
        y_coord = int((self.screen_heigth / 2) - (self.height / 2))

        self.window.geometry(f"{self.width}x{self.height}+{x_coord}+{y_coord}")

    def board_button(self, row, column):
        return ctk.CTkButton(
            self.board_frame, width=100, height=100, text="0", font=(self.tile_font)
        )

    def display_board(self):
        self.board_frame = ctk.CTkFrame(self.window, width=340, height=340)
        self.tile1 = self.board_button(0, 0)
        self.tile2 = self.board_button(0, 1)
        self.tile3 = self.board_button(0, 2)
        self.tile4 = self.board_button(1, 0)
        self.tile5 = self.board_button(1, 1)
        self.tile6 = self.board_button(1, 2)
        self.tile7 = self.board_button(2, 0)
        self.tile8 = self.board_button(2, 1)
        self.tile9 = self.board_button(2, 2)

        self.tile1.grid(row=0, column=0, padx=10, pady=10)
        self.tile2.grid(row=0, column=1, padx=10, pady=10)
        self.tile3.grid(row=0, column=2, padx=10, pady=10)
        self.tile4.grid(row=1, column=0, padx=10, pady=10)
        self.tile5.grid(row=1, column=1, padx=10, pady=10)
        self.tile6.grid(row=1, column=2, padx=10, pady=10)
        self.tile7.grid(row=2, column=0, padx=10, pady=10)
        self.tile8.grid(row=2, column=1, padx=10, pady=10)
        self.tile9.grid(row=2, column=2, padx=10, pady=10)

        self.board_frame.grid(row=0, column=0, padx=10, pady=10)
        self.center_window()
        self.window.mainloop()
