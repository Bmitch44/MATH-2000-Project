from manim import *
import numpy as np

class TaylorSeriesSin(Scene):
    def construct(self):
        title = Text("Taylor Series Approximations of", color=YELLOW)
        subtitle = MathTex(r"\sin\left(\frac{\pi}{2x}\right)")
        title.next_to(subtitle, UP, buff=0.5)

        # scale the title
        target_height = min(4, self.camera.frame_height * 0.8 / title.height)
        target_width = min(8, self.camera.frame_width * 0.8 / title.width)
        scale_factor = min(target_height, target_width)
        title.scale(scale_factor)

        self.play(Write(title), Write(subtitle))
        self.wait(1)
        self.clear()

        plane = NumberPlane(
            x_range=[-1, 5],
            y_range=[-3, 3],
            x_length=15,
            y_length=8,
        )
        plane.add_coordinates()

        self.play(Create(plane))

        sin_funcL = ParametricFunction(
            lambda t: plane.c2p(t, np.sin(np.pi / (2 * t))),
            t_range=(0.001, 3, 0.001),
            color=YELLOW
        )

        sin_funcR = ParametricFunction(
            lambda t: plane.c2p(t, np.sin(np.pi / (2 * t))),
            t_range=(-2, -0.001, 0.001),
            color=YELLOW
        )
        sin_label = MathTex(r"\sin\left(\frac{\pi}{2x}\right)").next_to(sin_funcL.get_end(), RIGHT, buff=0.2)

        self.play(Create(sin_funcL), Create(sin_funcR), Write(sin_label), run_time=2)

        # Read the Taylor series terms from the file
        with open("taylor_series.csv", "r") as file:
            taylor_data = [list(map(float, line.strip().split(','))) for line in file]

        # Plot the Taylor series approximations
        colors = [BLUE, GREEN, RED, ORANGE, PINK, PURPLE, TEAL, GOLD, MAROON]

        def taylor_term_func(x, n, coef):
            return coef * ((x - 1) ** n)

        for term_index, coef in taylor_data[:10]:

            def taylor_function(t, term_index, coef):
                return sum(taylor_term_func(t, idx, c) for idx, c in taylor_data[:int(term_index) + 1])

            taylor_graph = ParametricFunction(
                lambda t: plane.c2p(t, taylor_function(t, term_index, coef)),
                t_range=(-1, 2, 0.01),
                color=colors[int(term_index) % len(colors)],
            )

            term_text = MathTex(f"T_{{{int(term_index)}}}(x)=", f"{coef:.3f}", r"(x - 1)^{", f"{int(term_index)}", "}")
            term_text.next_to(taylor_graph.get_end(), RIGHT, buff=0.2)

            self.play(Create(taylor_graph), Write(term_text), run_time=3)
            self.wait(2)
            self.play(FadeOut(term_text))

        self.wait(2)