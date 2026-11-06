# Worked Example 1 — CSV Cleaner: before and after

## The problem

A client list exported from another tool arrived messy: extra spaces,
two duplicate rows, one completely empty row, and dates in three
different formats (06/11/2026, 2026-11-05, 05/11/2026).

## What was run

```bash
python3 scripts/csv_cleaner.py before_messy.csv after_clean.csv \
  --date-column date --date-format DMY
```

## The result (printed by the script)

```text
Rows read:        8
Empty rows dropped: 1
Duplicate rows dropped: 2
Rows written:     5
```

## What changed, row by row

| Before | After |
|---|---|
| `name ` (trailing space in header) | `name` |
| ` Alice Chen` (leading space) | `Alice Chen` |
| Alice Chen row appears twice | kept once |
| Bob Hartono row appears twice | kept once |
| One completely empty row | removed |
| Dates `06/11/2026`, `2026-11-05`, `05/11/2026` | all `YYYY-MM-DD` |
| ` Yogyakarta` (leading space) | `Yogyakarta` |

The original file (`before_messy.csv`) was never modified — the cleaned
data went into a new file (`after_clean.csv`). The sample files in this
folder are the real input and output of the command above.
