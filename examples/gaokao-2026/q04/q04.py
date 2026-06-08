"""2026高考数学第4题 - 切线方程可视化（白色主题）"""
from manim import *
import numpy as np

BG = "#FFFFFF"
TXT = "#2D3436"
DIM = "#B2BEC3"
BLUE = "#4fc3f7"
GREEN = "#00B894"
AMBER = "#e8a87c"
PINK = "#FF6B9D"
CORAL = "#c97b5d"

config.background_color = BG
config.frame_rate = 30
config.pixel_width = 1920
config.pixel_height = 1080

# TTS 时间轴（14段）
T = [0.0, 2.1, 8.84, 11.58, 14.96, 20.1, 25.08, 28.78, 31.52, 35.38, 38.92, 40.86, 45.52, 48.9]


class Q04(Scene):
    def construct(self):
        elapsed = 0.0

        def wait_to(seg_idx):
            nonlocal elapsed
            if seg_idx >= len(T):
                return
            gap = T[seg_idx] - elapsed
            if gap > 0.05:
                self.wait(gap)
                elapsed += gap

        def play_anim(seg_idx, *args, **kwargs):
            nonlocal elapsed
            self.play(*args, **kwargs)
            elapsed += kwargs.get("run_time", 1.0)

        # ═══ seg 0: 0.0s "我们来看第4题" ═══
        title = Text("第 4 题", font="Microsoft YaHei", font_size=56, color=TXT)
        subtitle = Text("2026年新高考一卷", font="Microsoft YaHei", font_size=24, color=DIM)
        subtitle.next_to(title, DOWN, buff=0.4)

        play_anim(0, FadeIn(title, shift=DOWN * 0.3), run_time=0.8)
        play_anim(0, FadeIn(subtitle), run_time=0.5)
        wait_to(1)

        # ═══ seg 1: 2.1s "曲线y=5x+8lnx 在点(1,5)处的切线方程" ═══
        problem = VGroup(
            Text("曲线", font="Microsoft YaHei", font_size=30, color=TXT),
            MathTex(r"y = 5x + 8\ln x", font_size=36, color=BLUE),
            Text("在点 (1, 5) 处的切线方程为？", font="Microsoft YaHei", font_size=30, color=TXT),
        ).arrange(RIGHT, buff=0.3)
        problem.next_to(title, DOWN, buff=0.8)

        options = VGroup(
            MathTex(r"\text{A. } y = 3x + 2", font_size=26, color=DIM),
            MathTex(r"\text{B. } y = 5x", font_size=26, color=DIM),
            MathTex(r"\text{C. } y = 8x - 3", font_size=26, color=DIM),
            MathTex(r"\text{D. } y = 13x - 8", font_size=26, color=DIM),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        options.next_to(problem, DOWN, buff=0.5, aligned_edge=LEFT)

        all_text = VGroup(problem, options)

        play_anim(1, FadeOut(subtitle), run_time=0.3)
        play_anim(1, FadeIn(all_text, shift=UP * 0.2), run_time=0.5)
        play_anim(1, title.animate.to_edge(UP, buff=0.4).scale(0.6), run_time=0.5)
        play_anim(1, all_text.animate.move_to(ORIGIN), run_time=0.5)
        wait_to(2)

        # ═══ seg 2: 8.84s "首先，画出这条曲线" ═══
        play_anim(2, FadeOut(all_text), run_time=0.3)

        axes = Axes(
            x_range=[0, 4, 1], y_range=[-5, 25, 5],
            x_length=8, y_length=5.5,
            axis_config={"color": DIM, "stroke_width": 1.5, "include_tip": True},
        ).shift(DOWN * 0.3 + RIGHT * 0.5)

        x_lab = MathTex("x", color=DIM, font_size=22).next_to(axes.x_axis.get_end(), DOWN, buff=0.1)
        y_lab = MathTex("y", color=DIM, font_size=22).next_to(axes.y_axis.get_end(), LEFT, buff=0.1)

        def f(x):
            return 5 * x + 8 * np.log(x)

        curve = axes.plot(f, x_range=[0.15, 3.5], color=BLUE, stroke_width=3)

        play_anim(2, Create(axes), FadeIn(x_lab), FadeIn(y_lab), run_time=0.8)
        play_anim(2, Create(curve), run_time=1.5)

        curve_lab = MathTex(r"y = 5x + 8\ln x", color=BLUE, font_size=28)
        curve_lab.next_to(axes.c2p(2.5, f(2.5)), UR, buff=0.3)
        play_anim(2, FadeIn(curve_lab), run_time=0.5)
        wait_to(3)

        # ═══ seg 3: 11.58s "对数函数和一次函数的叠加" ═══
        line_part = axes.plot(lambda x: 5 * x, x_range=[0.1, 3.5], color=DIM, stroke_width=1.5)
        log_part = axes.plot(lambda x: 8 * np.log(x), x_range=[0.15, 3.5], color=DIM, stroke_width=1.5)
        line_lab = MathTex("5x", color=DIM, font_size=22).next_to(axes.c2p(3, 15), LEFT, buff=0.2)
        log_lab = MathTex(r"8\ln x", color=DIM, font_size=22).next_to(axes.c2p(2.5, 8), DOWN, buff=0.2)

        play_anim(3, Create(line_part), FadeIn(line_lab), run_time=0.8)
        play_anim(3, Create(log_part), FadeIn(log_lab), run_time=0.8)
        wait_to(4)

        # ═══ seg 4: 14.96s "x趋向零时，lnx趋向负无穷" ═══
        asy_line = DashedLine(axes.c2p(0.15, -5), axes.c2p(0.15, 25), color=AMBER, stroke_width=1.5)
        asy_lab = Text("x → 0⁺", font="Microsoft YaHei", font_size=20, color=AMBER)
        asy_lab.next_to(asy_line, RIGHT, buff=0.2)
        arrow = CurvedArrow(axes.c2p(0.5, f(0.5)), axes.c2p(0.2, -3), color=AMBER, stroke_width=2, angle=-0.5)
        inf_lab = MathTex(r"y \to -\infty", color=AMBER, font_size=24)
        inf_lab.next_to(arrow, DOWN, buff=0.1)

        play_anim(4, Create(asy_line), FadeIn(asy_lab), run_time=0.8)
        play_anim(4, Create(arrow), FadeIn(inf_lab), run_time=0.8)
        wait_to(5)

        # ═══ seg 5: 20.1s "x增大，5x占主导" ═══
        play_anim(5, FadeOut(arrow), FadeOut(inf_lab), FadeOut(asy_line), FadeOut(asy_lab),
                  FadeOut(line_part), FadeOut(log_part), FadeOut(line_lab), FadeOut(log_lab), run_time=0.5)

        asy_line2 = axes.plot(lambda x: 5 * x, x_range=[0.5, 3.5], color=AMBER, stroke_width=1.5)
        asy_lab2 = MathTex(r"y \approx 5x\ (x \gg 1)", color=AMBER, font_size=22)
        asy_lab2.next_to(axes.c2p(3, 15), UR, buff=0.2)

        play_anim(5, Create(asy_line2), run_time=0.8)
        play_anim(5, FadeIn(asy_lab2), run_time=0.5)
        wait_to(6)

        # ═══ seg 6: 25.08s "在x等于1这个点的切线" ═══
        play_anim(6, FadeOut(asy_line2), FadeOut(asy_lab2), run_time=0.5)

        dot = Dot(axes.c2p(1, 5), color=GREEN, radius=0.12)
        dot_lab = MathTex(r"(1,\, 5)", color=GREEN, font_size=24)
        dot_lab.next_to(dot, DR, buff=0.15)
        pulse = Circle(radius=0.3, color=GREEN, stroke_width=2).move_to(dot.get_center())

        play_anim(6, FadeIn(dot), Write(dot_lab), run_time=0.6)
        play_anim(6, pulse.animate.scale(2).set_opacity(0), run_time=0.8)
        wait_to(7)

        # ═══ seg 7: 28.78s "切线斜率=导数" ═══
        deriv_concept = MathTex(r"\text{Tangent slope} = y'", color=PINK, font_size=32)
        deriv_concept.to_corner(UR, buff=0.6).shift(DOWN * 0.5)
        play_anim(7, Write(deriv_concept), run_time=0.8)
        wait_to(8)

        # ═══ seg 8: 31.52s "y'=5+8/x" ═══
        deriv_calc = MathTex(r"y' = 5 + \frac{8}{x}", color=PINK, font_size=32)
        deriv_calc.next_to(deriv_concept, DOWN, aligned_edge=LEFT, buff=0.4)
        play_anim(8, Write(deriv_calc), run_time=1.0)
        wait_to(9)

        # ═══ seg 9: 35.38s "x=1, k=13" ═══
        slope_calc = MathTex(r"x=1 \Rightarrow k = 5 + 8 = 13", color=AMBER, font_size=30)
        slope_calc.next_to(deriv_calc, DOWN, aligned_edge=LEFT, buff=0.4)
        play_anim(9, Write(slope_calc), run_time=1.0)

        k_lab = MathTex(r"k = 13", color=AMBER, font_size=36)
        k_lab.next_to(slope_calc, DOWN, buff=0.5)
        play_anim(9, FadeIn(k_lab, scale=1.3), run_time=0.6)
        wait_to(10)

        # ═══ seg 10: 38.92s "画切线" ═══
        tangent = axes.plot(lambda x: 13 * (x - 1) + 5, x_range=[0.3, 2.5], color=AMBER, stroke_width=3)
        play_anim(10, Create(tangent), run_time=1.0)
        wait_to(11)

        # ═══ seg 11: 40.86s "点斜式" ═══
        point_slope = MathTex(r"y - 5 = 13(x - 1)", color=PINK, font_size=30)
        point_slope.next_to(k_lab, DOWN, aligned_edge=LEFT, buff=0.4)
        play_anim(11, Write(point_slope), run_time=1.0)
        wait_to(12)

        # ═══ seg 12: 45.52s "y=13x-8" ═══
        final_eq = MathTex(r"y = 13x - 8", color=GREEN, font_size=36)
        final_eq.next_to(point_slope, DOWN, aligned_edge=LEFT, buff=0.4)
        play_anim(12, Write(final_eq), run_time=0.8)

        tangent_lab = MathTex(r"y = 13x - 8", color=AMBER, font_size=24)
        tangent_lab.next_to(axes.c2p(2, f(2)), UR, buff=0.2)
        play_anim(12, FadeIn(tangent_lab), run_time=0.5)
        wait_to(13)

        # ═══ seg 13: 48.9s "答案D" ═══
        answer = MathTex(r"\boxed{D}", color=GREEN, font_size=48)
        answer.to_edge(DOWN, buff=0.8).shift(RIGHT * 2)
        play_anim(13, FadeIn(answer, scale=1.5), run_time=0.6)

        # 结尾
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.0)
        self.wait(0.5)
