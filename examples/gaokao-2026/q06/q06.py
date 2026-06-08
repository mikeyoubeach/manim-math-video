"""2026高考数学第6题 - 函数最大值（v2: 视觉因果 + 正确生命周期）"""
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

# 22段TTS时间轴（index 0-21，T有23个元素：seg开始时间 + 结束时间）
T = [0.0, 3.22, 8.68, 11.26, 14.32, 19.62, 22.84, 25.74, 29.28, 33.3, 36.36, 38.78, 43.6, 51.62, 58.2, 62.7, 65.76, 71.38, 76.36, 80.22, 84.88, 86.82, 93.88]


class Q06(Scene):
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

        # ═══ seg 0: 0.0s "来看第六题，函数最大值" ═══
        title = Text("第 6 题", font="Microsoft YaHei", font_size=56, color=TXT)
        sub = Text("2026年新高考一卷", font="Microsoft YaHei", font_size=24, color=DIM)
        sub.next_to(title, DOWN, buff=0.4)
        play_anim(0, FadeIn(title, shift=DOWN * 0.3), run_time=0.8)
        play_anim(0, FadeIn(sub), run_time=0.5)
        wait_to(1)

        # ═══ seg 1: 3.22s "函数f(x)=(x+2)/(eˣ+a)" ═══
        problem = MathTex(r"f(x) = \frac{x+2}{e^x + a}", font_size=36, color=BLUE)
        problem.next_to(title, DOWN, buff=0.8)
        max_cond = Text("最大值为 1", font="Microsoft YaHei", font_size=30, color=GREEN)
        max_cond.next_to(problem, DOWN, buff=0.4)
        options = VGroup(
            MathTex(r"\text{A. } \frac{1}{2}", font_size=26, color=DIM),
            MathTex(r"\text{B. } 1", font_size=26, color=DIM),
            MathTex(r"\text{C. } \frac{3}{2}", font_size=26, color=DIM),
            MathTex(r"\text{D. } 2", font_size=26, color=DIM),
        ).arrange(RIGHT, buff=0.8)
        options.next_to(max_cond, DOWN, buff=0.4)
        all_text = VGroup(problem, max_cond, options)

        play_anim(1, FadeOut(sub), run_time=0.3)
        play_anim(1, title.animate.to_edge(UP, buff=0.4).scale(0.6), run_time=0.5)
        play_anim(1, FadeIn(all_text, shift=UP * 0.2), run_time=0.5)
        play_anim(1, all_text.animate.move_to(ORIGIN), run_time=0.5)
        wait_to(2)

        # ═══ seg 2: 8.68s "已知最大值为1，求a" ═══
        # 保持，加标注
        q_mark = Text("求 a = ?", font="Microsoft YaHei", font_size=32, color=PINK)
        q_mark.next_to(all_text, DOWN, buff=0.5)
        play_anim(2, FadeIn(q_mark, shift=UP * 0.2), run_time=0.6)
        wait_to(3)

        # ═══ seg 3: 11.26s "这道题考的是导数求极值" ═══
        play_anim(3, FadeOut(all_text), FadeOut(q_mark), run_time=0.3)

        # 画函数图像 (a=1 的情况)
        axes = Axes(
            x_range=[-3, 5, 1], y_range=[-0.5, 1.5, 0.5],
            x_length=9, y_length=5,
            axis_config={"color": DIM, "stroke_width": 1.5, "include_tip": True},
        ).shift(DOWN * 0.3 + LEFT * 0.5)
        x_lab = MathTex("x", color=DIM, font_size=22).next_to(axes.x_axis.get_end(), DOWN, buff=0.1)
        y_lab = MathTex("y", color=DIM, font_size=22).next_to(axes.y_axis.get_end(), LEFT, buff=0.1)

        def f(x):
            return (x + 2) / (np.exp(x) + 1)

        curve = axes.plot(f, x_range=[-2.8, 4.5], color=BLUE, stroke_width=3)

        play_anim(3, Create(axes), FadeIn(x_lab), FadeIn(y_lab), run_time=0.8)
        play_anim(3, Create(curve), run_time=2.0)

        curve_lab = MathTex(r"f(x) = \frac{x+2}{e^x+1}", color=BLUE, font_size=22)
        curve_lab.next_to(axes.c2p(-2, f(-2)), UL, buff=0.15)
        play_anim(3, FadeIn(curve_lab), run_time=0.5)
        wait_to(4)

        # ═══ seg 4: 14.32s "最大值为1，说明存在某个x使f(x)=1" ═══
        max_dot = Dot(axes.c2p(0, 1), color=GREEN, radius=0.12)
        max_lab = MathTex(r"f(0) = 1", color=GREEN, font_size=24)
        max_lab.next_to(max_dot, UR, buff=0.15)

        # 最高点标注
        h_line = DashedLine(axes.c2p(-3, 1), axes.c2p(5, 1), color=GREEN, stroke_width=1, stroke_opacity=0.5)

        play_anim(4, Create(h_line), FadeIn(max_dot), FadeIn(max_lab), run_time=0.8)
        wait_to(5)

        # ═══ seg 5: 19.62s "同时在这个点f'(x)=0" ═══
        # 视觉因果：f'(x)=0 → 箭头指向最高点
        deriv_note = MathTex(r"f'(x_0) = 0", color=AMBER, font_size=28)
        deriv_note.to_corner(UR, buff=0.5).shift(DOWN * 0.3)

        arrow_to_peak = Arrow(
            deriv_note.get_bottom() + DOWN * 0.1,
            max_dot.get_center() + UP * 0.3,
            color=AMBER, stroke_width=2, buff=0.1,
        )

        play_anim(5, FadeIn(deriv_note, shift=LEFT * 0.3), run_time=0.6)
        play_anim(5, Create(arrow_to_peak), run_time=0.6)
        wait_to(6)

        # ═══ seg 6: 22.84s "先看f(x)=1这个条件" ═══
        play_anim(5, FadeOut(arrow_to_peak), FadeOut(deriv_note), run_time=0.3)

        cond1_label = Text("条件 ①", font="Microsoft YaHei", font_size=28, color=BLUE)
        cond1_label.to_corner(UR, buff=0.5)
        play_anim(6, FadeIn(cond1_label, shift=LEFT * 0.3), run_time=0.6)
        wait_to(7)

        # ═══ seg 7: 25.74s "x+2 = eˣ + a" ═══
        eq1 = MathTex(r"x+2 = e^x + a", color=BLUE, font_size=30)
        eq1.next_to(cond1_label, DOWN, buff=0.3, aligned_edge=LEFT)
        play_anim(7, FadeIn(eq1, shift=LEFT * 0.3), run_time=0.8)
        wait_to(8)

        # ═══ seg 8: 29.28s "移项 a = x+2 - eˣ" ═══
        eq1_result = MathTex(r"a = x + 2 - e^x", color=BLUE, font_size=30)
        eq1_result.next_to(eq1, DOWN, buff=0.3, aligned_edge=LEFT)
        play_anim(8, FadeIn(eq1_result, shift=LEFT * 0.3), run_time=0.8)
        wait_to(9)

        # ═══ seg 9: 33.3s "再看f'(x)=0" ═══
        play_anim(9, FadeOut(cond1_label), FadeOut(eq1), run_time=0.3)

        cond2_label = Text("条件 ②", font="Microsoft YaHei", font_size=28, color=AMBER)
        cond2_label.to_corner(UR, buff=0.5)
        play_anim(9, FadeIn(cond2_label, shift=LEFT * 0.3), run_time=0.6)
        wait_to(10)

        # ═══ seg 10: 36.36s "商的求导法则" ═══
        rule = MathTex(r"\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}", color=DIM, font_size=26)
        rule.next_to(cond2_label, DOWN, buff=0.3, aligned_edge=LEFT)
        play_anim(10, FadeIn(rule, shift=LEFT * 0.3), run_time=0.8)
        wait_to(11)

        # ═══ seg 11: 38.78s "分子导数1，分母导数eˣ" ═══
        play_anim(11, FadeOut(rule), run_time=0.3)
        deriv_detail = MathTex(
            r"f'(x) = \frac{(e^x+a) - (x+2)e^x}{(e^x+a)^2}",
            color=AMBER, font_size=26,
        )
        deriv_detail.next_to(cond2_label, DOWN, buff=0.3, aligned_edge=LEFT)
        play_anim(11, FadeIn(deriv_detail, shift=LEFT * 0.3), run_time=0.8)
        wait_to(12)

        # ═══ seg 12: 43.6s "f'(x) = [eˣ+a - (x+2)eˣ] / (eˣ+a)²" ═══
        # 已在 seg 11 显示，这里加分子=0
        num_zero = Text("分子 = 0:", font="Microsoft YaHei", font_size=24, color=PINK)
        num_zero.next_to(deriv_detail, DOWN, buff=0.3, aligned_edge=LEFT)
        num_eq = MathTex(r"e^x + a - (x+2)e^x = 0", color=PINK, font_size=26)
        num_eq.next_to(num_zero, DOWN, buff=0.2, aligned_edge=LEFT)
        play_anim(12, FadeIn(num_zero), FadeIn(num_eq), run_time=0.8)
        wait_to(13)

        # ═══ seg 13: 51.62s "化简 a = (x+1)eˣ" ═══
        eq2_result = MathTex(r"a = (x+1)e^x", color=AMBER, font_size=30)
        eq2_result.next_to(num_eq, DOWN, buff=0.3, aligned_edge=LEFT)
        play_anim(13, FadeIn(eq2_result, shift=UP * 0.2), run_time=0.8)
        wait_to(14)

        # ═══ seg 14: 58.2s "现在有两个关于a的等式" ═══
        play_anim(14, FadeOut(cond2_label), FadeOut(deriv_detail), FadeOut(num_zero),
                  FadeOut(num_eq), run_time=0.3)

        sys_label = Text("两个等式联立", font="Microsoft YaHei", font_size=28, color=PINK)
        sys_label.to_corner(UR, buff=0.5)
        play_anim(14, FadeIn(sys_label, shift=LEFT * 0.3), run_time=0.6)
        wait_to(15)

        # ═══ seg 15: 62.7s "x+2-eˣ = (x+1)eˣ" ═══
        sys_eq = MathTex(r"x + 2 - e^x = (x+1)e^x", color=PINK, font_size=30)
        sys_eq.next_to(sys_label, DOWN, buff=0.3, aligned_edge=LEFT)
        play_anim(15, FadeIn(sys_eq, shift=LEFT * 0.3), run_time=0.8)
        wait_to(16)

        # ═══ seg 16: 65.76s "化简 eˣ(x+2) = x+2" ═══
        simplify = MathTex(r"e^x(x+2) = x+2", color=PINK, font_size=30)
        simplify.next_to(sys_eq, DOWN, buff=0.3, aligned_edge=LEFT)
        play_anim(16, FadeIn(simplify, shift=UP * 0.2), run_time=0.8)
        wait_to(17)

        # ═══ seg 17: 71.38s "所以eˣ=1, x=0" ═══
        solve = MathTex(r"e^x = 1 \Rightarrow x = 0", color=GREEN, font_size=32)
        solve.next_to(simplify, DOWN, buff=0.3, aligned_edge=LEFT)
        play_anim(17, FadeIn(solve, scale=1.2), run_time=0.8)

        # 在曲线上标出 x=0
        x0_marker = Dot(axes.c2p(0, 1), color=GREEN, radius=0.15)
        x0_label = MathTex(r"x=0", color=GREEN, font_size=22)
        x0_label.next_to(x0_marker, DOWN, buff=0.2)
        play_anim(17, FadeIn(x0_marker), FadeIn(x0_label), run_time=0.5)
        wait_to(18)

        # ═══ seg 18: 76.36s "代回去 a = (0+1)e⁰ = 1" ═══
        play_anim(18, FadeOut(eq1_result), FadeOut(eq2_result), FadeOut(sys_label),
                  FadeOut(sys_eq), FadeOut(simplify), FadeOut(solve), run_time=0.3)

        final_calc = MathTex(r"a = (0+1) \cdot e^0 = 1", color=GREEN, font_size=32)
        final_calc.to_corner(UR, buff=0.5).shift(DOWN * 0.3)
        play_anim(18, FadeIn(final_calc, shift=LEFT * 0.3), run_time=0.8)
        wait_to(19)

        # ═══ seg 19: 80.22s "答案选B" ═══
        play_anim(19, FadeOut(final_calc), run_time=0.3)
        answer = Text("答案 B", font="Microsoft YaHei", font_size=60, color=GREEN, weight=BOLD)
        answer.to_edge(DOWN, buff=0.8).shift(RIGHT * 2)
        play_anim(19, FadeIn(answer, scale=1.5), run_time=0.6)
        wait_to(20)

        # ═══ seg 20: 84.88s "核心思想：列两个方程" ═══
        play_anim(20, FadeOut(answer), run_time=0.3)

        tip = Text("核心思想：列两个方程", font="Microsoft YaHei", font_size=30, color=AMBER)
        tip.to_edge(DOWN, buff=1.0)
        play_anim(20, FadeIn(tip, shift=UP * 0.2), run_time=0.8)
        wait_to(21)

        # ═══ seg 21: 86.82s "一个来自f(x)=1，一个来自f'(x)=0" ═══
        t1 = MathTex(r"(1)\; f(x) = 1", color=BLUE, font_size=28)
        t2 = MathTex(r"(2)\; f'(x) = 0", color=AMBER, font_size=28)
        t_group = VGroup(t1, t2).arrange(RIGHT, buff=1.0)
        t_group.next_to(tip, UP, buff=0.4)

        # 视觉因果箭头
        arrow1 = Arrow(t1.get_top(), max_dot.get_center() + LEFT * 0.5, color=BLUE, stroke_width=2, buff=0.1)
        arrow2 = Arrow(t2.get_top(), max_dot.get_center() + RIGHT * 0.5, color=AMBER, stroke_width=2, buff=0.1)

        play_anim(21, FadeIn(t_group, shift=UP * 0.2), run_time=0.6)
        play_anim(21, Create(arrow1), Create(arrow2), run_time=0.8)

        # 结尾
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.0)
        self.wait(0.5)
