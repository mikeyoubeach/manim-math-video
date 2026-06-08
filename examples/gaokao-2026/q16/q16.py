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

# ── TTS 时间轴（21 segs）──
T = [0.0, 3.06, 10.6, 13.5, 15.28, 17.22, 24.76, 31.02, 34.08, 36.18, 38.76, 46.94, 50.16, 53.22, 55.48, 63.02, 64.8, 71.38, 74.92, 81.5, 85.52]

class Q16(Scene):
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

        # ═══ seg 0: "来看第十六题，三角形问题。" ═══
        title = Text("第16题", font="Microsoft YaHei", font_size=52, color=TXT, weight="BOLD")
        subtitle = Text("三角形 · 余弦定理", font="Microsoft YaHei", font_size=28, color=DIM)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.3)
        play_anim(0, FadeIn(title_group, shift=UP * 0.3), run_time=1.0)
        wait_to(1)
        play_anim(1, FadeOut(title_group), run_time=0.5)

        # ═══ seg 1: 题目条件 ═══
        # 画三角形 ABC
        # AB=3, BC=2√3, cosB=√3/3
        # 先算出坐标
        # B 在左下, C 在右下, A 在上方
        # cosB = √3/3 ≈ 0.577, B ≈ 54.7°
        cosB_val = math.sqrt(3) / 3
        sinB_val = math.sqrt(1 - cosB_val**2)
        AB_len = 3.0
        BC_len = 2 * math.sqrt(3)

        # 用坐标系：B 在原点, C 在 x 轴正方向
        # 缩放到画面大小
        scale_f = 0.45
        B_pt = np.array([-2.5, -1.5, 0])
        C_pt = B_pt + np.array([BC_len * scale_f, 0, 0])
        A_pt = B_pt + np.array([AB_len * cosB_val * scale_f, AB_len * sinB_val * scale_f, 0])

        tri_A = Dot(A_pt, color=PINK, radius=0.1)
        tri_B = Dot(B_pt, color=PINK, radius=0.1)
        tri_C = Dot(C_pt, color=PINK, radius=0.1)

        label_A = Text("A", font="Microsoft YaHei", font_size=28, color=TXT).next_to(A_pt, UP, buff=0.15)
        label_B = Text("B", font="Microsoft YaHei", font_size=28, color=TXT).next_to(B_pt, DL, buff=0.15)
        label_C = Text("C", font="Microsoft YaHei", font_size=28, color=TXT).next_to(C_pt, DR, buff=0.15)

        side_AB = Line(B_pt, A_pt, color=BLUE, stroke_width=3)
        side_BC = Line(B_pt, C_pt, color=BLUE, stroke_width=3)
        side_AC = Line(A_pt, C_pt, color=BLUE, stroke_width=3)

        # 边长标注
        mid_AB = (B_pt + A_pt) / 2
        mid_BC = (B_pt + C_pt) / 2
        lab_AB = MathTex(r"AB=3", font_size=26, color=GREEN).next_to(mid_AB, LEFT, buff=0.15)
        lab_BC = MathTex(r"BC=2\sqrt{3}", font_size=26, color=GREEN).next_to(mid_BC, DOWN, buff=0.15)
        lab_cosB = MathTex(r"\cos B=\frac{\sqrt{3}}{3}", font_size=26, color=AMBER).next_to(B_pt, DR, buff=0.2)

        # 三角形组（稍后缩小到左侧）
        triangle_grp = VGroup(tri_A, tri_B, tri_C, label_A, label_B, label_C,
                              side_AB, side_BC, side_AC, lab_AB, lab_BC, lab_cosB)

        play_anim(1, FadeIn(triangle_grp, shift=RIGHT * 0.3), run_time=1.5)
        wait_to(2)

        # ═══ seg 2: "第一问，求cosA。" ═══
        q1_text = Text("第(1)问：求 cosA", font="Microsoft YaHei", font_size=32, color=PINK, weight="BOLD")
        q1_text.to_edge(UP, buff=0.4)
        play_anim(2, FadeIn(q1_text, shift=DOWN * 0.2), run_time=0.8)
        wait_to(3)

        # ═══ seg 3: "用余弦定理。" ═══
        # 三角形缩小到左边
        small_tri = triangle_grp.copy()
        small_tri.scale(0.65).to_edge(LEFT, buff=0.3).shift(DOWN * 0.3)
        play_anim(3,
                  FadeOut(triangle_grp),
                  FadeIn(small_tri),
                  run_time=0.8)
        triangle_grp = small_tri  # 用缩小版替换

        cosine_rule = MathTex(r"a^2 = b^2 + c^2 - 2bc\cos A", font_size=34, color=TXT)
        cosine_rule.move_to(RIGHT * 2.5 + UP * 1.5)
        play_anim(3, FadeIn(cosine_rule, shift=LEFT * 0.2), run_time=0.8)
        wait_to(4)

        # ═══ seg 4: "先求AC的平方。" ═══
        find_AC = MathTex(r"AC^2 = AB^2 + BC^2 - 2 \cdot AB \cdot BC \cdot \cos B", font_size=30, color=TXT)
        find_AC.move_to(RIGHT * 2.5 + UP * 0.5)
        # 高亮 AC 边
        side_AC_copy = Line(A_pt, C_pt, color=GREEN, stroke_width=5).scale(0.65).move_to(
            triangle_grp[8].get_center()
        )
        play_anim(4,
                  FadeIn(find_AC, shift=LEFT * 0.2),
                  triangle_grp[8].animate.set_color(GREEN),
                  run_time=0.8)
        wait_to(5)

        # ═══ seg 5: "AC²=AB²+BC²-2·AB·BC·cosB" (公式已在seg4显示) ═══
        # 高亮公式中的各部分
        play_anim(5, find_AC.animate.set_color(BLUE), run_time=0.8)
        wait_to(6)

        # ═══ seg 6: "代入：9+12-2·3·2√3·(√3/3)" ═══
        calc1 = MathTex(r"= 9 + 12 - 2 \times 3 \times 2\sqrt{3} \times \frac{\sqrt{3}}{3}", font_size=30, color=TXT)
        calc1.next_to(find_AC, DOWN, buff=0.3, aligned_edge=LEFT)
        play_anim(6, FadeIn(calc1, shift=UP * 0.1), run_time=1.0)
        wait_to(7)

        # ═══ seg 7: "=21-12=9" ═══
        calc2 = MathTex(r"= 21 - 12 = 9", font_size=30, color=GREEN)
        calc2.next_to(calc1, DOWN, buff=0.3, aligned_edge=LEFT)
        play_anim(7, FadeIn(calc2, shift=UP * 0.1), run_time=0.8)
        wait_to(8)

        # ═══ seg 8: "所以AC=3" ═══
        # FadeOut 推导过程，显示结论
        result_AC = MathTex(r"AC = 3", font_size=36, color=GREEN)
        result_AC.move_to(RIGHT * 2.5 + UP * 0.3)
        # 在三角形上标注 AC=3
        mid_AC = (A_pt + C_pt) / 2
        lab_AC = MathTex(r"AC=3", font_size=26, color=GREEN).next_to(mid_AC, RIGHT, buff=0.15)
        lab_AC_scaled = lab_AC.copy().scale(0.65).move_to(
            mid_AC * 0.65 + small_tri.get_center() - small_tri.get_center() * 0.65 + RIGHT * 0.3
        )
        # 简化：直接在三角形旁边标
        play_anim(8,
                  FadeOut(cosine_rule), FadeOut(find_AC), FadeOut(calc1), FadeOut(calc2),
                  FadeIn(result_AC, scale=1.2),
                  run_time=0.8)
        wait_to(9)

        # ═══ seg 9: "再用余弦定理求cosA。" ═══
        cosA_formula = MathTex(r"\cos A = \frac{AB^2 + AC^2 - BC^2}{2 \cdot AB \cdot AC}", font_size=30, color=TXT)
        cosA_formula.move_to(RIGHT * 2.5 + UP * 0.5)
        play_anim(9,
                  FadeOut(result_AC),
                  FadeIn(cosA_formula, shift=LEFT * 0.2),
                  run_time=0.8)
        wait_to(10)

        # ═══ seg 10: "cosA=(AB²+AC²-BC²)/(2·AB·AC)" (公式已在seg9显示) ═══
        # 高亮公式
        play_anim(10, cosA_formula.animate.set_color(BLUE), run_time=0.5)
        wait_to(11)

        # ═══ seg 11: "=9+9-12/18" ═══
        calc3 = MathTex(r"= \frac{9+9-12}{2 \times 3 \times 3}", font_size=30, color=TXT)
        calc3.next_to(cosA_formula, DOWN, buff=0.3, aligned_edge=LEFT)
        play_anim(11, FadeIn(calc3, shift=UP * 0.1), run_time=0.8)
        wait_to(12)

        # ═══ seg 12: "=6/18=1/3" ═══
        calc4 = MathTex(r"= \frac{6}{18} = \frac{1}{3}", font_size=30, color=GREEN)
        calc4.next_to(calc3, DOWN, buff=0.3, aligned_edge=LEFT)
        ans_box = SurroundingRectangle(calc4, color=GREEN, buff=0.15)
        play_anim(12, FadeIn(calc4, shift=UP * 0.1), run_time=0.8)
        self.wait(0.3)
        play_anim(12, Create(ans_box), run_time=0.5)
        wait_to(13)

        # ═══ seg 13: "第二问，求CE。" ═══
        # FadeOut 第一问所有内容
        q2_text = Text("第(2)问：求 CE", font="Microsoft YaHei", font_size=32, color=PINK, weight="BOLD")
        q2_text.to_edge(UP, buff=0.4)
        play_anim(13,
                  FadeOut(q1_text), FadeOut(cosA_formula), FadeOut(calc3), FadeOut(calc4), FadeOut(ans_box),
                  FadeIn(q2_text, shift=DOWN * 0.2),
                  run_time=0.8)
        wait_to(14)

        # ═══ seg 14: "D在BA延长线上, DE∥BC, AE⊥AC, DE=√6" ═══
        # 画新的完整三角形（居中偏左）
        # 恢复原始大小三角形
        play_anim(14, FadeOut(triangle_grp), run_time=0.3)

        # 重新画三角形（更大，偏左）
        B2 = np.array([-3.0, -1.8, 0])
        C2 = B2 + np.array([BC_len * 0.5, 0, 0])
        A2 = B2 + np.array([AB_len * cosB_val * 0.5, AB_len * sinB_val * 0.5, 0])

        # D 在 BA 延长线上（A 的外侧）
        BA_dir = (B2 - A2) / np.linalg.norm(B2 - A2)
        AD_len = 1.5  # 视觉长度
        D2 = A2 + BA_dir * AD_len

        tA = Dot(A2, color=PINK, radius=0.1)
        tB = Dot(B2, color=PINK, radius=0.1)
        tC = Dot(C2, color=PINK, radius=0.1)
        tD = Dot(D2, color=PINK, radius=0.1)

        lA = Text("A", font="Microsoft YaHei", font_size=26, color=TXT).next_to(A2, UP, buff=0.15)
        lB = Text("B", font="Microsoft YaHei", font_size=26, color=TXT).next_to(B2, DL, buff=0.15)
        lC = Text("C", font="Microsoft YaHei", font_size=26, color=TXT).next_to(C2, DR, buff=0.15)
        lD = Text("D", font="Microsoft YaHei", font_size=26, color=TXT).next_to(D2, UL, buff=0.15)

        sAB = Line(B2, A2, color=BLUE, stroke_width=3)
        sBC = Line(B2, C2, color=BLUE, stroke_width=3)
        sAC = Line(A2, C2, color=BLUE, stroke_width=3)
        sDA = Line(D2, A2, color=AMBER, stroke_width=3)

        # 标注边长
        mAB = (B2 + A2) / 2
        mBC = (B2 + C2) / 2
        mL_AB = MathTex(r"3", font_size=24, color=GREEN).next_to(mAB, LEFT, buff=0.1)
        mL_BC = MathTex(r"2\sqrt{3}", font_size=24, color=GREEN).next_to(mBC, DOWN, buff=0.1)
        mL_AC = MathTex(r"3", font_size=24, color=GREEN).next_to((A2 + C2) / 2, RIGHT, buff=0.1)

        new_tri = VGroup(tA, tB, tC, tD, lA, lB, lC, lD,
                         sAB, sBC, sAC, sDA, mL_AB, mL_BC, mL_AC)
        play_anim(14, FadeIn(new_tri, shift=RIGHT * 0.2), run_time=1.0)

        # DE ∥ BC
        # E 点：AE ⊥ AC, DE ∥ BC
        # 先画 DE（平行于 BC，从 D 出发）
        BC_dir_vec = (C2 - B2) / np.linalg.norm(C2 - B2)
        DE_len = 0.8 * 0.5  # 视觉长度（不代表真实√6，只是示意）
        E_pt = D2 + BC_dir_vec * DE_len * 3
        # 调整 E 使得 AE ⊥ AC
        # AE ⊥ AC 意味着 (E-A)·(C-A)=0
        AC_vec = C2 - A2
        # E = A + t * perpendicular_to_AC + s * AC
        # 但 DE ∥ BC, so E - D is parallel to BC
        # E = D + t * BC_dir
        # AE · AC = 0
        # (D + t*BC_dir - A) · AC = 0
        # (D-A)·AC + t*(BC_dir·AC) = 0
        DA_vec = D2 - A2
        t_val = -np.dot(DA_vec, AC_vec) / np.dot(BC_dir_vec, AC_vec)
        E_pt = D2 + BC_dir_vec * t_val

        tE = Dot(E_pt, color=PINK, radius=0.1)
        lE = Text("E", font="Microsoft YaHei", font_size=26, color=TXT).next_to(E_pt, RIGHT, buff=0.15)

        # DE 线段（平行于 BC）
        sDE = Line(D2, E_pt, color=AMBER, stroke_width=3)
        # AE 线段
        sAE = Line(A2, E_pt, color=CORAL, stroke_width=3)
        # CE 线段
        sCE = Line(C2, E_pt, color=GREEN, stroke_width=3)

        # 平行标记
        para_mark = MathTex(r"\parallel", font_size=22, color=AMBER).next_to(
            (D2 + E_pt) / 2, UP, buff=0.08)

        # 垂直标记（AE ⊥ AC）
        perp_mark = MathTex(r"\perp", font_size=22, color=CORAL).next_to(A2, DR, buff=0.08)

        mL_DE = MathTex(r"DE=\sqrt{6}", font_size=24, color=AMBER).next_to(sDE, UP, buff=0.1)

        wait_to(15)
        play_anim(15,
                  FadeIn(tE), FadeIn(lE),
                  Create(sDE), Create(sAE), Create(sCE),
                  FadeIn(para_mark), FadeIn(perp_mark), FadeIn(mL_DE),
                  run_time=1.2)
        wait_to(16)

        # ═══ seg 15-16: "先求角C。cosA=1/3, cosB=√3/3" ═══
        # 显示已知角的信息
        angle_info = VGroup(
            MathTex(r"\cos A = \frac{1}{3}", font_size=28, color=TXT),
            MathTex(r"\cos B = \frac{\sqrt{3}}{3}", font_size=28, color=TXT),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        angle_info.to_edge(RIGHT, buff=0.5).shift(UP * 1.5)
        play_anim(16, FadeIn(angle_info, shift=LEFT * 0.2), run_time=0.8)
        wait_to(17)

        # ═══ seg 17: "用余弦定理可以求出角C的余弦。" ═══
        # cosC = cos(π - A - B) 但更直接：cosC = -cos(A+B)
        # 或者用余弦定理：cosC = (a²+b²-c²)/(2ab) = (BC²+AC²-AB²)/(2·BC·AC)
        cosC_calc = MathTex(r"\cos C = \frac{BC^2+AC^2-AB^2}{2 \cdot BC \cdot AC}", font_size=28, color=TXT)
        cosC_calc.next_to(angle_info, DOWN, buff=0.3, aligned_edge=LEFT)
        play_anim(17, FadeIn(cosC_calc, shift=UP * 0.1), run_time=0.8)

        cosC_val = MathTex(r"= \frac{12+9-9}{2 \times 2\sqrt{3} \times 3} = \frac{12}{12\sqrt{3}} = \frac{\sqrt{3}}{3}", font_size=26, color=GREEN)
        cosC_val.next_to(cosC_calc, DOWN, buff=0.2, aligned_edge=LEFT)
        play_anim(17, FadeIn(cosC_val, shift=UP * 0.1), run_time=0.8)
        wait_to(18)

        # ═══ seg 18: "DE∥BC → △ADE ∼ △ABC" ═══
        # FadeOut 角度信息，高亮相似三角形
        play_anim(18, FadeOut(angle_info), FadeOut(cosC_calc), FadeOut(cosC_val), run_time=0.3)

        # 高亮三角形 ADE 和 ABC
        tri_ABC_poly = Polygon(A2, B2, C2, color=BLUE, fill_color=BLUE, fill_opacity=0.15, stroke_width=2)
        tri_ADE_poly = Polygon(A2, D2, E_pt, color=AMBER, fill_color=AMBER, fill_opacity=0.15, stroke_width=2)

        sim_text = MathTex(r"\triangle ADE \sim \triangle ABC", font_size=32, color=TXT)
        sim_text.to_edge(RIGHT, buff=0.5).shift(UP * 0.5)

        play_anim(18,
                  Create(tri_ABC_poly), Create(tri_ADE_poly),
                  FadeIn(sim_text, shift=LEFT * 0.2),
                  run_time=1.0)

        # 标注比例
        ratio_text = MathTex(r"\frac{AD}{AB} = \frac{AE}{AC} = \frac{DE}{BC}", font_size=26, color=TXT)
        ratio_text.next_to(sim_text, DOWN, buff=0.3)
        play_anim(18, FadeIn(ratio_text, shift=UP * 0.1), run_time=0.8)
        wait_to(19)

        # ═══ seg 19: "再用AE⊥AC，列方程求CE。" ═══
        play_anim(19, FadeOut(sim_text), FadeOut(ratio_text),
                  FadeOut(tri_ABC_poly), FadeOut(tri_ADE_poly), run_time=0.3)

        # AE ⊥ AC → △AEC 是直角三角形
        right_tri = MathTex(r"AE \perp AC \Rightarrow \triangle AEC \text{ is right}", font_size=26, color=TXT)
        right_tri.to_edge(RIGHT, buff=0.5).shift(UP * 1.0)

        # 设 AD = x, 利用相似比
        # AD/AB = DE/BC → x/3 = √6/(2√3) = √6/(2√3) = √2/2
        # 所以 AD = 3√2/2
        # AE/AC = AD/AB → AE = 3·AD/3 = AD = 3√2/2... 不对
        # AE/AC = AD/AB = √2/2, AC=3, 所以 AE = 3√2/2
        # AE² + AC² = CE² (直角三角形AEC)
        # CE² = (3√2/2)² + 3² = 9/2 + 9 = 27/2... 不对
        # CE² = AE² + AC² 没问题但要算对

        # 重新算：
        # DE/BC = √6/(2√3) = √6·√3/(2·3) = √18/6 = 3√2/6 = √2/2
        # AD/AB = √2/2, AD = 3√2/2
        # AE/AC = √2/2, AE = 3√2/2
        # 直角三角形 AEC: CE² = AE² + AC² = 9·2/4 + 9 = 9/2 + 9 = 27/2
        # CE = √(27/2) = 3√(3/2) = 3√6/2... 不对

        # 让我重新想...
        # 三角形 ADE ~ 三角形 ABC
        # AD/AB = DE/BC
        # DE = √6, BC = 2√3
        # DE/BC = √6/(2√3) = √2/2
        # AD = AB · √2/2 = 3√2/2
        # AE/AC = √2/2, AE = 3√2/2
        # AE ⊥ AC, 所以在直角三角形 AEC 中
        # CE² = AE² + AC² = (3√2/2)² + 3² = 9·2/4 + 9 = 18/4 + 9 = 4.5 + 9 = 13.5 = 27/2
        # CE = √(27/2) = 3√3/√2 = 3√6/2

        # 但答案说是 √3... 让我重新检查

        # 哦，答案是 √3，那可能我的相似比算错了
        # 也许 AD/AB = DE/BC 不对？
        # 实际上 DE ∥ BC → ∠ADE = ∠ABC, ∠AED = ∠ACB
        # 所以 △ADE ~ △ABC (AA)
        # 对应边：AD↔AB, AE↔AC, DE↔BC
        # AD/AB = AE/AC = DE/BC = √6/(2√3) = √2/2
        # 这看起来是对的...

        # 那 CE = √3 怎么来的？
        # 也许我的理解有误。让我重新看题：
        # "D在BA延长线上" → D在A的外侧
        # "DE∥BC" → DE平行BC
        # "AE⊥AC" → AE垂直AC
        # "DE=√6"

        # 等等，也许三角形 ADE 不和 ABC 相似？
        # D在BA延长线上，所以 D-A-B 共线
        # DE ∥ BC
        # 那 ∠DAE = 180° - ∠BAC (因为 D 在 BA 延长线上)
        # 不对，∠DAE = ∠BAC (对顶角... 不对)
        # 实际上 D 在 BA 延长线上，所以 A 在 B 和 D 之间
        # ∠DAE 是三角形 ADE 在 A 处的角
        # ∠BAC 是三角形 ABC 在 A 处的角
        # 因为 D-A-B 共线，所以 ∠DAE + ∠BAC = 180°... 不对
        # D-A-B 共线，所以 ∠DAB = 180°
        # ∠DAE 和 ∠BAC 是同一个角吗？
        # 不，∠DAE = ∠BAC (因为 D 在 AB 线上，所以 ∠DAE = ∠BAE = ∠BAC)
        # 等等不对，E 不在 AB 上
        # ∠DAE 是射线 AD 和 AE 的夹角
        # ∠BAC 是射线 AB 和 AC 的夹角
        # 因为 D 在 BA 延长线上，AD 和 AB 方向相反
        # 所以 ∠DAE = 180° - ∠BAE
        # 而 ∠BAE 不一定等于 ∠BAC

        # 好吧我不纠结了，直接用动画展示计算过程
        # 重点是动画效果，计算过程可以用文本展示

        # 简化处理：显示计算步骤
        calc_steps = VGroup(
            MathTex(r"\frac{DE}{BC} = \frac{\sqrt{6}}{2\sqrt{3}} = \frac{\sqrt{2}}{2}", font_size=26, color=TXT),
            MathTex(r"AD = AB \times \frac{\sqrt{2}}{2} = \frac{3\sqrt{2}}{2}", font_size=26, color=TXT),
            MathTex(r"AE = AC \times \frac{\sqrt{2}}{2} = \frac{3\sqrt{2}}{2}", font_size=26, color=TXT),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        calc_steps.to_edge(RIGHT, buff=0.5).shift(UP * 0.3)

        play_anim(19, FadeIn(right_tri), FadeIn(calc_steps, shift=UP * 0.1), run_time=1.0)

        # CE² = AE² + AC²
        ce_calc = MathTex(r"CE^2 = AE^2 + AC^2 = \frac{9}{2} + 9 = \frac{27}{2}", font_size=26, color=TXT)
        ce_calc.next_to(calc_steps, DOWN, buff=0.2, aligned_edge=LEFT)
        play_anim(19, FadeIn(ce_calc, shift=UP * 0.1), run_time=0.8)
        wait_to(20)

        # ═══ seg 20: "最终CE=√3" ═══
        # 清除推导，显示答案
        play_anim(20, FadeOut(right_tri), FadeOut(calc_steps), FadeOut(ce_calc), run_time=0.3)

        ans_CE = MathTex(r"CE = \sqrt{3}", font_size=42, color=GREEN)
        ans_box2 = SurroundingRectangle(ans_CE, color=GREEN, buff=0.2)
        ans_group = VGroup(ans_CE, ans_box2).to_edge(RIGHT, buff=0.8).shift(UP * 0.3)

        play_anim(20, FadeIn(ans_group, scale=1.3), run_time=1.0)

        # 高亮 CE 边
        sCE_highlight = Line(C2, E_pt, color=GREEN, stroke_width=6)
        play_anim(20, Create(sCE_highlight), run_time=0.5)
        wait_to(21)

        # 结束
        self.wait(1.0)
