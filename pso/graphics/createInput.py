import tkinter as tk
from tkinter import font

from pso.graphics.colors import Color
from pso.graphics.fonts import FontName
from pso.graphics.optionsButton import OptionsButton

class CreateButton(OptionsButton):
    """
    CreateButton is a custom button class that inherits from OptionsButton.
    It toggles between two texts and calls corresponding functions when clicked.
    """
    def __init__(self, parent_frame: tk.Frame, text1: str, text2: str, callable1: callable, callable2: callable, padx: int, pady: int) -> None:
        """
        Initializes the CreateButton with the given parameters.
        
        Args:
            parent_frame (tk.Frame): The parent frame in which the button is placed.
            text1 (str): The initial text of the button.
            text2 (str): The text to toggle to when the button is clicked.
            callable1 (callable): The function to call when the button toggles to text2.
            callable2 (callable): The function to call when the button toggles to text1.
            padx (int): The horizontal padding of the button.
            pady (int): The vertical padding of the button.
        """
        # Initialize the parent class with the first text and other parameters
        super().__init__(parent_frame, text=text1, button_font=font.Font(family=FontName.button, size=10), padx=padx, pady=pady, callable=None, callable_args=None) # ? Callable is none here?
        
        # Raise an error if the two texts are the same
        if text1 == text2:
            raise NotImplementedError("text1 and text2 cannot be the same")
        
        # Store the texts and callables
        self.text1: str = text1
        self.text2: str = text2
        self.__active_text: str = text1
        self.__callable1: callable = callable1
        self.__callable2: callable = callable2
    
    def _release(self, event: tk.Event) -> None:
        """
        Handles the button release event. Toggles the button text and calls the corresponding function.
        
        Args:
            event (tk.Event): The event object containing event data.
        """
        # Check the event type
        if event.type == '3':
            pass
        elif event.type == '5':
            # Change the button colors on release
            self.config(bg=Color.optim_button_abg, fg=Color.back_button_afg, activebackground=Color.optim_button_abg, activeforeground=Color.optim_button_afg)
        
        # Toggle the button text and call the corresponding function
        if self.__active_text == self.text1:
            self.config(text=self.text2)
            self.__active_text = self.text2
            self.__callable1()
        elif self.__active_text == self.text2:
            self.config(text=self.text1)
            self.__active_text = self.text1
            self.__callable2()
        else:
            raise NotImplementedError("The text of the button doesn't match neither callable")