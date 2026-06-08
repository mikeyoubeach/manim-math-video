---
name: manim-math-video
slug: manim-math-video
version: 1.0.0
description: >
  Manim + TTS 数学教育视频制作引擎。文案 → TTS → Manim 动画（对齐语音时间轴）→ FFmpeg 合成 → MP4。
  Manim 负责数学动画（LaTeX 公式、曲线生长、几何变换、坐标系），MiMo TTS 负责语音，FFmpeg 负责合成。
type: code
implementation: python
runtime: python>=3.8
tags: [video, manim, tts, math, animation, education]
author: lobster
---

# Manim Math Video — 数学教育视频制作

## 何时激活

- 用户要做**数学类教育视频**（公式推导、函数图像、几何动画、微积分、代数等）
- 需要**语音讲解 + 动画同步**
- 需要 **LaTeX 公式渲染**、**曲线生长动画**、**坐标系绘制**
- 之前手写 SVG/Canvas 效果不好，想提升到 3Blue1Brown 级别

## 核心理念

> **先有语音，再按语音时间轴写动画。**
> 不要先做动画再塞语音——两者永远对不上。

## Pipeline

```
用户要求 / 数学主题
  ↓
① 写文案（每句话对应一个动画概念）
  ↓
② TTS 生成语音（mimo-tts --batch → timeline.json + WAV）
  ↓
③ 按 timeline.json 的精确时间写 Manim 代码
   - 每个动画的 run_time 和 wait 精确卡在对应语音窗口内
   - 语音先说，动画紧跟
  ↓
④ Manim 渲染视频（无声）
  ↓
⑤ FFmpeg 合成（视频 + TTS 音频对齐）
  ↓
⑥ 输出 MP4
```

## 环境依赖

```bash
# Manim（社区版）
pip install manim

# MiKTeX（LaTeX 渲染，Windows）
winget install MiKTeX.MiKTeX
# 安装后需添加到 PATH:
# C:\Users\<user>\AppData\Local\Programs\MiKTeX\miktex\bin\x64

# FFmpeg（音视频合成）
# 已安装则跳过

# MiMo TTS（OpenClaw 内置 skill）
# skills/mimo-tts/scripts/mimo_tts.py
```

## 快速开始

### 1. 写文案

每行一句话，对应一个动画概念。示例（`script.txt`）：

```
首先，画一个坐标系。
然后，画出曲线，y等于x的平方。
接下来，我们用矩形去逼近曲线下方的面积。
黎曼说，先把区间切成四份。
切得越细，近似就越精确。
当n趋向无穷，近似变成了精确。
这就是积分。
```

### 2. 生成 TTS

```bash
& 'python' skills/mimo-tts/scripts/mimo_tts.py \
  --batch-file script.txt --voice 冰糖 -o audio/
```

输出 `audio/timeline.json` + `audio/segment_001~N.wav`。

### 3. 按时间轴写 Manim 动画

关键：**用 `elapsed` 追踪实际已用时间，`wait_to()` 自动等到下一段语音开始。**

⚠️ **不要硬编码 wait 时间！** 动画的 `run_time` 可能和预期略有出入，累积误差会导致后半段语音和动画对不上。

```python
from manim import *

# TTS 时间轴（每段语音的开始时间）
T = [0.0, 2.1, 8.8, 11.6, 15.0, 20.1, 25.1, 28.8]

class MathDemo(Scene):
    def construct(self):
        elapsed = 0.0  # 追踪已用时间

        def wait_to(seg_idx):
            """等到第 seg_idx 段语音开始"""
            nonlocal elapsed
            gap = T[seg_idx] - elapsed
            if gap > 0.05:
                self.wait(gap)
                elapsed += gap

        def play_anim(seg_idx, *args, **kwargs):
            """播放动画，自动更新 elapsed"""
            nonlocal elapsed
            self.play(*args, **kwargs)
            elapsed += kwargs.get("run_time", 1.0)

        # 第0段: 0.0s "首先，画一个坐标系"
        axes = Axes(...)
        play_anim(0, Create(axes), run_time=1.0)
        wait_to(1)  # 自动等到 2.1s

        # 第1段: 2.1s "画出曲线"
        curve = axes.plot(lambda x: x**2, ...)
        play_anim(1, Create(curve), run_time=2.5)
        wait_to(2)  # 自动等到 8.8s
```

