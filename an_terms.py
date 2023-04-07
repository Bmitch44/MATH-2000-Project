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
        # add title to the scene project funtion is a_n^(1/n)
        project_function = MathTex(r"a_n^{\frac{1}{n}}")
        title = Text("Plotting the Coefficients of:", font="Arial", color=BLUE).next_to(project_function, LEFT)

        # Create a VGroup that contains both project_function and title
        project_title = VGroup(title, project_function).arrange(DOWN)
        
        # scale the title
        target_height = min(4, self.camera.frame_height * 0.8 / project_title.height)
        target_width = min(8, self.camera.frame_width * 0.8 / project_title.width)
        scale_factor = min(target_height, target_width)
        title.scale(scale_factor)

        self.play(Write(project_title))
        self.wait(2)
        self.play(FadeOut(project_title), run_time=3)
        self.clear()

        an_values = extract_an_values('taylor_series.txt')
        an1n_values = [an**(1/n) for n, an in enumerate(an_values) if an > 0 and n > 0 ]
        print(an1n_values)
        n_max = len(an1n_values)
        x_values = list(range(1, n_max+1))

        # Create a NumberPlane with grid lines
        plane = NumberPlane(
            x_range=[0, n_max, 1],
            y_range=[0, 2, 0.1],
            x_length=10,
            y_length=6,
            axis_config={"include_tip": True},
            y_axis_config={"label_direction": UP},
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 1.5,
                "stroke_opacity": 0.5,
            },
        )

        # Label axes
        x_labels, y_labels = plane.get_axis_labels("n", "a_n^{(1/n)}")

        self.play(Create(plane))
        self.play(Write(x_labels), Write(y_labels))

        # Plot the line graph
        line_graph = plane.plot_line_graph(
            x_values,
            an1n_values,
            line_color='#FF0000',
            add_vertex_dots=True,
            vertex_dot_radius=0.05,
            vertex_dot_style=None,
        )

        # Reverse the order of line and dots creation
        self.play(Create(line_graph["vertex_dots"]), run_time=10)
        self.play(Create(line_graph["line_graph"]), run_time=10)

        self.wait(2)

