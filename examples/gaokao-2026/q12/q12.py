"""2026高考数学第12题 - 双曲线离心率 - 重制版v2
重点: 双曲线+渐近线，b/a=√3 的视觉推导
修复: MathTex不使用中文，用Text代替
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

T = [0.0, 3.22, 7.72, 11.58, 13.36, 19.46, 23.8, 26.86, 29.76, 33.3, 35.56, 41.02, 43.12, 46.18, 47.8, 51.3]


class Q12(Scene):
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

        # seg 0: 标题
        title = Text("第 12 题", font="Microsoft YaHei", font_size=56, color=TXT)
        sub = Text("2026年新高考一卷 · 双曲线离心率", font="Microsoft YaHei", font_size=24, color=DIM)
        sub.next_to(title, DOWN, buff=0.4)
        play_anim(0, FadeIn(title, shift=DOWN * 0.3), run_time=0.8)
        play_anim(0, FadeIn(sub), run_time=0.5)
        wait_to(1)
        play_anim(1, FadeOut(title), FadeOut(sub), run_time=0.3)

        # seg 1-3: 画双曲线
        axes = Axes(
            x_range=[-5, 5, 1], y_range=[-5, 5, 1],
            x_length=8, y_length=8,
            axis_config={"color": DIM, "stroke_width": 1, "include_tip": True},
        )

        play_anim(1, Create(axes), run_time=0.8)

        # 双曲线 x² - y²/3 = 1 (a=1, b=√3)
        hyp_r_upper = axes.plot(lambda x: np.sqrt(3 * (x**2 - 1)), x_range=[1.02, 4.5], color=BLUE, stroke_width=2.5)
        hyp_r_lower = axes.plot(lambda x: -np.sqrt(3 * (x**2 - 1)), x_range=[1.02, 4.5], color=BLUE, stroke_width=2.5)
        hyp_l_upper = axes.plot(lambda x: np.sqrt(3 * (x**2 - 1)), x_range=[-4.5, -1.02], color=BLUE, stroke_width=2.5)
        hyp_l_lower = axes.plot(lambda x: -np.sqrt(3 * (x**2 - 1)), x_range=[-4.5, -1.02], color=BLUE, stroke_width=2.5)

        hyp_label = MathTex(r"\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1", font_size=28, color=BLUE)
        hyp_label.next_to(axes.c2p(2, 3), UR, buff=0.2)

        play_anim(2, Create(hyp_r_upper), Create(hyp_r_lower), run_time=1.0)
        play_anim(2, Create(hyp_l_upper), Create(hyp_l_lower), run_time=0.8)
        play_anim(2, FadeIn(hyp_label), run_time=0.5)

        # 标注顶点
        vertex_dot = Dot(axes.c2p(1, 0), color=GREEN, radius=0.08)
        vertex_lab = MathTex(r"(a, 0)", font_size=20, color=GREEN)
        vertex_lab.next_to(vertex_dot, DOWN, buff=0.15)
        play_anim(2, FadeIn(vertex_dot), FadeIn(vertex_lab), run_time=0.4)
        wait_to(3)

        # seg 3: 渐近线
        asy_r = DashedVMobject(axes.plot(lambda x: np.sqrt(3) * x, x_range=[-4, 4], color=AMBER, stroke_width=2), num_dashes=20)
        asy_l = DashedVMobject(axes.plot(lambda x: -np.sqrt(3) * x, x_range=[-4, 4], color=AMBER, stroke_width=2), num_dashes=20)

        play_anim(3, Create(asy_r), Create(asy_l), run_time=1.0)

        asy_label = MathTex(r"y = \pm\sqrt{3}\, x", font_size=24, color=AMBER)
        asy_label.next_to(axes.c2p(3, 3 * np.sqrt(3)), UR, buff=0.15)
        play_anim(3, FadeIn(asy_label), run_time=0.5)

        # 标注渐近线角度
        angle_arc = Arc(radius=1.2, start_angle=0, angle=np.arctan(np.sqrt(3)), color=AMBER, stroke_width=2)
        angle_arc.move_arc_center_to(axes.c2p(0, 0))
        angle_lab = MathTex(r"\theta", font_size=22, color=AMBER)
        angle_lab.next_to(angle_arc, RIGHT, buff=0.1)
        play_anim(3, FadeIn(angle_arc), FadeIn(angle_lab), run_time=0.5)
        wait_to(4)

        # seg 4-6: 渐近线公式推导
        play_anim(4, FadeOut(axes), FadeOut(hyp_r_upper), FadeOut(hyp_r_lower),
                  FadeOut(hyp_l_upper), FadeOut(hyp_l_lower),
                  FadeOut(asy_r), FadeOut(asy_l), FadeOut(asy_label),
                  FadeOut(hyp_label), FadeOut(vertex_dot), FadeOut(vertex_lab),
                  FadeOut(angle_arc), FadeOut(angle_lab), run_time=0.4)

        # 渐近线公式 - 用Text标中文，MathTex标公式
        lbl1 = Text("渐近线:", font="Microsoft YaHei", font_size=28, color=TXT)
        formula1 = MathTex(r"y = \pm\frac{b}{a}x", font_size=32, color=TXT)
        grp1 = VGroup(lbl1, formula1).arrange(RIGHT, buff=0.2)
        play_anim(5, FadeIn(grp1, shift=UP * 0.2), run_time=0.6)

        # 已知条件
        lbl2 = Text("已知:", font="Microsoft YaHei", font_size=26, color=AMBER)
        formula2 = MathTex(r"y = \sqrt{3}\, x", font_size=30, color=AMBER)
        grp2 = VGroup(lbl2, formula2).arrange(RIGHT, buff=0.2)
        grp2.next_to(grp1, DOWN, buff=0.5)
        play_anim(6, FadeIn(grp2, shift=UP * 0.2), run_time=0.6)

        # 对比
        arrow = Arrow(grp2.get_right(), grp1.get_right() + DOWN * 0.3, color=PINK, stroke_width=3)
        compare = MathTex(r"\frac{b}{a} = \sqrt{3}", font_size=32, color=GREEN)
        compare.next_to(arrow, RIGHT, buff=0.2)
        play_anim(6, Create(arrow), FadeIn(compare, scale=1.1), run_time=0.6)
        wait_to(7)

        # seg 7: b = √3 a
        play_anim(7, FadeOut(grp1), FadeOut(grp2), FadeOut(arrow), FadeOut(compare), run_time=0.3)

        step = MathTex(r"b = \sqrt{3}\, a", font_size=36, color=BLUE)
        play_anim(7, FadeIn(step, scale=1.1), run_time=0.6)
        wait_to(8)

        # seg 8-10: 求离心率 e
        play_anim(8, FadeOut(step), run_time=0.3)

        # 直角三角形: a, b=√3a, c=2a
        tri_a = Line(ORIGIN, RIGHT * 2, color=GREEN, stroke_width=4)
        tri_b = Line(RIGHT * 2, RIGHT * 2 + UP * 2 * np.sqrt(3), color=BLUE, stroke_width=4)
        tri_c = Line(ORIGIN, RIGHT * 2 + UP * 2 * np.sqrt(3), color=PINK, stroke_width=4)
        tri_group = VGroup(tri_a, tri_b, tri_c).scale(0.4).to_edge(LEFT, buff=1.5)

        a_lab = MathTex(r"a", font_size=24, color=GREEN).next_to(tri_a, DOWN, buff=0.1)
        b_lab = MathTex(r"\sqrt{3}\,a", font_size=24, color=BLUE).next_to(tri_b, RIGHT, buff=0.1)
        c_lab = MathTex(r"c", font_size=24, color=PINK).next_to(tri_c, LEFT + UP, buff=0.1)

        right_angle = Square(side_length=0.15, color=DIM, stroke_width=1.5).move_to(
            tri_a.get_end() + UP * 0.075 + LEFT * 0.075
        )

        play_anim(8, Create(tri_group), FadeIn(a_lab), FadeIn(b_lab), FadeIn(c_lab),
                  FadeIn(right_angle), run_time=0.8)

        calc = VGroup(
            MathTex(r"c^2 = a^2 + b^2", font_size=28, color=TXT),
            MathTex(r"= a^2 + 3a^2", font_size=28, color=TXT),
            MathTex(r"= 4a^2", font_size=30, color=GREEN),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        calc.to_edge(RIGHT, buff=1.5)
        play_anim(9, FadeIn(calc[0], shift=LEFT * 0.2), run_time=0.6)
        wait_to(10)

        play_anim(10, FadeIn(calc[1], shift=LEFT * 0.2), run_time=0.5)
        play_anim(10, FadeIn(calc[2], shift=LEFT * 0.2), run_time=0.5)
        wait_to(11)

        # seg 11: c = 2a
        play_anim(11, FadeOut(tri_group), FadeOut(a_lab), FadeOut(b_lab), FadeOut(c_lab),
                  FadeOut(right_angle), FadeOut(calc), run_time=0.3)

        result_group = VGroup(
            MathTex(r"c^2 = 4a^2 \Rightarrow c = 2a", font_size=30, color=TXT),
            MathTex(r"e = \frac{c}{a} = \frac{2a}{a} = 2", font_size=36, color=GREEN),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        play_anim(11, FadeIn(result_group[0], shift=UP * 0.2), run_time=0.6)
        wait_to(12)

        play_anim(12, FadeIn(result_group[1], scale=1.2), run_time=0.6)
        wait_to(13)

        # seg 12-13: 答案
        play_anim(13, FadeOut(result_group), run_time=0.3)

        answer = Text("答案 A", font="Microsoft YaHei", font_size=64, color=GREEN, weight=BOLD)
        play_anim(13, FadeIn(answer, scale=1.5), run_time=0.6)
        wait_to(14)

        # seg 14: 总结 + 回到双曲线图
        play_anim(14, FadeOut(answer), run_time=0.3)

        axes2 = Axes(
            x_range=[-4, 4, 1], y_range=[-4, 4, 1],
            x_length=6, y_length=6,
            axis_config={"color": DIM, "stroke_width": 1},
        ).to_edge(LEFT, buff=1)

        hyp_r = axes2.plot(lambda x: np.sqrt(3 * (x**2 - 1)), x_range=[1.02, 3.5], color=BLUE, stroke_width=2)
        hyp_r2 = axes2.plot(lambda x: -np.sqrt(3 * (x**2 - 1)), x_range=[1.02, 3.5], color=BLUE, stroke_width=2)
        hyp_l = axes2.plot(lambda x: np.sqrt(3 * (x**2 - 1)), x_range=[-3.5, -1.02], color=BLUE, stroke_width=2)
        hyp_l2 = axes2.plot(lambda x: -np.sqrt(3 * (x**2 - 1)), x_range=[-3.5, -1.02], color=BLUE, stroke_width=2)
        asy1 = DashedVMobject(axes2.plot(lambda x: np.sqrt(3) * x, x_range=[-3, 3], color=AMBER, stroke_width=1.5), num_dashes=15)
        asy2 = DashedVMobject(axes2.plot(lambda x: -np.sqrt(3) * x, x_range=[-3, 3], color=AMBER, stroke_width=1.5), num_dashes=15)

        tip = Text("渐近线斜率 = b/a", font="Microsoft YaHei", font_size=30, color=AMBER)
        tip.to_edge(RIGHT, buff=1)

        play_anim(14, FadeIn(axes2), Create(hyp_r), Create(hyp_r2), Create(hyp_l), Create(hyp_l2),
                  Create(asy1), Create(asy2), FadeIn(tip), run_time=1.0)
        wait_to(15)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.0)
        self.wait(0.5)
