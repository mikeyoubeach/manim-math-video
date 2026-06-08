"""Manim 效果展示 - 30秒混剪"""
from manim import *
import numpy as np

BG = "#0d1117"
C1 = "#4fc3f7"
C2 = "#e8a87c"
C3 = "#7ed3a4"
TXT = "#e4e2d8"

config.background_color = BG
config.frame_rate = 30
config.pixel_width = 1920
config.pixel_height = 1080


class MathShowcase(Scene):
    def construct(self):
        # ═══ 1. 形状变形 (0-5s) ═══
        circle = Circle(radius=1.2, color=C1, stroke_width=3)
        square = Square(side_length=2.4, color=C2, stroke_width=3)
        triangle = Triangle(color=C3, stroke_width=3).scale(1.4)

        self.play(Create(circle), run_time=0.8)
        self.wait(0.5)
        self.play(Transform(circle, square), run_time=1.0)
        self.wait(0.3)
        self.play(Transform(circle, triangle), run_time=1.0)
        self.wait(0.5)
        self.play(FadeOut(circle), run_time=0.5)

        # ═══ 2. 函数 + 导数切线 (5-12s) ═══
        axes = Axes(
            x_range=[-3, 3, 1], y_range=[-2, 4, 1],
            x_length=8, y_length=4.5,
            axis_config={"color": GREY, "stroke_width": 1.5},
        ).shift(DOWN * 0.3)

        curve = axes.plot(lambda x: 0.3 * x ** 2, x_range=[-2.5, 2.5], color=C1, stroke_width=2.5)
        curve_label = MathTex("y = 0.3x^2", color=C1, font_size=28).next_to(axes.c2p(2, 1.5), UR, buff=0.2)

        self.play(Create(axes), run_time=0.6)
        self.play(Create(curve), run_time=1.2)
        self.play(FadeIn(curve_label), run_time=0.5)

        # 切线动画 - 用 ValueTracker
        tracker = ValueTracker(-2)

        dot = always_redraw(lambda: Dot(
            axes.c2p(tracker.get_value(), 0.3 * tracker.get_value() ** 2),
            color=C2, radius=0.12
        ))

        tangent = always_redraw(lambda: axes.plot(
            lambda x: 0.6 * tracker.get_value() * (x - tracker.get_value()) + 0.3 * tracker.get_value() ** 2,
            x_range=[tracker.get_value() - 1, tracker.get_value() + 1],
            color=C2, stroke_width=2
        ))

        self.play(FadeIn(dot), Create(tangent), run_time=0.5)
        self.play(tracker.animate.set_value(2), run_time=3.5, rate_func=smooth)
        self.wait(0.5)

        # 导数公式
        deriv = MathTex(r"\frac{d}{dx}(0.3x^2) = 0.6x", color=C2, font_size=30)
        deriv.to_corner(UR, buff=0.5)
        self.play(Write(deriv), run_time=0.8)
        self.wait(0.5)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)

        # ═══ 3. 黎曼和→积分 (12-20s) ═══
        axes2 = Axes(
            x_range=[0, 3.5, 1], y_range=[0, 10, 2],
            x_length=8, y_length=4.5,
            axis_config={"color": GREY, "stroke_width": 1.5},
        ).shift(DOWN * 0.3)
        curve2 = axes2.plot(lambda x: x ** 2, x_range=[0, 3], color=C1, stroke_width=2.5)

        self.play(Create(axes2), Create(curve2), run_time=0.8)

        # 矩形逐步加密
        rects = None
        for n in [4, 8, 16, 32]:
            new_rects = axes2.get_riemann_rectangles(
                curve2, x_range=[0, 3], dx=3/n,
                stroke_width=0.5, stroke_color=WHITE,
                color=[C2, C3], fill_opacity=0.3,
            )
            if rects is None:
                rects = new_rects
                self.play(Create(rects), run_time=0.8)
            else:
                self.play(Transform(rects, new_rects), run_time=0.6)
            self.wait(0.3)

        # → 平滑面积
        area = axes2.get_area(curve2, x_range=[0, 3], color=[C1, C3], opacity=0.25)
        self.play(FadeOut(rects), FadeIn(area), run_time=1.0)

        integral = MathTex(r"\int_0^3 x^2\,dx = 9", color=C2, font_size=40)
        integral.to_edge(UP, buff=0.5)
        self.play(Write(integral), run_time=0.8)
        self.wait(0.5)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)

        # ═══ 4. 傅里叶叠加 (20-28s) ═══
        axes3 = Axes(
            x_range=[0, 4 * PI, PI], y_range=[-1.5, 1.5, 0.5],
            x_length=10, y_length=4,
            axis_config={"color": GREY, "stroke_width": 1.5},
        ).shift(DOWN * 0.3)

        self.play(Create(axes3), run_time=0.5)

        # 方波参考线
        sq = axes3.plot(lambda x: np.sign(np.sin(x)), x_range=[0.01, 4 * PI - 0.01],
                        color=GREY, stroke_width=1.5, discontinuities=[PI, 2*PI, 3*PI])
        self.play(Create(sq), run_time=0.5)

        # 逐个叠加谐波
        fourier_curve = None
        colors = [C1, C2, C3, "#b86b5e", "#d4a574"]

        for n_harmonics in [1, 3, 5, 9, 15]:
            def make_func(n):
                def f(x):
                    return sum(np.sin((2*k-1)*x) / (2*k-1) for k in range(1, n+1)) * (4/np.pi)
                return f

            new_curve = axes3.plot(make_func(n_harmonics), x_range=[0, 4*PI], color=C1, stroke_width=2.5)

            if fourier_curve is None:
                fourier_curve = new_curve
                self.play(Create(fourier_curve), run_time=0.8)
            else:
                self.play(Transform(fourier_curve, new_curve), run_time=0.7)

            # 谐波数标签
            label = MathTex(f"n = {n_harmonics}", color=C2, font_size=28)
            label.next_to(axes3, RIGHT, buff=0.3).shift(UP * 0.5)
            self.play(FadeIn(label), run_time=0.3)
            self.wait(0.4)
            self.play(FadeOut(label), run_time=0.2)

        fourier_label = MathTex(r"f(x) = \sum \frac{4}{n\pi}\sin(nx)", color=C1, font_size=28)
        fourier_label.to_edge(UP, buff=0.5)
        self.play(Write(fourier_label), run_time=0.8)
        self.wait(1)

