"""2026高考数学第13题 - 偶函数（重做版）
动画重点: 函数图像+f(x)和f(-x)的镜像对比，红✗→重新推导→绿✓纠错
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
RED = "#E17055"

config.background_color = BG
config.frame_rate = 30
config.pixel_width = 1920
config.pixel_height = 1080

T = [0.0, 2.9, 9.2, 12.5, 17.0, 24.3, 26.8, 31.8, 38.2, 45.0, 48.5, 55.7, 60.1, 68.1, 71.0, 77.9, 86.1, 87.7, 89.3, 95.1, 100.1, 105.2, 107.2, 110.7, 113.4, 115.4]


class Q13(Scene):
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
        title = Text("第 13 题", font="Microsoft YaHei", font_size=64, color=TXT)
        subtitle = Text("偶函数", font="Microsoft YaHei", font_size=40, color=BLUE)
        subtitle.next_to(title, DOWN, buff=0.4)
        grp = VGroup(title, subtitle)
        play_anim(0, FadeIn(grp, shift=DOWN * 0.3), run_time=0.8)
        wait_to(1)
        play_anim(1, FadeOut(grp), run_time=0.3)

        # ===== seg 1: 题目 =====
        prob = MathTex(r"f(x)=\ln\!\left|\frac{a+1}{1-x}\right|", font_size=42, color=TXT)
        cond = Text("已知 f(x) 是偶函数，求 a", font="Microsoft YaHei", font_size=30, color=AMBER)
        cond.next_to(prob, DOWN, buff=0.4)
        prob_grp = VGroup(prob, cond)
        play_anim(1, FadeIn(prob_grp, shift=UP * 0.2), run_time=0.8)
        wait_to(3)
        play_anim(3, FadeOut(prob_grp), run_time=0.3)

        # ===== seg 3: 偶函数定义 + 镜像图 =====
        # 左侧: 定义
        defn = MathTex(r"f(-x) = f(x)", font_size=48, color=AMBER)
        defn_label = Text("偶函数定义", font="Microsoft YaHei", font_size=24, color=DIM)
        defn_label.next_to(defn, DOWN, buff=0.3)
        defn_grp = VGroup(defn, defn_label)
        defn_grp.to_edge(LEFT, buff=1.0).shift(UP * 0.5)

        # 右侧: 坐标系 + 偶函数曲线示范
        axes = Axes(
            x_range=[-3, 3, 1], y_range=[-0.5, 5, 1],
            x_length=5, y_length=3.5,
            axis_config={"color": DIM, "include_numbers": False, "stroke_width": 1.5},
        )
        axes.shift(RIGHT * 3.5 + DOWN * 0.3)

        curve_f = axes.plot(lambda x: x**2 + 0.5, x_range=[-2.5, 2.5], color=BLUE, stroke_width=3)
        label_f = MathTex(r"f(x)", font_size=28, color=BLUE)
        label_f.next_to(axes.c2p(2, 4.5 + 0.5), RIGHT, buff=0.15)

        # y 轴虚线对称轴
        y_axis_line = DashedLine(
            axes.c2p(0, -0.5), axes.c2p(0, 5),
            color=PINK, stroke_width=2, dash_length=0.1,
        )
        sym_label = Text("对称轴", font="Microsoft YaHei", font_size=20, color=PINK)
        sym_label.next_to(y_axis_line, RIGHT, buff=0.15).shift(UP * 1.5)

        # 镜像箭头
        mirror_arrow = CurvedArrow(
            axes.c2p(1.5, 3.5), axes.c2p(-1.5, 3.5),
            color=PINK, stroke_width=2, angle=-0.5,
        )

        play_anim(3, FadeIn(defn_grp, shift=RIGHT * 0.3), Create(axes), run_time=1.0)
        play_anim(3, Create(curve_f), FadeIn(label_f), run_time=1.0)
        wait_to(4)
        play_anim(4, Create(y_axis_line), FadeIn(sym_label), run_time=0.6)
        wait_to(5)
        play_anim(5, Create(mirror_arrow), run_time=0.5)

        play_anim(5, FadeOut(VGroup(defn_grp, axes, curve_f, label_f, y_axis_line, sym_label, mirror_arrow)), run_time=0.4)

        # ===== seg 5: 去掉 ln，绝对值相等 =====
        step1 = MathTex(r"\ln|A|=\ln|B|", font_size=38, color=TXT)
        step1_arr = MathTex(r"\Rightarrow\ |A|=|B|", font_size=38, color=BLUE)
        step1_arr.next_to(step1, DOWN, buff=0.3)
        s5_grp = VGroup(step1, step1_arr)
        play_anim(5, FadeIn(s5_grp, shift=UP * 0.2), run_time=0.8)
        wait_to(6)
        play_anim(6, FadeOut(s5_grp), run_time=0.3)

        # ===== seg 6: ± 两种情况 =====
        plus = MathTex(r"\frac{a+1}{1+x} = +\frac{a+1}{1-x}", font_size=36, color=GREEN)
        minus = MathTex(r"\frac{a+1}{1+x} = -\frac{a+1}{1-x}", font_size=36, color=PINK)
        case_grp = VGroup(plus, minus).arrange(DOWN, buff=0.5)
        case_label = Text("两种情况", font="Microsoft YaHei", font_size=24, color=DIM)
        case_label.next_to(case_grp, DOWN, buff=0.3)
        play_anim(6, FadeIn(VGroup(case_grp, case_label), shift=UP * 0.2), run_time=0.8)
        wait_to(7)
        play_anim(7, FadeOut(VGroup(case_grp, case_label)), run_time=0.3)

        # ===== seg 7: 取负号 =====
        neg_title = Text("先取负号试试", font="Microsoft YaHei", font_size=28, color=PINK)
        neg_title.to_edge(UP, buff=0.8)
        neg_eq = MathTex(r"\frac{a+1}{1+x}+\frac{a+1}{1-x}=0", font_size=36, color=TXT)
        neg_eq.next_to(neg_title, DOWN, buff=0.5)
        play_anim(7, FadeIn(neg_title, shift=DOWN * 0.2), run_time=0.5)
        play_anim(7, FadeIn(neg_eq, shift=UP * 0.2), run_time=0.8)
        wait_to(8)

        # seg 8: 通分
        common = MathTex(r"\frac{(a+1)(1-x)+(a+1)(1+x)}{1-x^2}=0", font_size=32, color=TXT)
        common.next_to(neg_eq, DOWN, buff=0.4)
        play_anim(8, FadeIn(common, shift=UP * 0.2), run_time=0.8)
        wait_to(9)

        result_neg = MathTex(r"2(a+1)=0 \Rightarrow a=-1", font_size=36, color=PINK)
        result_neg.next_to(common, DOWN, buff=0.4)
        play_anim(9, FadeIn(result_neg, shift=UP * 0.2), run_time=0.8)
        wait_to(10)
        play_anim(10, FadeOut(VGroup(neg_title, neg_eq, common)), run_time=0.3)

        # ===== seg 10-12: 验证 a=-1 =====
        verify_title = Text("验证 a = -1", font="Microsoft YaHei", font_size=32, color=TXT)
        verify_title.to_edge(UP, buff=0.8)
        f_val = MathTex(r"f(x)=\ln\!\left|\frac{-x}{1-x}\right|", font_size=30, color=BLUE)
        f_val.next_to(verify_title, DOWN, buff=0.4)
        play_anim(10, FadeIn(verify_title, shift=DOWN * 0.2), run_time=0.5)
        play_anim(10, FadeIn(f_val, shift=UP * 0.2), run_time=0.8)
        wait_to(11)

        # seg 11: f(-x)
        f_neg_x = MathTex(r"f(-x)=\ln\!\left|\frac{x}{1+x}\right|", font_size=30, color=AMBER)
        f_neg_x.next_to(f_val, DOWN, buff=0.4)
        play_anim(11, FadeIn(f_neg_x, shift=UP * 0.2), run_time=0.8)
        wait_to(12)

        # seg 12: 对比 — 画两个曲线
        axes2 = Axes(
            x_range=[-3, 3, 1], y_range=[-2, 3, 1],
            x_length=4.5, y_length=2.8,
            axis_config={"color": DIM, "include_numbers": False, "stroke_width": 1},
        )
        axes2.to_edge(DOWN, buff=0.6).shift(LEFT * 2.5)

        # f(x) 和 f(-x) 的近似曲线
        def f_a_neg1(x):
            try:
                val = np.log(abs(x / (1-x)))
                return max(-2.0, min(3.0, val))
            except:
                return 0.0

        def f_a_neg1_neg(x):
            try:
                val = np.log(abs(-x / (1+x)))
                return max(-2.0, min(3.0, val))
            except:
                return 0.0

        # 分段画避开 x=0 和 x=1 的渐近线
        curve_fx_1 = axes2.plot(f_a_neg1, x_range=[-2.5, -0.1, 0.02],
                                color=BLUE, stroke_width=2.5)
        curve_fx_2 = axes2.plot(f_a_neg1, x_range=[0.1, 0.78, 0.02],
                                color=BLUE, stroke_width=2.5)
        label_fx2 = MathTex(r"f(x)", font_size=22, color=BLUE)
        label_fx2.next_to(axes2.c2p(-2, 1.5), LEFT, buff=0.1)

        curve_fnx_1 = axes2.plot(f_a_neg1_neg, x_range=[-2.5, -0.1, 0.02],
                                 color=PINK, stroke_width=2.5)
        curve_fnx_2 = axes2.plot(f_a_neg1_neg, x_range=[0.1, 0.78, 0.02],
                                 color=PINK, stroke_width=2.5)
        label_fnx2 = MathTex(r"f(-x)", font_size=22, color=PINK)
        label_fnx2.next_to(axes2.c2p(2, 1.5), RIGHT, buff=0.1)

        curve_fx = VGroup(curve_fx_1, curve_fx_2)
        curve_fnx = VGroup(curve_fnx_1, curve_fnx_2)

        play_anim(12, Create(axes2), run_time=0.5)
        play_anim(12, Create(curve_fx), FadeIn(label_fx2), run_time=0.8)
        play_anim(12, Create(curve_fnx), FadeIn(label_fnx2), run_time=0.8)
        wait_to(13)

        # ===== seg 13: 红 ✗ =====
        red_x = Text("✗", font_size=100, color=RED, weight=BOLD)
        red_x.move_to(RIGHT * 3 + UP * 0.5)
        play_anim(13, FadeIn(red_x, scale=2.0), run_time=0.4)
        not_eq_text = Text("f(x) ≠ f(-x)", font="Microsoft YaHei", font_size=28, color=RED)
        not_eq_text.next_to(red_x, DOWN, buff=0.3)
        play_anim(13, FadeIn(not_eq_text), run_time=0.5)
        wait_to(14)

        # seg 14: 清除，重新来
        play_anim(14, FadeOut(VGroup(red_x, not_eq_text, axes2, curve_fx, label_fx2, curve_fnx, label_fnx2, verify_title, f_val, f_neg_x, result_neg)), run_time=0.4)
        rethink = Text("重新推导...", font="Microsoft YaHei", font_size=36, color=DIM)
        play_anim(14, FadeIn(rethink, shift=UP * 0.2), run_time=0.5)
        wait_to(15)
        play_anim(15, FadeOut(rethink), run_time=0.2)

        # ===== seg 15: 取正号 =====
        pos_title = Text("取正号", font="Microsoft YaHei", font_size=32, color=GREEN)
        pos_title.to_edge(UP, buff=0.8)
        pos_eq = MathTex(r"\frac{1}{1+x}-\frac{1}{1-x}=0", font_size=36, color=TXT)
        pos_eq.next_to(pos_title, DOWN, buff=0.5)
        play_anim(15, FadeIn(pos_title, shift=DOWN * 0.2), run_time=0.5)
        play_anim(15, FadeIn(pos_eq, shift=UP * 0.2), run_time=0.8)
        wait_to(16)

        # seg 16: 这两个不相等
        not_match = Text("这不相等...", font="Microsoft YaHei", font_size=28, color=RED)
        not_match.next_to(pos_eq, DOWN, buff=0.4)
        play_anim(16, FadeIn(not_match, shift=UP * 0.2), run_time=0.5)
        wait_to(17)

        # seg 17: 重新算
        play_anim(17, FadeOut(VGroup(pos_title, pos_eq, not_match)), run_time=0.3)
        retry = Text("让我重新算", font="Microsoft YaHei", font_size=32, color=AMBER)
        play_anim(17, FadeIn(retry, shift=UP * 0.2), run_time=0.5)
        wait_to(18)
        play_anim(18, FadeOut(retry), run_time=0.2)

        # ===== seg 18: 取正号通分 =====
        pos2 = MathTex(r"\frac{(1-x)-(1+x)}{1-x^2}=0", font_size=34, color=TXT)
        play_anim(18, FadeIn(pos2, shift=UP * 0.2), run_time=0.8)
        wait_to(19)

        # seg 19
        pos3 = MathTex(r"\frac{-2x}{1-x^2}=0", font_size=34, color=BLUE)
        pos3.next_to(pos2, DOWN, buff=0.3)
        play_anim(19, FadeIn(pos3, shift=UP * 0.2), run_time=0.8)
        wait_to(20)

        # seg 20: 只在 x=0 成立
        only_zero = MathTex(r"x=0", font_size=38, color=AMBER)
        only_zero.next_to(pos3, DOWN, buff=0.3)
        play_anim(20, FadeIn(only_zero, shift=UP * 0.2), run_time=0.6)
        wait_to(21)

        # seg 21: 所以取负号是对的 → 绿 ✓
        play_anim(21, FadeOut(VGroup(pos2, pos3, only_zero)), run_time=0.3)
        green_check = Text("✓", font_size=100, color=GREEN, weight=BOLD)
        confirm_text = Text("取负号是正确的", font="Microsoft YaHei", font_size=32, color=GREEN)
        confirm_grp = VGroup(confirm_text, green_check).arrange(DOWN, buff=0.3)
        play_anim(21, FadeIn(confirm_grp, scale=0.8), run_time=0.6)
        wait_to(22)

        # ===== seg 22: a=-1，验证定义域 =====
        play_anim(22, FadeOut(confirm_grp), run_time=0.3)
        domain_info = VGroup(
            MathTex(r"a=-1", font_size=36, color=PINK),
            Text("验证定义域: x ≠ 0, x ≠ 1", font="Microsoft YaHei", font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.3)
        play_anim(22, FadeIn(domain_info, shift=UP * 0.2), run_time=0.8)
        wait_to(23)
        play_anim(23, FadeOut(domain_info), run_time=0.3)

        # ===== seg 23: 答案 ±1 =====
        ans_detail = VGroup(
            MathTex(r"a=1:\ f(x)=\ln\!\left|\frac{2}{1-x}\right|", font_size=28, color=BLUE),
            MathTex(r"a=-1:\ f(x)=\ln\!\left|\frac{x}{1-x}\right|", font_size=28, color=GREEN),
        ).arrange(DOWN, buff=0.3)
        play_anim(23, FadeIn(ans_detail, shift=UP * 0.2), run_time=0.8)
        wait_to(24)

        # ===== seg 24: 答案 C =====
        play_anim(24, FadeOut(ans_detail), run_time=0.3)
        answer = Text("答案 C：a = ±1", font="Microsoft YaHei", font_size=60, color=GREEN, weight=BOLD)
        play_anim(24, FadeIn(answer, scale=1.3), run_time=0.6)
        wait_to(25)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.0)
        self.wait(0.5)
