from manim import *
from math import factorial


class Intro(Scene):
    def construct(self):
        # add title to the scene project funtion is f(x) = sin(pi/2*x)
        project_function = MathTex(r"f(x) = \sin(\frac{\pi}{2x})")
        title = Text("Taylor Series of ", font="Arial", color=BLUE).next_to(project_function, UP)
        names = Text("Brady Mitchelmore, Maria Yaranga, Evan Best", font="Arial", color=BLUE).next_to(title, UP)
        project = Text("MATH 2000 - Group Project", font="Arial", color=BLUE).next_to(names, UP)

        # Create a VGroup that contains both project_function and title
        project_title = VGroup(project, names, title, project_function).arrange(DOWN)
        
        # scale the title
        target_height = min(4, self.camera.frame_height * 0.7 / project_title.height)
        target_width = min(8, self.camera.frame_width * 0.7 / project_title.width)
        scale_factor = min(target_height, target_width)
        title.scale(scale_factor)

        self.play(Write(project_title))
        self.wait(2)
        self.play(FadeOut(project_title), run_time=5)
        self.clear()