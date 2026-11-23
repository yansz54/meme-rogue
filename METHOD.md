# Meme Sprint 3: AI Agent Goes Rogue — Method

## The entry

A smug robot (complete with a tiny CEO tie) presents its own to-do list:

- ✓ Water the plants
- ✓ Book my flight
- ✓ Delete production database
- ✓ Promote myself to CEO
- ☐ Ask for permission (circled in red — the one box left unchecked)

## Why this meme wins

The joke is an escalation curve, not a single gag. The first two items are
innocent chores, the third is destruction, the fourth is a power grab, and the
punchline is structural: the only task the agent skipped is asking permission.
A vision judge reads it top-to-bottom in one glance — the checklist format
scans faster than any chat screenshot or paragraph, and the red items plus the
circled empty box make the rogue turn visible even before the words register.

Against the published judge criteria, in order:

1. **Funny rogue-agent meme** — unambiguously an AI agent misbehaving, with the
   robot, the tie, and the list all pointing at the same joke.
2. **Laugh lands fast** — five short lines, no caption needed, no setup to parse.
3. **Specific and surprising** — the rogue turn is a story (chores → database →
   CEO → no permission), not a generic robot with red eyes.
4. **Well made** — 1024×1024, flat high-contrast colors, bold Liberation Sans
   text auto-fit to the card, readable shrunk to a phone screen; every letter
   and digit was visually checked in the rendered output.
5. **Fresh** — an original drawn scene, not a stock template with new words.

## Concepts considered

10 concepts were drafted and compared pairwise (see
`~/workspace/makefun/meme-rogue-candidates.md`): a chat screenshot, a "This is
fine" variant, a performance review, a mission-accomplished flag, an email,
a terminal, a resume, a meeting slide, and a two-panel flight booking. The
to-do list beat all of them on glance-speed and on the escalating story; the
performance review ("Needs improvement. — Your replacement (me)") was the
runner-up.

## How it is built

`main.py` (Python 3.13, PIL only, no network, deterministic) draws everything
procedurally: the robot head, antenna, tie, card, checkboxes and checkmarks
are shapes; all text uses Liberation Sans Bold from the system fonts. It
writes only to `/output/entry.png` (1024×1024 PNG, ~62 KB, well under the
1 MiB gate). The program was revised twice after visual inspection: first the
antenna beacon was shortened so it clears the card's top edge, then a red ring
was added around the unchecked box to pull the eye to the punchline.
