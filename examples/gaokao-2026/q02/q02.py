"""2026高考数学第2题 - 向量共线（v2：向量箭头图 + 系数拆分视觉因果）
时间轴（TTS）：
  0.0-2.4   "来看第二题，向量共线。"
  2.9-5.5   "已知平面向量a和b不共线。"
  6.0-9.5   "也就是说，a和b是两个独立的方向。"
  10.0-14.0 "等式是2a加yb等于xa减3b。"
  14.5-15.9 "这道题考的是什么？"
  16.4-20.3 "两个向量相等，当且仅当它们的系数分别相等。"
  20.8-23.6 "所以我们把a的系数和b的系数分开看。"
  24.1-27.0 "左边a的系数是2，右边是x。"
  27.5-28.8 "所以x等于2。"
  29.3-32.0 "左边b的系数是y，右边是负3。"
  32.5-34.6 "所以y等于负3。"
  35.1-36.2 "答案选A。"
  36.7-39.3 "这道题的核心思想是向量分解。"
  39.8-42.8 "a和b不共线，所以它们线性无关。"
  43.3-45.1 "系数必须一一对应。"
  45.6-48.9 "记住这个套路，向量等式就拆系数。"
"""
from manim import *

# 白色主题
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

T = [0.0, 2.9, 6.0, 10.0, 14.5, 16.4, 20.8, 24.1, 27.5, 29.3, 32.5, 35.1, 36.7, 39.8, 43.3, 45.6, 49.4]


