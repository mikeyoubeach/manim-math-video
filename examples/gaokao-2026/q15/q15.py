"""2026高考数学第15题 - 直三棱柱（3D几何，重做版）
动画重点: ThreeDScene，三棱柱+发现B₁在平面上，3D放大
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
CORAL = "#c97b5d"

config.background_color = BG
config.frame_rate = 30
config.pixel_width = 1920
config.pixel_height = 1080

T = [0.0, 3.1, 8.8, 13.0, 15.8, 18.3, 24.8, 36.0, 38.6, 41.5, 46.9, 49.0, 55.8, 59.0, 64.6, 67.8, 71.7, 75.2, 81.0, 84.1, 86.8, 95.1, 97.4, 99.3, 102.7]


class Q15(ThreeDScene):
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

        self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES, zoom=0.8)

        # ===== seg 0: 标题 =====
        title = Text("第 15 题", font="Microsoft YaHei", font_size=64, color=TXT)
        subtitle = Text("直三棱柱", font="Microsoft YaHei", font_size=40, color=BLUE)
        subtitle.next_to(title, DOWN, buff=0.4)
        title_grp = VGroup(title, subtitle)
        self.add_fixed_in_frame_mobjects(title_grp)
        play_anim(0, FadeIn(title_grp, shift=DOWN * 0.3), run_time=0.8)
        wait_to(1)
        play_anim(1, FadeOut(title_grp), run_time=0.3)

        # ===== seg 1: 题目条件 =====
        prob1 = Text("直三棱柱 ABC-A₁B₁C₁", font="Microsoft YaHei", font_size=28, color=TXT)
        prob2 = Text("AB ⊥ BC, AB = BC = BB₁ = 2", font="Microsoft YaHei", font_size=26, color=DIM)
        prob3 = Text("求 B₁ 到平面 AC₁ 的距离", font="Microsoft YaHei", font_size=28, color=PINK)
        prob_grp = VGroup(prob1, prob2, prob3).arrange(DOWN, buff=0.25)
        self.add_fixed_in_frame_mobjects(prob_grp)
        play_anim(1, FadeIn(prob_grp, shift=UP * 0.2), run_time=0.8)
        wait_to(3)
        play_anim(3, FadeOut(prob_grp), run_time=0.3)

        # ===== seg 3-4: 画三棱柱 =====
        # 坐标: B原点, BA为x轴, BC为y轴, BB₁为z轴
        B = np.array([0, 0, 0])
        A = np.array([2, 0, 0])
        C = np.array([0, 2, 0])
        B1 = np.array([0, 0, 2])
        A1 = np.array([2, 0, 2])
        C1 = np.array([0, 2, 2])

        # 底面三角形
        bottom_edges = VGroup(
            Line(B, A, color=DIM, stroke_width=3),
            Line(B, C, color=DIM, stroke_width=3),
            Line(A, C, color=DIM, stroke_width=3),
        )
        # 顶面三角形
        top_edges = VGroup(
            Line(B1, A1, color=DIM, stroke_width=3),
            Line(B1, C1, color=DIM, stroke_width=3),
            Line(A1, C1, color=DIM, stroke_width=3),
        )
        # 竖边
        vert_edges = VGroup(
            Line(B, B1, color=DIM, stroke_width=3),
            Line(A, A1, color=DIM, stroke_width=3),
            Line(C, C1, color=DIM, stroke_width=3),
        )

        prism = VGroup(bottom_edges, top_edges, vert_edges)

        # 用半透明面填充底面和侧面
        bottom_face = Polygon(B, A, C, fill_color=BLUE, fill_opacity=0.15, stroke_width=0)
        side1 = Polygon(B, A, A1, B1, fill_color=BLUE, fill_opacity=0.08, stroke_width=0)
        side2 = Polygon(B, C, C1, B1, fill_color=BLUE, fill_opacity=0.08, stroke_width=0)
        side3 = Polygon(A, C, C1, A1, fill_color=BLUE, fill_opacity=0.05, stroke_width=0)
        top_face = Polygon(B1, A1, C1, fill_color=BLUE, fill_opacity=0.1, stroke_width=0)
        faces = VGroup(bottom_face, side1, side2, side3, top_face)

        play_anim(3, Create(prism), run_time=1.5)
        play_anim(3, FadeIn(faces), run_time=1.0)
        wait_to(4)

        # seg 4: 建坐标系文字
        coord_text = Text("建立空间直角坐标系", font="Microsoft YaHei", font_size=24, color=DIM)
        self.add_fixed_in_frame_mobjects(coord_text)
        coord_text.to_corner(UR, buff=0.5)
        play_anim(4, FadeIn(coord_text, shift=LEFT * 0.3), run_time=0.5)
        wait_to(5)

        # ===== seg 5: 标注坐标轴和点 =====
        # 坐标轴
        x_axis = Arrow(B, A * 1.3, color=RED, stroke_width=2, buff=0)
        y_axis = Arrow(B, C * 1.3, color=GREEN, stroke_width=2, buff=0)
        z_axis = Arrow(B, B1 * 1.3, color=BLUE, stroke_width=2, buff=0)
        axes_3d = VGroup(x_axis, y_axis, z_axis)

        x_label = Text("x", font_size=20, color=RED)
        y_label = Text("y", font_size=20, color=GREEN)
        z_label = Text("z", font_size=20, color=BLUE)
        x_label.move_to(A * 1.4 + DOWN * 0.2)
        y_label.move_to(C * 1.4 + LEFT * 0.2)
        z_label.move_to(B1 * 1.4 + RIGHT * 0.2)

        play_anim(5, Create(axes_3d), run_time=0.8)
        play_anim(5, FadeIn(VGroup(x_label, y_label, z_label)), run_time=0.5)

        # 标点
        point_data = [
            (B, "B", DOWN + LEFT * 0.3),
            (A, "A", DOWN + RIGHT * 0.2),
            (C, "C", DOWN + LEFT * 0.3),
            (B1, "B₁", LEFT * 0.3 + UP * 0.2),
            (A1, "A₁", RIGHT * 0.2 + UP * 0.2),
            (C1, "C₁", LEFT * 0.3 + UP * 0.2),
        ]
        dots = VGroup()
        dot_labels = VGroup()
        for pos, name, direction in point_data:
            d = Dot3D(pos, color=AMBER, radius=0.08)
            l = Text(name, font="Microsoft YaHei", font_size=18, color=AMBER)
            l.move_to(pos + direction * 0.3)
            dots.add(d)
            dot_labels.add(l)

        play_anim(5, FadeIn(dots), FadeIn(dot_labels), run_time=0.8)

        # 标直角符号
        right_angle = RightAngle(Line(B, A), Line(B, C), length=0.2, color=GREEN)
        play_anim(5, Create(right_angle), run_time=0.3)
        wait_to(6)

        # ===== seg 6: 坐标值 =====
        play_anim(6, FadeOut(coord_text), run_time=0.3)
        coords_info = VGroup(
            Text("B(0,0,0)  A(2,0,0)  C(0,2,0)", font="Microsoft YaHei", font_size=18, color=DIM),
            Text("B₁(0,0,2)  A₁(2,0,2)  C₁(0,2,2)", font="Microsoft YaHei", font_size=18, color=DIM),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(coords_info)
        coords_info.to_corner(UR, buff=0.4)
        play_anim(6, FadeIn(coords_info, shift=LEFT * 0.3), run_time=0.6)
        wait_to(7)

        # ===== seg 7-8: 转换视角，高亮平面 AC₁ =====
        play_anim(7, FadeOut(coords_info), run_time=0.3)
        self.move_camera(phi=50 * DEGREES, theta=-60 * DEGREES, zoom=0.85, run_time=1.0)
        elapsed += 1.0

        # 高亮 AC₁
        ac1_line = Line(A, C1, color=PINK, stroke_width=4)
        ac1_label = Text("AC₁", font="Microsoft YaHei", font_size=20, color=PINK)
        ac1_label.move_to((A + C1) / 2 + OUT * 0.3 + RIGHT * 0.3)
        play_anim(7, Create(ac1_line), FadeIn(ac1_label), run_time=0.8)
        wait_to(8)

        # seg 8: 需要三个点确定平面
        plane_hint = Text("平面 AC₁ 需三个点确定", font="Microsoft YaHei", font_size=22, color=DIM)
        self.add_fixed_in_frame_mobjects(plane_hint)
        plane_hint.to_corner(UR, buff=0.4)
        play_anim(8, FadeIn(plane_hint, shift=LEFT * 0.3), run_time=0.5)
        wait_to(9)

        # seg 9: 取中点 M
        play_anim(9, FadeOut(plane_hint), run_time=0.3)
        M = (A + C1) / 2  # (1, 1, 1)
        dot_m = Dot3D(M, color=GREEN, radius=0.1)
        label_m = Text("M(1,1,1)", font="Microsoft YaHei", font_size=18, color=GREEN)
        label_m.move_to(M + OUT * 0.3 + RIGHT * 0.3)
        play_anim(9, FadeIn(dot_m), FadeIn(label_m), run_time=0.6)
        wait_to(10)

        # ===== seg 10: 用向量法 =====
        play_anim(10, FadeOut(VGroup(plane_hint, dot_m, label_m)), run_time=0.3)
        vec_title = Text("向量法", font="Microsoft YaHei", font_size=28, color=BLUE)
        self.add_fixed_in_frame_mobjects(vec_title)
        vec_title.to_corner(UR, buff=0.4)
        play_anim(10, FadeIn(vec_title, shift=LEFT * 0.3), run_time=0.5)
        wait_to(11)

        # ===== seg 11: 向量 AC₁ 和 AB₁ =====
        play_anim(11, FadeOut(vec_title), run_time=0.3)

        # 向量可视化
        vec_ac1 = Arrow(A, C1, color=PINK, stroke_width=3, buff=0)
        vec_ab1 = Arrow(A, B1, color=AMBER, stroke_width=3, buff=0)
        vec_ac1_label = MathTex(r"\vec{AC_1}=(-2,2,2)", font_size=22, color=PINK)
        vec_ab1_label = MathTex(r"\vec{AB_1}=(-2,0,2)", font_size=22, color=AMBER)

        info_grp = VGroup(vec_ac1_label, vec_ab1_label).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(info_grp)
        info_grp.to_corner(UR, buff=0.4)

        play_anim(11, Create(vec_ac1), Create(vec_ab1), run_time=0.8)
        play_anim(11, FadeIn(info_grp, shift=LEFT * 0.3), run_time=0.6)
        wait_to(12)

        # seg 12: 法向量
        play_anim(12, FadeOut(info_grp), run_time=0.3)
        normal_info = VGroup(
            MathTex(r"\vec{n}=\vec{AC_1}\times\vec{AB_1}", font_size=24, color=GREEN),
            MathTex(r"=(4,0,4) \sim (1,0,1)", font_size=24, color=GREEN),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(normal_info)
        normal_info.to_corner(UR, buff=0.4)
        play_anim(12, FadeIn(normal_info, shift=LEFT * 0.3), run_time=0.8)
        wait_to(13)

        # seg 13: 简化
        play_anim(13, FadeOut(normal_info), run_time=0.3)
        normal_simple = MathTex(r"\vec{n}=(1,0,1)", font_size=28, color=GREEN)
        self.add_fixed_in_frame_mobjects(normal_simple)
        normal_simple.to_corner(UR, buff=0.4)
        play_anim(13, FadeIn(normal_simple, shift=LEFT * 0.3), run_time=0.5)
        wait_to(14)

        # ===== seg 14: 平面方程 =====
        play_anim(14, FadeOut(normal_simple), run_time=0.3)
        plane_eq_info = MathTex(r"x+z=d", font_size=28, color=AMBER)
        self.add_fixed_in_frame_mobjects(plane_eq_info)
        plane_eq_info.to_corner(UR, buff=0.4)
        play_anim(14, FadeIn(plane_eq_info, shift=LEFT * 0.3), run_time=0.5)

        # 画平面 AC₁ (半透明)
        plane_AC1 = Polygon(A, C, C1, A1, fill_color=PINK, fill_opacity=0.15, stroke_color=PINK, stroke_width=1.5)
        play_anim(14, FadeIn(plane_AC1), run_time=0.8)
        wait_to(15)

        # seg 15: 代入 A(2,0,0) → d=2
        play_anim(15, FadeOut(plane_eq_info), run_time=0.3)
        sub_a = MathTex(r"A(2,0,0): 2+0=d=2", font_size=24, color=TXT)
        plane_final = MathTex(r"x+z=2", font_size=32, color=GREEN)
        plane_grp = VGroup(sub_a, plane_final).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(plane_grp)
        plane_grp.to_corner(UR, buff=0.4)
        play_anim(15, FadeIn(plane_grp, shift=LEFT * 0.3), run_time=0.8)
        wait_to(16)

        # seg 16: 平面方程确认
        play_anim(16, FadeOut(plane_grp), run_time=0.3)
        plane_confirmed_label = Text("平面 AC₁: x+z=2", font="Microsoft YaHei", font_size=24, color=GREEN)
        self.add_fixed_in_frame_mobjects(plane_confirmed_label)
        plane_confirmed_label.to_corner(UR, buff=0.4)
        play_anim(16, FadeIn(plane_confirmed_label, shift=LEFT * 0.3), run_time=0.6)
        wait_to(17)

        # ===== seg 17: 求距离 =====
        play_anim(17, FadeOut(plane_confirmed_label), run_time=0.3)
        dist_formula = VGroup(
            Text("B₁到平面的距离:", font="Microsoft YaHei", font_size=22, color=TXT),
            MathTex(r"d=\frac{|0+0+2-2|}{\sqrt{1^2+0^2+1^2}}", font_size=26, color=BLUE),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(dist_formula)
        dist_formula.to_corner(UR, buff=0.4)
        play_anim(17, FadeIn(dist_formula, shift=LEFT * 0.3), run_time=0.8)
        wait_to(18)

        # seg 18: 计算结果
        play_anim(18, FadeOut(dist_formula), run_time=0.3)
        dist_result = MathTex(r"=\frac{0}{\sqrt{2}}=0", font_size=34, color=GREEN)
        self.add_fixed_in_frame_mobjects(dist_result)
        dist_result.to_corner(UR, buff=0.4)
        play_anim(18, FadeIn(dist_result, scale=1.2), run_time=0.6)
        wait_to(19)

        # ===== seg 19: 发现 B₁ 在平面上！关键转折 =====
        play_anim(19, FadeOut(dist_result), run_time=0.3)

        # 3D 放大: 缩放相机聚焦 B₁
        self.move_camera(
            phi=70 * DEGREES, theta=-40 * DEGREES,
            zoom=2.0,
            frame_center=B1,
            run_time=1.5,
        )
        elapsed += 1.5

        # 高亮 B₁ 点
        b1_highlight = Dot3D(B1, color=RED, radius=0.15)
        b1_glow = Dot3D(B1, color=RED, radius=0.25, fill_opacity=0.3)
        play_anim(19, FadeIn(b1_glow), FadeIn(b1_highlight), run_time=0.5)

        surprise = Text("B₁在平面上？!", font="Microsoft YaHei", font_size=36, color=RED)
        self.add_fixed_in_frame_mobjects(surprise)
        surprise.to_edge(DOWN, buff=1.0)
        play_anim(19, FadeIn(surprise, scale=1.3), run_time=0.5)
        wait_to(20)

        # ===== seg 20: 验证 B₁(0,0,2) 代入 x+z=2 =====
        play_anim(20, FadeOut(surprise), run_time=0.3)

        verify = VGroup(
            Text("验证 B₁(0,0,2):", font="Microsoft YaHei", font_size=22, color=TXT),
            Text("0 + 2 = 2 ✓", font_size=24, color=GREEN),
            Text("B₁确实在平面上!", font="Microsoft YaHei", font_size=24, color=GREEN),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(verify)
        verify.to_edge(DOWN, buff=0.8)

        play_anim(20, FadeIn(verify, shift=UP * 0.2), run_time=0.8)

        # B₁ 点变绿
        b1_green = Dot3D(B1, color=GREEN, radius=0.15)
        play_anim(20, Transform(b1_highlight, b1_green), run_time=0.5)
        wait_to(21)

        # ===== seg 21: 距离 = 0 =====
        play_anim(21, FadeOut(verify), run_time=0.3)
        play_anim(21, FadeOut(VGroup(b1_highlight, b1_glow)), run_time=0.3)

        # 恢复视角
        self.move_camera(phi=60 * DEGREES, theta=-45 * DEGREES, zoom=0.8, run_time=1.0)
        elapsed += 1.0

        dist_zero = MathTex(r"d=0", font_size=56, color=GREEN)
        self.add_fixed_in_frame_mobjects(dist_zero)
        dist_zero.to_edge(DOWN, buff=1.0)
        play_anim(21, FadeIn(dist_zero, scale=1.3), run_time=0.6)
        wait_to(22)

        # ===== seg 22: 答案 A =====
        play_anim(22, FadeOut(dist_zero), run_time=0.3)
        play_anim(22, FadeOut(VGroup(prism, faces, axes_3d, x_label, y_label, z_label, dots, dot_labels, right_angle, ac1_line, ac1_label, vec_ac1, vec_ab1, plane_AC1)), run_time=0.5)

        answer = Text("答案 A：距离 = 0", font="Microsoft YaHei", font_size=56, color=GREEN, weight=BOLD)
        self.add_fixed_in_frame_mobjects(answer)
        play_anim(22, FadeIn(answer, scale=1.3), run_time=0.6)
        wait_to(23)

        # ===== seg 23: 总结 =====
        play_anim(23, FadeOut(answer), run_time=0.3)
        tip = Text("关键: 发现 B₁ 在平面 AC₁ 上", font="Microsoft YaHei", font_size=30, color=AMBER)
        self.add_fixed_in_frame_mobjects(tip)
        play_anim(23, FadeIn(tip, shift=UP * 0.2), run_time=0.8)
        wait_to(24)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.0)
        self.wait(0.5)
