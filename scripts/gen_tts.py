#!/usr/bin/env python3
"""
TTS 生成 + 时间轴构建
读取文案文件，生成 TTS 音频，自动构建 timeline.json。

用法: python gen_tts.py <script.txt> <output_dir> [--voice 冰糖] [--gap 0.5]
"""
import json, os, sys, time, wave
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "mimo-tts", "scripts"))
from mimo_tts import MiMoTTS

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("script", help="文案文件路径")
    parser.add_argument("output", help="输出目录")
    parser.add_argument("--voice", default="冰糖", help="音色")
    parser.add_argument("--gap", type=float, default=0.5, help="每段之间静音秒数")
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)

    with open(args.script, encoding="utf-8") as f:
        texts = [line.strip() for line in f if line.strip()]

    print(f"文案: {len(texts)} 段, 音色: {args.voice}")

    tts = MiMoTTS()
    for i, text in enumerate(texts):
        seg_file = os.path.join(args.output, f"segment_{i+1:03d}.wav")
        if os.path.exists(seg_file):
            print(f"  [{i+1}/{len(texts)}] 已存在，跳过")
            continue
        for attempt in range(3):
            try:
                print(f"  [{i+1}/{len(texts)}] ...", end=" ", flush=True)
                wav = tts.synthesize(text, voice=args.voice)
                with open(seg_file, "wb") as f:
                    f.write(wav)
                print(f"OK ({len(wav)//1024}KB)")
                break
            except Exception as e:
                if "429" in str(e):
                    wait = 10 * (attempt + 1)
                    print(f"⏳ 限流，等{wait}s...")
                    time.sleep(wait)
                else:
                    print(f"❌ {e}")
                    break
        time.sleep(5)

    # Build timeline
    segments = []
    current = 0.0
    for i, text in enumerate(texts):
        p = os.path.join(args.output, f"segment_{i+1:03d}.wav")
        if not os.path.exists(p):
            continue
        with wave.open(p, "r") as w:
            dur = w.getnframes() / w.getframerate()
        segments.append({
            "index": i, "text": text, "file": f"segment_{i+1:03d}.wav",
            "start": round(current, 2), "end": round(current + dur, 2),
            "duration": round(dur, 2),
        })
        current += dur + args.gap

    timeline = {
        "total_duration": round(current, 2),
        "voice": args.voice,
        "segments": segments,
    }
    out_path = os.path.join(args.output, "timeline.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(timeline, f, ensure_ascii=False, indent=2)

    print(f"\n✅ 完成: {len(segments)} 段, {timeline['total_duration']:.1f}s")
    print(f"   时间轴: {out_path}")

if __name__ == "__main__":
    main()

