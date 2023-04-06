import numpy as np
from manim import *


class TaylorSeries(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        with open('taylor_series.txt', 'r') as f:
            lines = f.readlines()

        taylor_terms = []
        for line in lines[:10]:
            # Split the line by the pipe delimiter
            n, fn_x, fn_1, tn_x = line.strip().split("|")

            # Create the three MathTex objects
            n_term = MathTex(f"{n}")
            fn_x_term = MathTex(f"{fn_x}")
            fn_1_term = MathTex(f"{fn_1}")
            tn_x_term = MathTex(f"{tn_x}")

            # Create the VGroup for this line and position the terms
            line_group = VGroup(n_term, fn_x_term, fn_1_term, tn_x_term).arrange(DOWN, aligned_edge=LEFT, buff=0.5)

            # Append this line's group to the list of terms
            taylor_terms.append(line_group)

        term_groups = [taylor_terms[i:i+4] for i in range(0, len(taylor_terms), 4)]

        for group in term_groups:
            for term in group:
                # Save the current state of the camera frame
                self.camera.frame.save_state()

                # Calculate the scale factor to fit the terms on the screen
                terms_height = term.height
                terms_width = term.width
                scale_factor_h = 0.8 * self.camera.frame.height / terms_height if terms_height > self.camera.frame.height * 0.8 else 1
                scale_factor_w = 0.8 * self.camera.frame.width / terms_width if terms_width > self.camera.frame.width * 0.8 else 1
                scale_factor = min(scale_factor_h, scale_factor_w)

                # Animate camera frame position and scale
                self.play(
                    self.camera.frame.animate.set_center(term.get_center()),
                    self.camera.frame.animate.scale(1 / scale_factor),
                    run_time=0.5
                )

                # Show terms one by one
                self.play(Create(term))
                self.wait(3)

                # Uncreate terms
                self.play(Uncreate(term))
                self.wait(2)

                # Reset the camera frame to its original position and scale
                self.play(
                    Restore(self.camera.frame),
                    run_time=0.5
                )
