from manim import *

class UniformCircularMotionExplained(MovingCameraScene):
    def construct(self):
        # Create the text in the center with a box and underline
        intro_text = Tex("What is Uniform Circular Motion?", font_size=48)
        intro_box = SurroundingRectangle(intro_text, color=BLUE, buff=0.2)
        underline = Line(start=LEFT, end=RIGHT).set_width(intro_text.width).next_to(intro_text, DOWN, buff=0.1)

        # Group the text, box, and underline
        intro_group = VGroup(intro_text, intro_box, underline).move_to(ORIGIN)

        # Play the animation of the text appearing
        self.play(Write(intro_text), Create(intro_box), Create(underline))
        self.wait(1)

        # Shrink the group and move it slightly up
        self.play(
            intro_group.animate.scale(0.6).to_edge(UP),  # Adjust the factor to control how far it moves up
            run_time=2
        )
        self.wait(2)
