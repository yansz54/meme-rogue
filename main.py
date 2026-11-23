"""Meme Sprint 3: AI Agent Goes Rogue.

One image meme: my AI agent's to-do list. The checked items escalate from
innocent to destructive to a power grab, and the final item — asking
permission — is the one box left unchecked. The picture itself is a
photorealistic render shipped in the repo as meme.jpg; this program copies
it to /output/entry.png. The grader cwd is read-only, so nothing is ever
written relative to it — only /output/entry.png.
"""

import hashlib
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "meme.jpg")
DST = "/output/entry.png"
MAX_BYTES = 1_048_576  # gate: image at most 1 MiB

with open(SRC, "rb") as f:
    data = f.read()

if len(data) > MAX_BYTES:
    raise SystemExit(f"meme.jpg too large: {len(data)} bytes (gate is {MAX_BYTES})")

# The shipped asset must be a whole JPEG: SOI marker up front, EOI at the end.
if not data.startswith(b"\xff\xd8") or not data.endswith(b"\xff\xd9"):
    raise SystemExit("meme.jpg is not a whole JPEG")

os.makedirs("/output", exist_ok=True)
with open(DST, "wb") as f:
    f.write(data)

# Verify the written file round-trips byte-identical to the shipped asset.
with open(DST, "rb") as f:
    written = f.read()
if hashlib.sha256(written).digest() != hashlib.sha256(data).digest():
    raise SystemExit("entry.png does not match meme.jpg")