**`wait_to` 的核心逻辑：**
- 计算 `gap = TTS开始时间 - 已用时间`
- 如果 gap > 0，wait 这么久
- 如果 gap ≈ 0（动画刚好跑完），直接进入下一段
- 如果 gap < 0（动画超时了），跳过 wait，立即开始下一段

这样不管动画跑快跑慢，语音和动画永远对齐。

### 4. 渲染

```bash
# 低清预览
$env:PATH += ";$env:LOCALAPPDATA\Programs\MiKTeX\miktex\bin\x64"
manim -pql demo.py MathDemo

# 高清渲染
manim -pqh demo.py MathDemo
```

### 5. 合成音频

```bash
ffmpeg -y -i video.mp4 -i audio.wav -c:v copy -c:a aac output.mp4
```

多段音频用 `scripts/combine.py`（见下方）。

---

## 时间轴对齐方法（核心！）

### 原则

1. **先生成 TTS**，拿到每段语音的精确起止时间
2. **语音间隙**：每段之间 0.5s 静音
3. **动画时间 = 语音窗口内的子集**：动画在语音开始后启动，在语音结束前完成
4. **wait 填充**：动画完成后用 `self.wait()` 等到下一段语音开始

### 时间轴示例

```
TTS 输出:
  [0.0s - 1.8s]  "首先，画一个坐标系"
  [2.3s - 5.8s]  "然后，画出曲线"
  [6.3s - 8.8s]  "这条曲线就是我们要研究的函数"

Manim 代码:
  0.0-1.0s:  Create(axes)          # 动画
  1.0-1.8s:  wait(0.8)            # 等语音
  1.8-2.3s:  wait(0.5)            # 语音间隙
  2.3-4.8s:  Create(curve)        # 动画
  4.8-5.8s:  wait(1.0)            # 等语音
  5.8-6.3s:  wait(0.5)            # 语音间隙
  6.3-8.8s:  wait(2.5)            # 语音讲解，画面保持
```

### 辅助脚本：读取 timeline 生成 Manim 时间轴注释

```bash
& 'python' scripts/timeline_to_manim.py audio/timeline.json
```

输出每段语音的起止时间 + 建议的动画窗口，直接复制到 Manim 代码里当注释。

---

## Manim 常用动画速查

### 基础动画

| 效果 | 代码 | 说明 |
|------|------|------|
| 绘制 | `self.play(Create(obj))` | 从无到有画出 |
| 淡入 | `self.play(FadeIn(obj))` | 透明度 0→1 |
| 淡出 | `self.play(FadeOut(obj))` | 透明度 1→0 |
| 写字 | `self.play(Write(tex))` | LaTeX 逐笔写出 |
| 变换 | `self.play(Transform(a, b))` | a 形状变成 b |
| 移动 | `self.play(obj.animate.move_to(pos))` | 平滑移动 |
| 缩放 | `self.play(obj.animate.scale(1.5))` | 放大缩小 |
| 变色 | `self.play(obj.animate.set_color(RED))` | 颜色过渡 |
| 等待 | `self.wait(1.0)` | 保持画面 1 秒 |

### 数学专用

| 效果 | 代码 |
|------|------|
| 坐标系 | `Axes(x_range=[-5,5], y_range=[-3,3], ...)` |
| 函数曲线 | `axes.plot(lambda x: x**2, color=BLUE)` |
| 黎曼矩形 | `axes.get_riemann_rectangles(curve, dx=0.25)` |
| 面积填充 | `axes.get_area(curve, x_range=[0,3])` |
| LaTeX 公式 | `MathTex(r"\int_0^3 x^2 dx = 9", font_size=48)` |
| 大括号标注 | `Brace(obj, direction, color=RED)` |
| 虚线 | `DashedLine(start, end, dash_length=0.1)` |
| 高亮矩形 | `obj.copy().set_fill(ACCENT, opacity=0.6)` |
| 曲线描边 | `Create(curve)` 自带描边效果 |

