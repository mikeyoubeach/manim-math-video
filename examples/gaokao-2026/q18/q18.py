from manim import *
import numpy as np

# ── 配色（白色主题）──
BG = "#FFFFFF"
TXT = "#2D3436"
DIM = "#B2BEC3"
BLUE = "#4fc3f7"
GREEN = "#00B894"
AMBER = "#e8a87c"
PINK = "#FF6B9D"
CORAL = "#c97b5d"

# ── TTS 时间轴 ──
T = [0.0, 2.42, 8.84, 13.82, 16.4, 19.94, 25.56, 29.74, 34.24, 36.5,
     42.12, 44.22, 47.92, 54.82, 60.28, 65.26, 68.48, 70.58, 75.08,
     79.26, 81.84, 85.38, 91.48, 95.18, 98.72]


class Q18(Scene):
    def construct(self):
        self.camera.background_color = BG
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

        # ═══════════════════════════════════════
        # seg 0: "来看第十八题，椭圆。"
        # ═══════════════════════════════════════
        title = Text("第18题  椭圆", font="Microsoft YaHei", font_size=42, color=TXT)
        title.to_edge(UP, buff=0.5)
        play_anim(0, FadeIn(title, shift=DOWN * 0.3), run_time=1.0)
        wait_to(1)

        # ═══════════════════════════════════════
        # seg 1: "椭圆C的方程是x²/a²+y²/b²=1，a>b>0"
        # ═══════════════════════════════════════
        eq_general = MathTex(
            r"\frac{x^2}{a^2}+\frac{y^2}{b^2}=1,\quad a>b>0",
            font_size=38, color=TXT
        )
        eq_general.next_to(title, DOWN, buff=0.6)
        play_anim(1, Write(eq_general), run_time=2.0)
        wait_to(2)

        # ═══════════════════════════════════════
        # seg 2: "左焦点F(-1,0)，离心率=1/2"
        # ═══════════════════════════════════════
        focus_info = MathTex(r"F(-1,\,0),\quad e=\frac{1}{2}", font_size=36, color=BLUE)
        focus_info.next_to(eq_general, DOWN, buff=0.4)
        play_anim(2, FadeIn(focus_info, shift=UP * 0.2), run_time=1.0)
        wait_to(3)

        # ═══════════════════════════════════════
        # seg 3: "第一问，求椭圆方程"
        # ═══════════════════════════════════════
        play_anim(3, FadeOut(title), run_time=0.5)
        step1_title = Text("（1）求椭圆方程", font="Microsoft YaHei", font_size=36, color=PINK)
        step1_title.to_edge(UP, buff=0.5)
        play_anim(3, FadeIn(step1_title, shift=DOWN * 0.2), run_time=0.8)
        wait_to(4)

        # ═══════════════════════════════════════
        # seg 4: "左焦点=−c，所以c=1"
        # ═══════════════════════════════════════
        c_calc = MathTex(r"-c=-1 \;\Rightarrow\; c=1", font_size=36, color=GREEN)
        c_calc.next_to(focus_info, DOWN, buff=0.5)
        arrow_c = Arrow(focus_info.get_bottom(), c_calc.get_top(), color=GREEN, buff=0.15, stroke_width=2)
        play_anim(4, GrowArrow(arrow_c), FadeIn(c_calc), run_time=1.0)
        wait_to(5)

        # ═══════════════════════════════════════
        # seg 5: "e=c/a=1/2, 所以a=2"
        # ═══════════════════════════════════════
        a_calc = MathTex(r"e=\frac{c}{a}=\frac{1}{2}\;\Rightarrow\; a=2", font_size=36, color=GREEN)
        a_calc.next_to(c_calc, DOWN, buff=0.4)
        arrow_a = Arrow(c_calc.get_bottom(), a_calc.get_top(), color=GREEN, buff=0.15, stroke_width=2)
        play_anim(5, GrowArrow(arrow_a), FadeIn(a_calc), run_time=1.2)
        wait_to(6)

        # ═══════════════════════════════════════
        # seg 6: "b²=a²−c²=4−1=3"
        # ═══════════════════════════════════════
        b_calc = MathTex(r"b^2=a^2-c^2=4-1=3", font_size=36, color=GREEN)
        b_calc.next_to(a_calc, DOWN, buff=0.4)
        arrow_b = Arrow(a_calc.get_bottom(), b_calc.get_top(), color=GREEN, buff=0.15, stroke_width=2)
        play_anim(6, GrowArrow(arrow_b), FadeIn(b_calc), run_time=1.0)
        wait_to(7)

        # ═══════════════════════════════════════
        # seg 7: "椭圆方程: x²/4+y²/3=1"
        # FadeOut 推导过程，显示最终结果 + 画椭圆
        # ═══════════════════════════════════════
        play_anim(7, FadeOut(VGroup(eq_general, focus_info, arrow_c, c_calc, arrow_a, a_calc, arrow_b, b_calc)), run_time=0.8)

        final_eq = MathTex(r"\frac{x^2}{4}+\frac{y^2}{3}=1", font_size=48, color=TXT)
        final_eq.to_edge(LEFT, buff=0.8).shift(UP * 0.5)

        # 画椭圆（缩小到左侧）
        axes = Axes(
            x_range=[-3, 3, 1], y_range=[-2.5, 2.5, 1],
            x_length=5, y_length=3.5,
            axis_config={"color": DIM, "stroke_width": 1.5, "include_numbers": False},
        ).scale(0.65)
        axes.move_to(RIGHT * 2.5 + DOWN * 0.3)

        ellipse = axes.plot_parametric_curve(
            lambda t: np.array([2 * np.cos(t), np.sqrt(3) * np.sin(t)]),
            t_range=[0, 2 * PI], color=BLUE, stroke_width=2.5
        )
        # 焦点
        f_dot = Dot(axes.c2p(-1, 0), radius=0.08, color=PINK)
        f_label = MathTex(r"F", font_size=28, color=PINK).next_to(f_dot, DL, buff=0.1)

        play_anim(7,
            FadeIn(final_eq),
            Create(axes), Create(ellipse),
            FadeIn(f_dot), FadeIn(f_label),
            run_time=2.0
        )
        wait_to(8)

        # ═══════════════════════════════════════
        # seg 8: "第二问第一小题"
        # ═══════════════════════════════════════
        play_anim(8, FadeOut(step1_title), run_time=0.4)
        step2_title = Text("（2）①", font="Microsoft YaHei", font_size=36, color=PINK)
        step2_title.to_edge(UP, buff=0.5)
        play_anim(8, FadeIn(step2_title, shift=DOWN * 0.2), run_time=0.5)
        wait_to(9)

        # ═══════════════════════════════════════
        # seg 9: "过F且斜率>0的动直线l与椭圆交于P,Q"
        # 用 ValueTracker 展示直线旋转
        # ═══════════════════════════════════════
        k_tracker = ValueTracker(0.5)

        def get_line():
            k = k_tracker.get_value()
            # y = k(x+1), 从 x=-3 到 x=3
            return axes.plot(
                lambda x: k * (x + 1),
                x_range=[-3, 3],
                color=AMBER, stroke_width=2.5
            )

        line_l = always_redraw(get_line)
        l_label = MathTex(r"l", font_size=30, color=AMBER).move_to(axes.c2p(2.5, 2.2))

        play_anim(9, FadeIn(line_l), FadeIn(l_label), run_time=1.5)
        wait_to(10)

        # ═══════════════════════════════════════
        # seg 10: "Q在第三象限"
        # 标注 P (第一象限附近) 和 Q (第三象限附近)
        # ═══════════════════════════════════════
        # 交点计算: y=k(x+1) 代入 x²/4+y²/3=1
        # (3+4k²)x² + 8k²x + (4k²-12) = 0
        def get_intersections(k):
            A = 3 + 4 * k**2
            B = 8 * k**2
            C = 4 * k**2 - 12
            disc = B**2 - 4 * A * C
            if disc < 0:
                return (0, 0), (0, 0)
            x1 = (-B + np.sqrt(disc)) / (2 * A)
            x2 = (-B - np.sqrt(disc)) / (2 * A)
            y1 = k * (x1 + 1)
            y2 = k * (x2 + 1)
            return (x1, y1), (x2, y2)

        def get_P_dot():
            k = k_tracker.get_value()
            p, q = get_intersections(k)
            return Dot(axes.c2p(*p), radius=0.1, color=GREEN)

        def get_Q_dot():
            k = k_tracker.get_value()
            p, q = get_intersections(k)
            return Dot(axes.c2p(*q), radius=0.1, color=CORAL)

        p_dot = always_redraw(get_P_dot)
        q_dot = always_redraw(get_Q_dot)
        p_label = MathTex(r"P", font_size=28, color=GREEN).add_updater(
            lambda m: m.next_to(p_dot, UR, buff=0.1)
        )
        q_label = MathTex(r"Q", font_size=28, color=CORAL).add_updater(
            lambda m: m.next_to(q_dot, DL, buff=0.1)
        )

        play_anim(10, FadeIn(p_dot), FadeIn(q_dot), FadeIn(p_label), FadeIn(q_label), run_time=1.0)
        wait_to(11)

        # ═══════════════════════════════════════
        # seg 11: "直线PO与椭圆另一个交点为R"
        # ═══════════════════════════════════════
        def get_R_dot():
            k = k_tracker.get_value()
            p, q = get_intersections(k)
            px, py = p
            # R is the other intersection of line OP with ellipse
            # If P = (px, py), then R = (-px, -py) for central symmetry
            return Dot(axes.c2p(-px, -py), radius=0.1, color=PINK)

        def get_PO_line():
            k = k_tracker.get_value()
            p, _ = get_intersections(k)
            px, py = p
            if abs(px) < 0.01:
                return Line(axes.c2p(0, -3), axes.c2p(0, 3), color=PINK, stroke_width=1.5)
            m = py / px
            return axes.plot(lambda x: m * x, x_range=[-3, 3], color=PINK, stroke_width=1.5)

        r_dot = always_redraw(get_R_dot)
        po_line = always_redraw(get_PO_line)
        r_label = MathTex(r"R", font_size=28, color=PINK).add_updater(
            lambda m: m.next_to(r_dot, DL, buff=0.1)
        )

        play_anim(11, Create(po_line), FadeIn(r_dot), FadeIn(r_label), run_time=1.2)
        wait_to(12)

        # ═══════════════════════════════════════
        # seg 12: "△PQR面积=3×△PFO面积，求l方程"
        # 显示面积条件
        # ═══════════════════════════════════════
        area_cond = MathTex(r"S_{\triangle PQR}=3\,S_{\triangle PFO}", font_size=36, color=TXT)
        area_cond.to_edge(RIGHT, buff=0.5).shift(UP * 1.5)

        play_anim(12, FadeIn(area_cond, shift=LEFT * 0.3), run_time=1.2)
        wait_to(13)

        # ═══════════════════════════════════════
        # seg 13: "设l斜率为k，方程y=k(x+1)"
        # ═══════════════════════════════════════
        line_eq = MathTex(r"l:\; y=k(x+1)", font_size=34, color=AMBER)
        line_eq.next_to(area_cond, DOWN, buff=0.4)

        play_anim(13, FadeIn(line_eq, shift=LEFT * 0.2), run_time=1.0)
        wait_to(14)

        # ═══════════════════════════════════════
        # seg 14: "代入椭圆，韦达定理求P,Q坐标关系"
        # ═══════════════════════════════════════
        vieta = MathTex(
            r"x_P+x_Q=-\frac{8k^2}{3+4k^2},\quad x_P x_Q=\frac{4k^2-12}{3+4k^2}",
            font_size=30, color=TXT
        )
        vieta.next_to(line_eq, DOWN, buff=0.4)

        play_anim(14, Write(vieta), run_time=2.0)
        wait_to(15)

        # ═══════════════════════════════════════
        # seg 15: "由面积条件，得到关于k的方程"
        # ═══════════════════════════════════════
        area_eq = MathTex(
            r"\frac{S_{\triangle PQR}}{S_{\triangle PFO}}=\frac{|x_P-x_Q|}{|x_F|}=3",
            font_size=32, color=GREEN
        )
        area_eq.next_to(vieta, DOWN, buff=0.4)

        play_anim(15, FadeIn(area_eq, shift=UP * 0.2), run_time=1.0)
        wait_to(16)

        # ═══════════════════════════════════════
        # seg 16: "解出k=1"
        # 清理推导，显示结果
        # ═══════════════════════════════════════
        k_result = MathTex(r"k=1", font_size=44, color=GREEN)
        k_result.move_to(ORIGIN + DOWN * 0.5)

        play_anim(16, FadeOut(VGroup(vieta, area_eq)), FadeIn(k_result, scale=1.5), run_time=0.8)
        wait_to(17)

        # ═══════════════════════════════════════
        # seg 17: "l方程: y=x+1"
        # 让 k_tracker 滑到 1，直线锁定
        # ═══════════════════════════════════════
        play_anim(17,
            k_tracker.animate.set_value(1.0),
            run_time=2.0
        )

        answer1 = MathTex(r"l:\; y=x+1", font_size=42, color=GREEN)
        answer1.next_to(k_result, DOWN, buff=0.4)
        box = SurroundingRectangle(answer1, color=GREEN, buff=0.15, stroke_width=2)

        play_anim(17, FadeIn(answer1), Create(box), run_time=1.0)
        wait_to(18)

        # ═══════════════════════════════════════
        # seg 18: "第二小题，求tan∠PQR最小值"
        # ═══════════════════════════════════════
        # 清屏准备新内容
        play_anim(18, FadeOut(VGroup(area_cond, line_eq, k_result, answer1, box, step2_title)), run_time=0.8)
        # 保留椭圆图在右侧

        step2b_title = Text("（2）② 求 tan∠PQR 最小值", font="Microsoft YaHei", font_size=34, color=PINK)
        step2b_title.to_edge(UP, buff=0.5)
        play_anim(18, FadeIn(step2b_title, shift=DOWN * 0.2), run_time=0.8)
        wait_to(19)

        # ═══════════════════════════════════════
        # seg 19: "用向量法或斜率公式"
        # ═══════════════════════════════════════
        method = Text("斜率公式法", font="Microsoft YaHei", font_size=30, color=AMBER)
        method.to_edge(LEFT, buff=0.8).shift(UP * 1.0)
        play_anim(19, FadeIn(method), run_time=0.8)
        wait_to(20)

        # ═══════════════════════════════════════
        # seg 20: "设P,Q坐标，用参数t表示"
        # ═══════════════════════════════════════
        param_text = MathTex(
            r"P(x_1,y_1),\;Q(x_2,y_2),\;R(-x_1,-y_1)",
            font_size=30, color=TXT
        )
        param_text.next_to(method, DOWN, buff=0.4)
        play_anim(20, FadeIn(param_text), run_time=1.0)
        wait_to(21)

        # ═══════════════════════════════════════
        # seg 21: "tan∠PQR = |k_QP−k_QR|/(1+k_QP·k_QR)"
        # ═══════════════════════════════════════
        tan_formula = MathTex(
            r"\tan\angle PQR=\left|\frac{k_{QP}-k_{QR}}{1+k_{QP}\cdot k_{QR}}\right|",
            font_size=32, color=PINK
        )
        tan_formula.next_to(param_text, DOWN, buff=0.4)
        play_anim(21, Write(tan_formula), run_time=1.5)
        wait_to(22)

        # ═══════════════════════════════════════
        # seg 22: "韦达定理化简，得到关于k的表达式"
        # ═══════════════════════════════════════
        play_anim(22, FadeOut(method), run_time=0.3)
        simplified = MathTex(
            r"\tan\angle PQR=\frac{4\sqrt{3}}{3}\cdot\frac{k}{1+4k^2}",
            font_size=34, color=BLUE
        )
        simplified.next_to(tan_formula, DOWN, buff=0.5)
        arrow_simp = Arrow(tan_formula.get_bottom(), simplified.get_top(), color=BLUE, buff=0.15, stroke_width=2)
        play_anim(22, GrowArrow(arrow_simp), FadeIn(simplified), run_time=1.5)
        wait_to(23)

        # ═══════════════════════════════════════
        # seg 23: "求导或均值不等式求最小值"
        # ═══════════════════════════════════════
        # 用均值不等式: k/(1+4k²) = 1/(1/k + 4k) ≤ 1/(2√4) = 1/4
        ineq = MathTex(
            r"\frac{k}{1+4k^2}=\frac{1}{\frac{1}{k}+4k}\leq\frac{1}{2\sqrt{4}}=\frac{1}{4}",
            font_size=32, color=GREEN
        )
        ineq.next_to(simplified, DOWN, buff=0.5)
        play_anim(23, Write(ineq), run_time=1.5)
        wait_to(24)

        # ═══════════════════════════════════════
        # seg 24: "tan∠PQR最小值=√3/3"
        # ═══════════════════════════════════════
        play_anim(24, FadeOut(VGroup(param_text, tan_formula, arrow_simp, ineq, simplified)), run_time=0.8)

        min_result = MathTex(
            r"\min\;\tan\angle PQR=\frac{\sqrt{3}}{3}",
            font_size=48, color=GREEN
        )
        min_result.move_to(ORIGIN + DOWN * 0.3)
        box2 = SurroundingRectangle(min_result, color=GREEN, buff=0.2, stroke_width=2.5)

        play_anim(24, FadeIn(min_result, scale=1.3), Create(box2), run_time=1.5)
        wait_to(25)

        # 结束 - 保持画面
        self.wait(2)
