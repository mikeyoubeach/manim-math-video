"""2026高考数学第8题 - 四面体体积（3D几何）"""
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
RED = "#e74c3c"

config.background_color = BG
config.frame_rate = 30
config.pixel_width = 1920
config.pixel_height = 1080

# T from timeline.json (29 segs, indices 0-28)
T = [
    0.0, 3.22, 5.48, 9.82, 13.04, 16.42, 18.84, 22.86, 27.36, 31.38,
    35.4, 40.06, 42.0, 45.86, 49.08, 53.1, 56.64, 59.22, 64.84, 68.06,
    70.0, 71.62, 77.24, 81.42, 86.08, 92.98, 97.64, 100.38, 106.0,
]


class Q08(ThreeDScene):
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

        self.set_camera_orientation(phi=65 * DEGREES, theta=-50 * DEGREES)

        # ═══ seg 0: 标题 ═══
        title = Text("第 8 题", font="Microsoft YaHei", font_size=56, color=TXT)
        sub = Text("2026年新高考一卷", font="Microsoft YaHei", font_size=24, color=DIM)
        sub.next_to(title, DOWN, buff=0.4)
        self.add_fixed_in_frame_mobjects(title, sub)
        play_anim(0, FadeIn(title, shift=DOWN * 0.3), run_time=0.8)
        play_anim(0, FadeIn(sub), run_time=0.5)
        wait_to(1)
        play_anim(1, FadeOut(title), FadeOut(sub), run_time=0.3)

        # ═══ seg 1-3: 题目 ═══
        problem = Text(
            "正方体棱长为2，E,F,G,H为棱中点",
            font="Microsoft YaHei", font_size=28, color=TXT,
        )
        question = Text("求四面体 EFGH 体积", font="Microsoft YaHei", font_size=28, color=PINK)
        q_group = VGroup(problem, question).arrange(DOWN, buff=0.3)
        self.add_fixed_in_frame_mobjects(q_group)
        play_anim(1, FadeIn(q_group, shift=UP * 0.2), run_time=0.8)
        wait_to(3)
        play_anim(3, FadeOut(q_group), run_time=0.3)

        # ═══ seg 3-5: 画正方体 ═══
        s = 1.2
        verts = [
            np.array([-s, -s, -s]), np.array([s, -s, -s]),
            np.array([s, s, -s]), np.array([-s, s, -s]),
            np.array([-s, -s, s]), np.array([s, -s, s]),
            np.array([s, s, s]), np.array([-s, s, s]),
        ]
        edges = [
            (0,1),(1,2),(2,3),(3,0),
            (4,5),(5,6),(6,7),(7,4),
            (0,4),(1,5),(2,6),(3,7),
        ]

        cube_lines = VGroup()
        for i, j in edges:
            line = Line3D(start=verts[i], end=verts[j], color=DIM, stroke_width=2)
            cube_lines.add(line)

        v_names = ["A", "B", "C", "D", "A₁", "B₁", "C₁", "D₁"]
        v_labels = VGroup()
        for i, name in enumerate(v_names):
            lab = Text(name, font_size=18, color=DIM)
            lab.move_to(verts[i] + np.array([0.15, 0.15, 0.15]) * (1 if i < 4 else -1))
            v_labels.add(lab)

        play_anim(3, Create(cube_lines), run_time=1.5)
        play_anim(3, FadeIn(v_labels), run_time=0.5)
        wait_to(5)

        # ═══ seg 5-9: 标出中点 E,F,G,H ═══
        E = (np.array([-s,-s,-s]) + np.array([s,-s,-s])) / 2
        F = (np.array([-s,-s,-s]) + np.array([-s,s,-s])) / 2
        G = (np.array([s,-s,-s]) + np.array([s,-s,s])) / 2
        H = (np.array([-s,s,-s]) + np.array([-s,s,s])) / 2

        points_data = [
            ("E", E, "AB中点", BLUE),
            ("F", F, "AD中点", GREEN),
            ("G", G, "BB₁中点", AMBER),
            ("H", H, "DD₁中点", PINK),
        ]

        all_dots = VGroup()
        all_labels = VGroup()
        coord_texts = VGroup()
        for idx, (name, pos, desc, color) in enumerate(points_data):
            dot = Dot3D(pos, color=color, radius=0.08)
            lab = Text(name, font_size=22, color=color)
            lab.move_to(pos + np.array([0.2, 0.2, 0.2]))
            all_dots.add(dot)
            all_labels.add(lab)
            play_anim(5 + idx, FadeIn(dot), FadeIn(lab), run_time=0.6)
            coord_txt = Text(
                f"{name} = {desc}",
                font="Microsoft YaHei", font_size=20, color=color,
            )
            self.add_fixed_in_frame_mobjects(coord_txt)
            coord_txt.to_corner(UR, buff=0.3).shift(DOWN * idx * 0.35)
            coord_texts.add(coord_txt)
            play_anim(5 + idx, FadeIn(coord_txt), run_time=0.3)
            wait_to(6 + idx)

        wait_to(9)

        # ═══ seg 9: 连成四面体 ═══
        tetra_faces = VGroup(
            Polygon(E, F, G, color=BLUE, fill_opacity=0.15, stroke_width=2, stroke_color=BLUE),
            Polygon(E, F, H, color=GREEN, fill_opacity=0.15, stroke_width=2, stroke_color=GREEN),
            Polygon(E, G, H, color=AMBER, fill_opacity=0.15, stroke_width=2, stroke_color=AMBER),
            Polygon(F, G, H, color=PINK, fill_opacity=0.15, stroke_width=2, stroke_color=PINK),
        )
        tetra_edges = VGroup(
            Line3D(E, F, color=BLUE, stroke_width=3),
            Line3D(E, G, color=GREEN, stroke_width=3),
            Line3D(E, H, color=AMBER, stroke_width=3),
            Line3D(F, G, color=PINK, stroke_width=3),
            Line3D(F, H, color=CORAL, stroke_width=3),
            Line3D(G, H, color=RED, stroke_width=3),
        )
        play_anim(9, FadeIn(tetra_faces), FadeIn(tetra_edges), run_time=1.0)
        wait_to(10)

        # ═══ seg 10: 体积公式提示 ═══
        vol_hint = Text("四面体体积 = (1/6)|混合积|", font="Microsoft YaHei", font_size=24, color=TXT)
        self.add_fixed_in_frame_mobjects(vol_hint)
        vol_hint.to_edge(DOWN, buff=0.5)
        play_anim(10, FadeIn(vol_hint), run_time=0.6)
        wait_to(11)
        play_anim(11, FadeOut(vol_hint), run_time=0.3)

        # ═══ seg 11: 用向量方法 ═══
        method_txt = Text("用向量法", font="Microsoft YaHei", font_size=26, color=AMBER)
        self.add_fixed_in_frame_mobjects(method_txt)
        method_txt.to_corner(UR, buff=0.3)
        play_anim(11, FadeIn(method_txt), run_time=0.5)
        wait_to(12)

        # ═══ seg 12-14: 向量 ═══
        vec_texts = VGroup(
            MathTex(r"\vec{EF} = (-1, 1, 0)", font_size=26, color=BLUE),
            MathTex(r"\vec{EG} = (0, -1, 1)", font_size=26, color=GREEN),
            MathTex(r"\vec{EH} = (-1, 1, 1)", font_size=26, color=AMBER),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(vec_texts)
        vec_texts.to_corner(UR, buff=0.3).shift(DOWN * 0.5)

        play_anim(12, FadeOut(method_txt), run_time=0.2)
        play_anim(12, FadeIn(vec_texts[0]), run_time=0.5)
        wait_to(13)
        play_anim(13, FadeIn(vec_texts[1]), run_time=0.5)
        wait_to(14)
        play_anim(14, FadeIn(vec_texts[2]), run_time=0.5)
        wait_to(15)

        # ═══ seg 15: 混合积 = 行列式 ═══
        play_anim(15, FadeOut(vec_texts), run_time=0.3)
        det_tex = MathTex(
            r"\begin{vmatrix} -1 & 1 & 0 \\ 0 & -1 & 1 \\ -1 & 1 & 1 \end{vmatrix}",
            font_size=30, color=TXT,
        )
        self.add_fixed_in_frame_mobjects(det_tex)
        det_tex.to_corner(UR, buff=0.3)
        play_anim(15, FadeIn(det_tex), run_time=0.6)
        wait_to(16)

        # ═══ seg 16-18: 错误计算 ═══
        play_anim(16, FadeOut(det_tex), run_time=0.3)
        calc1 = VGroup(
            MathTex(r"= (-1)(-1)(1) - (1)(1)(1) + 0", font_size=24, color=TXT),
            MathTex(r"= 1 - 1 + 0 = 0", font_size=26, color=RED),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(calc1)
        calc1.to_corner(UR, buff=0.3)
        play_anim(16, FadeIn(calc1[0]), run_time=0.6)
        wait_to(17)
        play_anim(17, FadeIn(calc1[1]), run_time=0.5)
        wait_to(18)

        # ═══ seg 18-19: 红叉 → "等等这不对" ═══
        cross = Cross(stroke_color=RED, stroke_width=6).scale(0.4)
        self.add_fixed_in_frame_mobjects(cross)
        cross.move_to(calc1[1])
        play_anim(18, FadeIn(cross, scale=1.5), run_time=0.5)
        wait_to(19)
        err_text = Text("等等，这不对！", font="Microsoft YaHei", font_size=30, color=RED)
        self.add_fixed_in_frame_mobjects(err_text)
        err_text.move_to(DOWN * 2)
        play_anim(19, FadeIn(err_text, shift=UP * 0.3), run_time=0.5)
        wait_to(20)

        # ═══ seg 20: 清除错误 ═══
        play_anim(20, FadeOut(err_text), FadeOut(cross), FadeOut(calc1), run_time=0.3)
        retry = Text("重新计算...", font="Microsoft YaHei", font_size=28, color=AMBER)
        self.add_fixed_in_frame_mobjects(retry)
        retry.to_corner(UR, buff=0.3)
        play_anim(20, FadeIn(retry), run_time=0.4)
        wait_to(21)

        # ═══ seg 21-23: 重新算向量 ═══
        play_anim(21, FadeOut(retry), run_time=0.2)
        vec2 = VGroup(
            MathTex(r"\vec{EF} = (-1, 1, 0)", font_size=24, color=BLUE),
            MathTex(r"\vec{EG} = (0, -1, 1)", font_size=24, color=GREEN),
            MathTex(r"\vec{EH} = (-1, 1, 1)", font_size=24, color=AMBER),
        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(vec2)
        vec2.to_corner(UR, buff=0.3)

        play_anim(21, FadeIn(vec2[0]), run_time=0.5)
        wait_to(22)
        play_anim(22, FadeIn(vec2[1]), run_time=0.5)
        wait_to(23)
        play_anim(23, FadeIn(vec2[2]), run_time=0.5)
        wait_to(24)

        # ═══ seg 24-26: 正确行列式展开 ═══
        play_anim(24, FadeOut(vec2), run_time=0.3)
        det2 = MathTex(
            r"\begin{vmatrix} -1 & 1 & 0 \\ 0 & -1 & 1 \\ -1 & 1 & 1 \end{vmatrix}",
            font_size=28, color=TXT,
        )
        self.add_fixed_in_frame_mobjects(det2)
        det2.to_corner(UR, buff=0.3)
        play_anim(24, FadeIn(det2), run_time=0.4)

        expand = MathTex(
            r"= (-1)(-1-1) - 1(0-(-1)) + 0",
            font_size=22, color=TXT,
        )
        self.add_fixed_in_frame_mobjects(expand)
        expand.next_to(det2, DOWN, buff=0.15)
        play_anim(24, FadeIn(expand), run_time=0.6)
        wait_to(25)

        # ═══ seg 25: 继续 ═══
        expand2 = MathTex(r"= (-1)(-2) - 1(1) + 0", font_size=24, color=TXT)
        self.add_fixed_in_frame_mobjects(expand2)
        expand2.next_to(expand, DOWN, buff=0.12)
        play_anim(25, FadeIn(expand2), run_time=0.5)
        wait_to(26)

        # ═══ seg 26: 结果 = 1 → 绿勾 ═══
        result1 = MathTex(r"= 2 - 1 = 1", font_size=28, color=GREEN)
        self.add_fixed_in_frame_mobjects(result1)
        result1.next_to(expand2, DOWN, buff=0.12)
        play_anim(26, FadeIn(result1), run_time=0.5)
        check = Text("✓", font_size=36, color=GREEN)
        self.add_fixed_in_frame_mobjects(check)
        check.next_to(result1, RIGHT, buff=0.2)
        play_anim(26, FadeIn(check, scale=1.5), run_time=0.4)
        wait_to(27)

        # ═══ seg 27: 体积 ═══
        play_anim(27, FadeOut(det2), FadeOut(expand), FadeOut(expand2),
                  FadeOut(result1), FadeOut(check), run_time=0.3)
        vol_final = VGroup(
            MathTex(r"V = \frac{1}{6} |det| = \frac{1}{6} \times 1", font_size=30, color=TXT),
            MathTex(r"V = \frac{1}{6}", font_size=38, color=GREEN),
        ).arrange(DOWN, buff=0.25)
        self.add_fixed_in_frame_mobjects(vol_final)
        vol_final.move_to(ORIGIN + DOWN * 2)
        play_anim(27, FadeIn(vol_final[0]), run_time=0.6)
        play_anim(27, FadeIn(vol_final[1], scale=1.2), run_time=0.6)
        wait_to(28)

        # ═══ seg 28: 答案 ═══
        play_anim(28, FadeOut(vol_final), run_time=0.3)
        answer = Text("答案 C：1/6", font="Microsoft YaHei", font_size=52, color=GREEN, weight=BOLD)
        self.add_fixed_in_frame_mobjects(answer)
        answer.move_to(DOWN * 2)
        play_anim(28, FadeIn(answer, scale=1.3), run_time=0.7)

        self.play(
            *[FadeOut(m) for m in [cube_lines, v_labels, all_dots, all_labels, coord_texts, tetra_faces, tetra_edges]],
            run_time=0.8,
        )
        self.play(FadeOut(answer), run_time=0.5)
        self.wait(0.5)
