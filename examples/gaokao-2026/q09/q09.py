"""2026高考数学第9题 - 复数运算（复平面可视化）"""
from manim import *

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

# T from timeline.json (13 segs, indices 0-12)
T = [0.0, 2.9, 5.32, 8.38, 10.64, 12.74, 16.92, 19.34, 22.08, 25.3, 30.92, 33.18, 34.8]


class Q09(Scene):
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
        title = Text("第 9 题", font="Microsoft YaHei", font_size=56, color=TXT)
        sub = Text("2026年新高考一卷", font="Microsoft YaHei", font_size=24, color=DIM)
        sub.next_to(title, DOWN, buff=0.4)
        play_anim(0, FadeIn(title, shift=DOWN * 0.3), run_time=0.8)
        play_anim(0, FadeIn(sub), run_time=0.5)
        wait_to(1)
        play_anim(1, FadeOut(title), FadeOut(sub), run_time=0.3)

        # ═══ seg 1-2: 题目 ═══
        problem = MathTex(r"z = 1 + i", font_size=44, color=TXT)
        question = MathTex(r"|z^2 - 2z| = \ ?", font_size=38, color=PINK)
        q_group = VGroup(problem, question).arrange(DOWN, buff=0.4)
        play_anim(1, FadeIn(q_group, shift=UP * 0.2), run_time=0.8)
        wait_to(2)

        # Options
        options = VGroup(
            MathTex(r"\text{A. } 0", font_size=26, color=DIM),
            MathTex(r"\text{B. } 1", font_size=26, color=DIM),
            MathTex(r"\text{C. } \sqrt{2}", font_size=26, color=DIM),
            MathTex(r"\text{D. } 2", font_size=26, color=DIM),
        ).arrange(RIGHT, buff=1.0)
        options.next_to(q_group, DOWN, buff=0.5)
        play_anim(2, FadeIn(options, shift=UP * 0.15), run_time=0.5)
        wait_to(3)
        play_anim(3, FadeOut(q_group), FadeOut(options), run_time=0.3)

        # ═══ seg 3: "直接算就行" ═══
        approach = Text("直接计算", font="Microsoft YaHei", font_size=32, color=AMBER)
        play_anim(3, FadeIn(approach, shift=UP * 0.2), run_time=0.5)
        wait_to(4)
        play_anim(4, FadeOut(approach), run_time=0.3)

        # ═══ seg 4-5: 算 z² ═══
        step1_title = MathTex(r"z^2 = (1+i)^2", font_size=38, color=BLUE)
        step1_title.move_to(UP * 1.5)
        play_anim(4, FadeIn(step1_title, shift=UP * 0.2), run_time=0.6)
        wait_to(5)

        step1_expand = MathTex(r"= 1 + 2i + i^2", font_size=36, color=BLUE)
        step1_expand.next_to(step1_title, DOWN, buff=0.3)
        play_anim(5, FadeIn(step1_expand, shift=UP * 0.15), run_time=0.6)
        wait_to(6)

        # ═══ seg 6: i² = -1 ═══
        i2_note = MathTex(r"i^2 = -1", font_size=30, color=DIM)
        i2_note.next_to(step1_expand, DOWN, buff=0.25)
        play_anim(6, FadeIn(i2_note, shift=UP * 0.15), run_time=0.5)
        wait_to(7)

        # ═══ seg 7: z² = 2i ═══
        play_anim(7, FadeOut(step1_title), FadeOut(step1_expand), FadeOut(i2_note), run_time=0.3)
        result_z2 = MathTex(r"z^2 = 2i", font_size=44, color=GREEN)
        result_z2.move_to(UP * 1)
        play_anim(7, FadeIn(result_z2, scale=1.2), run_time=0.6)
        wait_to(8)

        # ═══ seg 8: 2z = 2+2i ═══
        play_anim(8, FadeOut(result_z2), run_time=0.3)
        step2 = MathTex(r"2z = 2(1+i) = 2 + 2i", font_size=36, color=AMBER)
        step2.move_to(UP * 1)
        play_anim(8, FadeIn(step2, shift=UP * 0.2), run_time=0.7)
        wait_to(9)

        # ═══ seg 9: z² - 2z ═══
        play_anim(9, FadeOut(step2), run_time=0.3)
        step3 = VGroup(
            MathTex(r"z^2 - 2z = 2i - (2 + 2i)", font_size=34, color=TXT),
            MathTex(r"= 2i - 2 - 2i", font_size=34, color=TXT),
            MathTex(r"= -2", font_size=40, color=GREEN),
        ).arrange(DOWN, buff=0.25)
        step3.move_to(UP * 0.8)
        for line in step3:
            play_anim(9, FadeIn(line, shift=UP * 0.15), run_time=0.5)
        wait_to(10)

        # ═══ seg 10: 模 ═══
        play_anim(10, FadeOut(step3), run_time=0.3)
        modulus = MathTex(r"|z^2 - 2z| = |-2| = 2", font_size=42, color=GREEN)
        modulus.move_to(UP * 0.5)
        play_anim(10, FadeIn(modulus, scale=1.1), run_time=0.7)

        # ═══ seg 10: 复平面可视化 (在右侧) ═══
        # Complex plane axes
        plane = ComplexPlane(
            x_range=[-3, 3, 1], y_range=[-2, 2, 1],
            x_length=5, y_length=3.5,
            background_line_style={"stroke_color": DIM, "stroke_width": 1, "stroke_opacity": 0.4},
            axis_config={"stroke_color": TXT, "stroke_width": 1.5},
        ).scale(0.8)
        plane.move_to(RIGHT * 3.5 + DOWN * 0.5)

        # Labels
        plane_labels = VGroup()
        for val, pos in [(-2, LEFT*2), (-1, LEFT), (1, RIGHT), (2, RIGHT*2)]:
            lab = MathTex(str(val), font_size=18, color=DIM)
            lab.next_to(plane.c2p(val, 0), DOWN, buff=0.1)
            plane_labels.add(lab)
        for val, pos in [(-1, DOWN), (1, UP)]:
            lab = MathTex(str(val) + "i", font_size=18, color=DIM)
            lab.next_to(plane.c2p(0, val), LEFT, buff=0.1)
            plane_labels.add(lab)

        # Mark z = 1+i
        z_dot = Dot(plane.c2p(1, 1), color=BLUE, radius=0.08)
        z_label = MathTex(r"z=1+i", font_size=22, color=BLUE)
        z_label.next_to(z_dot, UR, buff=0.1)

        # Mark z²-2z = -2
        result_dot = Dot(plane.c2p(-2, 0), color=GREEN, radius=0.08)
        result_label = MathTex(r"z^2-2z=-2", font_size=22, color=GREEN)
        result_label.next_to(result_dot, DOWN, buff=0.15)

        play_anim(10, FadeIn(plane), FadeIn(plane_labels), run_time=0.6)
        play_anim(10, FadeIn(z_dot), FadeIn(z_label), run_time=0.4)
        play_anim(10, FadeIn(result_dot), FadeIn(result_label), run_time=0.4)

        # Arrow showing modulus
        mod_arrow = Arrow(
            plane.c2p(0, 0), plane.c2p(-2, 0),
            color=PINK, stroke_width=3, buff=0.05,
        )
        mod_lbl = MathTex(r"|{-2}|=2", font_size=22, color=PINK)
        mod_lbl.next_to(mod_arrow, UP, buff=0.1)
        play_anim(10, FadeIn(mod_arrow), FadeIn(mod_lbl), run_time=0.4)
        wait_to(11)

        # ═══ seg 11: 答案 D ═══
        play_anim(11, FadeOut(modulus), FadeOut(plane), FadeOut(plane_labels),
                  FadeOut(z_dot), FadeOut(z_label), FadeOut(result_dot),
                  FadeOut(result_label), FadeOut(mod_arrow), FadeOut(mod_lbl),
                  run_time=0.3)
        answer = Text("答案 D：2", font="Microsoft YaHei", font_size=56, color=GREEN, weight=BOLD)
        play_anim(11, FadeIn(answer, scale=1.3), run_time=0.6)
        wait_to(12)

        # ═══ seg 12: 总结 ═══
        play_anim(12, FadeOut(answer), run_time=0.3)
        tip = VGroup(
            Text("复数运算别慌", font="Microsoft YaHei", font_size=30, color=AMBER),
            Text("先算平方 → 再算乘法 → 最后相减", font="Microsoft YaHei", font_size=24, color=TXT),
        ).arrange(DOWN, buff=0.25)
        tip.move_to(ORIGIN)
        play_anim(12, FadeIn(tip, shift=UP * 0.2), run_time=0.8)
        wait_to(13)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.0)
        self.wait(0.5)
