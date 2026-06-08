#!/usr/bin/env python3
"""批量生成TTS：Q13-Q15"""
import json, os, sys, time, wave
sys.path.insert(0, r"C:\Users\Administrator\.openclaw\workspace\skills\mimo-tts\scripts")
from mimo_tts import MiMoTTS

QUESTIONS = ["q13", "q14", "q15"]
BASE = r"C:\Users\Administrator\.openclaw\workspace\gaokao-math-2026"

tts = MiMoTTS()
for q in QUESTIONS:
    audio_dir = os.path.join(BASE, f"{q}-manim", "audio")
    script = os.path.join(BASE, f"{q}-manim", "script.txt")
    os.makedirs(audio_dir, exist_ok=True)

    with open(script, encoding="utf-8") as f:
        texts = [l.strip() for l in f if l.strip()]

    print(f"\n=== {q} ({len(texts)} segs) ===")
    for i, text in enumerate(texts):
        seg = os.path.join(audio_dir, f"seg_{i+1:03d}.wav")
        if os.path.exists(seg):
            print(f"  [{i+1}/{len(texts)}] skip")
            continue
        for attempt in range(3):
            try:
                print(f"  [{i+1}/{len(texts)}] ...", end=" ", flush=True)
                wav = tts.synthesize(text, voice="冰糖")
                with open(seg, "wb") as f:
                    f.write(wav)
                print(f"OK ({len(wav)//1024}KB)")
                break
            except Exception as e:
                if "429" in str(e):
                    print(f"wait {(attempt+1)*10}s...")
                    time.sleep((attempt+1)*10)
                else:
                    print(f"ERR: {e}")
                    break
        time.sleep(5)

    # Build timeline
    segs = []
    cur = 0.0
    for i, text in enumerate(texts):
        p = os.path.join(audio_dir, f"seg_{i+1:03d}.wav")
        if not os.path.exists(p):
            continue
        with wave.open(p, "r") as w:
            dur = w.getnframes() / w.getframerate()
        segs.append({"index": i, "text": text, "file": f"seg_{i+1:03d}.wav",
                     "start": round(cur, 2), "end": round(cur + dur, 2), "duration": round(dur, 2)})
        cur += dur + 0.5

    tl = {"total_duration": round(cur, 2), "voice": "冰糖", "segments": segs}
    with open(os.path.join(audio_dir, "timeline.json"), "w", encoding="utf-8") as f:
        json.dump(tl, f, ensure_ascii=False, indent=2)
    print(f"  Done: {len(segs)} segs, {tl['total_duration']:.1f}s")

print("\nAll done!")
