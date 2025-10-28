from tkinter import Tk, Canvas, Frame, BOTH

def main():
    root = Tk()
    Scene()

    root.geometry("800x600")
    root.mainloop()

class Scene(Frame):

    def _init_(self):

        super()._init_()

        self.master.title("Scene")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.pack(fill=BOTH, expand=1)

        draw_scene(canvas, 0, 0, 799, 599)

def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    
    draw_grid(canvas, scene_left, scene_top, scene_right, scene_bottom, 100)

def draw_grid(canvas, left, top, right, bottom, grid_space):
    
    for i in range(top, bottom, grid_space):
        canvas.create_line(left, i, right, i)


        
main()