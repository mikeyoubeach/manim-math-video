#!/usr/bin/env python3
"""
视频 + TTS 音频合成脚本（v2: 拼接代替混音，避免音量忽大忽小）
用法: python combine.py <audio_dir> <video_in> <video_out>
"""
import json, subprocess, os, sys, wave, struct, tempfile

def main():
    if len(sys.argv) < 4:
        print("用法: python combine.py <audio_dir> <video_in> <video_out>")
        sys.exit(1)

    audio_dir = sys.argv[1]
    video_in = sys.argv[2]
    video_out = sys.argv[3]

    timeline_path = os.path.join(audio_dir, "timeline.json")
    if not os.path.exists(timeline_path):
        print(f"找不到 {timeline_path}")
        sys.exit(1)

    with open(timeline_path, encoding="utf-8") as f:
        tl = json.load(f)

    segs = tl["segments"]
    total_dur = tl["total_duration"]
    print(f"TTS: {len(segs)} 段, {total_dur:.1f}s")

    # Step 1: 把所有 TTS 片段拼成一个完整的 WAV（中间补静音）
    # 读取第一个 WAV 获取参数
    first_wav = os.path.join(audio_dir, segs[0]["file"])
    with wave.open(first_wav, "r") as w:
        params = w.getparams()
        framerate = w.getframerate()
        sampwidth = w.getsampwidth()
        nchannels = w.getnchannels()

    # 生成完整音频（静音 + 各段语音）
    total_frames = int(total_dur * framerate) + framerate  # +1s buffer
    silence = b"\x00" * (sampwidth * nchannels)
    all_audio = bytearray(total_frames * sampwidth * nchannels)

    for seg in segs:
        wav_path = os.path.join(audio_dir, seg["file"])
        if not os.path.exists(wav_path):
            print(f"⚠️ 缺失: {wav_path}")
            continue
        with wave.open(wav_path, "r") as w:
            frames = w.readframes(w.getnframes())
        start_frame = int(seg["start"] * framerate)
        byte_offset = start_frame * sampwidth * nchannels
        all_audio[byte_offset:byte_offset + len(frames)] = frames

    # 写入临时 WAV
    tmp_wav = os.path.join(audio_dir, "_combined.wav")
    with wave.open(tmp_wav, "w") as w:
        w.setparams(params._replace(nframes=total_frames))
        w.writeframes(bytes(all_audio))

    print(f"拼接音频: {tmp_wav} ({os.path.getsize(tmp_wav)/(1024*1024):.1f}MB)")

    # Step 2: 合并视频 + 音频
    cmd = [
        "ffmpeg", "-y",
        "-i", video_in,
        "-i", tmp_wav,
        "-map", "0:v", "-map", "1:a",
        "-c:v", "copy",
        "-c:a", "aac", "-b:a", "128k",
        "-shortest",
        video_out,
    ]

    print("合成中...")
    r = subprocess.run(cmd, capture_output=True, timeout=300)
    if r.returncode != 0:
        err = r.stderr.decode("utf-8", errors="replace")[-300:]
        print(f"❌ FFmpeg 错误: {err}")
        sys.exit(1)

    # 清理临时文件
    os.remove(tmp_wav)

    sz = os.path.getsize(video_out) / (1024 * 1024)
    print(f"✅ 完成: {video_out} ({sz:.1f} MB)")

if __name__ == "__main__":
    main()

