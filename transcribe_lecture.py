from faster_whisper import WhisperModel

VIDEO = "e98e5fbe-cf5e-45bb-9b27-ab47005220b3-70ac36d0-273c-4fac-8ffc-ab470057e751.mp4"
OUT = "lecture_transcript.txt"

model = WhisperModel("base.en", device="cpu", compute_type="int8")
segments, info = model.transcribe(VIDEO, beam_size=5, vad_filter=True)

print(f"Duration: {info.duration:.0f}s")
with open(OUT, "w") as f:
    for seg in segments:
        line = f"[{seg.start:7.1f}s] {seg.text.strip()}"
        f.write(line + "\n")
        print(line, flush=True)
print("Done ->", OUT)
