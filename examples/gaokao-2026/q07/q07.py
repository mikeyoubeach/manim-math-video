"""2026高考数学第7题 - 积木塔（等差数列求和）"""
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

# T from timeline.json (seg 0-14 end times)
T = [0.0, 2.58, 5.96, 10.62, 13.52, 15.78, 18.84, 24.3, 26.24, 28.18, 34.6, 39.9, 46.96, 49.06, 53.4]


class Q07(Scene):
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
        title = Text("第 7 题", font="Microsoft YaHei", font_size=56, color=TXT)
        sub = Text("2026年新高考一卷", font="Microsoft YaHei", font_size=24, color=DIM)
        sub.next_to(title, DOWN, buff=0.4)
        play_anim(0, FadeIn(title, shift=DOWN * 0.3), run_time=0.8)
        play_anim(0, FadeIn(sub), run_time=0.5)
        wait_to(1)
        play_anim(1, FadeOut(title), FadeOut(sub), run_time=0.3)

        # ═══ seg 1-2: 题目描述 ═══
        problem = VGroup(
            Text("积木塔：从第2层起，每层比下层少1块", font="Microsoft YaHei", font_size=28, color=TXT),
            Text("底层 15 块，顶层 7 块", font="Microsoft YaHei", font_size=28, color=TXT),
            Text("问：一共有多少块积木？", font="Microsoft YaHei", font_size=28, color=PINK),
        ).arrange(DOWN, buff=0.25)
        play_anim(1, FadeIn(problem, shift=UP * 0.2), run_time=0.8)
        wait_to(3)
        play_anim(3, FadeOut(problem), run_time=0.3)

        # ═══ seg 2-4: 积木塔可视化 ═══
        layers = list(range(15, 6, -1))  # 15,14,...,7 (9 layers)
        tower = VGroup()
        layer_labels = VGroup()
        for i, count in enumerate(layers):
            row = VGroup()
            for j in range(count):
                box = RoundedRectangle(
                    width=0.38, height=0.38, corner_radius=0.04,
                    color=BLUE, fill_opacity=0.25, stroke_width=1.5, stroke_color=BLUE,
                )
                row.add(box)
            row.arrange(RIGHT, buff=0.04)
            # layer number label on the right
            lbl = Text(str(count), font="Microsoft YaHei", font_size=18, color=DIM)
            lbl.next_to(row, RIGHT, buff=0.2)
            layer_labels.add(lbl)
            tower.add(row)
        tower.arrange(DOWN, buff=0.06, aligned_edge=ORIGIN)
        layer_labels.arrange(DOWN, buff=0.06)
        # align labels with tower rows
        for i in range(len(tower)):
            layer_labels[i].next_to(tower[i], RIGHT, buff=0.15)
        tower_group = VGroup(tower, layer_labels)
        tower_group.move_to(LEFT * 1.5)

        # Animate tower building from bottom up
        play_anim(3, FadeIn(tower_group, shift=UP * 0.3), run_time=1.2)
        wait_to(5)

        # ═══ seg 5: "等差数列求和" label ═══
        eq_label = Text("等差数列求和", font="Microsoft YaHei", font_size=30, color=AMBER)
        eq_label.move_to(RIGHT * 4 + UP * 2.5)
        play_anim(5, FadeIn(eq_label, shift=LEFT * 0.3), run_time=0.8)
        wait_to(6)

        # ═══ seg 6: 首项/末项/公差标注 ═══
        play_anim(6, FadeOut(eq_label), run_time=0.3)
        # Highlight bottom layer (15) and top layer (7)
        bottom_arrow = Arrow(
            tower[0].get_right() + RIGHT * 0.5, tower[0].get_right() + RIGHT * 0.1,
            color=BLUE, stroke_width=3, buff=0.05,
        )
        bottom_lbl = Text("a₁ = 15（首项）", font="Microsoft YaHei", font_size=22, color=BLUE)
        bottom_lbl.next_to(bottom_arrow, RIGHT, buff=0.1)

        top_arrow = Arrow(
            tower[-1].get_right() + RIGHT * 0.5, tower[-1].get_right() + RIGHT * 0.1,
            color=PINK, stroke_width=3, buff=0.05,
        )
        top_lbl = Text("aₙ = 7（末项）", font="Microsoft YaHei", font_size=22, color=PINK)
        top_lbl.next_to(top_arrow, RIGHT, buff=0.1)

        d_lbl = Text("公差 d = -1", font="Microsoft YaHei", font_size=22, color=CORAL)
        d_lbl.move_to(RIGHT * 4 + DOWN * 1.5)

        play_anim(6, FadeIn(bottom_arrow), FadeIn(bottom_lbl), run_time=0.6)
        play_anim(6, FadeIn(top_arrow), FadeIn(top_lbl), run_time=0.5)
        play_anim(6, FadeIn(d_lbl, shift=LEFT * 0.2), run_time=0.5)
        wait_to(8)

        # ═══ seg 8: 算层数 ═══
        play_anim(8, FadeOut(bottom_arrow), FadeOut(bottom_lbl), FadeOut(top_arrow), FadeOut(top_lbl), FadeOut(d_lbl), run_time=0.3)
        n_calc = VGroup(
            MathTex(r"n = 15 - 7 + 1 = 9", font_size=34, color=GREEN),
            Text("（层数 = 首项 - 末项 + 1）", font="Microsoft YaHei", font_size=20, color=DIM),
        ).arrange(DOWN, buff=0.15)
        n_calc.move_to(RIGHT * 4 + UP * 0.5)
        play_anim(8, FadeIn(n_calc, shift=LEFT * 0.3), run_time=0.8)
        wait_to(10)

        # ═══ seg 10: 求和公式 ═══
        play_anim(10, FadeOut(n_calc), run_time=0.3)
        formula = MathTex(r"S_n = \frac{(a_1 + a_n) \times n}{2}", font_size=40, color=TXT)
        formula.move_to(RIGHT * 4 + UP * 0.5)
        play_anim(10, FadeIn(formula, shift=LEFT * 0.3), run_time=0.8)
        wait_to(11)

        # ═══ seg 11: 代入计算（逐步） ═══
        play_anim(11, FadeOut(formula), run_time=0.3)
        calc_lines = VGroup(
            MathTex(r"S = \frac{(15 + 7) \times 9}{2}", font_size=34, color=TXT),
            MathTex(r"= \frac{22 \times 9}{2}", font_size=34, color=TXT),
            MathTex(r"= \frac{198}{2}", font_size=34, color=TXT),
            MathTex(r"= 99", font_size=40, color=GREEN),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        calc_lines.move_to(RIGHT * 3.8 + UP * 0.3)
        for line in calc_lines:
            play_anim(11, FadeIn(line, shift=UP * 0.15), run_time=0.6)
            wait_to(11)  # stay on seg 11

        wait_to(12)

        # ═══ seg 12: 答案 ═══
        play_anim(12, FadeOut(calc_lines), FadeOut(tower_group), run_time=0.3)
        answer = Text("答案 C：99 块", font="Microsoft YaHei", font_size=56, color=GREEN, weight=BOLD)
        play_anim(12, FadeIn(answer, scale=1.3), run_time=0.7)
        wait_to(13)

        # ═══ seg 13: 总结 - 关键 ═══
        play_anim(13, FadeOut(answer), run_time=0.3)
        tip = VGroup(
            Text("关键：搞清楚首项、末项、项数", font="Microsoft YaHei", font_size=28, color=AMBER),
            MathTex(r"n = a_1 - a_n + 1", font_size=32, color=BLUE),
        ).arrange(DOWN, buff=0.3)
        tip.move_to(ORIGIN)
        play_anim(13, FadeIn(tip, shift=UP * 0.2), run_time=0.8)
        wait_to(14)

        # ═══ seg 14: 易错提醒 ═══
        warn = Text("⚠ 别忘了加 1！15到7是9层，不是8层", font="Microsoft YaHei", font_size=26, color=PINK)
        warn.next_to(tip, DOWN, buff=0.5)
        play_anim(14, FadeIn(warn, shift=UP * 0.2), run_time=0.8)
        wait_to(15)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.0)
        self.wait(0.5)
