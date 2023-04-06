from manim import *
import numpy as np
import re

def extract_an_values(file_path):
    an_values = []

    with open(file_path, 'r') as file:
        for line in file:
            n, fn_x, fn_1, tn_x, an1 = line.strip().split("|")
            an = float(an1)
            an_values.append(an)

    return an_values

def an_nth_root(an, n):
    if an >= 0:
        if n != 0:
            return an**(1/n)
        else:
            return 0
    else:
        r = abs(an)
        theta = np.angle(an)
        result = r**(1/n) * (np.cos(theta/n) + 1j * np.sin(theta/n))
        return result

class AnTermsScene(Scene):
    def construct(self):
        an_values = extract_an_values('taylor_series.txt')
        n_max = len(an_values)
        points = []

        for n in range(n_max):
            term = an_nth_root(an_values[n], n)
            points.append(np.array([n, term.real, 0]))

        # Create a graph using the points
        graph = VMobject()
        graph.set_points_as_corners(points)
        graph.set_color(YELLOW)

        # Create axes
        axes = Axes(
            x_range=[0, n_max, 1],
            y_range=[-2, 2, 1],  # Adjust y_range as needed
            x_length=10,
            y_length=6,
            axis_config={"include_tip": True},
            y_axis_config={"label_direction": UP},
            tips=False,
        )

        # Label axes
        x_labels = axes.x_axis.get_tick_marks()
        y_labels = axes.y_axis.get_tick_marks()

        self.play(Create(axes))
        self.play(Write(x_labels), Write(y_labels))

        # Add graph to the scene
        self.play(Create(graph))
        self.wait(2)

# if __name__ == "__main__":
#     from manim import *
#     config.media_width = "60%"
#     config.background_color = WHITE
#     scene = AnTermsScene()
#     scene.render()
