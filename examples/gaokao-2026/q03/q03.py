"""2026高考数学第3题 - 三角函数集合交集（v2：必须用单位圆！）
时间轴（TTS）：
  0.0-3.0   "来看第三题，三角函数集合交集。"
  3.5-10.6  "集合A有三个元素，分别是sin六分之七π，cos三分之五π，tan四分之五π。"
  11.1-16.4 "集合B也有三个元素，负二分之根号三，负二分之一，和1。"
  16.9-18.3 "求A和B的交集。"
  18.8-21.8 "这道题考的是特殊角的三角函数值。"
  22.3-23.6 "我们一个一个算。"
  24.1-28.6 "sin六分之七π，就是sin一百五十度，等于二分之一。"
  29.1-33.7 "cos三分之五π，就是cos三百度，等于二分之一。"
  34.2-38.4 "tan四分之五π，就是tan二百二十五度，等于1。"
  38.9-42.9 "所以A等于二分之一，二分之一，1。"
  43.4-47.4 "注意，集合有互异性，重复的只算一次。"
  47.9-50.3 "所以A等于二分之一和1。"
  50.8-54.8 "再看B，负二分之根号三，负二分之一，1。"
  55.3-57.7 "A和B的公共元素，只有1。"
  58.2-60.3 "所以A交B等于1。"
  60.8-62.1 "答案选C。"
"""
from manim import *
import numpy as np

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

T = [0.0, 3.5, 11.1, 16.9, 18.8, 22.3, 24.1, 29.1, 34.2, 38.9, 43.4, 47.9, 50.8, 55.3, 58.2, 60.8, 62.6]


def make_unit_circle(angle_deg, coord_type, value_text, value_color, label_text):
    """创建单位圆场景：转到指定角度，标出 y/x 坐标
    coord_type: "sin" → 标y, "cos" → 标x, "tan" → 标y/x比
    """
    circle = Circle(radius=1.5, color=BLUE, stroke_width=2)
    # 坐标轴
    x_axis = Arrow(LEFT * 2, RIGHT * 2, buff=0, color=DIM, stroke_width=1.5, max_tip_length_to_length_ratio=0.03)
    y_axis = Arrow(DOWN * 2, UP * 2, buff=0, color=DIM, stroke_width=1.5, max_tip_length_to_length_ratio=0.03)
    axes = VGroup(x_axis, y_axis)

    angle_rad = np.radians(angle_deg)
    # 终边上的点
    end_x = 1.5 * np.cos(angle_rad)
    end_y = 1.5 * np.sin(angle_rad)
    point = Dot([end_x, end_y, 0], radius=0.08, color=value_color)
    # 终边射线
    ray = Line(ORIGIN, [end_x, end_y, 0], color=value_color, stroke_width=3)
    # 角度弧
    angle_arc = Arc(radius=0.5, start_angle=0, angle=angle_rad, color=AMBER, stroke_width=2)
    angle_label = MathTex(f"{angle_deg}^\\circ", font_size=22, color=AMBER)
    angle_label.move_to(0.65 * np.array([np.cos(angle_rad / 2), np.sin(angle_rad / 2), 0]))

    # 标注坐标
    coord_mark = None
    if coord_type == "sin":
        # 标 y 坐标：从原点到点的 y 投影，用虚线
        proj = DashedLine([end_x, 0, 0], [end_x, end_y, 0], color=value_color, stroke_width=2, dash_length=0.08)
        val_label = MathTex(value_text, font_size=28, color=value_color)
        val_label.next_to(proj, RIGHT, buff=0.15)
        coord_mark = VGroup(proj, val_label)
    elif coord_type == "cos":
        # 标 x 坐标：从原点到点的 x 投影
        proj = DashedLine([0, end_y, 0], [end_x, end_y, 0], color=value_color, stroke_width=2, dash_length=0.08)
        val_label = MathTex(value_text, font_size=28, color=value_color)
        val_label.next_to(proj, DOWN, buff=0.15)
        coord_mark = VGroup(proj, val_label)
    elif coord_type == "tan":
        # tan: 标 y/x，画切线段
        val_label = MathTex(value_text, font_size=28, color=value_color)
        val_label.next_to(point, UR, buff=0.15)
        coord_mark = val_label

    # 函数名标签
    func_label = Text(label_text, font="Microsoft YaHei", font_size=24, color=TXT)
    func_label.to_edge(UP, buff=0.3)

    return VGroup(circle, axes, angle_arc, angle_label, ray, point, coord_mark, func_label)


