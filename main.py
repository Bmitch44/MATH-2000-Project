from manim import *
from math import factorial


class TaylorSeries(Scene):
    def construct(self):
        # add title to the scene project funtion is f(x) = sin(pi/2*x)
        project_function = MathTex(r"f(x) = \sin(\frac{\pi}{2}x)")
        title = Text("Taylor Series of ", font="Arial", color=BLUE).next_to(project_function, UP)

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

        with open('taylor_series.txt', 'r') as f:
            lines = f.readlines()

        taylor_terms = []
        for line in lines[:10]:
            # Split the line by the pipe delimiter
            n, fn_x, fn_1, tn_x, a1n = line.strip().split("|")
            an = float(a1n) / factorial(int(n.split('=')[-1]))

            # Create the MathTex objects
            n_term = MathTex(f"{n}")
            fn_x_term = MathTex(f"{fn_x}")
            fn_1_term = MathTex(f"{fn_1}")
            tn_x_term = MathTex(f"{tn_x}")
            anfact_term = MathTex(f"a_n = {an}")

            # Create the VGroup for this line and position the terms
            line_group = VGroup(n_term, fn_x_term, fn_1_term, tn_x_term, anfact_term).arrange(DOWN, aligned_edge=LEFT, buff=0.5)

            # Append this line's group to the list of terms
            taylor_terms.append(line_group)

        for term_group in taylor_terms:

            # Scale the group dynamically based on its size
            target_height = min(4, self.camera.frame_height * 0.8 / term_group.height)
            target_width = min(8, self.camera.frame_width * 0.8 / term_group.width)
            scale_factor = min(target_height, target_width)
            term_group.scale(scale_factor)

            self.play(Write(term_group[0]))

            for i in range(1, len(term_group)):
                self.play(TransformMatchingTex(term_group[i - 1], term_group[i]))
                self.wait(1)

            self.play(FadeOut(term_group), run_time=3)
            self.wait(0.5)
            self.clear()
