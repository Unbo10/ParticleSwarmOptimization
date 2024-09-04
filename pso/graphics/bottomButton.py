
import tkinter as tk

from pso.graphics.colors import Color
from pso.graphics.popUpFrame import PopUpFrame

class BottomButton(tk.Button):
    def __init__(self, main_frame: tk.Frame, parent_frame: tk.Frame, image: tk.PhotoImage, active_image: tk.PhotoImage, pop_up_text: str, name: str, pop_up_frame_height: int, pop_up_frame_width: int, pop_up_frame_y: int, abg: str = Color.bottom_button_abg, cbg: str = Color.bottom_button_cbg, args: dict = {
        "relief": "flat",
        "bg": Color.bottom_button_bg,
        "highlightbackground": Color.bottom_button_hbg,
        "highlightcolor": Color.bottom_button_hcolor,
        "highlightthickness": 1,
        "borderwidth": 0,
        "cursor": "hand2"
        }) -> None:
        super().__init__(parent_frame, image=image, **args)
        self.__image: tk.PhotoImage = image
        self.__active_image: tk.PhotoImage = active_image
        self.__bg: str = args["bg"]
        self.__abg: str = abg
        self.__cbg: str = cbg
        self.pop_up_frame: PopUpFrame = PopUpFrame(main_frame, name=name, height=pop_up_frame_height, width=pop_up_frame_width, y=pop_up_frame_y, text=pop_up_text)

    def __enter(self, e):
        self.config(bg=self.__abg, activebackground=self.__abg, image=self.__active_image)
    
    def __leave(self, e):
        self.config(bg=self.__bg, image=self.__image)

    def __click(self, e):
        self.config(bg=self.__cbg, activebackground=self.__cbg, image=self.__image)

    def __release(self, event: tk.Event, pop_up_frames: list["PopUpFrame"]):
        other_frames: list[PopUpFrame] = [frame for frame in pop_up_frames if frame.get_name() != self.pop_up_frame.get_name()]
        if event.type == '3':
            pass
        elif event.type == '5':
            self.config(
                image=self.__active_image,
                activebackground=self.__abg,
                bg=self.__bg
            )
            # ! Could be improved: If we were to manage more than three 
            print([frame.name for frame in other_frames])
        self.pop_up_frame.display(other_frames[0])
        # if self.pop_up_frame.visible == False:
        #     print("C")
        #     for frame in other_frames:
        #         frame.visible = False
        #         frame.place_forget()
        #     self.pop_up_frame.visible = True
        #     self.pop_up_frame.display(other_frames[0])
        
        # elif self.pop_up_frame.visible == True:
        #     print("B")
        #     self.place_forget()
        #     self.pop_up_frame.visible = False
        #     for frame in other_frames:
        #         frame.visible = False
        #         frame.place_forget()
        #     # other_frames[0].visible = True
        #     # other_frames[0].display(self)
        #     print("A")

        # else:
        #     raise NotImplementedError("Frame not implemented in release method")
        # TODO after: Configure the release method so that it correctly opens and closes different frames depending on their visibility
        # TODO: add a bind_to_event methods to all classes that require it. Remember, a method represents a single behavior just as a function represents a single action.

    def bind_to_events(self, pop_up_frames: dict):
        self.bind("<Enter>", self.__enter)
        self.bind("<Leave>", self.__leave)
        self.bind("<Button-1>", self.__click)
        self.bind("<ButtonRelease-1>", lambda event: self.__release(event, pop_up_frames))
        self.bind("<KeyRelease-Return>", lambda event: self.__release(event, pop_up_frames))

    def display(self, pop_up_frames: list[PopUpFrame], row: int, column: int, sticky: str):
        self.bind_to_events(pop_up_frames)
        self.grid(row=row, column=column, sticky=sticky)

