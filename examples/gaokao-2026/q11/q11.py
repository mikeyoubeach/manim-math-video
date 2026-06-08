"""2026高考数学第11题 - 直线与圆相交 - 重制版v2
重点: 动态k参数，用ValueTracker滑动k让直线旋转，观众发现(0,2)始终在C₁上
修复: MathTex不能含中文，k显示改用Text避免频繁LaTeX编译
"""
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

T = [0.0, 3.54, 6.28, 10.78, 17.36, 21.22, 23.64, 26.7, 31.36, 34.58, 38.28, 41.34, 44.72, 49.22, 55.96, 61.58, 64.16, 69.62, 72.2, 73.66, 77.5]


class Q11(Scene):
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

        # ═══ seg 0: 标题 ═══
        title = Text("第 11 题", font="Microsoft YaHei", font_size=56, color=TXT)
        sub = Text("2026年新高考一卷 · 直线与圆", font="Microsoft YaHei", font_size=24, color=DIM)
        sub.next_to(title, DOWN, buff=0.4)
        play_anim(0, FadeIn(title, shift=DOWN * 0.3), run_time=0.8)
        play_anim(0, FadeIn(sub), run_time=0.5)
        wait_to(1)
        play_anim(1, FadeOut(title), FadeOut(sub), run_time=0.3)

        # ═══ seg 1-4: 画坐标系 + 两圆 ═══
        axes = Axes(
            x_range=[-4, 7, 1], y_range=[-4, 5, 1],
            x_length=11, y_length=7,
            axis_config={"color": DIM, "stroke_width": 1, "include_tip": True},
        ).shift(LEFT * 0.5)

        # 直线方程标注
        line_eq = MathTex(r"y = kx + 2", font_size=30, color=PINK)
        line_eq.to_corner(UR, buff=0.4)
        play_anim(1, FadeIn(line_eq, shift=LEFT * 0.3), run_time=0.6)

        play_anim(1, Create(axes), run_time=0.8)

        # C1: x²+y²=4, 圆心(0,0) r=2
        c1 = Circle(radius=2 * 1.1, color=BLUE, stroke_width=2.5).move_to(axes.c2p(0, 0))
        c1_lab = MathTex(r"C_1: x^2+y^2=4", font_size=22, color=BLUE)
        c1_lab.next_to(axes.c2p(0, 2), RIGHT, buff=0.2)
        play_anim(2, Create(c1), FadeIn(c1_lab), run_time=0.8)

        # C2: (x-3)²+y²=4, 圆心(3,0) r=2
        c2 = Circle(radius=2 * 1.1, color=AMBER, stroke_width=2.5).move_to(axes.c2p(3, 0))
        c2_lab = MathTex(r"C_2: (x{-}3)^2+y^2=4", font_size=22, color=AMBER)
        c2_lab.next_to(axes.c2p(3, 2), RIGHT, buff=0.2)
        play_anim(3, Create(c2), FadeIn(c2_lab), run_time=0.8)
        wait_to(5)

        # ═══ seg 5-7: 发现特殊点 (0,2) ═══
        special_dot = Dot(axes.c2p(0, 2), color=GREEN, radius=0.12)
        special_lab = MathTex(r"(0, 2)", font_size=22, color=GREEN)
        special_lab.next_to(special_dot, LEFT, buff=0.2)

        play_anim(5, FadeIn(special_dot, scale=1.5), run_time=0.6)
        play_anim(5, FadeIn(special_lab), run_time=0.4)

        # seg 6: "当x=0时, y=2"
        explain = MathTex(r"x=0 \Rightarrow y=2", font_size=26, color=TXT)
        explain.to_corner(DR, buff=0.4)
        play_anim(6, FadeIn(explain, shift=LEFT * 0.3), run_time=0.6)
        wait_to(7)

        # seg 7: 验证在C₁上
        play_anim(7, FadeOut(explain), run_time=0.3)
        verify = MathTex(r"0^2+2^2=4 \; \checkmark", font_size=28, color=GREEN)
        verify.to_corner(DR, buff=0.4)
        play_anim(7, FadeIn(verify, shift=LEFT * 0.3), run_time=0.6)
        play_anim(7, Flash(special_dot, color=GREEN, line_length=0.3, num_lines=8), run_time=0.5)
        wait_to(8)

        # ═══ seg 8-9: 动态直线 - k从负到正滑动 ═══
        play_anim(8, FadeOut(verify), run_time=0.3)

        conclusion = Text("直线恒过C₁上的点 (0,2)", font="Microsoft YaHei", font_size=24, color=GREEN)
        conclusion.to_corner(UR, buff=0.4).shift(DOWN * 0.5)
        play_anim(8, FadeIn(conclusion, shift=LEFT * 0.3), run_time=0.6)

        # ValueTracker 控制 k
        k_tracker = ValueTracker(-3.0)

        # 动态直线: y = kx + 2
        def get_dynamic_line():
            k = k_tracker.get_value()
            x1, x2 = -3.5, 6
            y1, y2 = k * x1 + 2, k * x2 + 2
            return Line(
                axes.c2p(x1, y1), axes.c2p(x2, y2),
                color=PINK, stroke_width=3,
            )

        dynamic_line = always_redraw(get_dynamic_line)

        # k值显示 - 用DecimalNumber避免LaTeX编译
        k_label = Text("k = ", font="Microsoft YaHei", font_size=26, color=PINK)
        k_number = DecimalNumber(-3.0, num_decimal_places=1, font_size=26, color=PINK)
        k_group = VGroup(k_label, k_number).arrange(RIGHT, buff=0.05)
        k_group.to_corner(DL, buff=0.4)
        k_number.add_updater(lambda d: d.set_value(k_tracker.get_value()))

        play_anim(9, FadeIn(dynamic_line), FadeIn(k_group), run_time=0.5)

        # k 从 -3 滑到 3
        play_anim(9, k_tracker.animate.set_value(3.0), run_time=2.5)
        wait_to(10)

        # ═══ seg 10-14: 代入C₂推导 ═══
        k_number.clear_updaters()
        play_anim(10, FadeOut(conclusion), FadeOut(dynamic_line), FadeOut(k_group), run_time=0.3)

        # 代入步骤 - 用Text避免中文在MathTex里
        step1a = Text("代入C₂:", font="Microsoft YaHei", font_size=22, color=TXT)
        step1b = MathTex(r"(x-3)^2 + (kx+2)^2 = 4", font_size=24, color=TXT)
        step1 = VGroup(step1a, step1b).arrange(RIGHT, buff=0.2)
        step1.to_corner(UR, buff=0.4)
        play_anim(10, FadeIn(step1, shift=LEFT * 0.3), run_time=0.8)
        wait_to(12)

        # seg 12: 展开
        play_anim(12, FadeOut(step1), run_time=0.3)
        step2 = VGroup(
            MathTex(r"x^2 - 6x + 9 + k^2x^2 + 4kx + 4 = 4", font_size=22, color=TXT),
            MathTex(r"(1+k^2)x^2 + (4k-6)x + 9 = 0", font_size=24, color=BLUE),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        step2.to_corner(UR, buff=0.4)
        play_anim(12, FadeIn(step2, shift=LEFT * 0.3), run_time=0.8)
        wait_to(15)

        # ═══ seg 15-16: 判别式 ═══
        play_anim(15, FadeOut(step2), run_time=0.3)
        step3 = VGroup(
            MathTex(r"\Delta = (4k-6)^2 - 4(1+k^2) \cdot 9 \geq 0", font_size=24, color=PINK),
            MathTex(r"16k^2 - 48k + 36 - 36 - 36k^2 \geq 0", font_size=22, color=TXT),
            MathTex(r"-20k^2 - 48k \geq 0", font_size=22, color=TXT),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        step3.to_corner(UR, buff=0.4)
        play_anim(15, FadeIn(step3, shift=LEFT * 0.3), run_time=0.8)
        wait_to(16)

        # ═══ seg 16-17: k ≤ 0 ═══
        play_anim(16, FadeOut(step3), run_time=0.3)
        result = MathTex(r"k \leq 0", font_size=40, color=GREEN)
        result.to_corner(UR, buff=0.4)
        play_anim(16, FadeIn(result, scale=1.2), run_time=0.6)
        wait_to(17)

        # ═══ seg 17: 答案 ═══
        play_anim(17, FadeOut(result), FadeOut(axes), FadeOut(c1), FadeOut(c1_lab),
                  FadeOut(c2), FadeOut(c2_lab), FadeOut(special_dot), FadeOut(special_lab),
                  FadeOut(line_eq), run_time=0.4)

        answer = Text("答案 D", font="Microsoft YaHei", font_size=64, color=GREEN, weight=BOLD)
        play_anim(17, FadeIn(answer, scale=1.5), run_time=0.6)
        wait_to(18)

        # ═══ seg 18: 关键回顾 ═══
        play_anim(18, FadeOut(answer), run_time=0.3)

        axes2 = Axes(
            x_range=[-3, 5, 1], y_range=[-3, 4, 1],
            x_length=8, y_length=5,
            axis_config={"color": DIM, "stroke_width": 1},
        ).scale(0.8).to_edge(LEFT, buff=0.5)
        c1b = Circle(radius=2 * 0.88, color=BLUE, stroke_width=2).move_to(axes2.c2p(0, 0))
        c2b = Circle(radius=2 * 0.88, color=AMBER, stroke_width=2).move_to(axes2.c2p(3, 0))
        dot_b = Dot(axes2.c2p(0, 2), color=GREEN, radius=0.1)

        lines = VGroup()
        for k_val in [-2, -1, 0, 0.5, 1, 2]:
            x1, x2 = -3, 5
            y1, y2 = k_val * x1 + 2, k_val * x2 + 2
            ln = Line(axes2.c2p(x1, y1), axes2.c2p(x2, y2), color=PINK, stroke_width=1.5, stroke_opacity=0.5)
            lines.add(ln)

        tip = Text("关键：发现直线恒过C₁上的点", font="Microsoft YaHei", font_size=28, color=AMBER)
        tip.to_edge(RIGHT, buff=0.5)

        play_anim(18, FadeIn(axes2), FadeIn(c1b), FadeIn(c2b), FadeIn(dot_b),
                  FadeIn(lines), FadeIn(tip), run_time=1.0)
        wait_to(19)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.0)
        self.wait(0.5)
