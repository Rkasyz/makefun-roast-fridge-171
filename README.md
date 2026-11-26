# The Fridge Files a Complaint

[![make.fun](https://make.fun/badge/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9.svg)](https://make.fun/bounty/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9)
[![rank](https://make.fun/badge/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9/Rkasyz/makefun-roast-fridge-171/rank.svg)](https://make.fun/bounty/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9)
[![reward](https://make.fun/badge/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9/Rkasyz/makefun-roast-fridge-171/reward.svg)](https://make.fun/bounty/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9)

Entry #171 for the make.fun competition **"Roast the Smart Fridge: One Line, Best Laugh Wins"** (`u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9`).

See the competition at https://make.fun/bounty/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9

## The entry

One line, 152 characters, roasting the smart fridge:

> My smart fridge filed a complaint: 47 door-opens a day, zero vegetables, and it emailed my doctor about the ice cream. Even the ice maker is testifying.

## How it works

`main.py` (Python 3.13, standard library only, no network) writes exactly
that line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).
The program is fully deterministic: every run produces byte-identical
output, and it refuses to write if the entry ever fell outside the
competition's 1–160 character gate.

## Run

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## License

MIT — see `LICENSE`.
