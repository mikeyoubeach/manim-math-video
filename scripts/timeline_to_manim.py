#!/usr/bin/env python3
"""
TTS timeline → Manim 时间轴注释
读取 timeline.json，输出每段语音的起止时间 + 建议的动画窗口。
直接复制到 Manim 代码里当注释。

用法: python timeline_to_manim.py <timeline.json>
"""
import json, sys

def main():
    if len(sys.argv) < 2:
        print("用法: python timeline_to_manim.py <timeline.json>")
        sys.exit(1)

    with open(sys.argv[1], encoding="utf-8") as f:
        tl = json.load(f)

    segs = tl["segments"]
    print(f"# Manim 时间轴注释（共 {len(segs)} 段, {tl['total_duration']:.1f}s）")
    print(f"# 原则：动画在语音窗口内完成，wait 填充到下一段开始")
    print()

    for i, s in enumerate(segs):
        start = s["start"]
        end = s["end"]
        dur = s["duration"]
        text = s["text"]

        # 计算建议动画窗口（语音开始后 0.3s 启动，留 0.5s 给 wait）
        anim_start = start
        anim_end = min(end - 0.3, start + dur * 0.7)
        anim_dur = max(anim_end - anim_start, 0.5)

        # 下一段开始时间
        next_start = segs[i + 1]["start"] if i + 1 < len(segs) else tl["total_duration"]
        wait_after = next_start - end

        print(f"# [{start:5.1f}s - {end:5.1f}s] ({dur:.1f}s) {text}")
        print(f"#   动画窗口: {anim_start:.1f}s ~ {anim_end:.1f}s (run_time={anim_dur:.1f}s)")
        if wait_after > 0.1:
            print(f"#   wait: {wait_after:.1f}s (到下一段)")
        print()

if __name__ == "__main__":
    main()

