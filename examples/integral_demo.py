"""积分演示 v3 - 动画严格对齐 TTS 时间轴

时间轴（基于 TTS 语音）：
  0.0-1.8   "首先，画一个坐标系。"
  2.3-5.8   "然后，画出曲线，y等于x的平方。"
  6.3-8.8   "这条曲线，就是我们要研究的函数。"
  9.3-13.3  "接下来，我们用矩形，去逼近曲线下方的面积。"
  13.8-16.6 "黎曼说，先把区间切成四份。"
  17.1-19.8 "每个矩形的宽度，是Δx。"
  20.3-23.0 "矩形的高度，取函数在中间的值。"
  23.5-25.9 "四个矩形加起来，是近似值。"
  26.4-27.7 "但太粗糙了。"
  28.2-29.9 "切成八份，更接近。"
  30.4-32.2 "十六份，更精确。"
  32.7-34.8 "三十二份，几乎一样了。"
  35.3-38.0 "六十四份，肉眼已经分不出了。"
  38.5-41.7 "当n趋向无穷，Δx趋向零。"
  42.2-45.2 "矩形的数量无穷多，宽度无穷小。"
  45.7-47.8 "近似，变成了精确。"
  48.3-49.8 "这就是积分。"
  50.3-52.2 "它的结果，等于九。"
  52.7-56.0 "积分，是无穷多个无穷小的矩形之和。"
  56.0-60.0  预留结尾

总时长 ~60s @ 30fps = 1800 帧
"""
from manim import *
import numpy as np

BG = "#0d1117"
CURVE = "#4fc3f7"
RECT = "#e8a87c"
ACCENT = "#7ed3a4"
TXT = "#e4e2d8"

config.background_color = BG
config.frame_rate = 30
config.pixel_width = 1920
config.pixel_height = 1080


