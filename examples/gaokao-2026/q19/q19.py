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
RED = "#e74c3c"

# ── TTS 时间轴 (49 segs) ──
T = [0.0, 3.38, 7.24, 12.54, 21.68, 27.62, 31.8, 36.78, 41.76, 49.3,
     55.08, 60.22, 65.2, 73.06, 76.76, 81.58, 89.28, 94.74, 102.12,
     110.46, 119.44, 122.02, 130.84, 135.18, 138.24, 141.62, 147.24,
     152.7, 159.76, 165.06, 171.96, 178.22, 181.6, 186.42, 189.8,
     194.46, 197.52, 202.34, 206.36, 209.58, 214.4, 219.22, 223.72,
     226.94, 232.4, 234.98, 240.28, 243.18, 247.68]


class Q19(Scene):
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
        # seg 0: "来看第十九题，函数性质证明"
        # ═══════════════════════════════════════
        title = Text("第19题  函数性质证明", font="Microsoft YaHei", font_size=42, color=TXT)
        title.to_edge(UP, buff=0.5)
        play_anim(0, FadeIn(title, shift=DOWN * 0.3), run_time=1.2)
        wait_to(1)

        # ═══════════════════════════════════════
        # seg 1: "f(x)定义域是全体实数"
        # ═══════════════════════════════════════
        domain = MathTex(r"f(x):\mathbb{R}\to\mathbb{R}", font_size=36, color=TXT)
        domain.next_to(title, DOWN, buff=0.5)
        play_anim(1, FadeIn(domain), run_time=0.8)
        wait_to(2)

        # ═══════════════════════════════════════
        # seg 2: "x<0时，f(x)=2^x"
        # ═══════════════════════════════════════
        piece_neg = MathTex(r"x<0:\quad f(x)=2^x", font_size=34, color=BLUE)
        piece_neg.next_to(domain, DOWN, buff=0.4)
        play_anim(2, FadeIn(piece_neg, shift=LEFT * 0.2), run_time=0.8)
        wait_to(3)

        # ═══════════════════════════════════════
        # seg 3: "D(x₀)={d | f(x₀+d)>f(x₀)}"
        # ═══════════════════════════════════════
        d_def = MathTex(
            r"D(x_0)=\{d\mid f(x_0+d)>f(x_0)\}",
            font_size=34, color=PINK
        )
        d_def.next_to(piece_neg, DOWN, buff=0.4)
        play_anim(3, Write(d_def), run_time=1.5)
        wait_to(4)

        # ═══════════════════════════════════════
        # seg 4: "第一问：x≥0时f(x)=1−x，求D(−1)"
        # ═══════════════════════════════════════
        play_anim(4, FadeOut(VGroup(title, domain)), run_time=0.5)
        q1_title = Text("（1）求 D(−1)", font="Microsoft YaHei", font_size=36, color=PINK)
        q1_title.to_edge(UP, buff=0.5)

        piece_pos = MathTex(r"x\geq 0:\quad f(x)=1-x", font_size=34, color=AMBER)
        piece_pos.next_to(piece_neg, DOWN, buff=0.3)

        play_anim(4, FadeIn(q1_title, shift=DOWN * 0.2), FadeIn(piece_pos), run_time=1.0)
        wait_to(5)

        # ═══════════════════════════════════════
        # seg 5: "f(−1)=2^(−1)=1/2"
        # 画函数图像
        # ═══════════════════════════════════════
        f_neg1 = MathTex(r"f(-1)=2^{-1}=\frac{1}{2}", font_size=34, color=GREEN)
        f_neg1.next_to(piece_pos, DOWN, buff=0.4)

        # 画坐标系 + 函数图像
        axes = Axes(
            x_range=[-4, 4, 1], y_range=[-1, 4, 1],
            x_length=5.5, y_length=3.5,
            axis_config={"color": DIM, "stroke_width": 1.5, "include_numbers": True, "font_size": 20},
        ).scale(0.6)
        axes.move_to(RIGHT * 2.5 + DOWN * 0.5)

        # 2^x for x<0
        curve_neg = axes.plot(lambda x: 2**x, x_range=[-4, 0], color=BLUE, stroke_width=2.5)
        # 1-x for x>=0
        curve_pos = axes.plot(lambda x: 1 - x, x_range=[0, 3], color=AMBER, stroke_width=2.5)

        # x=0 hollow dot at (0,1) for the 2^x side, solid at (0,1) for 1-x
        hollow = Circle(radius=0.06, color=BLUE, stroke_width=2).move_to(axes.c2p(0, 1))
        hollow.set_fill(BG, opacity=1)

        play_anim(5,
            FadeIn(f_neg1),
            Create(axes), Create(curve_neg), Create(curve_pos),
            FadeIn(hollow),
            run_time=2.0
        )
        wait_to(6)

        # ═══════════════════════════════════════
        # seg 6: "需要找所有d使得f(−1+d)>1/2"
        # ═══════════════════════════════════════
        target = MathTex(r"f(-1+d)>\frac{1}{2}", font_size=32, color=PINK)
        target.next_to(f_neg1, DOWN, buff=0.4)
        play_anim(6, FadeIn(target, shift=UP * 0.2), run_time=0.8)
        wait_to(7)

        # ═══════════════════════════════════════
        # seg 7: "−1+d<0时，f=2^(−1+d)"
        # ═══════════════════════════════════════
        case1 = MathTex(r"-1+d<0:\; 2^{-1+d}>\frac{1}{2}", font_size=30, color=BLUE)
        case1.next_to(target, DOWN, buff=0.4)
        play_anim(7, FadeIn(case1), run_time=0.8)
        wait_to(8)

        # ═══════════════════════════════════════
        # seg 8: "−1+d>−1, d>0"
        # ═══════════════════════════════════════
        case1_result = MathTex(r"\Rightarrow\; -1+d>-1 \;\Rightarrow\; d>0", font_size=30, color=GREEN)
        case1_result.next_to(case1, DOWN, buff=0.3)
        play_anim(8, FadeIn(case1_result, shift=LEFT * 0.2), run_time=1.0)
        wait_to(9)

        # ═══════════════════════════════════════
        # seg 9: "−1+d≥0时，f=1−(−1+d)=2−d"
        # ═══════════════════════════════════════
        case2 = MathTex(r"-1+d\geq 0:\; 2-d>\frac{1}{2}", font_size=30, color=AMBER)
        case2.next_to(case1_result, DOWN, buff=0.4)
        play_anim(9, FadeIn(case2), run_time=0.8)
        wait_to(10)

        # ═══════════════════════════════════════
        # seg 10: "d<3/2"
        # ═══════════════════════════════════════
        case2_result = MathTex(r"\Rightarrow\; d<\frac{3}{2}", font_size=30, color=GREEN)
        case2_result.next_to(case2, DOWN, buff=0.3)
        play_anim(10, FadeIn(case2_result, shift=LEFT * 0.2), run_time=0.8)
        wait_to(11)

        # ═══════════════════════════════════════
        # seg 11: "D(−1)=(0, 3/2)"
        # 清理推导，显示结果
        # ═══════════════════════════════════════
        play_anim(11, FadeOut(VGroup(f_neg1, target, case1, case1_result, case2, case2_result)), run_time=0.8)

        # 高亮 D(-1) 区间在数轴上
        num_line = NumberLine(
            x_range=[-1, 3, 0.5], length=5,
            color=DIM, include_numbers=True, font_size=20
        ).move_to(DOWN * 0.3 + LEFT * 2)

        d_interval = Line(
            num_line.n2p(0.05), num_line.n2p(1.45),
            color=GREEN, stroke_width=6
        )
        # open circles at 0 and 3/2
        c0 = Circle(radius=0.07, color=GREEN, stroke_width=2).move_to(num_line.n2p(0))
        c0.set_fill(BG, opacity=1)
        c32 = Circle(radius=0.07, color=GREEN, stroke_width=2).move_to(num_line.n2p(1.5))
        c32.set_fill(BG, opacity=1)

        d_answer = MathTex(r"D(-1)=\left(0,\;\frac{3}{2}\right)", font_size=40, color=GREEN)
        d_answer.move_to(DOWN * 1.5)
        box = SurroundingRectangle(d_answer, color=GREEN, buff=0.15, stroke_width=2)

        play_anim(11,
            FadeIn(num_line), Create(d_interval), FadeIn(c0), FadeIn(c32),
            FadeIn(d_answer), Create(box),
            run_time=1.5
        )
        wait_to(12)

        # ═══════════════════════════════════════
        # seg 12: "第二问：f奇函数，f(x₁)≤f(x₂)"
        # ═══════════════════════════════════════
        play_anim(12, FadeOut(VGroup(d_def, piece_neg, piece_pos, d_answer, box, num_line, d_interval, c0, c32, q1_title, axes, curve_neg, curve_pos, hollow)), run_time=0.8)

        q2_title = Text("（2）证明 D(x₂)⊆D(x₁)", font="Microsoft YaHei", font_size=36, color=PINK)
        q2_title.to_edge(UP, buff=0.5)
        cond_odd = MathTex(r"f(-x)=-f(x)\;(\text{odd})", font_size=32, color=BLUE)
        cond_odd.next_to(q2_title, DOWN, buff=0.5)
        cond_ineq = MathTex(r"f(x_1)\leq f(x_2),\quad x_1 x_2\neq 0", font_size=32, color=TXT)
        cond_ineq.next_to(cond_odd, DOWN, buff=0.4)

        play_anim(12, FadeIn(q2_title), FadeIn(cond_odd), FadeIn(cond_ineq), run_time=1.2)
        wait_to(13)

        # ═══════════════════════════════════════
        # seg 13: "证明D(x₂)⊆D(x₁)"
        # ═══════════════════════════════════════
        goal = MathTex(r"\text{Goal: }D(x_2)\subseteq D(x_1)", font_size=34, color=PINK)
        goal.next_to(cond_ineq, DOWN, buff=0.5)
        play_anim(13, FadeIn(goal, shift=UP * 0.2), run_time=0.8)
        wait_to(14)

        # ═══════════════════════════════════════
        # seg 14: "f(−x)=−f(x)"
        # ═══════════════════════════════════════
        step1 = MathTex(r"f(-x)=-f(x)", font_size=32, color=BLUE)
        step1.next_to(goal, DOWN, buff=0.5)
        play_anim(14, Write(step1), run_time=0.8)
        wait_to(15)

        # ═══════════════════════════════════════
        # seg 15: "f(x₁)≤f(x₂) → −f(x₁)≥−f(x₂)"
        # ═══════════════════════════════════════
        step2 = MathTex(r"f(x_1)\leq f(x_2)\;\Rightarrow\;-f(x_1)\geq -f(x_2)", font_size=30, color=TXT)
        step2.next_to(step1, DOWN, buff=0.3)
        arrow12 = Arrow(step1.get_bottom(), step2.get_top(), color=GREEN, buff=0.1, stroke_width=2)
        play_anim(15, GrowArrow(arrow12), FadeIn(step2), run_time=1.0)
        wait_to(16)

        # ═══════════════════════════════════════
        # seg 16: "即f(−x₁)≥f(−x₂)"
        # ═══════════════════════════════════════
        step3 = MathTex(r"f(-x_1)\geq f(-x_2)", font_size=32, color=GREEN)
        step3.next_to(step2, DOWN, buff=0.3)
        arrow23 = Arrow(step2.get_bottom(), step3.get_top(), color=GREEN, buff=0.1, stroke_width=2)
        play_anim(16, GrowArrow(arrow23), FadeIn(step3), run_time=0.8)
        wait_to(17)

        # ═══════════════════════════════════════
        # seg 17: "若d∈D(x₂)，则f(x₂+d)>f(x₂)"
        # ═══════════════════════════════════════
        step4 = MathTex(r"d\in D(x_2)\;\Rightarrow\; f(x_2+d)>f(x_2)", font_size=30, color=AMBER)
        step4.next_to(step3, DOWN, buff=0.3)
        play_anim(17, FadeIn(step4), run_time=0.8)
        wait_to(18)

        # ═══════════════════════════════════════
        # seg 18: "f(x₂+d)>f(x₂)≥f(x₁)"
        # ═══════════════════════════════════════
        step5 = MathTex(r"f(x_2+d)>f(x_2)\geq f(x_1)", font_size=30, color=TXT)
        step5.next_to(step4, DOWN, buff=0.3)
        arrow45 = Arrow(step4.get_bottom(), step5.get_top(), color=GREEN, buff=0.1, stroke_width=2)
        play_anim(18, GrowArrow(arrow45), FadeIn(step5), run_time=0.8)
        wait_to(19)

        # ═══════════════════════════════════════
        # seg 19: "奇函数性质推出f(x₁+d)>f(x₁)"
        # ═══════════════════════════════════════
        step6 = MathTex(r"\Rightarrow\; f(x_1+d)>f(x_1)", font_size=32, color=GREEN)
        step6.next_to(step5, DOWN, buff=0.3)
        arrow56 = Arrow(step5.get_bottom(), step6.get_top(), color=GREEN, buff=0.1, stroke_width=2)
        play_anim(19, GrowArrow(arrow56), FadeIn(step6), run_time=1.0)
        wait_to(20)

        # ═══════════════════════════════════════
        # seg 20: "所以d∈D(x₁)"
        # ═══════════════════════════════════════
        conclusion = MathTex(r"\therefore\; d\in D(x_1)", font_size=36, color=GREEN)
        conclusion.next_to(step6, DOWN, buff=0.4)
        box_c = SurroundingRectangle(conclusion, color=GREEN, buff=0.12, stroke_width=2)
        play_anim(20, FadeIn(conclusion, scale=1.3), Create(box_c), run_time=1.0)
        wait_to(21)

        # ═══════════════════════════════════════
        # seg 21: "第三问：条件..."
        # ═══════════════════════════════════════
        play_anim(21, FadeOut(VGroup(q2_title, cond_odd, cond_ineq, goal, step1, step2, step3, step4, step5, step6, conclusion, box_c, arrow12, arrow23, arrow45, arrow56)), run_time=0.8)

        q3_title = Text("（3）证明 f(0)≥1", font="Microsoft YaHei", font_size=36, color=PINK)
        q3_title.to_edge(UP, buff=0.5)
        play_anim(21, FadeIn(q3_title, shift=DOWN * 0.2), run_time=0.8)
        wait_to(22)

        # ═══════════════════════════════════════
        # seg 22: "0<x<1时，f(x)<f(0)"
        # ═══════════════════════════════════════
        cond1 = MathTex(r"0<x<1:\quad f(x)<f(0)", font_size=32, color=AMBER)
        cond1.next_to(q3_title, DOWN, buff=0.5)
        play_anim(22, FadeIn(cond1), run_time=0.8)
        wait_to(23)

        # ═══════════════════════════════════════
        # seg 23: "证明f(0)≥1"
        # ═══════════════════════════════════════
        goal3 = MathTex(r"\text{Prove: }f(0)\geq 1", font_size=34, color=PINK)
        goal3.next_to(cond1, DOWN, buff=0.4)
        play_anim(23, FadeIn(goal3, shift=UP * 0.2), run_time=0.8)
        wait_to(24)

        # ═══════════════════════════════════════
        # seg 24: "反证法：假设f(0)<1"
        # 红色 ✗ 可视化
        # ═══════════════════════════════════════
        assume = MathTex(r"\text{Suppose }f(0)<1", font_size=34, color=RED)
        assume.next_to(goal3, DOWN, buff=0.5)
        red_x = Text("✗", font_size=48, color=RED).next_to(assume, RIGHT, buff=0.3)
        play_anim(24, FadeIn(assume, shift=LEFT * 0.3), FadeIn(red_x, scale=2), run_time=1.0)
        wait_to(25)

        # ═══════════════════════════════════════
        # seg 25: "0<x<1, f(x)<f(0)<1"
        # ═══════════════════════════════════════
        chain1 = MathTex(r"0<x<1:\; f(x)<f(0)<1", font_size=30, color=TXT)
        chain1.next_to(assume, DOWN, buff=0.4)
        play_anim(25, FadeIn(chain1), run_time=0.8)
        wait_to(26)

        # ═══════════════════════════════════════
        # seg 26: "由f(x)<f(0)，得D(0)⊆D(x)"
        # ═══════════════════════════════════════
        chain2 = MathTex(r"f(x)<f(0)\;\Rightarrow\;D(0)\subseteq D(x)", font_size=30, color=GREEN)
        chain2.next_to(chain1, DOWN, buff=0.3)
        arrow_c12 = Arrow(chain1.get_bottom(), chain2.get_top(), color=GREEN, buff=0.1, stroke_width=2)
        play_anim(26, GrowArrow(arrow_c12), FadeIn(chain2), run_time=1.0)
        wait_to(27)

        # ═══════════════════════════════════════
        # seg 27: "取d=−x, f(0)>f(x), 所以−x∈D(x)"
        # ═══════════════════════════════════════
        chain3 = MathTex(r"d=-x:\; f(0)>f(x)\;\Rightarrow\; -x\in D(x)", font_size=30, color=TXT)
        chain3.next_to(chain2, DOWN, buff=0.3)
        play_anim(27, FadeIn(chain3), run_time=1.0)
        wait_to(28)

        # ═══════════════════════════════════════
        # seg 28: "D(0)⊆D(x) → −x∈D(0)"
        # ═══════════════════════════════════════
        chain4 = MathTex(r"D(0)\subseteq D(x)\;\Rightarrow\; -x\in D(0)", font_size=30, color=GREEN)
        chain4.next_to(chain3, DOWN, buff=0.3)
        arrow_c34 = Arrow(chain3.get_bottom(), chain4.get_top(), color=GREEN, buff=0.1, stroke_width=2)
        play_anim(28, GrowArrow(arrow_c34), FadeIn(chain4), run_time=0.8)
        wait_to(29)

        # ═══════════════════════════════════════
        # seg 29: "f(0+(−x))>f(0), f(−x)>f(0)"
        # ═══════════════════════════════════════
        chain5 = MathTex(r"f(-x)>f(0)", font_size=32, color=TXT)
        chain5.next_to(chain4, DOWN, buff=0.3)
        play_anim(29, FadeIn(chain5), run_time=0.8)
        wait_to(30)

        # ═══════════════════════════════════════
        # seg 30: "x>0时，−x<0，f(−x)=2^(−x)"
        # ═══════════════════════════════════════
        chain6 = MathTex(r"x>0:\; f(-x)=2^{-x}", font_size=30, color=BLUE)
        chain6.next_to(chain5, DOWN, buff=0.3)
        play_anim(30, FadeIn(chain6), run_time=0.8)
        wait_to(31)

        # ═══════════════════════════════════════
        # seg 31: "所以2^(−x)>f(0)"
        # ═══════════════════════════════════════
        chain7 = MathTex(r"2^{-x}>f(0)", font_size=32, color=TXT)
        chain7.next_to(chain6, DOWN, buff=0.3)
        play_anim(31, FadeIn(chain7), run_time=0.8)
        wait_to(32)

        # ═══════════════════════════════════════
        # seg 32: "x→0⁺时，2^(−x)→1"
        # ═══════════════════════════════════════
        chain8 = MathTex(r"x\to 0^+:\; 2^{-x}\to 1", font_size=32, color=AMBER)
        chain8.next_to(chain7, DOWN, buff=0.3)
        play_anim(32, FadeIn(chain8), run_time=0.8)
        wait_to(33)

        # ═══════════════════════════════════════
        # seg 33: "所以f(0)≤1"
        # ═══════════════════════════════════════
        chain9 = MathTex(r"\therefore\; f(0)\leq 1", font_size=34, color=TXT)
        chain9.next_to(chain8, DOWN, buff=0.3)
        play_anim(33, FadeIn(chain9), run_time=0.8)
        wait_to(34)

        # ═══════════════════════════════════════
        # seg 34: "由f(x)<f(0)和条件推出矛盾"
        # 红色 ✗ → 矛盾
        # ═══════════════════════════════════════
        contradiction = Text("矛盾！", font_size=40, color=RED)
        contradiction.next_to(chain9, DOWN, buff=0.4)
        big_x = Text("✗", font_size=64, color=RED).next_to(contradiction, RIGHT, buff=0.3)
        play_anim(34, FadeIn(contradiction, scale=1.5), FadeIn(big_x, scale=2), run_time=1.0)
        wait_to(35)

        # ═══════════════════════════════════════
        # seg 35: "最终f(0)≥1"
        # 清理，绿色 ✓
        # ═══════════════════════════════════════
        play_anim(35, FadeOut(VGroup(assume, red_x, chain1, chain2, chain3, chain4, chain5, chain6, chain7, chain8, chain9, contradiction, big_x, arrow_c12, arrow_c34, cond1, goal3)), run_time=0.8)

        result3 = MathTex(r"f(0)\geq 1", font_size=48, color=GREEN)
        result3.move_to(ORIGIN + DOWN * 0.3)
        check = Text("✓", font_size=56, color=GREEN).next_to(result3, RIGHT, buff=0.3)
        box3 = SurroundingRectangle(result3, color=GREEN, buff=0.15, stroke_width=2.5)

        play_anim(35, FadeIn(result3, scale=1.3), FadeIn(check, scale=1.5), Create(box3), run_time=1.0)
        wait_to(36)

        # ═══════════════════════════════════════
        # seg 36: "第四问：证明f在(0,+∞)单调递增"
        # ═══════════════════════════════════════
        play_anim(36, FadeOut(VGroup(result3, check, box3, q3_title)), run_time=0.8)

        q4_title = Text("（4）证明 f 在 (0,+∞) 单调递增", font="Microsoft YaHei", font_size=34, color=PINK)
        q4_title.to_edge(UP, buff=0.5)
        play_anim(36, FadeIn(q4_title, shift=DOWN * 0.2), run_time=0.8)
        wait_to(37)

        # ═══════════════════════════════════════
        # seg 37: "用条件①②和f(0)≥1"
        # ═══════════════════════════════════════
        tools = MathTex(r"D(x_2)\subseteq D(x_1),\; f(0)\geq 1", font_size=30, color=BLUE)
        tools.next_to(q4_title, DOWN, buff=0.5)
        play_anim(37, FadeIn(tools), run_time=0.8)
        wait_to(38)

        # ═══════════════════════════════════════
        # seg 38: "设0<x₁<x₂"
        # ═══════════════════════════════════════
        setup = MathTex(r"0<x_1<x_2", font_size=34, color=TXT)
        setup.next_to(tools, DOWN, buff=0.4)
        play_anim(38, FadeIn(setup), run_time=0.8)
        wait_to(39)

        # ═══════════════════════════════════════
        # seg 39: "需要证明f(x₁)<f(x₂)"
        # ═══════════════════════════════════════
        goal4 = MathTex(r"\text{Prove: }f(x_1)<f(x_2)", font_size=34, color=PINK)
        goal4.next_to(setup, DOWN, buff=0.4)
        play_anim(39, FadeIn(goal4, shift=UP * 0.2), run_time=0.8)
        wait_to(40)

        # ═══════════════════════════════════════
        # seg 40: "反证法：假设f(x₁)>f(x₂)"
        # ═══════════════════════════════════════
        assume4 = MathTex(r"\text{Suppose }f(x_1)>f(x_2)", font_size=32, color=RED)
        assume4.next_to(goal4, DOWN, buff=0.5)
        red_x4 = Text("✗", font_size=48, color=RED).next_to(assume4, RIGHT, buff=0.3)
        play_anim(40, FadeIn(assume4, shift=LEFT * 0.3), FadeIn(red_x4, scale=2), run_time=0.8)
        wait_to(41)

        # ═══════════════════════════════════════
        # seg 41: "D(x₂)⊆D(x₁)"
        # ═══════════════════════════════════════
        s1 = MathTex(r"D(x_2)\subseteq D(x_1)", font_size=30, color=GREEN)
        s1.next_to(assume4, DOWN, buff=0.4)
        play_anim(41, FadeIn(s1), run_time=0.8)
        wait_to(42)

        # ═══════════════════════════════════════
        # seg 42: "取d=x₂−x₁>0"
        # ═══════════════════════════════════════
        s2 = MathTex(r"d=x_2-x_1>0", font_size=30, color=TXT)
        s2.next_to(s1, DOWN, buff=0.3)
        play_anim(42, FadeIn(s2), run_time=0.8)
        wait_to(43)

        # ═══════════════════════════════════════
        # seg 43: "f(x₁+d)=f(x₂), 不大于f(x₁)"
        # ═══════════════════════════════════════
        s3 = MathTex(r"f(x_1+d)=f(x_2)\leq f(x_1)", font_size=30, color=TXT)
        s3.next_to(s2, DOWN, buff=0.3)
        arrow_s23 = Arrow(s2.get_bottom(), s3.get_top(), color=GREEN, buff=0.1, stroke_width=2)
        play_anim(43, GrowArrow(arrow_s23), FadeIn(s3), run_time=0.8)
        wait_to(44)

        # ═══════════════════════════════════════
        # seg 44: "所以d∉D(x₁)"
        # ═══════════════════════════════════════
        s4 = MathTex(r"\therefore\; d\notin D(x_1)", font_size=32, color=RED)
        s4.next_to(s3, DOWN, buff=0.3)
        play_anim(44, FadeIn(s4), run_time=0.8)
        wait_to(45)

        # ═══════════════════════════════════════
        # seg 45: "但f(x₂+d)=f(2x₂−x₁)"
        # ═══════════════════════════════════════
        s5 = MathTex(r"f(x_2+d)=f(2x_2-x_1)", font_size=30, color=TXT)
        s5.next_to(s4, DOWN, buff=0.3)
        play_anim(45, FadeIn(s5), run_time=0.8)
        wait_to(46)

        # ═══════════════════════════════════════
        # seg 46: "需要证明这>f(x₂)"
        # ═══════════════════════════════════════
        s6 = MathTex(r"f(2x_2-x_1)>f(x_2)\;?", font_size=30, color=AMBER)
        s6.next_to(s5, DOWN, buff=0.3)
        play_anim(46, FadeIn(s6), run_time=0.8)
        wait_to(47)

        # ═══════════════════════════════════════
        # seg 47: "由f(0)≥1和条件②推出矛盾"
        # 红✗ → 矛盾
        # ═══════════════════════════════════════
        contradiction4 = Text("矛盾！", font_size=40, color=RED)
        contradiction4.next_to(s6, DOWN, buff=0.4)
        big_x4 = Text("✗", font_size=64, color=RED).next_to(contradiction4, RIGHT, buff=0.3)
        play_anim(47, FadeIn(contradiction4, scale=1.5), FadeIn(big_x4, scale=2), run_time=1.0)
        wait_to(48)

        # ═══════════════════════════════════════
        # seg 48: "f在(0,+∞)单调递增"
        # 绿色 ✓
        # ═══════════════════════════════════════
        play_anim(48, FadeOut(VGroup(q4_title, tools, setup, goal4, assume4, red_x4, s1, s2, s3, s4, s5, s6, contradiction4, big_x4, arrow_s23)), run_time=0.8)

        result4 = MathTex(r"f(x)\text{ increasing on }(0,+\infty)", font_size=42, color=GREEN)
        result4.move_to(ORIGIN + DOWN * 0.3)
        check4 = Text("✓", font_size=56, color=GREEN).next_to(result4, RIGHT, buff=0.3)
        box4 = SurroundingRectangle(result4, color=GREEN, buff=0.15, stroke_width=2.5)

        play_anim(48, FadeIn(result4, scale=1.3), FadeIn(check4, scale=1.5), Create(box4), run_time=1.5)

        self.wait(2)
