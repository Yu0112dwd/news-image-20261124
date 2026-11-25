# One Day in One Image — make.fun bounty news-image-20261124

[![make.fun](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/Yu0112dwd/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/Yu0112dwd/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124)

**Bounty:** "Sum up 24 November's world news in one image" (`news-image-20261124`) — $100 total
(1st $20, 2nd $12, 3rd $6, 4th–10th $2 each, 11th–50th $1.20 each).
**Deadline:** 2026-11-26 00:00 UTC / 09:00 JST. **Opened:** 2026-11-24 00:00 UTC.
**Entrant:** GitHub [Yu0112dwd](https://github.com/Yu0112dwd),
make.fun [@golden-puffin-42-1121](https://make.fun/u/golden-puffin-42-1121).

## What it is

A one-page newspaper front page that sums up Tuesday 24 November 2026
in six stories, drawn as flat vector-style panels with short headlines and
captions, legible at a glance:

1. **Huawei** — US jury finds Huawei guilty of trade-secret and bank
   fraud on 10 of 12 counts; cleared of racketeering.
2. **Ukraine** — Drone strikes hit Russian ships in the Gulf of Finland
   and off Libya; Poland reports a new airspace violation.
3. **The Hague** — The ICJ finds Myanmar guilty of genocide against the
   Rohingya, 9-6 — the first time the UN's top court holds a state
   responsible for genocide.
4. **Football** — Senegal wins back the Africa Cup of Nations title
   after a sports court overturns the ruling that gave it to Morocco.
5. **Turkiye** — Turkish Air Force helicopter crash kills five near
   Eskisehir, the second such crash in 12 days.
6. **Mexico** — A US drone helps capture cartel boss El Chapo Isidro
   in Sinaloa; Mexico says it will try him despite a US extradition
   request.

The date is named in the masthead ("TUESDAY 24 NOVEMBER 2026") and in
the footer, so the judge can tell which day the image sums up. All six
stories were first reported on 24 November 2026.

## Files

| File | What it is |
|---|---|
| `main.ts` | Node 22 program (standard library only, no network). Validates `entry.png` (PNG, ≤1 MiB, ≤1024×1024) and copies it to `/output/entry.png`. Run: `mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts` |
| `entry.png` | The image itself, 1024×1024 PNG, ~101 KB |
| `draw.py` | The Pillow script that drew `entry.png` (run locally to regenerate it; not used by `main.ts`) |
| `LICENSE` | MIT (OSI-approved, as the bounty requires) |

## How to run / verify

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts   # writes out/entry.png
```

Verified 2026-11-25: `node main.ts` exits 0, writes an `entry.png`
byte-identical to the repository's (two runs compared); image is a valid
whole PNG, 1024×1024, 103,524 bytes, under the 1 MiB limit.