class Q03(Scene):
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
        title = Text("第 3 题", font="Microsoft YaHei", font_size=56, color=TXT)
        sub = Text("2026年新高考一卷", font="Microsoft YaHei", font_size=24, color=DIM)
        sub.next_to(title, DOWN, buff=0.4)
        play_anim(0, FadeIn(title, shift=DOWN * 0.3), run_time=0.8)
        play_anim(0, FadeIn(sub), run_time=0.5)
        wait_to(1)

        # ═══ seg 1: 题目显示 ═══
        play_anim(1, FadeOut(title), FadeOut(sub), run_time=0.3)
        problem = MathTex(
            r"A = \left\{\sin\frac{7\pi}{6},\; \cos\frac{5\pi}{3},\; \tan\frac{5\pi}{4}\right\}",
            font_size=32, color=TXT,
        )
        problem2 = MathTex(
            r"B = \left\{-\frac{\sqrt{3}}{2},\; -\frac{1}{2},\; 1\right\}",
            font_size=32, color=TXT,
        )
        question = Text("求 A ∩ B", font="Microsoft YaHei", font_size=32, color=PINK)
        q_group = VGroup(problem, problem2, question).arrange(DOWN, buff=0.5)
        q_group.move_to(ORIGIN)
        play_anim(1, FadeIn(q_group, shift=UP * 0.2), run_time=1.0)
        wait_to(2)
        # seg 2-3: 保持显示
        wait_to(3)
        play_anim(3, FadeOut(q_group), run_time=0.3)

        # ═══ seg 4: "考的是特殊角的三角函数值" ═══
        tip = Text("特殊角的三角函数值", font="Microsoft YaHei", font_size=36, color=AMBER)
        play_anim(4, FadeIn(tip, shift=UP * 0.2), run_time=0.8)
        wait_to(5)

        # ═══ seg 5: "我们一个一个算" ═══
        play_anim(5, FadeOut(tip), run_time=0.3)
        ready = Text("一个一个算 ↓", font="Microsoft YaHei", font_size=28, color=DIM)
        play_anim(5, FadeIn(ready), run_time=0.4)
        wait_to(6)
        play_anim(6, FadeOut(ready), run_time=0.2)

        # ═══ seg 6: sin(7π/6) = sin150° → 单位圆！ ═══
        # 构建单位圆：150°，标 y 坐标 = 1/2
        circle1 = Circle(radius=1.5, color=BLUE, stroke_width=2)
        x_ax = Arrow(LEFT * 2.2, RIGHT * 2.2, buff=0, color=DIM, stroke_width=1.5,
                      max_tip_length_to_length_ratio=0.02)
        y_ax = Arrow(DOWN * 2.2, UP * 2.2, buff=0, color=DIM, stroke_width=1.5,
                      max_tip_length_to_length_ratio=0.02)
        axes1 = VGroup(x_ax, y_ax)

        # 150° 终边
        a1 = np.radians(150)
        end1 = 1.5 * np.array([np.cos(a1), np.sin(a1), 0])
        ray1 = Line(ORIGIN, end1, color=PINK, stroke_width=3)
        pt1 = Dot(end1, radius=0.1, color=PINK)
        arc1 = Arc(radius=0.45, start_angle=0, angle=a1, color=AMBER, stroke_width=2)
        al1 = MathTex(r"150^\circ", font_size=20, color=AMBER)
        al1.move_to(0.6 * np.array([np.cos(a1 / 2), np.sin(a1 / 2), 0]))
        # y 坐标虚线
        y_line1 = DashedLine(
            [end1[0], 0, 0], end1, color=PINK, stroke_width=2, dash_length=0.06,
        )
        y_val1 = MathTex(r"\frac{1}{2}", font_size=30, color=PINK)
        y_val1.next_to(y_line1, RIGHT, buff=0.12)
        sin_label = Text("sin 150° = y 坐标", font="Microsoft YaHei", font_size=22, color=TXT)
        sin_label.to_edge(UP, buff=0.3)

        uc1 = VGroup(circle1, axes1, arc1, al1, ray1, pt1, y_line1, y_val1, sin_label)
        uc1.scale(0.55).move_to(LEFT * 2.5)

        # 右边公式
        eq1 = MathTex(r"\sin\frac{7\pi}{6} = \sin150^\circ = \frac{1}{2}", font_size=34, color=PINK)
        eq1.move_to(RIGHT * 2.5 + UP * 0.3)

        play_anim(6, FadeIn(uc1, scale=0.9), run_time=0.8)
        play_anim(6, FadeIn(eq1, shift=LEFT * 0.3), run_time=0.6)
        wait_to(7)
        play_anim(7, FadeOut(uc1), FadeOut(eq1), run_time=0.3)

        # ═══ seg 7: cos(5π/3) = cos300° → 单位圆 ═══
        circle2 = Circle(radius=1.5, color=BLUE, stroke_width=2)
        axes2 = VGroup(
            Arrow(LEFT * 2.2, RIGHT * 2.2, buff=0, color=DIM, stroke_width=1.5,
                  max_tip_length_to_length_ratio=0.02),
            Arrow(DOWN * 2.2, UP * 2.2, buff=0, color=DIM, stroke_width=1.5,
                  max_tip_length_to_length_ratio=0.02),
        )
        a2 = np.radians(300)
        end2 = 1.5 * np.array([np.cos(a2), np.sin(a2), 0])
        ray2 = Line(ORIGIN, end2, color=GREEN, stroke_width=3)
        pt2 = Dot(end2, radius=0.1, color=GREEN)
        arc2 = Arc(radius=0.45, start_angle=0, angle=a2, color=AMBER, stroke_width=2)
        al2 = MathTex(r"300^\circ", font_size=20, color=AMBER)
        al2.move_to(0.6 * np.array([np.cos(a2 / 2), np.sin(a2 / 2), 0]))
        # x 坐标虚线
        x_line2 = DashedLine(
            [0, end2[1], 0], end2, color=GREEN, stroke_width=2, dash_length=0.06,
        )
        x_val2 = MathTex(r"\frac{1}{2}", font_size=30, color=GREEN)
        x_val2.next_to(x_line2, DOWN, buff=0.12)
        cos_label = Text("cos 300° = x 坐标", font="Microsoft YaHei", font_size=22, color=TXT)
        cos_label.to_edge(UP, buff=0.3)

        uc2 = VGroup(circle2, axes2, arc2, al2, ray2, pt2, x_line2, x_val2, cos_label)
        uc2.scale(0.55).move_to(LEFT * 2.5)

        eq2 = MathTex(r"\cos\frac{5\pi}{3} = \cos300^\circ = \frac{1}{2}", font_size=34, color=GREEN)
        eq2.move_to(RIGHT * 2.5 + UP * 0.3)

        play_anim(7, FadeIn(uc2, scale=0.9), run_time=0.8)
        play_anim(7, FadeIn(eq2, shift=LEFT * 0.3), run_time=0.6)
        wait_to(8)
        play_anim(8, FadeOut(uc2), FadeOut(eq2), run_time=0.3)

        # ═══ seg 8: tan(5π/4) = tan225° → 单位圆 ═══
        circle3 = Circle(radius=1.5, color=BLUE, stroke_width=2)
        axes3 = VGroup(
            Arrow(LEFT * 2.2, RIGHT * 2.2, buff=0, color=DIM, stroke_width=1.5,
                  max_tip_length_to_length_ratio=0.02),
            Arrow(DOWN * 2.2, UP * 2.2, buff=0, color=DIM, stroke_width=1.5,
                  max_tip_length_to_length_ratio=0.02),
        )
        a3 = np.radians(225)
        end3 = 1.5 * np.array([np.cos(a3), np.sin(a3), 0])
        ray3 = Line(ORIGIN, end3, color=CORAL, stroke_width=3)
        pt3 = Dot(end3, radius=0.1, color=CORAL)
        arc3 = Arc(radius=0.45, start_angle=0, angle=a3, color=AMBER, stroke_width=2)
        al3 = MathTex(r"225^\circ", font_size=20, color=AMBER)
        al3.move_to(0.6 * np.array([np.cos(a3 / 2), np.sin(a3 / 2), 0]))
        # tan = y/x = 1，在点旁标注
        tan_val = MathTex(r"\tan225^\circ = 1", font_size=28, color=CORAL)
        tan_val.next_to(pt3, DL, buff=0.15)
        tan_label = Text("tan 225° = y/x = 1", font="Microsoft YaHei", font_size=22, color=TXT)
        tan_label.to_edge(UP, buff=0.3)

        uc3 = VGroup(circle3, axes3, arc3, al3, ray3, pt3, tan_val, tan_label)
        uc3.scale(0.55).move_to(LEFT * 2.5)

        eq3 = MathTex(r"\tan\frac{5\pi}{4} = \tan225^\circ = 1", font_size=34, color=CORAL)
        eq3.move_to(RIGHT * 2.5 + UP * 0.3)

        play_anim(8, FadeIn(uc3, scale=0.9), run_time=0.8)
        play_anim(8, FadeIn(eq3, shift=LEFT * 0.3), run_time=0.6)
        wait_to(9)
        play_anim(9, FadeOut(uc3), FadeOut(eq3), run_time=0.3)

        # ═══ seg 9: "A = {1/2, 1/2, 1}" ═══
        set_a_raw = MathTex(r"A = \left\{\frac{1}{2},\; \frac{1}{2},\; 1\right\}", font_size=40, color=BLUE)
        play_anim(9, FadeIn(set_a_raw, scale=1.1), run_time=0.8)
        wait_to(10)

        # ═══ seg 10: "注意集合有互异性" ═══
        play_anim(10, FadeOut(set_a_raw), run_time=0.3)
        note = Text("集合有互异性，重复只算一次", font="Microsoft YaHei", font_size=30, color=DIM)
        # 用红色框标出重复的 1/2
        example = MathTex(r"\left\{\frac{1}{2},\; \frac{1}{2},\; 1\right\}", font_size=36, color=TXT)
        example_group = VGroup(note, example).arrange(DOWN, buff=0.4)
        example_group.move_to(ORIGIN)
        # 红色 X 标记重复项
        dup_mark = Text("✗ 重复", font_size=22, color=PINK)
        dup_mark.next_to(example, DOWN, buff=0.2)
        play_anim(10, FadeIn(example_group, shift=UP * 0.2), run_time=0.6)
        play_anim(10, FadeIn(dup_mark), run_time=0.3)
        wait_to(11)
        play_anim(11, FadeOut(example_group), FadeOut(dup_mark), run_time=0.3)

        # ═══ seg 11: "A = {1/2, 1}" ═══
        set_a = MathTex(r"A = \left\{\frac{1}{2},\; 1\right\}", font_size=44, color=BLUE)
        play_anim(11, FadeIn(set_a, scale=1.2), run_time=0.8)
        wait_to(12)
        play_anim(12, FadeOut(set_a), run_time=0.3)

        # ═══ seg 12: "B = {-√3/2, -1/2, 1}" ═══
        set_b = MathTex(
            r"B = \left\{-\frac{\sqrt{3}}{2},\; -\frac{1}{2},\; 1\right\}",
            font_size=40, color=AMBER,
        )
        play_anim(12, FadeIn(set_b, shift=UP * 0.2), run_time=0.8)
        wait_to(13)
        play_anim(13, FadeOut(set_b), run_time=0.3)

        # ═══ seg 13: "公共元素只有1" ═══
        # 并排显示 A 和 B，高亮公共的 1
        set_a2 = MathTex(r"A = \left\{\frac{1}{2},\; 1\right\}", font_size=36, color=BLUE)
        set_b2 = MathTex(r"B = \left\{-\frac{\sqrt{3}}{2},\; -\frac{1}{2},\; 1\right\}", font_size=36, color=AMBER)
        sets = VGroup(set_a2, set_b2).arrange(DOWN, buff=0.4)
        sets.move_to(ORIGIN + UP * 0.3)
        # 高亮 1
        common = Text("公共元素：只有 1", font="Microsoft YaHei", font_size=30, color=GREEN)
        common.next_to(sets, DOWN, buff=0.6)
        play_anim(13, FadeIn(sets), run_time=0.6)
        play_anim(13, FadeIn(common, shift=UP * 0.2), run_time=0.5)
        wait_to(14)
        play_anim(14, FadeOut(sets), FadeOut(common), run_time=0.3)

        # ═══ seg 14: "A交B等于1" ═══
        result = MathTex(r"A \cap B = \{1\}", font_size=48, color=GREEN)
        play_anim(14, FadeIn(result, scale=1.3), run_time=0.8)
        wait_to(15)

        # ═══ seg 15: "答案选C" ═══
        play_anim(15, FadeOut(result), run_time=0.3)
        answer = Text("答案 C", font="Microsoft YaHei", font_size=64, color=GREEN, weight=BOLD)
        answer.move_to(ORIGIN)
        play_anim(15, FadeIn(answer, scale=1.5), run_time=0.6)
        wait_to(16)

        # 结尾
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.0)
        self.wait(0.5)
