"""2026高考数学第10题 - 二面角（3D几何）- 重制版v2
简化3D对象，避免Arrow3D等过重元素
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

T = [0.0, 2.58, 6.76, 11.9, 14.8, 17.38, 23.48, 32.46, 35.04, 41.78, 45.32, 48.86, 51.92, 55.3, 59.96, 64.62, 68.64, 71.22, 72.84, 78.0]


class Q10(ThreeDScene):
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
        title = Text("第 10 题", font="Microsoft YaHei", font_size=56, color=TXT)
        sub = Text("2026年新高考一卷 · 二面角", font="Microsoft YaHei", font_size=24, color=DIM)
        sub.next_to(title, DOWN, buff=0.4)
        self.add_fixed_in_frame_mobjects(title, sub)
        play_anim(0, FadeIn(title, shift=DOWN * 0.3), run_time=0.8)
        play_anim(0, FadeIn(sub), run_time=0.5)
        wait_to(1)
        play_anim(1, FadeOut(title), FadeOut(sub), run_time=0.3)

        # ═══ seg 1-2: 题目描述 ═══
        problem = Text(
            "正方体棱长1，E为AA₁中点",
            font="Microsoft YaHei", font_size=28, color=TXT,
        )
        question = Text("求平面BDE与底面ABCD所成二面角的正切值",
                        font="Microsoft YaHei", font_size=24, color=PINK)
        q_group = VGroup(problem, question).arrange(DOWN, buff=0.3)
        self.add_fixed_in_frame_mobjects(q_group)
        play_anim(1, FadeIn(q_group, shift=UP * 0.2), run_time=0.8)
        wait_to(3)
        play_anim(3, FadeOut(q_group), run_time=0.3)

        # ═══ seg 3-5: 画正方体（3D放大占满画面）═══
        self.set_camera_orientation(phi=65 * DEGREES, theta=-45 * DEGREES, zoom=1.2)

        s = 1.0
        B = np.array([0, 0, 0])
        A = np.array([s, 0, 0])
        C = np.array([0, s, 0])
        D = np.array([s, s, 0])
        B1 = np.array([0, 0, s])
        A1 = np.array([s, 0, s])
        C1 = np.array([0, s, s])
        D1 = np.array([s, s, s])
        E = (A + A1) / 2  # AA₁中点 = (1, 0, 0.5)

        all_verts = [B, A, C, D, B1, A1, C1, D1]
        edges = [
            (0, 1), (1, 3), (3, 2), (2, 0),  # 底面
            (4, 5), (5, 7), (7, 6), (6, 4),  # 顶面
            (0, 4), (1, 5), (2, 6), (3, 7),  # 竖边
        ]

        # 用Line代替Line3D（更轻量）
        cube_lines = VGroup()
        for i, j in edges:
            line = Line(all_verts[i], all_verts[j], color=DIM, stroke_width=2)
            cube_lines.add(line)

        play_anim(3, Create(cube_lines), run_time=1.5)

        # 标注关键点
        point_info = [
            ("B", B, DOWN + LEFT),
            ("A", A, DOWN + RIGHT),
            ("D", D, UP + RIGHT),
            ("E", E, RIGHT + OUT),
        ]

        dots = VGroup()
        label_groups = VGroup()
        for name, pos, direction in point_info:
            dot = Dot3D(pos, color=AMBER, radius=0.06)
            lab = Text(name, font_size=20, color=AMBER)
            lab.next_to(dot, direction, buff=0.1)
            dots.add(dot)
            label_groups.add(lab)

        play_anim(5, FadeIn(dots), FadeIn(label_groups), run_time=0.8)
        wait_to(6)

        # ═══ seg 6: 坐标系标注 ═══
        coord_info = VGroup(
            MathTex(r"B(0,0,0)", font_size=24, color=TXT),
            MathTex(r"D(1,1,0)", font_size=24, color=TXT),
            MathTex(r"E\left(1,0,\tfrac{1}{2}\right)", font_size=24, color=TXT),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(coord_info)
        coord_info.to_corner(UR, buff=0.4)
        play_anim(6, FadeIn(coord_info, shift=LEFT * 0.3), run_time=0.8)
        wait_to(7)

        # ═══ seg 7-8: 高亮平面BDE + 交线BD ═══
        play_anim(7, FadeOut(coord_info), run_time=0.3)

        plane_bde = Polygon(B, D, E, color=BLUE, fill_opacity=0.25, stroke_width=2)
        plane_bottom = Polygon(B, A, D, C, color=DIM, fill_opacity=0.1, stroke_width=1)
        play_anim(7, FadeIn(plane_bde), FadeIn(plane_bottom), run_time=0.8)

        # 高亮交线 BD
        bd_highlight = Line(B, D, color=PINK, stroke_width=5)
        play_anim(8, Create(bd_highlight), run_time=0.6)

        bd_lab = Text("交线 BD", font="Microsoft YaHei", font_size=22, color=PINK)
        self.add_fixed_in_frame_mobjects(bd_lab)
        bd_lab.to_corner(DR, buff=0.4)
        play_anim(8, FadeIn(bd_lab), run_time=0.4)
        wait_to(9)

        # ═══ seg 9-10: 向量 BD, BE ═══
        play_anim(9, FadeOut(bd_lab), run_time=0.3)

        # 用Line画向量（带箭头效果）
        vec_bd = Line(B, D, color=BLUE, stroke_width=4)
        vec_be = Line(B, E, color=AMBER, stroke_width=4)
        play_anim(9, Create(vec_bd), Create(vec_be), run_time=0.6)

        vec_info = VGroup(
            MathTex(r"\vec{BD} = (1, 1, 0)", font_size=28, color=BLUE),
            MathTex(r"\vec{BE} = (1, 0, \tfrac{1}{2})", font_size=28, color=AMBER),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(vec_info)
        vec_info.to_corner(UR, buff=0.4)
        play_anim(9, FadeIn(vec_info, shift=LEFT * 0.3), run_time=0.8)
        wait_to(11)

        # ═══ seg 10-11: 法向量计算 ═══
        play_anim(10, FadeOut(vec_info), run_time=0.3)

        cross_calc = VGroup(
            MathTex(r"\vec{n} = \vec{BD} \times \vec{BE}", font_size=28, color=GREEN),
            MathTex(r"= \left(\tfrac{1}{2}, -\tfrac{1}{2}, -1\right)", font_size=26, color=GREEN),
            MathTex(r"\propto (1, -1, -2)", font_size=28, color=GREEN),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(cross_calc)
        cross_calc.to_corner(UR, buff=0.4)
        play_anim(10, FadeIn(cross_calc, shift=LEFT * 0.3), run_time=0.8)
        wait_to(12)

        # ═══ seg 11-12: 底面法向量 ═══
        play_anim(11, FadeOut(cross_calc), run_time=0.3)

        n_bottom = MathTex(r"\vec{n_0} = (0, 0, 1)", font_size=28, color=DIM)
        self.add_fixed_in_frame_mobjects(n_bottom)
        n_bottom.to_corner(UR, buff=0.4)
        play_anim(11, FadeIn(n_bottom), run_time=0.5)

        # 底面法向量（向上）
        n0_line = Line(np.array([0.5, 0.5, 0]), np.array([0.5, 0.5, 0.6]), color=DIM, stroke_width=3)
        play_anim(11, Create(n0_line), run_time=0.5)
        wait_to(13)

        # ═══ seg 13-15: 夹角计算 ═══
        play_anim(13, FadeOut(n_bottom), run_time=0.3)

        calc = VGroup(
            MathTex(r"\cos\theta = \frac{|\vec{n} \cdot \vec{n_0}|}{|\vec{n}||\vec{n_0}|}", font_size=28, color=TXT),
            MathTex(r"= \frac{|{-2}|}{\sqrt{6} \cdot 1} = \frac{2}{\sqrt{6}}", font_size=26, color=TXT),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(calc)
        calc.to_corner(UR, buff=0.4)
        play_anim(13, FadeIn(calc, shift=LEFT * 0.3), run_time=0.8)
        wait_to(16)

        # ═══ seg 15-16: tan θ = 1 ═══
        play_anim(15, FadeOut(calc), run_time=0.3)

        tan_result = VGroup(
            MathTex(r"\cos\theta = \frac{2}{\sqrt{6}}", font_size=28, color=TXT),
            MathTex(r"\tan\theta = 1", font_size=38, color=GREEN),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(tan_result)
        tan_result.to_corner(UR, buff=0.4)
        play_anim(15, FadeIn(tan_result, shift=LEFT * 0.3), run_time=0.8)
        wait_to(17)

        # ═══ seg 16-17: 答案 ═══
        play_anim(16, FadeOut(tan_result), run_time=0.3)
        play_anim(16, FadeOut(plane_bde), FadeOut(plane_bottom), FadeOut(bd_highlight),
                  FadeOut(vec_bd), FadeOut(vec_be), FadeOut(n0_line),
                  FadeOut(cube_lines), FadeOut(dots), FadeOut(label_groups), run_time=0.5)

        answer = Text("答案 D", font="Microsoft YaHei", font_size=64, color=GREEN, weight=BOLD)
        self.add_fixed_in_frame_mobjects(answer)
        play_anim(17, FadeIn(answer, scale=1.5), run_time=0.6)
        wait_to(18)

        # ═══ seg 18: 总结 ═══
        play_anim(18, FadeOut(answer), run_time=0.3)
        tip = Text("二面角 → 向量法 → 找法向量 → 算夹角",
                    font="Microsoft YaHei", font_size=28, color=AMBER)
        self.add_fixed_in_frame_mobjects(tip)
        play_anim(18, FadeIn(tip, shift=UP * 0.2), run_time=0.8)
        wait_to(19)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.0)
        self.wait(0.5)