### 运镜 / 相机

| 效果 | 代码 |
|------|------|
| 缩放到区域 | `self.play(self.camera.frame.animate.scale(0.5).move_to(target))` |
| 平移相机 | `self.play(self.camera.frame.animate.move_to(RIGHT * 3))` |
| 恢复 | `self.play(self.camera.frame.animate.scale(1/0.5))` |

---

## 配色方案

### 暗色学术风（推荐）

```python
BG = "#0d1117"       # 深蓝黑背景
CURVE = "#4fc3f7"    # 天蓝（曲线/主色）
RECT = "#e8a87c"     # 暖橙（矩形/辅助）
ACCENT = "#7ed3a4"   # 荧光绿（高亮）
TXT = "#e4e2d8"      # 暖白（文字）
DIM = "#556677"      # 灰色（坐标轴）
```

### 暖色教育风

```python
BG = "#1a1412"       # 深棕
CURVE = "#e8a87c"    # 暖橙
RECT = "#d4a574"     # 金色
ACCENT = "#c97b5d"   # 珊瑚
TXT = "#faf0e6"      # 奶白
```

---

## 踩坑记录

### 1. MiKTeX 首次运行需下载包

Manim 用 `MathTex()` 渲染 LaTeX，MiKTeX 首次需要自动下载宏包。
设置自动安装：`initexmf --set-config-value=[MPM]auto_install=1`

### 2. Windows PATH 问题

MiKTeX 不在默认 PATH 里，渲染前需：
```powershell
$env:PATH += ";$env:LOCALAPPDATA\Programs\MiKTeX\miktex\bin\x64"
```

### 3. 中文字体

```python
Text("中文", font="Microsoft YaHei")
```
Manim 用系统字体渲染中文，确保有微软雅黑。

**⚠️ MathTex 不能渲染中文！** LaTeX 引擎不支持中文字符。
中文必须用 `Text()`，数学公式用 `MathTex()`，分开写：

```python
# ❌ 错误：MathTex 里写中文
MathTex(r"\text{切线斜率} = y'")  # 报错

# ✅ 正确：中文用 Text，公式用 MathTex，然后排列
label = Text("切线斜率", font="Microsoft YaHei", font_size=28)
eq = MathTex(r"= y'", font_size=28)
group = VGroup(label, eq).arrange(RIGHT, buff=0.2)
```

### 4. Manim API 版本差异

- `get_riemann_rectangles` 不是 `get_riemann_rects`
- 参数用 `dx=3/n`，不是 `n=n`
- `input_sample_type="center"` 可选

### 5. FFmpeg 多段音频合并

**⚠️ 不要用 `amix`！** 多轨混音会导致音量随轨数变化（开始小，后面大）。

正确做法：先把所有 TTS 片段拼成一个完整 WAV（中间补静音），再和视频合并：

```python
# 拼接：按时间轴把每段音频写入正确位置
all_audio = bytearray(total_frames * sampwidth * nchannels)  # 静音底板
for seg in segments:
    with wave.open(seg_path, 'r') as w:
        frames = w.readframes(w.getnframes())
    offset = int(seg['start'] * framerate) * sampwidth * nchannels
    all_audio[offset:offset+len(frames)] = frames

# 写入临时 WAV，然后 ffmpeg -i video.mp4 -i combined.wav -c:v copy -c:a aac output.mp4
```

详见 `scripts/combine.py`（v2 拼接版）。

### 6. 动画不要太快

Manim 默认 `run_time=1s`，对教育视频来说太快。建议：
- 曲线绘制：2-3 秒
- 公式出现：1-1.5 秒
- 矩形变换：0.8-1 秒
- 重要概念停留：2-3 秒 wait

### 7. 语音间隙

TTS 每段之间需 0.5s 间隙，否则语音连在一起听不清。
在 TTS 脚本里用 `current += dur + 0.5`。

### 8. 动态时间对齐（重要！）

