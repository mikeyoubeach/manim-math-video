"""2026高考数学第14题 - 等比数列（重做版）
动画重点: 数列可视化（柱状图），q=2 的倍增效果
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

config.background_color = BG
config.frame_rate = 30
config.pixel_width = 1920
config.pixel_height = 1080

T = [0.0, 3.1, 9.6, 11.1, 17.2, 21.9, 25.2, 28.0, 32.3, 38.3, 41.3, 46.1, 47.8, 52.1]


class Q14(Scene):
    def construct(self):
        elapsed = 0.0
        def wait_to(i):
            nonlocal elapsed
            if i >= len(T): return
            gap = T[i] - elapsed
            if gap > 0.05: self.wait(gap); elapsed += gap
        def play_anim(i, *a, **kw):
            nonlocal elapsed
            self.play(*a, **kw)
            elapsed += kw.get("run_time", 1.0)

        # ===== seg 0: 标题 =====
        title = Text("第 14 题", font="Microsoft YaHei", font_size=64, color=TXT)
        subtitle = Text("等比数列", font="Microsoft YaHei", font_size=40, color=BLUE)
        subtitle.next_to(title, DOWN, buff=0.4)
        grp = VGroup(title, subtitle)
        play_anim(0, FadeIn(grp, shift=DOWN * 0.3), run_time=0.8)
        wait_to(1)
        play_anim(1, FadeOut(grp), run_time=0.3)

        # ===== seg 1: 题目 =====
        prob = VGroup(
            MathTex(r"a_1+a_3=10", font_size=36, color=TXT),
            MathTex(r"a_2+a_4=20", font_size=36, color=TXT),
        ).arrange(RIGHT, buff=1.0)
        cond = Text("等比数列 {aₙ}，求 a₇", font="Microsoft YaHei", font_size=28, color=AMBER)
        cond.next_to(prob, DOWN, buff=0.4)
        prob_grp = VGroup(prob, cond)
        play_anim(1, FadeIn(prob_grp, shift=UP * 0.2), run_time=0.8)
        wait_to(2)
        play_anim(2, FadeOut(prob_grp), run_time=0.3)

        # ===== seg 2: 问题 =====
        q_text = MathTex(r"a_7 = \ ?", font_size=48, color=PINK)
        play_anim(2, FadeIn(q_text, scale=1.3), run_time=0.6)
        wait_to(3)
        play_anim(3, FadeOut(q_text), run_time=0.3)

        # ===== seg 3: 等比数列性质 =====
        prop_title = Text("等比数列性质", font="Microsoft YaHei", font_size=32, color=BLUE)
        prop_title.to_edge(UP, buff=0.8)

        prop1 = MathTex(r"a_2 = a_1 \cdot q", font_size=34, color=TXT)
        prop2 = MathTex(r"a_4 = a_3 \cdot q", font_size=34, color=TXT)
        prop_grp = VGroup(prop1, prop2).arrange(DOWN, buff=0.3)
        prop_grp.next_to(prop_title, DOWN, buff=0.5)

        play_anim(3, FadeIn(prop_title, shift=DOWN * 0.2), run_time=0.5)
        play_anim(3, FadeIn(prop_grp, shift=UP * 0.2), run_time=0.8)
        wait_to(4)

        # ===== seg 4: 推出 q =====
        derive_q = MathTex(r"a_2+a_4=(a_1+a_3)\cdot q", font_size=34, color=BLUE)
        derive_q.next_to(prop_grp, DOWN, buff=0.4)
        play_anim(4, FadeIn(derive_q, shift=UP * 0.2), run_time=0.8)
        wait_to(5)
        play_anim(5, FadeOut(VGroup(prop_title, prop_grp)), run_time=0.3)

        # seg 5: 20=10q, q=2
        q_calc = MathTex(r"20 = 10 \cdot q", font_size=38, color=TXT)
        q_calc.move_to(UP * 1.5)
        q_result = MathTex(r"q = 2", font_size=48, color=GREEN)
        q_result.next_to(q_calc, DOWN, buff=0.5)
        play_anim(5, FadeIn(q_calc, shift=UP * 0.2), run_time=0.6)
        play_anim(5, FadeIn(q_result, scale=1.2), run_time=0.8)
        wait_to(6)

        # ===== seg 6-7: 柱状图可视化 q=2 =====
        play_anim(6, FadeOut(VGroup(derive_q, q_calc, q_result)), run_time=0.3)

        # 柱状图: a1=2, q=2
        bar_title = Text("等比数列可视化 (q=2)", font="Microsoft YaHei", font_size=28, color=BLUE)
        bar_title.to_edge(UP, buff=0.4)

        # 数据: a1=2, a2=4, a3=8, a4=16, a5=32, a6=64, a7=128
        values = [2, 4, 8, 16, 32, 64, 128]
        labels = ["a₁", "a₂", "a₃", "a₄", "a₅", "a₆", "a₇"]
        max_val = 128
        bar_width = 0.8
        bar_spacing = 1.2
        chart_height = 4.0
        chart_bottom = -2.5

        bars = VGroup()
        bar_labels = VGroup()
        bar_values = VGroup()

        for i, (val, label) in enumerate(zip(values, labels)):
            h = (val / max_val) * chart_height
            bar = Rectangle(
                width=bar_width, height=h,
                fill_color=BLUE if i < 6 else GREEN,
                fill_opacity=0.7,
                stroke_color=BLUE if i < 6 else GREEN,
                stroke_width=2,
            )
            bar.move_to(LEFT * 3.5 + RIGHT * i * bar_spacing + UP * (chart_bottom + h / 2))

            bl = Text(label, font="Microsoft YaHei", font_size=20, color=TXT)
            bl.next_to(bar, DOWN, buff=0.15)

            bv = Text(str(val), font="Microsoft YaHei", font_size=18, color=DIM)
            bv.next_to(bar, UP, buff=0.1)

            bars.add(bar)
            bar_labels.add(bl)
            bar_values.add(bv)

        play_anim(6, FadeIn(bar_title, shift=DOWN * 0.2), run_time=0.5)

        # 先显示前3个柱子 (a1, a2, a3)
        for i in range(3):
            play_anim(6, GrowFromEdge(bars[i], DOWN), FadeIn(bar_labels[i]), FadeIn(bar_values[i]), run_time=0.4)

        wait_to(7)

        # seg 7: 倍增效果 — 逐个增长显示 a4-a7
        # 先找 a1
        a1_val = MathTex(r"a_1=2", font_size=30, color=AMBER)
        a1_val.to_edge(RIGHT, buff=0.8).shift(UP * 1)
        play_anim(7, FadeIn(a1_val, shift=LEFT * 0.2), run_time=0.5)

        # a3 = a1 * q² = 4*a1
        a3_relation = MathTex(r"a_3=a_1 \cdot q^2=4a_1", font_size=28, color=PINK)
        a3_relation.next_to(a1_val, DOWN, buff=0.3)
        play_anim(7, FadeIn(a3_relation, shift=UP * 0.2), run_time=0.6)
        wait_to(8)

        # seg 8: a1+4a1=10, a1=2
        sum_eq = MathTex(r"a_1+4a_1=10", font_size=30, color=TXT)
        sum_eq.next_to(a3_relation, DOWN, buff=0.3)
        a1_result = MathTex(r"a_1=2", font_size=34, color=GREEN)
        a1_result.next_to(sum_eq, DOWN, buff=0.3)
        play_anim(8, FadeIn(sum_eq, shift=UP * 0.2), run_time=0.6)
        play_anim(8, FadeIn(a1_result, scale=1.1), run_time=0.6)
        wait_to(9)

        # ===== seg 9: 显示所有柱子 + 倍增动画 =====
        play_anim(9, FadeOut(VGroup(a1_val, a3_relation, sum_eq, a1_result)), run_time=0.3)

        # 显示剩余柱子 a4-a7，带倍增标注
        for i in range(3, 7):
            play_anim(9, GrowFromEdge(bars[i], DOWN), FadeIn(bar_labels[i]), FadeIn(bar_values[i]), run_time=0.3)

        # ×2 标注
        multiply_labels = VGroup()
        for i in range(1, 7):
            arrow = MathTex(r"\times 2", font_size=18, color=AMBER)
            arrow.move_to(bars[i].get_center() + UP * 0.5)
            multiply_labels.add(arrow)

        play_anim(9, FadeIn(multiply_labels), run_time=0.6)
        wait_to(10)

        # ===== seg 10: a7 = a1 * q^6 =====
        play_anim(10, FadeOut(VGroup(bar_title, bars, bar_labels, bar_values, multiply_labels)), run_time=0.3)

        a7_eq = MathTex(r"a_7 = a_1 \cdot q^6", font_size=38, color=TXT)
        a7_eq.move_to(UP * 1)
        play_anim(10, FadeIn(a7_eq, shift=UP * 0.2), run_time=0.8)

        a7_calc = MathTex(r"= 2 \times 2^6 = 2 \times 64 = 128", font_size=36, color=GREEN)
        a7_calc.next_to(a7_eq, DOWN, buff=0.4)
        play_anim(10, FadeIn(a7_calc, shift=UP * 0.2), run_time=0.8)
        wait_to(11)

        # ===== seg 11: 答案 =====
        play_anim(11, FadeOut(VGroup(a7_eq, a7_calc)), run_time=0.3)
        answer = Text("答案 D：128", font="Microsoft YaHei", font_size=60, color=GREEN, weight=BOLD)
        play_anim(11, FadeIn(answer, scale=1.3), run_time=0.6)
        wait_to(12)

        # ===== seg 12: 总结 =====
        play_anim(12, FadeOut(answer), run_time=0.3)
        tip = Text("等比数列性质：相邻项的比 = 公比 q", font="Microsoft YaHei", font_size=30, color=AMBER)
        play_anim(12, FadeIn(tip, shift=UP * 0.2), run_time=0.8)
        wait_to(13)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.0)
        self.wait(0.5)
