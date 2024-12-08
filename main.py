import tkinter as tk
from tkinter import ttk, colorchooser, filedialog, messagebox
import turtle
from PIL import Image, ImageTk
import io
import random
from pyswirl import swirl


class SwirlApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Swirl Art Generator")
        self.root.geometry("1200x800")  # Set the initial window size

        # Setup main frame
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill="both", expand=True)

        # Setup left frame for controls
        self.controls_frame = tk.Frame(self.main_frame, width=300)
        self.controls_frame.pack(side="left", fill="y")

        # Setup canvas for turtle graphics
        self.canvas_frame = tk.Frame(self.main_frame)
        self.canvas_frame.pack(side="right", fill="both", expand=True)

        self.canvas = tk.Canvas(self.canvas_frame, width=1000, height=1000)  # Canvas size changed to 1000x1000
        self.canvas.pack(fill="both", expand=True)

        # Initialize the turtle screen
        self.screen = turtle.TurtleScreen(self.canvas)
        self.screen.bgcolor("#ffffff")
        self.screen.tracer(0)  # Turn off automatic updates for smoother drawing
        self.swirl_obj = swirl(self.canvas)

        # Control variables
        self.selected_angle = tk.IntVar(value=10)
        self.selected_iterations = tk.IntVar(value=500)
        self.selected_color_palette = tk.StringVar(value="#537c78, #7ba591, #cc222b, #f15b4c, #faa41b, #ffd45b")
        self.selected_background_color = tk.StringVar(value="#ffffff")
        self.selected_pen_color = tk.StringVar(value="#000000")
        self.change_width_var = tk.BooleanVar(value=False)
        self.selected_line_style = tk.StringVar(value="line")
        self.style_var = tk.StringVar(value="default")

        # Add controls to the left frame
        self.create_controls()

    def create_controls(self):

        # Line style dropdown (Line, Circle, Rhombus)
        self.line_style_label = tk.Label(self.controls_frame, text="Line Style:")
        self.line_style_label.pack()
        self.line_style_dropdown = ttk.Combobox(self.controls_frame, textvariable=self.selected_line_style, values=["line", "circle", "rhombus"], state="readonly", width=15)
        self.line_style_dropdown.pack()

        # Angle controls
        self.angle_label = tk.Label(self.controls_frame, text="Angle:")
        self.angle_label.pack()
        self.angle_entry = tk.Entry(self.controls_frame, textvariable=self.selected_angle)
        self.angle_entry.pack()

        # Iteration controls
        self.iterations_label = tk.Label(self.controls_frame, text="Iterations:")
        self.iterations_label.pack()
        self.iterations_entry = tk.Entry(self.controls_frame, textvariable=self.selected_iterations)
        self.iterations_entry.pack()

        # Background color input
        self.bg_color_label = tk.Label(self.controls_frame, text="Background Color:")
        self.bg_color_label.pack()
        self.bg_color_entry = tk.Entry(self.controls_frame, textvariable=self.selected_background_color)
        self.bg_color_entry.pack()

        # Color palette input
        self.color_palette_label = tk.Label(self.controls_frame, text="Color Palette (comma separated):")
        self.color_palette_label.pack()
        self.color_palette_entry = tk.Entry(self.controls_frame, textvariable=self.selected_color_palette)
        self.color_palette_entry.pack()

        # Add other control buttons (Pause, Resume)
        self.pause_button = tk.Button(self.controls_frame, text="Pause", command=self.pause_animation)
        self.pause_button.pack()
        self.resume_button = tk.Button(self.controls_frame, text="Resume", command=self.resume_animation)
        self.resume_button.pack()

        # Start drawing button
        self.start_button = tk.Button(self.controls_frame, text="Start", command=self.draw_swirl)
        self.start_button.pack()

        # Clear canvas button
        self.clear_button = tk.Button(self.controls_frame, text="Clear", command=self.clear_canvas)
        self.clear_button.pack()
        
        # Reset button
        self.reset_button = tk.Button(self.controls_frame, text="Reset", command=self.reset_settings)
        self.reset_button.pack()

        # Demo button to trigger the demo animation
        self.demo_button = tk.Button(self.controls_frame, text="Demo", command=self.play_demo)
        self.demo_button.pack()

    def play_demo(self):
        self.swirl_obj.demo()
        
    # Reset Settings Method
    def reset_settings(self):
        # Reset all variables to default values
        self.selected_angle.set(10)
        self.selected_iterations.set(500)
        self.selected_color_palette.set("#537c78, #7ba591, #cc222b, #f15b4c, #faa41b, #ffd45b")
        self.selected_background_color.set("#ffffff")
        self.selected_pen_color.set("#000000")
        self.change_width_var.set(False)
        self.selected_line_style.set("line")
        self.style_var.set("default")
        
        # Clear the canvas and reset the spiral
        self.swirl_obj.reset()
        self.canvas.delete("all")  # Clears the canvas

    def pause_animation(self):
        self.swirl_obj.paused = True

    def resume_animation(self):
        self.swirl_obj.paused = False

        color_palette = self.selected_color_palette.get()
        colors = [color.strip() for color in color_palette.split(",")]
        self.swirl_obj.color_palette = colors
        self.swirl_obj.spiral.screen.bgcolor(self.selected_background_color.get())
        
        # Start drawing
        self.angle = self.selected_angle.get()
        self.total_iterations = self.selected_iterations.get()
        self.circles = self.selected_line_style.get() == "circle"
        self.rhombus = self.selected_line_style.get() == "rhombus"
        self.swirl_obj.draw(self.angle, self.total_iterations, change_width=True, circles=self.circles, rhombus=self.rhombus)

    def draw_swirl(self):
        self.swirl_obj.paused = False
        self.clear_canvas()

        color_palette = self.selected_color_palette.get()
        colors = [color.strip() for color in color_palette.split(",")]
        self.swirl_obj.color_palette = colors
        self.swirl_obj.spiral.screen.bgcolor(self.selected_background_color.get())
        
        # Start drawing
        self.angle = self.selected_angle.get()
        self.total_iterations = self.selected_iterations.get()
        self.circles = self.selected_line_style.get() == "circle"
        self.rhombus = self.selected_line_style.get() == "rhombus"
        self.swirl_obj.draw(self.angle, self.total_iterations, change_width=True, circles=self.circles, rhombus=self.rhombus)

    def clear_canvas(self):
        self.swirl_obj.reset()


if __name__ == "__main__":
    root = tk.Tk()
    app = SwirlApp(root)
    root.mainloop()
