import tkinter as tk



def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.cls

    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame, background="#D5FFFF")
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)
   
    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right,scene_bottom):
    
    
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.
    tree_center = scene_left + 500
    tree_top = scene_top + 300
    tree_height = 150
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)

    tree_center = scene_left + 300
    tree_top = scene_top + 258
    tree_height = 190
    draw_pine_tree2(canvas, tree_center, tree_top, tree_height)

    tree_center = scene_left + 400
    tree_top = scene_top + 279
    tree_height = 220
    draw_pine_tree2(canvas, tree_center, tree_top, tree_height)

    tree_center = scene_left + 200
    tree_top = scene_top + 310
    tree_height = 180
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)

    ground_center = scene_left + 500
    ground_top = scene_top + 400
    ground_height = 10 
    draw_ground(canvas, ground_center, ground_top, ground_height)

    sun_center = scene_left + 300
    sun_top = scene_top + 200
    sun_height = 50 
    draw_sun(canvas, sun_center, sun_top, sun_height)

    clound_center = scene_left + 200
    clound_top = scene_top + 200
    clound_height = 50 
    draw_clound(canvas, clound_center, clound_top, clound_height)

    clound_center = scene_left + 100
    clound_top = scene_top + 50
    clound_height = 50
  
     

# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.


def draw_pine_tree(canvas, peak_x, peak_y, height):
    
    trunk_width = height / 10
    trunk_height = height / 3
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    # Draw the trunk of the pine tree.
    canvas.create_rectangle(trunk_left, skirt_bottom,
            trunk_right, trunk_bottom, fill="tan3")

    # Draw the crown (also called skirt) of the pine tree.
    canvas.create_polygon(peak_x, peak_y,
            skirt_right, skirt_bottom,
            skirt_left, skirt_bottom, fill="dark green")


def draw_ground(canvas, peak_x, peack_y, height):

    x1 = 0
    x2 = 800
    y1 = 489
    y2 = 500
    canvas.create_rectangle(x1, y2, x2, y1, fill="#996633")

def draw_sun(canvas, peak_x, peak_y, height):

    x1 = 50
    x2 = 250
    y1 = 250
    y2 = 50
    
    canvas.create_oval(x1, x2, y1, y2, fill="yellow")

def draw_clound(canvas, peak_x, peak_y, height):

    x1 = 350
    x2 = 100
    y1 = 250
    y2 = 40
    
    canvas.create_oval(x1, x2, y1, y2, fill="white")        

def draw_pine_tree2(canvas, peak_x, peak_y, height):
    
    trunk_width = height / 9
    trunk_height = height / 5
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    # Draw the trunk of the pine tree.
    canvas.create_rectangle(trunk_left, skirt_bottom,
            trunk_right, trunk_bottom, fill="tan3")

    # Draw the crown (also called skirt) of the pine tree.
    canvas.create_polygon(peak_x, peak_y,
            skirt_right, skirt_bottom,
            skirt_left, skirt_bottom, fill="dark green")



# Call the main function so that
# this program will start executing.
main()