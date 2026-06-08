# 高考数学视频制作 - Agent 共享上下文

## 你的任务
为指定的高考数学题制作 Manim 动画视频。

## 技术栈
- Manim (Community版) + MiMo TTS 冰糖语音
- Python: `C:\ProgramData\Miniconda3\python.exe`
- MiKTeX PATH: `$env:PATH += ";$env:LOCALAPPDATA\Programs\MiKTeX\miktex\bin\x64"`
- 渲染: `manim -pqh qXX.py QXX`
- 合音: `C:\Users\Administrator\.openclaw\workspace\skills\manim-math-video\scripts\combine.py`

## 白色主题配色
```python
BG = "#FFFFFF"
TXT = "#2D3436"
DIM = "#B2BEC3"
BLUE = "#4fc3f7"
GREEN = "#00B894"
AMBER = "#e8a87c"
PINK = "#FF6B9D"
CORAL = "#c97b5d"
```

## 动态时间对齐（必须用）
```python
T = [...]  # 从 timeline.json 提取

elapsed = 0.0
def wait_to(seg_idx):
    nonlocal elapsed
    if seg_idx >= len(T): return
    gap = T[seg_idx] - elapsed
    if gap > 0.05: self.wait(gap); elapsed += gap

def play_anim(seg_idx, *args, **kwargs):
    nonlocal elapsed
    self.play(*args, **kwargs)
    elapsed += kwargs.get("run_time", 1.0)
```

## 元素生命周期（必须遵守）
每个 seg 结束时 FadeOut 自己的元素：
```python
# seg 5: 显示某个公式
formula = MathTex(r"x = 2", font_size=36, color=GREEN)
play_anim(5, FadeIn(formula, shift=UP * 0.2), run_time=0.8)
wait_to(6)
play_anim(6, FadeOut(formula), run_time=0.3)  # 结束时清掉

# seg 6: 新内容
new_thing = Text("下一步...", ...)
play_anim(6, FadeIn(new_thing), run_time=0.8)
```

## 11 条动画设计原则

1. **动画是论证，不是配图** — 动画要证明老师说的话
2. **屏幕只能有一个主角** — 一次只强调一个元素
3. **因此要有视觉因果** — f'(x)=0 → 箭头指向最高点 → 答案
4. **图缩小到边上，公式在另一边** — 不要叠在一起
5. **旧的走了新的来** — FadeOut 旧的，FadeIn 新的
6. **3D图要放大** — 占满画面
7. **曲线从起点生长** — 用 Create() 或 stroke-dashoffset
8. **单位圆是三角函数标配** — 转角度，标坐标
9. **动态参数展示关系** — 滑动参数让观众看到变化
10. **自我纠错要可视化** — 红✗ → 检查 → 绿✓
11. **配音不念计算过程** — 简洁

## 中文注意事项
- 中文用 `Text("中文", font="Microsoft YaHei", font_size=30)`
- 数学公式用 `MathTex(r"x^2 + 1", font_size=36)`
- **MathTex 里不能写中文！**

## 每道题的工作流
1. 读取 `audio/timeline.json` 获取 T 数组
2. 写 Manim 脚本（遵循上述原则）
3. 渲染: `manim -pqh qXX.py QXX`
4. 合音: `python combine.py audio/ media/videos/QXX/1080p30/QXX.mp4 output.mp4`
5. 输出路径: `C:\Users\Administrator\.openclaw\workspace\gaokao-math-2026\qXX-manim\qXX_final.mp4`