class IntegralDemo(Scene):
    def construct(self):
        # ═══ 0.0-1.8s: 坐标系 ═══
        axes = Axes(
            x_range=[0, 3.5, 1], y_range=[0, 10, 2],
            x_length=9, y_length=5,
            axis_config={"color": GREY, "stroke_width": 2, "include_tip": True},
        ).shift(DOWN * 0.3 + LEFT * 0.5)

        x_lab = MathTex("x", color=TXT, font_size=28).next_to(axes.x_axis.get_end(), DOWN, buff=0.12)
        y_lab = MathTex("y", color=TXT, font_size=28).next_to(axes.y_axis.get_end(), LEFT, buff=0.12)

        self.play(Create(axes), run_time=1.0)           # 0.0-1.0s
        self.play(FadeIn(x_lab), FadeIn(y_lab), run_time=0.5)  # 1.0-1.5s
        self.wait(0.4)                                    # 1.5-1.8s (等语音说完)

        # ═══ 2.3-5.8s: 曲线 y=x² (语音领先，动画在 2.3s 开始) ═══
        self.wait(0.5)  # 1.8→2.3 语音间隙

        curve = axes.plot(lambda x: x**2, x_range=[0, 3], color=CURVE, stroke_width=3)
        curve_lab = MathTex("y = x^2", color=CURVE, font_size=36)
        curve_lab.move_to(axes.c2p(2.8, 9) + UP * 0.3 + RIGHT * 0.3)

        self.play(Create(curve), run_time=2.5, rate_func=smooth)  # 2.3-4.8s
        self.play(FadeIn(curve_lab, shift=DOWN * 0.2), run_time=0.6)  # 4.8-5.4s
        self.wait(0.5)  # 5.4-5.8s

        # ═══ 6.3-8.8s: 曲线说明（视觉保持，等语音） ═══
        self.wait(0.5)  # 5.8→6.3 间隙
        # 曲线已在画面上，不需要新动画，等语音说完
        self.wait(2.5)  # 6.3-8.8s

        # ═══ 9.3-13.3s: 矩形逼近概念引入 ═══
        self.wait(0.5)  # 8.8→9.3 间隙

        # 淡入 Δx 公式（右上角）
        dx_tex = MathTex(r"\Delta x = \frac{3}{4} = 0.75", color=RECT, font_size=30)
        dx_tex.to_corner(UR, buff=0.6).shift(DOWN * 0.5)
        self.play(FadeIn(dx_tex, shift=LEFT * 0.3), run_time=0.8)  # 9.3-10.1

        # 4 个矩形出现
        rects = axes.get_riemann_rectangles(
            curve, x_range=[0, 3], dx=0.75,
            input_sample_type="center", stroke_width=1, stroke_color=WHITE,
            color=[RECT, ACCENT], fill_opacity=0.3,
        )
        n_lab = MathTex("n = 4", color=TXT, font_size=30)
        n_lab.next_to(dx_tex, DOWN, aligned_edge=LEFT, buff=0.3)

        self.play(Create(rects), run_time=1.5)  # 10.1-11.6s
        self.play(FadeIn(n_lab), run_time=0.5)   # 11.6-12.1s
        self.wait(1.3)  # 12.1-13.3s (等语音"逼近曲线下方的面积"说完)

        # ═══ 13.8-16.6s: "黎曼说，先把区间切成四份" — 高亮 Δx 和 f(xᵢ) ═══
        self.wait(0.5)  # 13.3→13.8

        # 高亮一个矩形
        highlight = rects[1].copy().set_fill(ACCENT, opacity=0.6)
        self.play(FadeIn(highlight), run_time=0.5)  # 13.8-14.3

        # Δx 大括号
        brace = Brace(rects[1], DOWN, color=RECT, buff=0.1)
        brace_tex = brace.get_tex(r"\Delta x").set_color(RECT)
        self.play(Create(brace), Write(brace_tex), run_time=0.8)  # 14.3-15.1

        # f(xᵢ) 标注
        h_line = DashedLine(axes.c2p(0.75, 0), axes.c2p(0.75, 0.75**2),
                            color=ACCENT, stroke_width=1.5, dash_length=0.08)
        h_lab = MathTex(r"f(x_i)", color=ACCENT, font_size=26).next_to(h_line, RIGHT, buff=0.2)
        self.play(Create(h_line), Write(h_lab), run_time=0.8)  # 15.1-15.9
        self.wait(0.8)  # 15.9-16.6

        # ═══ 17.1-19.8s: "每个矩形的宽度，是Δx" — 保持标注 ═══
        self.wait(0.5)  # 16.6→17.1
        self.wait(2.7)  # 17.1-19.8 (语音讲解，画面保持)

        # ═══ 20.3-23.0s: "矩形的高度，取函数在中间的值" ═══
        self.wait(0.5)  # 19.8→20.3
        # 高亮已经在了，等语音说完
        self.wait(2.7)  # 20.3-23.0

        # ═══ 23.5-25.9s: "四个矩形加起来，是近似值" — 清除标注 ═══
        self.wait(0.5)  # 23.0→23.5
        self.play(
            FadeOut(highlight), FadeOut(brace), FadeOut(brace_tex),
            FadeOut(h_line), FadeOut(h_lab),
            run_time=0.8
        )  # 23.5-24.3
        self.wait(1.6)  # 24.3-25.9

        # ═══ 26.4-27.7s: "但太粗糙了" — 快速闪烁 ═══
        self.wait(0.5)  # 25.9→26.4
        self.wait(1.3)  # 26.4-27.7

        # ═══ 28.2-29.9s: "切成八份，更接近" ═══
        self.wait(0.5)  # 27.7→28.2
        rects_8 = axes.get_riemann_rectangles(
            curve, x_range=[0, 3], dx=3/8,
            input_sample_type="center", stroke_width=1, stroke_color=WHITE,
            color=[RECT, ACCENT], fill_opacity=0.3,
        )
        n8 = MathTex("n = 8", color=TXT, font_size=30).move_to(n_lab)
        self.play(Transform(rects, rects_8), Transform(n_lab, n8), run_time=0.8)  # 28.2-29.0
        self.wait(0.9)  # 29.0-29.9

        # ═══ 30.4-32.2s: "十六份，更精确" ═══
        self.wait(0.5)  # 29.9→30.4
        rects_16 = axes.get_riemann_rectangles(
            curve, x_range=[0, 3], dx=3/16,
            input_sample_type="center", stroke_width=1, stroke_color=WHITE,
            color=[RECT, ACCENT], fill_opacity=0.3,
        )
        n16 = MathTex("n = 16", color=TXT, font_size=30).move_to(n_lab)
        self.play(Transform(rects, rects_16), Transform(n_lab, n16), run_time=0.8)
        self.wait(1.0)

        # ═══ 32.7-34.8s: "三十二份，几乎一样了" ═══
        self.wait(0.5)  # 32.2→32.7
        rects_32 = axes.get_riemann_rectangles(
            curve, x_range=[0, 3], dx=3/32,
            input_sample_type="center", stroke_width=1, stroke_color=WHITE,
            color=[RECT, ACCENT], fill_opacity=0.3,
        )
        n32 = MathTex("n = 32", color=TXT, font_size=30).move_to(n_lab)
        self.play(Transform(rects, rects_32), Transform(n_lab, n32), run_time=0.8)
        self.wait(1.3)

        # ═══ 35.3-38.0s: "六十四份，肉眼已经分不出了" ═══
        self.wait(0.5)  # 34.8→35.3
        rects_64 = axes.get_riemann_rectangles(
            curve, x_range=[0, 3], dx=3/64,
            input_sample_type="center", stroke_width=1, stroke_color=WHITE,
            color=[RECT, ACCENT], fill_opacity=0.3,
        )
        n64 = MathTex("n = 64", color=TXT, font_size=30).move_to(n_lab)
        self.play(Transform(rects, rects_64), Transform(n_lab, n64), run_time=0.8)
        self.wait(1.9)

        # ═══ 38.5-41.7s: "当n趋向无穷，Δx趋向零" — 极限公式 ═══
        self.wait(0.5)  # 38.0→38.5
        limit = MathTex(r"n \to \infty", r",\quad", r"\Delta x \to 0", color=RECT, font_size=36)
        limit.to_edge(DOWN, buff=0.8)
        self.play(Write(limit), run_time=1.5)  # 38.5-40.0
        self.wait(1.7)  # 40.0-41.7

        # ═══ 42.2-45.2s: "矩形的数量无穷多，宽度无穷小" ═══
        self.wait(0.5)  # 41.7→42.2
        self.wait(3.0)  # 42.2-45.2

        # ═══ 45.7-47.8s: "近似，变成了精确" — 矩形→面积 ═══
        self.wait(0.5)  # 45.2→45.7
        area = axes.get_area(curve, x_range=[0, 3], color=[CURVE, ACCENT], opacity=0.25)
        self.play(
            FadeOut(rects), FadeOut(n_lab), FadeOut(dx_tex),
            FadeIn(area),
            run_time=1.5
        )  # 45.7-47.2
        self.wait(0.6)  # 47.2-47.8

        # ═══ 48.3-49.8s: "这就是积分" — 积分公式 ═══
        self.wait(0.5)  # 47.8→48.3
        integral = MathTex(r"\int_0^3", r"x^2", r"\,dx", r"=", r"9", font_size=52)
        integral[0].set_color(ACCENT)
        integral[1].set_color(CURVE)
        integral[2].set_color(ACCENT)
        integral[3].set_color(TXT)
        integral[4].set_color(ACCENT)
        integral.to_edge(UP, buff=0.6)
        self.play(Write(integral), run_time=1.0)  # 48.3-49.3
        self.wait(0.5)  # 49.3-49.8

        # ═══ 50.3-52.2s: "它的结果，等于九" — 高亮结果 ═══
        self.wait(0.5)  # 49.8→50.3
        # 9 高亮放大
        self.play(
            integral[4].animate.scale(1.3).set_color(CURVE),
            run_time=0.6
        )  # 50.3-50.9
        self.wait(1.3)  # 50.9-52.2

        # ═══ 52.7-56.0s: "积分，是无穷多个无穷小的矩形之和" ═══
        self.wait(0.5)  # 52.2→52.7
        conclusion = Text(
            "积分 = 无穷多个无穷小的矩形之和",
            font="Microsoft YaHei", font_size=28, color=TXT
        ).next_to(integral, DOWN, buff=0.5)
        self.play(FadeIn(conclusion, shift=UP * 0.2), run_time=0.8)  # 52.7-53.5
        self.wait(2.5)  # 53.5-56.0

        # ═══ 56.0-60.0s: 结尾 ═══
        self.wait(1.0)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.0)
        self.wait(1.5)

