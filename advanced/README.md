# Advanced Percy + Selenium-Python example — STUB

**Status:** Phase 1 stub. `matrix.yml` is populated based on `percy-selenium` (Python) research. Test code in `tests/advanced.py` is **not yet written**.

See the basic example at the repo root. See [`matrix.yml`](./matrix.yml) for the planned matrix-row coverage.

## What this example will cover

Each test will exercise one row of the matrix (widths, minHeight, enable_javascript, responsive_snapshot_capture, readiness preset, sync, percyCSS via `.percy.yml`, dual snake_case/camelCase kwarg naming).

Note: `scope`, `dom_transformation`, `regions`, `discovery` are marked `N/A` — not exposed in `percy-selenium` 2.1.2 kwargs surface.

## Run locally (once tests are written)

```bash
cd advanced
pip install -r requirements.txt
export PERCY_TOKEN="<your project token>"      # do NOT commit
npx @percy/cli exec -- python -m pytest tests/
```

## Coverage matrix

Source of truth: [`matrix.yml`](./matrix.yml).

> Phase 1 stub: most rows are currently `Planned`. Basic example has three bare `percy_snapshot(browser, name)` calls. `tests/readiness.py` in the existing example already exercises readiness preset variants.
