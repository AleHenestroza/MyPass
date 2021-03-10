from tkinter import Canvas
from constants import BACKGROUND_COLOR


class Logo(Canvas):

    def __init__(self, image):
        super().__init__(width=200, height=200, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.create_image(60, 100, image=image)
        self.grid(row=0, column=1, columnspan=2)
