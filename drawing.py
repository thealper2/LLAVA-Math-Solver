import tkinter as tk
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

class DrawCanvas(tk.Canvas):
    def __init__(self, root, w, h):
        super().__init__(root, bg='black', width=w, height=h)
        self.img = Image.new("RGB", (w, h), (0, 0, 0))
        self.drawer = ImageDraw.Draw(self.img)

        self.bind("<Button-1>", self.start)
        self.bind("<B1-Motion>", self.draw)
        self.bind("<ButtonRelease-1>", self.stop)

        self.x, self.y = None, None
        self.actions, self.current = [], []

    def start(self, event):
        self.current = []
        self.x, self.y = event.x, event.y

    def draw(self, event):
        x, y = event.x, event.y
        if self.x and self.y:
            line_id = self.create_line((self.x, self.y, x, y), fill='white', width=5)
            self.drawer.line((self.x, self.y, x, y), fill='white', width=5)
            self.current.append((line_id, (self.x, self.y, x, y)))
            
        self.x, self.y = x, y

    def stop(self, event):
        self.x, self.y = None, None
        if self.current:
            self.actions.append(self.current)

    def clear(self):
        self.delete("all")
        self.img = Image.new("RGB", (self.winfo_width(), self.winfo_height()), (0, 0, 0))
        self.drawer = ImageDraw.Draw(self.img)
        self.actions = []

    def redraw(self):
        self.clear()
        for action in self.actions:
            for _, coords in action:
                self.drawer.line(coords, fill='white', width=5)
                self.create_line(coords, fill='white', width=5)

    def get_img(self):
        buf = BytesIO()
        self.img.save(buf, format="PNG")
        return buf.getvalue()

    def draw_result(self, result, font):
        if not self.actions:
            return
        last_action = self.actions[-1]
        _, last_coords = last_action[-1]
        eq_x, eq_y = last_coords[2], last_coords[3]
        x, y = eq_x + 50, eq_y - 20

        self.create_text(x, y, text=result, font=font, fill="#00FF00")
        font_pil = ImageFont.load_default(size=80)
        self.drawer.text((x, y - 50), result, font=font_pil, fill="#00FF00")
