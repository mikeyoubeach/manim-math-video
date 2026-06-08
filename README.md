# Manim Math Video - AI数学动画视频制作引擎

> 用 Manim + TTS 制作数学教育视频的完整工具链。支持子Agent并行制作、动态时间对齐、LaTeX公式渲染、3D几何体、曲线生长动画。

## 效果展示

| 效果 | 说明 |
|------|------|
| 曲线生长 | 函数图像从起点一笔一笔画出 |
| 形状变形 | 圆→正方形→三角形 Transform |
| 黎曼和→积分 | 矩形逐步加密→平滑面积 |
| 傅里叶叠加 | 正弦波逐个叠加逼近方波 |
| 导数切线 | 切点移动+切线跟随 |
| 3D几何体 | 正方体、四面体、马鞍面 |

## 快速开始

### 环境要求

```bash
pip install manim          # Manim Community Edition
winget install MiKTeX.MiKTeX  # LaTeX 渲染引擎（Windows）
# 或 apt install texlive-full  # Linux
```

### 1. 写文案

```text
来看第一题，中位数。
样本数据是6、8、4、5、12。
从小到大排列：4、5、6、8、12。
最中间那个是6，所以中位数是6。
```

### 2. 生成TTS

```bash
python scripts/gen_tts.py script.txt audio/ --voice 冰糖
```

输出 `audio/timeline.json` + `audio/segment_001~N.wav`

### 3. 写Manim动画

```python
from manim import *

T = [0.0, 2.7, 5.8, 11.3, 16.9, 18.5, 23.2, 26.5, 29.0, 30.4, 35.6, 39.3, 41.7]

class Q01(Scene):
    def construct(self):
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

        # seg 0: 标题
        title = Text("第 1 题", font_size=56)
        play_anim(0, FadeIn(title), run_time=0.8)
        wait_to(1)
        play_anim(1, FadeOut(title), run_time=0.3)

        # seg 1: 题目
        problem = Text("中位数 = 排序后正中间的数", font_size=30)
        play_anim(1, FadeIn(problem), run_time=0.8)
        wait_to(2)
        # ... 依此类推
```

### 4. 渲染

```bash
# 低清预览
manim -pql q01.py Q01

# 高清渲染
manim -pqh q01.py Q01
```

### 5. 合成音频

```bash
python scripts/combine.py audio/ media/videos/Q01/1080p30/Q01.mp4 output.mp4
```

## 动画设计原则

> 来自 15+ 道高考数学题的实战经验和专业评价。

1. **动画是论证，不是配图** — 动画要证明老师说的话
2. **屏幕只能有一个主角** — 一次只强调一个元素
3. **因此要有视觉因果** — f'(x)=0 → 箭头指向最高点
4. **图缩小到边上，公式在另一边**
5. **旧的走了新的来** — FadeOut旧元素，FadeIn新元素
6. **3D图要放大** — 占满画面
7. **曲线从起点生长** — 用 Create()
8. **单位圆是三角函数标配**
9. **动态参数展示关系** — 滑动参数让观众看到变化
10. **自我纠错要可视化** — 红✗→检查→绿✓
11. **配音不念计算过程** — 简洁
12. **先设计再动手**

## 子Agent并行制作

适用于批量制作多个视频。每个子Agent拿到：
- 共享上下文（AGENT_CONTEXT.md）
- 具体题目+TTS时间轴
- 渲染+合音命令

```
主Agent → 派5个子Agent并行
  ├─ Agent 1: Q1-Q3
  ├─ Agent 2: Q4-Q6
  ├─ Agent 3: Q7-Q9
  ├─ Agent 4: Q10-Q12
  └─ Agent 5: Q13-Q15
```

## 目录结构

```
manim-math-video/
├── SKILL.md              # 完整文档（流程/原则/踩坑）
├── scripts/
│   ├── gen_tts.py        # TTS生成 + 时间轴构建
│   ├── combine.py        # 视频+音频合成
│   └── timeline_to_manim.py  # 时间轴转Manim注释
├── examples/
│   ├── integral_demo.py  # 积分演示
│   └── showcase.py       # 效果展示混剪
└── README.md
```

## 依赖

- [Manim Community](https://www.manim.community/) — 数学动画引擎
- [MiMo TTS](https://github.com/xiaomi/mimo) — 语音合成
- [MiKTeX](https://miktex.org/) 或 [TeX Live](https://tug.org/texlive/) — LaTeX
- [FFmpeg](https://ffmpeg.org/) — 音视频合成

## License

MIT
