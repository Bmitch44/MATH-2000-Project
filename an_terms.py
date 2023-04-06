from manim import *
import numpy as np
from math import factorial

def extract_an_values(file_path):
    an_values = []

    with open(file_path, 'r') as file:
        for line in file:
            n, fn_x, fn_1, tn_x, an1 = line.strip().split("|")
            an = float(an1)/factorial(int(n.split('=')[-1]))
            an_values.append(an)

    return an_values

class AnTermsScene(Scene):
    def construct(self):
        an_values = extract_an_values('taylor_series.txt')
        an1n_values = [an**(1/n) for n, an in enumerate(an_values) if an > 0 and n > 0 ]
        print(an1n_values)
        n_max = len(an1n_values)
        x_values = list(range(1, n_max+1))

        # Create axes
        axes = Axes(
            x_range=[0, n_max, 1],
            y_range=[min(an1n_values), max(an1n_values), 1],  # Adjust y_range to start at the minimum value of an1n_values
            x_length=10,
            y_length=6,
            axis_config={"include_tip": True},
            y_axis_config={"label_direction": UP},
            tips=False,
        )

        # Label axes
        x_labels, y_labels = axes.get_axis_labels("n", "a_n^{(1/n)}")

        self.play(Create(axes))
        self.play(Write(x_labels), Write(y_labels))

        # Plot the line graph
        line_graph = axes.plot_line_graph(
            x_values,
            an1n_values,
            line_color='#FF0000',
            add_vertex_dots=True,
            vertex_dot_radius=0.1,
            vertex_dot_style=None,
        )

        # Reverse the order of line and dots creation
        self.play(Create(line_graph["vertex_dots"]), run_time=10)
        self.play(Create(line_graph["line_graph"]), run_time=10)

        self.wait(2)
