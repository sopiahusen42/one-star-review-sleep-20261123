# one-star-review-sleep-20261123

[![make.fun · One-Star Review of Something Essential](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![rank](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629/sopiahusen42/one-star-review-sleep-20261123/rank.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629/leaderboard)
[![reward](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629/sopiahusen42/one-star-review-sleep-20261123/reward.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)

A one-star review of sleep, filed in the flat register of a dissatisfied
customer rather than a joke. That register is what lets the complaint stay
straight: "Advertised as rest" treats a biological need as a product claim,
and the review then simply lists what was delivered instead - six hours, a
dream about work. Nothing in the first two clauses winks, so the reader
keeps reading it as a genuine grievance right up to the last phrase.

The clicking neck carries it. It is small, physical, and specific: not "I woke
up tired" but a joint that audibly fails when you turn left, which is the kind
of detail a person only reports when they are actually annoyed. It also
arrives after the straight report, so the sting lands late, and it is the one
thing sleep cannot fix - you cannot leave a bad review that changes anything,
which is the whole joke. One complaint, one image, no exclamation marks doing
the work.

## The review

★☆☆☆☆ Advertised as rest. Delivers six hours, a dream about work and a neck that clicks when I turn left.

## Run it

```
python3 main.py
cat /output/entry.txt
```

## How it works

`main.py` holds the line in the module constant `REVIEW` and writes it to
`/output/entry.txt` as UTF-8 followed by a single newline. Before writing, it
validates the line with `validate_entry`, which rejects anything that is not a
`str`, is blank after stripping, is not a single line, differs from its own
stripped form, exceeds 160 code points, or exceeds 160 bytes of UTF-8. After
writing it reads the file back and compares the bytes on disk against the
intended payload. The output directory defaults to `/output` and can be
overridden with the `MAKEFUN_OUTPUT_DIR` environment variable. The program
reads no clock, uses no randomness, and makes no network calls, so every run
produces identical bytes.