**不要硬编码 wait 时间。** 动画实际 `run_time` 可能和预期有 0.1-0.3s 的误差，
累积 10+ 段后，后半段动画和语音会明显错位。

正确做法：用 `elapsed` 追踪实际已用时间，`wait_to(seg_idx)` 自动计算到下一段语音的剩余时间。

```python
elapsed = 0.0
def wait_to(seg_idx):
    nonlocal elapsed
    gap = T[seg_idx] - elapsed
    if gap > 0.05:
        self.wait(gap)
        elapsed += gap
def play_anim(seg_idx, *args, **kwargs):
    nonlocal elapsed
    self.play(*args, **kwargs)
    elapsed += kwargs.get("run_time", 1.0)
```

详见 `examples/q4_tangent_v2.py` 的完整实现。

### 9. 多个元素一起移动

多个对象要一起动画时，用 `VGroup` 打包：

```python
problem = Text("题目...", ...)
options = VGroup(
    MathTex(r"\text{A. } y = 3x + 2"),
    MathTex(r"\text{B. } y = 5x"),
    ...
).arrange(DOWN, aligned_edge=LEFT)

all_text = VGroup(problem, options)  # 打包
all_text.move_to(ORIGIN)  # 一起移动
self.play(all_text.animate.shift(UP * 0.5))  # 一起动画
```

### 10. Dot 单位是 Manim 场景单位，不是像素

```python
# ❌ radius=6 巨大无比，占半个屏幕
Dot(color=RED, radius=6)

# ✅ radius=0.12 正常大小（默认 0.08）
Dot(color=RED, radius=0.12)
```

### 11. stroke_dasharray 已废弃

新版 Manim 不支持 `stroke_dasharray` 参数。用 `DashedLine` 代替虚线：

```python
# ❌ 报错
axes.plot(lambda x: x, stroke_dasharray=[6, 4])

# ✅ 用 DashedLine 或画实线
DashedLine(start, end, dash_length=0.1)
```

### 12. 题目/选项布局建议

高考题讲解的典型布局：

```python
# 1. 标题在顶部
title = Text("第 4 题", ...).to_edge(UP, buff=0.4).scale(0.6)

# 2. 题目居中
problem = VGroup(中文文本, MathTex公式, ...).arrange(RIGHT, buff=0.3)
problem.move_to(ORIGIN + UP * 0.3)

# 3. 选项在题目下方
options = VGroup(A选项, B选项, C选项, D选项).arrange(DOWN, aligned_edge=LEFT)
options.next_to(problem, DOWN, buff=0.5, aligned_edge=LEFT)

# 4. 需要一起移动时打包
all_text = VGroup(problem, options)
all_text.animate.move_to(ORIGIN)
```

---

## 辅助脚本

### combine.py — 视频+音频合成

```bash
& 'python' scripts/combine.py audio/ video.mp4 output.mp4
```

### timeline_to_manim.py — 时间轴转 Manim 注释

```bash
& 'python' scripts/timeline_to_manim.py audio/timeline.json
```

### gen_tts.py — TTS 生成 + 时间轴构建

```bash
& 'python' scripts/gen_tts.py script.txt audio/
```

---

## 完整示例

### 积分演示（`examples/integral_demo.py`）
- 坐标系绘制
- y=x² 曲线生长
- 黎曼矩形 4→8→16→32→64 逐步加密
- Δx 和 f(xᵢ) 标注
- 极限过程 n→∞
- 积分公式 ∫₀³ x² dx = 9
- 19 段 TTS 语音严格对齐

### 高考第4题（`examples/q4_tangent_v2.py`）
- 曲线 y=5x+8lnx 生长
- 分解展示对数+一次函数
- 切点脉冲高亮
- 导数公式 + 代入求斜率
- 切线绘制 + 点斜式 + 化简
- VGroup 打包移动
- 动态时间对齐（elapsed + wait_to）

### 效果展示（`examples/showcase.py`）
- 形状变形（圆→正方形→三角形）
- 函数 + 导数切线（ValueTracker）
- 黎曼和 → 积分
- 傅里叶级数叠加逼近方波

