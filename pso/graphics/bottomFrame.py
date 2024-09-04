import tkinter as tk
from tkinter import font

from pso.graphics.colors import Color
from pso.graphics.fonts import FontName
from pso.graphics.bottomButton import BottomButton
from pso.graphics.popUpFrame import PopUpFrame

class BottomFrame():
    def __init__(self, master_frame, main_frame: tk.Frame, window_width: int, window_height, title_height: int, bottom_frame_height: int, program_version: str):
        # ! Pop-up frame must be another class
        self.root: tk.Frame = tk.Frame(main_frame, bg=Color.test3_bg)
        self.__window_width: int = window_width
        self.__window_height: int = window_height
        self.root_height: int = bottom_frame_height
        self._pop_up_frame_height: int = self.__window_height - title_height - self.root_height
        # self._pop_up_frame_pady: tuple = (10, 10)

        info_image: tk.PhotoImage = tk.PhotoImage(file="assets/info.png").subsample(3)
        info_active_image: tk.PhotoImage = tk.PhotoImage(file="assets/info-active.png").subsample(3)
        self.__info_button: BottomButton = BottomButton(master_frame, self.root, image=info_image, active_image=info_active_image, name="info", pop_up_frame_height=self._pop_up_frame_height, pop_up_frame_width=self.__window_width, pop_up_frame_y=title_height, pop_up_text=" aaaaaaaaaaaaa Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?")
        help_image: tk.PhotoImage = tk.PhotoImage(file="assets/help.png").subsample(3)
        help_active_image: tk.PhotoImage = tk.PhotoImage(file="assets/help-active.png").subsample(3)
        self.__help_button: BottomButton = BottomButton(master_frame, self.root, image=help_image, active_image=help_active_image, name="help", pop_up_frame_height=self._pop_up_frame_height, pop_up_frame_width=self.__window_width, pop_up_frame_y=title_height, pop_up_text="Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?")
        self._pop_up_frames: list[PopUpFrame] = [self.__help_button.pop_up_frame, self.__info_button.pop_up_frame] # ! Could be immutable actually
        self._pop_up_frames.sort(key=lambda frame: frame.get_name())
        
        self.__version_label: tk.Label = tk.Label(
            self.root,
            text=f"V {program_version}",
            bg=Color.bottom_button_bg,
            fg=Color.bottom_button_fg,
            font=font.Font(family=FontName.label, size=10, weight="bold")
            )

    def display(self):     
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.__info_button.display(self._pop_up_frames, row=0, column=0, sticky="nsew")
        self.__help_button.display(self._pop_up_frames, row=0, column=1, sticky="nsew")
        self.__version_label.grid(row=0, column=2, sticky="nsew")
        self.root.place(x=0, y=self.__window_height - self.root_height, width=self.__window_width, height=self.root_height)