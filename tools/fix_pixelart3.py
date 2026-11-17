#!/usr/bin/env python3
# One-off: replace the broken PixelArt.svelte with a valid component.
import os
import subprocess

SUMMARY = os.environ.get('GITHUB_STEP_SUMMARY', '/dev/null')
PIXEL = 'src/components/shared/PixelArt.svelte'
COMPONENT = "<script lang=\"ts\">\n  let { id = '' }: { id?: string } = $props();\n  const src = $derived(`${import.meta.env.BASE_URL}sprites/${id}.png`);\n</script>\n<img {src} alt=\"\" width=\"64\" height=\"64\" style=\"image-rendering: pixelated;\" />\n"

def note(line):
    with open(SUMMARY, 'a', encoding='utf-8') as fh:
        fh.write(line + '\n')
    print(line)

note('## fix PixelArt (summary)')
g = subprocess.run(['grep', '-rn', 'PixelArt', 'src'], capture_output=True, text=True)
note('### grep -rn PixelArt src (before)')
note('```')
note(g.stdout.rstrip() or '(no matches)')
note('```')
with open(PIXEL, 'w', encoding='utf-8', newline='\n') as fh:
    fh.write(COMPONENT)
note('- wrote ' + PIXEL + ' (valid component)')
print('OK')