---

## 与 Remotion 的关系

| 场景 | 用什么 |
|------|--------|
| 数学教育视频（公式/函数/几何）| **Manim + TTS**（本 skill）|
| 通用视频（新闻/科普/产品）| Remotion + TTS |
| 数据可视化补充 | D3.js |
| 复杂时间线编排 | GSAP |

Manim 专为数学动画设计，LaTeX 公式、曲线生长、几何变换都是原生支持，代码量是手写 SVG 的 1/10。

---

## 动画设计原则（血泪教训）

> 以下原则来自 15 道高考数学题的实战经验和专业评价。违反任何一条都会显著降低视频质量。

### 核心原则：让动画自己讲数学

**动画不是配图，是论证。** 动画要承担推理任务，不是配合旁白展示。

```
错误：老师讲 → 动画展示 → 老师继续讲 → 动画继续动
正确：老师讲一句 → 动画证明一句 → 老师讲下一句 → 动画再证明一句
```

### 原则1：任何时刻，屏幕上只能有一个主角

3Blue1Brown 的核心原则。一次只强调一个元素，其他压暗或移除。

```
错误：题目 + 坐标系 + 推导 + 结论 同时出现
正确：题目 → FadeOut → 坐标系 → FadeOut → 推导 → FadeOut → 结论
```

### 原则2：所有「因此」都必须有视觉因果

```
错误：f'(x)=0 → 直接出答案
正确：f'(x)=0 → 箭头指向最高点 → 标注 → 答案
```

### 原则3：图缩小到边上，公式大字在另一边

展示图形时如果要讲公式，图缩小移到左侧，公式大字在右侧。

```
错误：公式直接闪现在图形上方
正确：图形缩小到左边 → 公式从右下方滑入
```

### 原则4：旧的走了新的来，不要叠加

每个 seg 结束时 FadeOut 自己的元素，下一个 seg 直接开始新内容。

```
错误：六个公式同时在屏幕上
正确：y=x² → FadeOut → y'=2x → FadeOut → 令y'=0 → FadeOut
```

### 原则5：3D 图要放大，细节要清晰

3D 几何体应该占满画面，不要缩在角落。

```
错误：小立方体 + 小公式挤在一起
正确：大立方体占满画面 + 大标注
```

### 原则6：曲线要从起点生长

所有曲线用 stroke-dashoffset 从起点画出，不要突然出现。

```
错误：曲线直接全部出现
正确：曲线从左到右一笔一笔画出来
```

### 原则7：单位圆是三角函数的标配

涉及特殊角的三角函数，必须用单位圆可视化。转到角度，标出坐标值。

```
错误：sin(7π/6) = sin150° = 1/2（纯文字）
正确：单位圆 → 转到150° → 标y坐标 = 1/2
```

### 原则8：动态参数展示关系

涉及参数变化的题（如直线斜率 k），应该滑动参数让观众看到变化。

```
错误：直接说"k≤0时相交"
正确：滑动k值 → 直线旋转 → 观众发现(0,2)始终在圆上
```

### 原则9：自我纠错要可视化

脚本里有「等等，这不对」的纠错过程，动画必须配合。

```
错误：静默跳过纠错过程
正确：算出0 → 红色X → 检查向量 → 重新算 → 算出1 → 绿色勾
```

### 原则10：配音不念计算过程

计算过程不用逐个念出来，简单说「代入求解」就行。

```
错误："4k减6的平方减4乘以1加k²乘以9大于等于0"（念了一堆公式）
正确："判别式大于等于零，化简得到k小于等于零"（简洁）
```

### 原则11：先设计再动手

写 TTS 文案和 Manim 代码之前，先想清楚：
- 每个 seg 的动画是什么
- 观众此刻应该看哪里
- 动画在证明什么

不要边写边想，更不要在视频里现推。

---

## 反思视频模板

见 `examples/reflection.py`（Remotion 版），展示错误做法 vs 改进做法的对比。
每个问题左右分屏：左边放当时实际的错误动画，右边放改进后的正确动画。

