"""2026高考数学第5题 - 抛物线焦点距离（v2: 白色主题 + 完整动画）"""
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

# 12段TTS时间轴
T = [0.0, 3.22, 11.72, 14.94, 18.0, 20.42, 28.92, 36.3, 43.04, 50.58, 53.64, 61.82]


class Q05(Scene):
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

        # ═══ seg 0: 0.0s "来看第五题，抛物线焦点距离" ═══
        title = Text("第 5 题", font="Microsoft YaHei", font_size=56, color=TXT)
        sub = Text("2026年新高考一卷", font="Microsoft YaHei", font_size=24, color=DIM)
        sub.next_to(title, DOWN, buff=0.4)
        play_anim(0, FadeIn(title, shift=DOWN * 0.3), run_time=0.8)
        play_anim(0, FadeIn(sub), run_time=0.5)
        wait_to(1)

        # ═══ seg 1: 3.22s "两条抛物线C1...C2..." ═══
        problem = VGroup(
            MathTex(r"C_1: y^2 = 2p_1 x", font_size=30, color=BLUE),
            MathTex(r"C_2: x^2 = 2p_2 y", font_size=30, color=AMBER),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        point_text = Text("均经过点 (4, 8)", font="Microsoft YaHei", font_size=28, color=GREEN)
        point_text.next_to(problem, DOWN, buff=0.4)
        question = Text("求两焦点之间的距离", font="Microsoft YaHei", font_size=28, color=PINK)
        question.next_to(point_text, DOWN, buff=0.3)
        all_text = VGroup(problem, point_text, question)

        play_anim(1, FadeOut(sub), run_time=0.3)
        play_anim(1, title.animate.to_edge(UP, buff=0.4).scale(0.6), run_time=0.5)
        play_anim(1, FadeIn(all_text, shift=UP * 0.2), run_time=0.5)
        play_anim(1, all_text.animate.move_to(ORIGIN), run_time=0.5)
        wait_to(2)

        # ═══ seg 2: 11.72s "它们都经过点(4,8)" ═══
        play_anim(2, FadeOut(all_text), run_time=0.3)

        # 画坐标系
        axes = Axes(
            x_range=[-1, 7, 1], y_range=[-1, 10, 2],
            x_length=8, y_length=5,
            axis_config={"color": DIM, "stroke_width": 1.5, "include_tip": True},
        ).shift(DOWN * 0.3)
        x_lab = MathTex("x", color=DIM, font_size=22).next_to(axes.x_axis.get_end(), DOWN, buff=0.1)
        y_lab = MathTex("y", color=DIM, font_size=22).next_to(axes.y_axis.get_end(), LEFT, buff=0.1)

        play_anim(2, Create(axes), FadeIn(x_lab), FadeIn(y_lab), run_time=1.0)

        # 画两条抛物线
        # C1: y² = 2p₁x, p₁=8 → y² = 16x → x = y²/16
        def c1_x(y):
            return y**2 / 16

        # C2: x² = 2p₂y, p₂=1 → x² = 2y → y = x²/2
        def c2_y(x):
            return x**2 / 2

        parab_c1 = axes.plot_parametric_curve(
            lambda t: axes.c2p(c1_x(t), t),
            t_range=[-0.5, 9.5],
            color=BLUE, stroke_width=3,
        )
        parab_c2 = axes.plot(c2_y, x_range=[-0.5, 4.5], color=AMBER, stroke_width=3)

        c1_lab = MathTex(r"C_1: y^2 = 16x", color=BLUE, font_size=22)
        c1_lab.next_to(axes.c2p(5, 9), UR, buff=0.1)
        c2_lab = MathTex(r"C_2: x^2 = 2y", color=AMBER, font_size=22)
        c2_lab.next_to(axes.c2p(4, 8.5), RIGHT, buff=0.1)

        play_anim(2, Create(parab_c1), FadeIn(c1_lab), run_time=1.0)
        play_anim(2, Create(parab_c2), FadeIn(c2_lab), run_time=1.0)

        # 标注点(4,8)
        dot = Dot(axes.c2p(4, 8), color=GREEN, radius=0.12)
        dot_lab = MathTex(r"(4, 8)", color=GREEN, font_size=22)
        dot_lab.next_to(dot, UR, buff=0.15)
        play_anim(2, FadeIn(dot), FadeIn(dot_lab), run_time=0.6)
        wait_to(3)

        # ═══ seg 3: 14.94s "求两焦点之间的距离" ═══
        # 保持图像，加问题标注
        q_mark = Text("?", font="Microsoft YaHei", font_size=40, color=PINK)
        q_mark.to_corner(UR, buff=0.8)
        play_anim(3, FadeIn(q_mark, scale=1.3), run_time=0.6)
        wait_to(4)

        # ═══ seg 4: 18.0s "先代入点(4,8)" ═══
        play_anim(4, FadeOut(q_mark), run_time=0.3)
        sub_note = Text("代入点 (4, 8)", font="Microsoft YaHei", font_size=26, color=GREEN)
        sub_note.to_corner(UR, buff=0.5)
        play_anim(4, FadeIn(sub_note, shift=LEFT * 0.3), run_time=0.6)
        wait_to(5)

        # ═══ seg 5: 20.42s "C1: 8²=2p₁×4, p₁=8" ═══
        calc1 = MathTex(r"C_1: 64 = 8p_1 \Rightarrow p_1 = 8", color=BLUE, font_size=28)
        calc1.next_to(sub_note, DOWN, buff=0.3, aligned_edge=LEFT)
        play_anim(5, FadeIn(calc1, shift=LEFT * 0.3), run_time=0.8)
        wait_to(6)

        # ═══ seg 6: 28.92s "C2: 4²=2p₂×8, p₂=1" ═══
        calc2 = MathTex(r"C_2: 16 = 16p_2 \Rightarrow p_2 = 1", color=AMBER, font_size=28)
        calc2.next_to(calc1, DOWN, buff=0.3, aligned_edge=LEFT)
        play_anim(6, FadeIn(calc2, shift=LEFT * 0.3), run_time=0.8)
        wait_to(7)

        # ═══ seg 7: 36.3s "C1焦点在x轴上 (4,0)" ═══
        play_anim(7, FadeOut(sub_note), FadeOut(calc1), FadeOut(calc2), run_time=0.3)

        focus1 = Dot(axes.c2p(4, 0), color=BLUE, radius=0.12)
        focus1_lab = MathTex(r"F_1(4, 0)", color=BLUE, font_size=22)
        focus1_lab.next_to(focus1, DOWN, buff=0.15)

        # 焦点公式标注
        f1_formula = MathTex(r"F_1\left(\frac{p_1}{2}, 0\right) = (4, 0)", color=BLUE, font_size=26)
        f1_formula.to_corner(UR, buff=0.5)

        play_anim(7, FadeIn(focus1), FadeIn(focus1_lab), run_time=0.6)
        play_anim(7, FadeIn(f1_formula, shift=LEFT * 0.3), run_time=0.6)
        wait_to(8)

        # ═══ seg 8: 43.04s "C2焦点在y轴上 (0,0.5)" ═══
        focus2 = Dot(axes.c2p(0, 0.5), color=AMBER, radius=0.12)
        focus2_lab = MathTex(r"F_2(0, 0.5)", color=AMBER, font_size=22)
        focus2_lab.next_to(focus2, LEFT, buff=0.15)

        f2_formula = MathTex(r"F_2\left(0, \frac{p_2}{2}\right) = (0, 0.5)", color=AMBER, font_size=26)
        f2_formula.next_to(f1_formula, DOWN, buff=0.3, aligned_edge=LEFT)

        play_anim(8, FadeIn(focus2), FadeIn(focus2_lab), run_time=0.6)
        play_anim(8, FadeIn(f2_formula, shift=LEFT * 0.3), run_time=0.6)
        wait_to(9)

        # ═══ seg 9: 50.58s "两点之间的距离，用距离公式" ═══
        line = DashedLine(axes.c2p(4, 0), axes.c2p(0, 0.5), color=PINK, stroke_width=2)
        play_anim(9, Create(line), run_time=0.8)

        dist_formula = MathTex(r"d = \sqrt{4^2 + 0.5^2}", color=PINK, font_size=28)
        dist_formula.next_to(axes, DOWN, buff=0.4)
        play_anim(9, FadeIn(dist_formula, shift=UP * 0.2), run_time=0.6)
        wait_to(10)

        # ═══ seg 10: 53.64s "根号16.25 = 根号65/2" ═══
        dist_result = MathTex(r"= \sqrt{16.25} = \frac{\sqrt{65}}{2}", color=PINK, font_size=28)
        dist_result.next_to(dist_formula, DOWN, buff=0.2, aligned_edge=LEFT)
        play_anim(10, FadeIn(dist_result, shift=UP * 0.2), run_time=0.8)
        wait_to(11)

        # ═══ seg 11: 61.82s "答案选D" ═══
        play_anim(11, FadeOut(f1_formula), FadeOut(f2_formula), FadeOut(dist_formula), FadeOut(dist_result), run_time=0.3)
        answer = Text("答案 D", font="Microsoft YaHei", font_size=60, color=GREEN, weight=BOLD)
        answer.to_edge(DOWN, buff=0.8)
        play_anim(11, FadeIn(answer, scale=1.5), run_time=0.6)

        # 结尾
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.0)
        self.wait(0.5)
