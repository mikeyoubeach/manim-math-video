from manim import *
import math

# ── 配色（白色主题）──
BG = "#FFFFFF"
TXT = "#2D3436"
DIM = "#B2BEC3"
BLUE = "#4fc3f7"
GREEN = "#00B894"
AMBER = "#e8a87c"
PINK = "#FF6B9D"
CORAL = "#c97b5d"

# ── TTS 时间轴（18 segs）──
T = [0.0, 2.74, 6.12, 10.3, 13.36, 15.94, 20.92, 25.58, 30.24, 38.1, 45.0, 51.1, 59.6, 62.66, 65.88, 74.38, 77.28, 81.94]

class Q17(Scene):
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

        # ═══ seg 0: "来看第十七题，概率分布。" ═══
        title = Text("第17题", font="Microsoft YaHei", font_size=52, color=TXT, weight="BOLD")
        subtitle = Text("概率分布 · 投篮问题", font="Microsoft YaHei", font_size=28, color=DIM)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.3)
        play_anim(0, FadeIn(title_group, shift=UP * 0.3), run_time=1.0)
        wait_to(1)
        play_anim(1, FadeOut(title_group), run_time=0.5)

        # ═══ seg 1: "用一个球投篮练习，至多投篮N次。" ═══
        problem1 = Text("投篮练习：至多投 N 次", font="Microsoft YaHei", font_size=30, color=TXT)
        problem1.to_edge(UP, buff=0.5)
        play_anim(1, FadeIn(problem1, shift=DOWN * 0.2), run_time=0.8)
        wait_to(2)

        # ═══ seg 2: "当且仅当投中1次或N次都没中时停止。" ═══
        rule_text = Text("停止条件：投中 1 次 或 N 次全未中",
                         font="Microsoft YaHei", font_size=28, color=PINK)
        rule_text.next_to(problem1, DOWN, buff=0.4)
        play_anim(2, FadeIn(rule_text, shift=DOWN * 0.2), run_time=0.8)
        wait_to(3)

        # ═══ seg 3: "每次投中概率为p，各次独立。" ═══
        p_text = Text("每次投中概率为 p", font="Microsoft YaHei", font_size=28, color=TXT)
        p_text.next_to(rule_text, DOWN, buff=0.4)
        play_anim(3, FadeIn(p_text, shift=DOWN * 0.2), run_time=0.8)
        wait_to(4)

        # ═══ seg 4: "X为停止时的投篮次数。" ═══
        x_text = Text("X = 停止时的投篮次数", font="Microsoft YaHei", font_size=28, color=BLUE)
        x_text.next_to(p_text, DOWN, buff=0.4)
        play_anim(4, FadeIn(x_text, shift=DOWN * 0.2), run_time=0.8)
        wait_to(5)

        # ═══ seg 5: "N=4, p=1/3, 求X分布列" ═══
        # 清除题目，显示具体参数
        play_anim(5,
                  FadeOut(problem1), FadeOut(rule_text), FadeOut(p_text), FadeOut(x_text),
                  run_time=0.3)

        params = VGroup(
            MathTex(r"N = 4", font_size=36, color=TXT),
            MathTex(r"p = \frac{1}{3}", font_size=36, color=TXT),
            MathTex(r"q = 1-p = \frac{2}{3}", font_size=36, color=TXT),
        ).arrange(RIGHT, buff=0.8)
        params.to_edge(UP, buff=0.5)
        play_anim(5, FadeIn(params, shift=DOWN * 0.2), run_time=0.8)

        goal_text = Text("求 X 的分布列", font="Microsoft YaHei", font_size=30, color=PINK, weight="BOLD")
        goal_text.next_to(params, DOWN, buff=0.4)
        play_anim(5, FadeIn(goal_text, shift=DOWN * 0.2), run_time=0.8)
        wait_to(6)

        # ═══ seg 6: "X的可能取值是1、2、3、4。" ═══
        # 流程图展示投篮过程
        play_anim(6, FadeOut(params), FadeOut(goal_text), run_time=0.3)

        x_vals = VGroup(
            MathTex(r"X=1", font_size=32, color=PINK),
            MathTex(r"X=2", font_size=32, color=BLUE),
            MathTex(r"X=3", font_size=32, color=GREEN),
            MathTex(r"X=4", font_size=32, color=AMBER),
        ).arrange(RIGHT, buff=0.8)
        x_vals.to_edge(UP, buff=0.5)

        x_label = Text("X 的可能取值：", font="Microsoft YaHei", font_size=28, color=TXT)
        x_label.next_to(x_vals, LEFT, buff=0.3)
        play_anim(6, FadeIn(VGroup(x_label, x_vals), shift=DOWN * 0.2), run_time=1.0)

        # 树状图
        # 第1次投篮
        root = Dot(np.array([0, 1.0, 0]), color=TXT, radius=0.1)
        root_label = Text("第1次", font="Microsoft YaHei", font_size=22, color=TXT).next_to(root, UP, buff=0.1)

        # 命中分支 → X=1
        hit1_end = np.array([-3.5, -0.3, 0])
        hit1_line = Line(root.get_center(), hit1_end, color=GREEN, stroke_width=2)
        hit1_label = MathTex(r"\frac{1}{3}", font_size=22, color=GREEN).move_to(
            (root.get_center() + hit1_end) / 2 + UP * 0.2 + LEFT * 0.2)
        hit1_result = MathTex(r"X=1", font_size=24, color=PINK).next_to(hit1_end, DOWN, buff=0.1)

        # 未中分支 → 继续
        miss1_end = np.array([3.5, -0.3, 0])
        miss1_line = Line(root.get_center(), miss1_end, color=AMBER, stroke_width=2)
        miss1_label = MathTex(r"\frac{2}{3}", font_size=22, color=AMBER).move_to(
            (root.get_center() + miss1_end) / 2 + UP * 0.2 + RIGHT * 0.2)

        tree_grp = VGroup(root, root_label, hit1_line, hit1_label, hit1_result,
                          miss1_line, miss1_label)
        play_anim(6, FadeIn(tree_grp), run_time=1.0)
        wait_to(7)

        # ═══ seg 7: "X=1: 第一次就投中。概率=1/3。" ═══
        # 高亮 X=1 分支
        x1_box = SurroundingRectangle(hit1_result, color=PINK, buff=0.1)
        x1_prob = MathTex(r"P(X=1) = \frac{1}{3}", font_size=32, color=PINK)
        x1_prob.to_edge(DOWN, buff=1.0).shift(LEFT * 3)
        play_anim(7, Create(x1_box), FadeIn(x1_prob, shift=UP * 0.2), run_time=0.8)
        wait_to(8)

        # ═══ seg 8: "X=2: 第一次没中，第二次投中。概率=2/3×1/3=2/9。" ═══
        # 在未中分支后继续展开
        play_anim(8, FadeOut(x1_box), run_time=0.2)

        # 第2次投篮（从未中分支展开）
        node2 = miss1_end
        # 命中 → X=2
        hit2_end = np.array([2.0, -1.6, 0])
        hit2_line = Line(node2, hit2_end, color=GREEN, stroke_width=2)
        hit2_label = MathTex(r"\frac{1}{3}", font_size=20, color=GREEN).move_to(
            (node2 + hit2_end) / 2 + LEFT * 0.3)
        hit2_result = MathTex(r"X=2", font_size=24, color=BLUE).next_to(hit2_end, DOWN, buff=0.1)

        # 未中 → 继续
        miss2_end = np.array([4.8, -1.6, 0])
        miss2_line = Line(node2, miss2_end, color=AMBER, stroke_width=2)
        miss2_label = MathTex(r"\frac{2}{3}", font_size=20, color=AMBER).move_to(
            (node2 + miss2_end) / 2 + RIGHT * 0.3)

        tree2 = VGroup(hit2_line, hit2_label, hit2_result, miss2_line, miss2_label)
        play_anim(8, FadeIn(tree2), run_time=0.8)

        x2_prob = MathTex(r"P(X=2) = \frac{2}{3} \times \frac{1}{3} = \frac{2}{9}", font_size=30, color=BLUE)
        x2_prob.next_to(x1_prob, RIGHT, buff=0.5)
        play_anim(8, FadeIn(x2_prob, shift=UP * 0.2), run_time=0.8)
        wait_to(9)

        # ═══ seg 9: "X=3: 前两次没中，第三次投中。概率=4/27。" ═══
        # 第3次投篮
        node3 = miss2_end
        hit3_end = np.array([3.5, -2.9, 0])
        hit3_line = Line(node3, hit3_end, color=GREEN, stroke_width=2)
        hit3_label = MathTex(r"\frac{1}{3}", font_size=20, color=GREEN).move_to(
            (node3 + hit3_end) / 2 + LEFT * 0.3)
        hit3_result = MathTex(r"X=3", font_size=24, color=GREEN).next_to(hit3_end, DOWN, buff=0.1)

        miss3_end = np.array([5.8, -2.9, 0])
        miss3_line = Line(node3, miss3_end, color=AMBER, stroke_width=2)
        miss3_label = MathTex(r"\frac{2}{3}", font_size=20, color=AMBER).move_to(
            (node3 + miss3_end) / 2 + RIGHT * 0.3)

        tree3 = VGroup(hit3_line, hit3_label, hit3_result, miss3_line, miss3_label)
        play_anim(9, FadeIn(tree3), run_time=0.8)

        x3_prob = MathTex(r"P(X=3) = \left(\frac{2}{3}\right)^2 \times \frac{1}{3} = \frac{4}{27}", font_size=30, color=GREEN)
        x3_prob.next_to(x2_prob, DOWN, buff=0.3, aligned_edge=LEFT)
        play_anim(9, FadeIn(x3_prob, shift=UP * 0.2), run_time=0.8)
        wait_to(10)

        # ═══ seg 10: "X=4: 要么第三次没中第四次投中，要么四次都没中。" ═══
        # 第4次投篮（从未中分支展开）
        node4 = miss3_end
        # 命中 → X=4
        hit4_end = np.array([4.8, -4.2, 0])
        hit4_line = Line(node4, hit4_end, color=GREEN, stroke_width=2)
        hit4_label = MathTex(r"\frac{1}{3}", font_size=20, color=GREEN).move_to(
            (node4 + hit4_end) / 2 + LEFT * 0.3)

        # 未中 → X=4 (四次都未中也停)
        miss4_end = np.array([6.5, -4.2, 0])
        miss4_line = Line(node4, miss4_end, color=AMBER, stroke_width=2)
        miss4_label = MathTex(r"\frac{2}{3}", font_size=20, color=AMBER).move_to(
            (node4 + miss4_end) / 2 + RIGHT * 0.3)

        x4_result = MathTex(r"X=4", font_size=24, color=AMBER).move_to(
            (hit4_end + miss4_end) / 2 + DOWN * 0.4)

        tree4 = VGroup(hit4_line, hit4_label, miss4_line, miss4_label, x4_result)
        play_anim(10, FadeIn(tree4), run_time=1.0)

        x4_text = Text("X=4: 两种停止方式", font="Microsoft YaHei", font_size=26, color=TXT)
        x4_text.to_edge(DOWN, buff=0.8).shift(RIGHT * 2)
        play_anim(10, FadeIn(x4_text, shift=UP * 0.2), run_time=0.8)
        wait_to(11)

        # ═══ seg 11: "概率=8/81+16/81=24/81=8/27" ═══
        play_anim(11, FadeOut(x4_text), run_time=0.2)

        x4_prob = MathTex(r"P(X=4) = \left(\frac{2}{3}\right)^3 \times \frac{1}{3} + \left(\frac{2}{3}\right)^4", font_size=28, color=TXT)
        x4_prob.to_edge(DOWN, buff=1.2)
        play_anim(11, FadeIn(x4_prob, shift=UP * 0.2), run_time=0.8)

        x4_prob2 = MathTex(r"= \frac{8}{81} + \frac{16}{81} = \frac{24}{81} = \frac{8}{27}", font_size=28, color=AMBER)
        x4_prob2.next_to(x4_prob, DOWN, buff=0.2)
        play_anim(11, FadeIn(x4_prob2, shift=UP * 0.2), run_time=0.8)
        wait_to(12)

        # ═══ seg 12: "验证：所有概率加起来等于1。" ═══
        # 清除树状图，显示分布列
        play_anim(12,
                  FadeOut(root), FadeOut(root_label),
                  FadeOut(hit1_line), FadeOut(hit1_label), FadeOut(hit1_result),
                  FadeOut(miss1_line), FadeOut(miss1_label),
                  FadeOut(hit2_line), FadeOut(hit2_label), FadeOut(hit2_result),
                  FadeOut(miss2_line), FadeOut(miss2_label),
                  FadeOut(hit3_line), FadeOut(hit3_label), FadeOut(hit3_result),
                  FadeOut(miss3_line), FadeOut(miss3_label),
                  FadeOut(hit4_line), FadeOut(hit4_label),
                  FadeOut(miss4_line), FadeOut(miss4_label), FadeOut(x4_result),
                  FadeOut(x4_prob), FadeOut(x4_prob2),
                  run_time=0.5)

        # 分布列表格
        header = VGroup(
            MathTex(r"X", font_size=34, color=TXT),
            MathTex(r"1", font_size=34, color=PINK),
            MathTex(r"2", font_size=34, color=BLUE),
            MathTex(r"3", font_size=34, color=GREEN),
            MathTex(r"4", font_size=34, color=AMBER),
        ).arrange(RIGHT, buff=0.8)

        probs = VGroup(
            MathTex(r"P(X)", font_size=34, color=TXT),
            MathTex(r"\frac{1}{3}", font_size=34, color=PINK),
            MathTex(r"\frac{2}{9}", font_size=34, color=BLUE),
            MathTex(r"\frac{4}{27}", font_size=34, color=GREEN),
            MathTex(r"\frac{8}{27}", font_size=34, color=AMBER),
        ).arrange(RIGHT, buff=0.8)

        table = VGroup(header, probs).arrange(DOWN, buff=0.4)
        table.move_to(ORIGIN)

        # 画表格线
        table_bg = SurroundingRectangle(table, color=DIM, buff=0.3, corner_radius=0.1)

        play_anim(12, FadeIn(table_bg), FadeIn(table, shift=UP * 0.2), run_time=1.0)

        # 验证和=1
        verify = MathTex(r"\frac{1}{3} + \frac{2}{9} + \frac{4}{27} + \frac{8}{27} = \frac{9+6+4+8}{27} = \frac{27}{27} = 1", font_size=28, color=GREEN)
        verify.next_to(table, DOWN, buff=0.5)
        play_anim(12, FadeIn(verify, shift=UP * 0.2), run_time=1.0)

        # 绿色勾
        check = MathTex(r"\checkmark", font_size=40, color=GREEN).next_to(verify, RIGHT, buff=0.3)
        play_anim(12, FadeIn(check, scale=1.5), run_time=0.5)
        wait_to(13)

        # ═══ seg 13-17: 第二问（条件概率/无记忆性）═══
        # 清除分布列
        play_anim(13, FadeOut(table_bg), FadeOut(table), FadeOut(verify), FadeOut(check),
                  FadeOut(x1_prob), FadeOut(x2_prob), FadeOut(x3_prob),
                  run_time=0.3)

        q2_title = Text("第(2)问：无记忆性", font="Microsoft YaHei", font_size=32, color=PINK, weight="BOLD")
        q2_title.to_edge(UP, buff=0.5)
        play_anim(13, FadeIn(q2_title, shift=DOWN * 0.2), run_time=0.8)
        wait_to(14)

        # ═══ seg 14: 条件概率公式 ═══
        cond_prob = MathTex(
            r"P(X > k+m \mid X > k) = P(X > m)",
            font_size=32, color=TXT,
            tex_template=TexTemplate()
        )
        cond_prob.next_to(q2_title, DOWN, buff=0.5)
        cond_note = Text("当 k+m ≤ N-1 时成立", font="Microsoft YaHei", font_size=24, color=DIM)
        cond_note.next_to(cond_prob, DOWN, buff=0.3)

        play_anim(14, FadeIn(cond_prob, shift=DOWN * 0.2), FadeIn(cond_note), run_time=1.0)
        wait_to(15)

        # ═══ seg 15: "这本质上是无记忆性的证明。" ═══
        memory_text = Text("这是「无记忆性」的体现", font="Microsoft YaHei", font_size=28, color=BLUE)
        memory_text.next_to(cond_note, DOWN, buff=0.5)
        play_anim(15, FadeIn(memory_text, shift=DOWN * 0.2), run_time=0.8)
        wait_to(16)

        # ═══ seg 16: "因为每次投篮独立，前k次的结果不影响后面的概率。" ═══
        reason = Text("每次投篮独立 → 前 k 次不影响后续",
                       font="Microsoft YaHei", font_size=26, color=TXT)
        reason.next_to(memory_text, DOWN, buff=0.4)
        play_anim(16, FadeIn(reason, shift=DOWN * 0.2), run_time=0.8)
        wait_to(17)

        # ═══ seg 17: "所以条件概率等于无条件概率。" ═══
        conclusion = MathTex(
            r"P(X > k+m \mid X > k) = \frac{P(X > k+m)}{P(X > k)} = P(X > m)",
            font_size=28, color=GREEN,
            tex_template=TexTemplate()
        )
        conclusion.next_to(reason, DOWN, buff=0.4)

        conclusion_box = SurroundingRectangle(conclusion, color=GREEN, buff=0.15)
        play_anim(17, FadeIn(conclusion, shift=UP * 0.2), run_time=0.8)
        self.wait(0.3)
        play_anim(17, Create(conclusion_box), run_time=0.5)
        wait_to(18)

        self.wait(1.0)
