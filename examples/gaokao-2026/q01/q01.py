"""2026高考数学第1题 - 中位数（v2：Transform排序动画 + 高亮中间值）
时间轴（TTS）：
  0.0-2.2   "来看第一题，中位数。"
  2.7-5.3   "这道题简单，但咱们把它讲清楚。"
  5.8-10.8  "样本数据是6、8、4、5、12，一共五个数。"
  11.3-16.4 "中位数是啥？就是把这组数据从小到大排一排，最中间那个。"
  16.9-18.0 "来，排一下。"
  18.5-22.7 "4、5、6、8、12。"
  23.2-26.0 "五个数，中间那个是第三个。"
  26.5-28.5 "所以中位数是6。"
  29.0-29.9 "答案选B。"
  30.4-35.1 "记住啊，中位数不是平均数，是排序后正中间那个。"
  35.6-38.8 "偶数个数的话，取中间两个的平均值。"
  39.3-41.2 "这道题白送分，别丢。"
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

T = [0.0, 2.7, 5.8, 11.3, 16.9, 18.5, 23.2, 26.5, 29.0, 30.4, 35.6, 39.3, 41.7]


def make_card(n, color=BLUE, size=1.0):
    """数字卡片：圆角方块 + 数字"""
    box = RoundedRectangle(
        corner_radius=0.15, width=size, height=size,
        color=color, stroke_width=2, fill_color=WHITE, fill_opacity=1,
    )
    txt = Text(str(n), font_size=int(40 * size), color=TXT, font="Microsoft YaHei")
    txt.move_to(box)
    return VGroup(box, txt)


class Q01(Scene):
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

        # ═══ seg 0: "来看第一题，中位数" → 标题 ═══
        title = Text("第 1 题", font="Microsoft YaHei", font_size=56, color=TXT)
        subtitle = Text("2026年新高考一卷", font="Microsoft YaHei", font_size=24, color=DIM)
        subtitle.next_to(title, DOWN, buff=0.4)
        play_anim(0, FadeIn(title, shift=DOWN * 0.3), run_time=0.8)
        play_anim(0, FadeIn(subtitle), run_time=0.5)
        wait_to(1)

        # ═══ seg 1: "这道题简单，但咱们把它讲清楚" → 题目 + 选项 ═══
        problem = Text(
            "样本数据 6, 8, 4, 5, 12 的中位数为？",
            font="Microsoft YaHei", font_size=32, color=TXT,
        )
        options = VGroup(
            Text("A. 5", font="Microsoft YaHei", font_size=26, color=DIM),
            Text("B. 6", font="Microsoft YaHei", font_size=26, color=GREEN),
            Text("C. 8", font="Microsoft YaHei", font_size=26, color=DIM),
            Text("D. 9", font="Microsoft YaHei", font_size=26, color=DIM),
        ).arrange(RIGHT, buff=1.0)
        options.next_to(problem, DOWN, buff=0.5)
        all_text = VGroup(problem, options)

        play_anim(1, FadeOut(subtitle), run_time=0.3)
        play_anim(1, FadeIn(all_text, shift=UP * 0.2), run_time=0.5)
        play_anim(1, title.animate.to_edge(UP, buff=0.4).scale(0.6), run_time=0.5)
        play_anim(1, all_text.animate.move_to(ORIGIN), run_time=0.5)
        wait_to(2)

        # ═══ seg 2: "样本数据是6、8、4、5、12" → 清题目，显示原始数据卡片 ═══
        play_anim(2, FadeOut(all_text), run_time=0.3)
        raw_nums = [6, 8, 4, 5, 12]
        raw_cards = VGroup(*[make_card(n, BLUE) for n in raw_nums])
        raw_cards.arrange(RIGHT, buff=0.5)
        raw_cards.move_to(ORIGIN + DOWN * 0.2)
        play_anim(2, LaggedStart(*[FadeIn(c, scale=0.8) for c in raw_cards], lag_ratio=0.2), run_time=1.5)
        wait_to(3)

        # ═══ seg 3: "中位数是啥？排序后最中间那个" ═══
        explain = Text(
            "中位数 = 排序后正中间的数",
            font="Microsoft YaHei", font_size=28, color=AMBER,
        )
        explain.next_to(raw_cards, DOWN, buff=1.0)
        play_anim(3, FadeIn(explain, shift=UP * 0.2), run_time=0.8)
        wait_to(4)

        # ═══ seg 4: "来，排一下" → Transform 排序动画 ═══
        play_anim(4, FadeOut(explain), run_time=0.3)
        # 排序后位置：4,5,6,8,12 — 让每个卡片 Transform 到目标位置
        sorted_cards = VGroup(*[make_card(n, AMBER) for n in [4, 5, 6, 8, 12]])
        sorted_cards.arrange(RIGHT, buff=0.5)
        sorted_cards.move_to(ORIGIN + DOWN * 0.2)
        # 排序映射：原始[6,8,4,5,12] → 排序[4,5,6,8,12]
        # 原始idx: 0→6, 1→8, 2→4, 3→5, 4→12
        # 排序idx: 4, 3, 0, 1, 4
        mapping = [2, 3, 0, 1, 4]  # sorted[i] comes from raw[mapping[i]]
        # 但更直观：每个raw card Transform 到对应sorted card
        anims = []
        for i in range(5):
            src_idx = [2, 3, 0, 1, 4][i]  # sorted[i] 对应 raw[src_idx]
            anims.append(Transform(raw_cards[src_idx], sorted_cards[i]))
        play_anim(4, *anims, run_time=1.5)
        # 更新引用
        raw_cards = sorted_cards
        wait_to(5)

        # ═══ seg 5: "4、5、6、8、12" → 排序完成，等待 ═══
        wait_to(6)

        # ═══ seg 6: "中间那个是第三个" → 高亮第3个 ═══
        # 脉冲高亮效果
        highlight = SurroundingRectangle(
            raw_cards[2], color=GREEN, stroke_width=5, buff=0.15, corner_radius=0.2
        )
        # 数字变色
        raw_cards[2][0].set_fill(GREEN, opacity=0.15)
        arrow = Arrow(
            raw_cards[2].get_top() + UP * 0.8,
            raw_cards[2].get_top() + UP * 0.1,
            color=GREEN, stroke_width=3,
        )
        label = Text("正中间", font="Microsoft YaHei", font_size=22, color=GREEN)
        label.next_to(arrow, UP, buff=0.1)
        # 标序号 1 2 ③ 4 5
        nums_label = VGroup()
        for i in range(5):
            if i == 2:
                t = Text("③", font_size=20, color=GREEN, font="Microsoft YaHei")
            else:
                t = Text(str(i + 1), font_size=18, color=DIM, font="Microsoft YaHei")
            t.next_to(raw_cards[i], DOWN, buff=0.2)
            nums_label.add(t)

        play_anim(6, Create(highlight), run_time=0.5)
        play_anim(6, GrowArrow(arrow), run_time=0.4)
        play_anim(6, FadeIn(label), run_time=0.3)
        play_anim(6, LaggedStart(*[FadeIn(n) for n in nums_label], lag_ratio=0.1), run_time=0.5)
        wait_to(7)

        # ═══ seg 7: "所以中位数是6" ═══
        result = Text("中位数 = 6", font="Microsoft YaHei", font_size=48, color=GREEN)
        result.next_to(raw_cards, DOWN, buff=1.2)
        play_anim(7, FadeIn(result, scale=1.3), run_time=0.8)
        wait_to(8)

        # ═══ seg 8: "答案选B" ═══
        play_anim(8, FadeOut(raw_cards), FadeOut(highlight), FadeOut(arrow),
                  FadeOut(label), FadeOut(nums_label), FadeOut(result), run_time=0.5)
        answer = Text("答案 B", font="Microsoft YaHei", font_size=64, color=GREEN, weight=BOLD)
        answer.move_to(ORIGIN)
        play_anim(8, FadeIn(answer, scale=1.5), run_time=0.6)
        wait_to(9)

        # ═══ seg 9: "记住啊，中位数不是平均数" ═══
        play_anim(9, FadeOut(answer), run_time=0.3)
        tip1 = Text(
            "中位数 ≠ 平均数",
            font="Microsoft YaHei", font_size=36, color=AMBER,
        )
        tip1.move_to(ORIGIN + UP * 0.5)
        play_anim(9, FadeIn(tip1, shift=UP * 0.2), run_time=0.8)
        tip1b = Text(
            "是排序后正中间那个",
            font="Microsoft YaHei", font_size=28, color=TXT,
        )
        tip1b.next_to(tip1, DOWN, buff=0.4)
        play_anim(9, FadeIn(tip1b), run_time=0.5)
        wait_to(10)

        # ═══ seg 10: "偶数个数的话，取中间两个的平均值" ═══
        tip2 = Text(
            "偶数个 → 取中间两个的平均值",
            font="Microsoft YaHei", font_size=28, color=BLUE,
        )
        tip2.next_to(tip1b, DOWN, buff=0.5)
        play_anim(10, FadeIn(tip2, shift=UP * 0.2), run_time=0.8)
        wait_to(11)

        # ═══ seg 11: "白送分，别丢" ═══
        play_anim(11, FadeOut(tip1), FadeOut(tip1b), FadeOut(tip2), run_time=0.3)
        final = Text("白送分，别丢！", font="Microsoft YaHei", font_size=48, color=GREEN)
        final.move_to(ORIGIN)
        play_anim(11, FadeIn(final, scale=1.3), run_time=0.6)
        wait_to(12)

        # 结尾
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.0)
        self.wait(0.5)