class Q02(Scene):
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
        title = Text("第 2 题", font="Microsoft YaHei", font_size=56, color=TXT)
        sub = Text("2026年新高考一卷", font="Microsoft YaHei", font_size=24, color=DIM)
        sub.next_to(title, DOWN, buff=0.4)
        play_anim(0, FadeIn(title, shift=DOWN * 0.3), run_time=0.8)
        play_anim(0, FadeIn(sub), run_time=0.5)
        wait_to(1)

        # ═══ seg 1: "已知平面向量a和b不共线" → 题目 ═══
        play_anim(1, FadeOut(sub), FadeOut(title), run_time=0.3)
        problem = Text(
            "已知平面向量 a, b 不共线，且 2a + yb = xa − 3b",
            font="Microsoft YaHei", font_size=30, color=TXT,
        )
        play_anim(1, FadeIn(problem, shift=UP * 0.2), run_time=0.8)
        wait_to(2)

        # ═══ seg 2: "a和b是两个独立的方向" → 向量箭头图 ═══
        play_anim(2, FadeOut(problem), run_time=0.3)
        origin = ORIGIN + DOWN * 0.8
        vec_a = Arrow(origin, origin + RIGHT * 3 + UP * 1.8,
                      color=BLUE, stroke_width=5, buff=0, max_tip_length_to_length_ratio=0.15)
        vec_b = Arrow(origin, origin + RIGHT * 1.2 + DOWN * 2.2,
                      color=AMBER, stroke_width=5, buff=0, max_tip_length_to_length_ratio=0.15)
        la = MathTex(r"\vec{a}", font_size=40, color=BLUE).next_to(vec_a.get_end(), UR, buff=0.15)
        lb = MathTex(r"\vec{b}", font_size=40, color=AMBER).next_to(vec_b.get_end(), DR, buff=0.15)
        # "不共线" 标注
        note = Text("不共线 = 两个独立方向", font="Microsoft YaHei", font_size=24, color=DIM)
        note.to_edge(UP, buff=0.5)

        play_anim(2, Create(vec_a), FadeIn(la), run_time=0.6)
        play_anim(2, Create(vec_b), FadeIn(lb), run_time=0.6)
        play_anim(2, FadeIn(note), run_time=0.4)
        wait_to(3)

        # ═══ seg 3: "等式是2a加yb等于xa减3b" → 显示等式 ═══
        play_anim(3, FadeOut(note), run_time=0.3)
        # 向量缩小到左边
        vec_group = VGroup(vec_a, vec_b, la, lb)
        play_anim(3, vec_group.animate.scale(0.5).to_edge(LEFT, buff=0.5).shift(DOWN * 0.3), run_time=0.6)
        # 等式在右边
        eq = MathTex(r"2\vec{a} + y\vec{b} = x\vec{a} - 3\vec{b}", font_size=44, color=TXT)
        eq.to_edge(RIGHT, buff=1.0).shift(UP * 0.5)
        play_anim(3, FadeIn(eq, shift=LEFT * 0.3), run_time=0.8)
        wait_to(4)

        # ═══ seg 4: "这道题考的是什么？" → 保留画面 ═══
        wait_to(5)

        # ═══ seg 5: "系数分别相等" → 原理文字 ═══
        principle = Text(
            "向量相等 ⇔ 系数分别相等",
            font="Microsoft YaHei", font_size=28, color=PINK,
        )
        principle.next_to(eq, DOWN, buff=0.6)
        play_anim(5, FadeIn(principle, shift=UP * 0.2), run_time=0.8)
        wait_to(6)

        # ═══ seg 6: "把a和b的系数分开看" → 拆分可视化 ═══
        play_anim(6, FadeOut(eq), FadeOut(principle), FadeOut(vec_group), run_time=0.4)
        # 大等式 + 彩色高亮框
        eq_full = MathTex(
            r"2\vec{a}", r"+", r"y\vec{b}", r"=", r"x\vec{a}", r"-", r"3\vec{b}",
            font_size=48, color=TXT,
        )
        eq_full.move_to(ORIGIN + UP * 0.8)
        # a系数高亮框（蓝色）
        a_box_left = SurroundingRectangle(VGroup(eq_full[0]), color=BLUE, buff=0.12, stroke_width=3)
        a_box_right = SurroundingRectangle(VGroup(eq_full[4]), color=BLUE, buff=0.12, stroke_width=3)
        # b系数高亮框（橙色）
        b_box_left = SurroundingRectangle(VGroup(eq_full[2]), color=AMBER, buff=0.12, stroke_width=3)
        b_box_right = SurroundingRectangle(VGroup(eq_full[6]), color=AMBER, buff=0.12, stroke_width=3)

        play_anim(6, FadeIn(eq_full), run_time=0.6)
        play_anim(6, Create(a_box_left), Create(a_box_right), run_time=0.5)
        play_anim(6, Create(b_box_left), Create(b_box_right), run_time=0.5)
        # a/b 标签
        a_label = Text("a 的系数", font="Microsoft YaHei", font_size=22, color=BLUE)
        a_label.next_to(a_box_left, DOWN, buff=0.2)
        b_label = Text("b 的系数", font="Microsoft YaHei", font_size=22, color=AMBER)
        b_label.next_to(b_box_left, DOWN, buff=0.2)
        play_anim(6, FadeIn(a_label), FadeIn(b_label), run_time=0.4)
        wait_to(7)

        # ═══ seg 7: "左边a的系数是2，右边是x" → 拆出方程 ═══
        eq_a = MathTex(r"2 = x", font_size=44, color=BLUE)
        eq_a.move_to(DOWN * 0.5)
        arrow_a = Arrow(a_box_left.get_bottom() + DOWN * 0.1, eq_a.get_top() + UP * 0.1,
                        color=BLUE, stroke_width=2)
        play_anim(7, GrowArrow(arrow_a), FadeIn(eq_a, scale=1.2), run_time=0.8)
        wait_to(8)

        # ═══ seg 8: "x等于2" → 绿色答案 ═══
        ans_x = MathTex(r"x = 2", font_size=52, color=GREEN)
        ans_x.move_to(DOWN * 0.5)
        play_anim(8, Transform(eq_a, ans_x), run_time=0.6)
        # 打勾
        check_x = Text("✓", font_size=36, color=GREEN).next_to(eq_a, RIGHT, buff=0.3)
        play_anim(8, FadeIn(check_x, scale=1.5), run_time=0.3)
        wait_to(9)

        # ═══ seg 9: "左边b的系数是y，右边是-3" ═══
        play_anim(9, FadeOut(eq_a), FadeOut(check_x), FadeOut(arrow_a), run_time=0.3)
        eq_b = MathTex(r"y = -3", font_size=44, color=AMBER)
        eq_b.move_to(DOWN * 0.5)
        arrow_b = Arrow(b_box_left.get_bottom() + DOWN * 0.1, eq_b.get_top() + UP * 0.1,
                        color=AMBER, stroke_width=2)
        play_anim(9, GrowArrow(arrow_b), FadeIn(eq_b, scale=1.2), run_time=0.8)
        wait_to(10)

        # ═══ seg 10: "y等于-3" → 绿色答案 ═══
        ans_y = MathTex(r"y = -3", font_size=52, color=GREEN)
        ans_y.move_to(DOWN * 0.5)
        play_anim(10, Transform(eq_b, ans_y), run_time=0.6)
        check_y = Text("✓", font_size=36, color=GREEN).next_to(eq_b, RIGHT, buff=0.3)
        play_anim(10, FadeIn(check_y, scale=1.5), run_time=0.3)
        wait_to(11)

        # ═══ seg 11: "答案选A" ═══
        play_anim(11, FadeOut(eq_full), FadeOut(a_box_left), FadeOut(a_box_right),
                  FadeOut(b_box_left), FadeOut(b_box_right), FadeOut(a_label), FadeOut(b_label),
                  FadeOut(eq_b), FadeOut(check_y), FadeOut(arrow_b), run_time=0.5)
        answer = Text("答案 A：x=2, y=−3", font="Microsoft YaHei", font_size=52, color=GREEN, weight=BOLD)
        answer.move_to(ORIGIN)
        play_anim(11, FadeIn(answer, scale=1.5), run_time=0.6)
        wait_to(12)

        # ═══ seg 12: "核心思想是向量分解" ═══
        play_anim(12, FadeOut(answer), run_time=0.3)
        tip1 = Text("核心思想：向量分解", font="Microsoft YaHei", font_size=34, color=AMBER)
        tip1.move_to(ORIGIN + UP * 0.5)
        play_anim(12, FadeIn(tip1, shift=UP * 0.2), run_time=0.8)
        wait_to(13)

        # ═══ seg 13: "a和b不共线，所以线性无关" ═══
        tip2 = Text("a, b 不共线 → 线性无关", font="Microsoft YaHei", font_size=28, color=BLUE)
        tip2.next_to(tip1, DOWN, buff=0.5)
        play_anim(13, FadeIn(tip2, shift=UP * 0.2), run_time=0.8)
        wait_to(14)

        # ═══ seg 14: "系数必须一一对应" ═══
        tip3 = Text("系数必须一一对应", font="Microsoft YaHei", font_size=28, color=CORAL)
        tip3.next_to(tip2, DOWN, buff=0.5)
        play_anim(14, FadeIn(tip3, shift=UP * 0.2), run_time=0.6)
        wait_to(15)

        # ═══ seg 15: "记住这个套路" ═══
        play_anim(15, FadeOut(tip1), FadeOut(tip2), FadeOut(tip3), run_time=0.3)
        final = Text("向量等式 → 拆系数！", font="Microsoft YaHei", font_size=48, color=GREEN)
        final.move_to(ORIGIN)
        play_anim(15, FadeIn(final, scale=1.3), run_time=0.6)
        wait_to(16)

        # 结尾
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.0)
        self.wait(0.5)
