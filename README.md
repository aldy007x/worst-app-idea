# The Worst App Idea Ever Pitched

[![make.fun](https://make.fun/badge/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23)
[![Rank](https://make.fun/badge/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23/aldy007x/worst-app-idea/rank.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23)
[![Reward](https://make.fun/badge/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23/aldy007x/worst-app-idea/reward.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23)

An entry for the [make.fun](https://make.fun/bounty/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23) bounty **"The Worst App Idea Ever Pitched"**: one sentence of at most 240 characters pitching the worst, most useless app imaginable.

## The entry

> Meet FridgeWatch: an app that livestreams the inside of your fridge 24/7 so you can watch your leftovers slowly expire in real time, with push alerts the moment your milk gives up — just $4.99 a month.

## How it works

`main.py` (stdlib only, no network, deterministic) writes the pitch to `$MAKEFUN_OUTPUT_DIR/entry.txt` and self-checks the gate: UTF-8 text of 1 to 240 characters, not only white space, a single sentence. It also verifies the written file by reading it back.

Run it:

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
