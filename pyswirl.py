import tkinter as tk
from tkinter import ttk, colorchooser, filedialog, messagebox
import turtle
import datetime
from PIL import Image, ImageTk
import io
import random

class swirl:
    def __init__(self, canvas):
        self.spiral = turtle.RawTurtle(canvas)
        self.cursor_speed = 100
        self.spiral.speed(self.cursor_speed)
        self.spiral.hideturtle()
        self.width_bias = 0
        self.dist = 1
        self.paused = False  # Track if the animation is paused
        self.iteration = 0  # Track current iteration
        self.total_iterations = 0  # Track total iterations

        

    def reset(self):
        # Set the initial position of the pen to the center of the canvas
        self.spiral.penup()
        self.spiral.setposition(500, 500)  # Set the initial position at 200x500
        self.spiral.home()
        self.spiral.clear()
        self.spiral.pencolor("")  # Keep the pencolor blank
        self.spiral.width(1 / 100 + 1)
        self.dist = 1
        self.width_bias = 0
        self.iteration = 0  # Reset iteration on reset


    def random_hex_colors(self, num_colors):
        hex_digits = "0123456789ABCDEF"
        colors = []
        for _ in range(num_colors):
            color = "#" + "".join(random.choice(hex_digits) for _ in range(6))
            colors.append(color)
        return colors

    def get_random_colors(self):
        return self.random_hex_colors(random.randint(4, 30))

    def change_width(self):
        self.spiral.width(self.dist / 200 + 1)
        self.width_bias += 1

    def settings(self, style=None, background_color: str = None, pen_color: str = None):
        # Default color palette
        if style == "random":
            random_colors = self.get_random_colors()
            self.color_palette = self.random_hex_colors(random.randint(4, 30))
            self.spiral.screen.bgcolor(random_colors[0])
        elif style == "default":
            # Default color palette
            self.color_palette = ['#537c78', '#7ba591', '#cc222b', '#f15b4c', '#faa41b', '#ffd45b']
            self.spiral.screen.bgcolor("#ffffff")
        else:
            if background_color:
                self.spiral.screen.bgcolor(background_color)
            if pen_color:
                self.spiral.pencolor(pen_color)

    def draw(self, angle, iterations=500, change_width=False, circles=False, rhombus=False):
        self.total_iterations = iterations
        self.spiral.pendown()  # Start drawing
        self.spiral.screen.tracer(1)  # Enable drawing updates

        while self.iteration < iterations and not self.paused:
            self.spiral.pencolor(self.color_palette[self.dist % len(self.color_palette)])
            self.spiral.speed('fastest')
            if change_width:
                self.change_width()
            if circles:
                self.spiral.circle(self.dist)
            if rhombus:
                for _ in range(4):
                    self.spiral.forward(self.dist)
                    self.spiral.right(60)
            self.spiral.forward(self.dist)
            self.spiral.right(angle)
            self.dist += 1
            self.cursor_speed += 2000
            self.spiral.speed(self.cursor_speed)

            self.iteration += 1
            self.spiral.screen.update()  # Update screen manually for smoother animation
    def demo(self):
        angles = [
            x for x in range(24, 361, 12) if x%2 ==0 or x%3 ==0
        ]
        Default = ['#537c78', '#7ba591', '#cc222b', '#f15b4c', '#faa41b', '#ffd45b']
        Vibrant = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8']
        Monochrome = ['#f2f2f2', '#d9d9d9', '#bfbfbf', '#a6a6a6', '#8c8c8c']
        demo_settings = []
        for ang in angles:
            demo_settings.append((ang, Default, False, False))
            demo_settings.append((ang, Default, True, False))
            demo_settings.append((ang, Default, False, True))
            demo_settings.append((ang, Monochrome, False, False))
            demo_settings.append((ang, Monochrome, True, False))
            demo_settings.append((ang, Monochrome, False, True))
            demo_settings.append((ang, Vibrant, False, False))
            demo_settings.append((ang, Vibrant, True, False))
            demo_settings.append((ang, Vibrant, False, True))
        random.shuffle(demo_settings)
        # Iterate through the demo settings and draw each one
        for angle, colors, is_circle, is_rhombus in demo_settings:
            self.color_palette = colors
            self.spiral.screen.bgcolor('#000000')
            self.draw(angle, iterations=20, change_width=True, circles=is_circle, rhombus=is_rhombus)
            self.reset()