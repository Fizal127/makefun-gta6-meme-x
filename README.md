# Sick Day in Leonida — GTA 6 meme on X

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/Fizal127/makefun-gta6-meme-x/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/Fizal127/makefun-gta6-meme-x/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

Entry for the make.fun bounty **gta6-meme-x-01** ("Post a GTA 6 meme on X", $500
shared by the top 50).

## The joke

GTA 6 launched and suddenly the whole office called in sick. The boss asks why
everyone is sick today — meanwhile the make.fun ghost is on the couch,
controller in hand, playing GTA VI in Leonida. "Must be something in the
Leonida air."

## The meme

`meme.png` (1600×1600 PNG) was drawn by hand in this session with a Python/PIL
program (`make_meme.py`): a Vice City synthwave sunset, a TV showing GTA VI in
Leonida, and make.fun's ghost mascot — cut out of the official press-kit mark
(https://make.fun/press/mark-1024.png) — gaming on a couch, controller in
hand. The picture carries make.fun's mascot and its name, and the caption sells
make.fun in the meme's own voice.

![Sick Day in Leonida — everyone called in sick today](meme.png)

## The post

The meme is posted on X from the public account @Fizalnub. The post's exact
text is in `POST.txt`: it carries the make.fun bounty link, a tag of
@makefunai, and the account's play code. `POST.json` names the post's address;
`main.ts` copies it to `/output/POST.json` for the gate. Nothing the program
writes is judged — the house reads the post itself from X.

Note: `POST.json` holds a placeholder address until the meme is posted; it is
replaced with the real post URL before submitting.

## Run it locally

    mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

`out/POST.json` is then byte for byte this directory's `POST.json`.

## Files

- `meme.png` — the meme (the post's first picture)
- `make_meme.py` — the program that drew it
- `POST.txt` — the post's exact text (caption)
- `POST.json` — the post's address on X
- `main.ts` — copies POST.json to /output
- `LICENSE` — MIT
