#!/usr/bin/env python3
# One-off fix: remove the broken PixelArt.svelte and its unused imports.
import os
import sys

FILES = [
    "src/components/progression/MountainPath.svelte",
    "src/components/level/LevelIntro.svelte",
]
PIXEL = "src/components/shared/PixelArt.svelte"


def fail(msg):
    print("FAILED: " + msg)
    sys.exit(1)


for path in FILES:
    with open(path, encoding="utf-8", newline="") as fh:
        raw = fh.read()
    lines = raw.splitlines(keepends=True)
    kept = []
    removed = 0
    for line in lines:
        if "PixelArt" in line and "import" in line and "PixelArt.svelte" in line:
            removed += 1
            continue
        kept.append(line)
    if removed != 1:
        fail(path + ": expected 1 PixelArt import line, removed " + str(removed))
    out = "".join(kept)
    leftovers = [l for l in out.splitlines() if "PixelArt" in l]
    if leftovers:
        fail(path + ": PixelArt still referenced: " + repr(leftovers[:3]))
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(out)
    print("removed import from " + path)

for root, _dirs, names in os.walk("src"):
    for name in names:
        full = os.path.join(root, name)
        if full == PIXEL or full in FILES:
            continue
        if not name.endswith((".svelte", ".ts", ".js")):
            continue
        with open(full, encoding="utf-8", errors="ignore") as fh:
            if "PixelArt" in fh.read():
                fail("other file references PixelArt: " + full)

if not os.path.exists(PIXEL):
    fail(PIXEL + " does not exist")
os.remove(PIXEL)
print("deleted " + PIXEL)
print("OK")
