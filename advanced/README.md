# Advanced Percy + Selenium-Python example

This directory exercises the full applicable Percy SDK feature surface for `percy-selenium` (Python). See the basic example at the repo root for the minimum integration.

## What this example covers

A pytest suite (`tests/test_todomvc_advanced.py`) where each test exercises one row of the [Percy SDK Advanced Feature Matrix](../../../docs/advanced-example-feature-matrix.md). Global SDK config — readiness preset, default widths, percyCSS, discovery — lives in `.percy.yml`.

Note: `scope`, `domTransformation`, `regions`, `discovery` are marked `N/A` — not exposed in `percy-selenium` 2.1.2 kwargs surface.

## Run locally

```bash
cd advanced
make install                       # creates .venv, installs requirements.txt
export PERCY_TOKEN="<your token>"  # do NOT commit this
make test
```

To run without a real token (CI assertion mode):

```bash
make test-advanced-ci   # uses --testing + PERCY_TOKEN=fake_token + captures /test/requests
```

The CI variant asserts every matrix row appears in the captured POST bodies at the local `/test/requests` endpoint. No real Percy build is created.

## Coverage matrix

States: `Covered` / `N/A — <reason>` / `Planned` / `Deprecated`. Source of truth is [`matrix.yml`](./matrix.yml).

| Feature | State | Test |
|---|---|---|
| widths | Covered | `test_exercises_widths` |
| minHeight (`min_height`) | Covered | `test_exercises_min_height` |
| enableJavaScript (`enable_javascript`) | Covered | `test_exercises_enable_javascript` |
| responsiveSnapshotCapture (`responsive_snapshot_capture`) | Covered | `test_exercises_responsive_snapshot_capture` |
| readiness preset | Covered | `test_exercises_readiness_preset` |
| sync | Covered | `test_exercises_sync` |
| labels | Covered | `test_exercises_labels` |
| testCase (`test_case`) | Covered | `test_exercises_test_case` |
| devicePixelRatio (`device_pixel_ratio`) | Covered | `test_exercises_device_pixel_ratio` |
| browsers override | Covered | `test_exercises_browsers` |
| snake_case + camelCase dual naming | Covered | `test_exercises_snake_case_camelcase_dual_naming` |
| percyCSS | Covered | global via `.percy.yml` |
| cross-origin iframe handling | Covered | automatic via `percy-selenium >= 2.1.2` |
| `.percy.yml` global config | Covered | `.percy.yml` consumed at build start |
| environment info reporting | Covered | automatic via `percy-selenium` client info |
| PERCY_SERVER_ADDRESS via env | Covered | CI advanced job picks up `PERCY_SERVER_ADDRESS` |
| `disable_shadow_dom` | Planned | — |
| `enable_layout` | Planned | — |
| `scope` | N/A | Not exposed in SDK 2.1.2 |
| `domTransformation` | N/A | Not exposed in SDK 2.1.2 |
| `regions` per-snapshot | N/A | `create_region` is Automate-only |
| `discovery` per-snapshot | N/A | discovery is per-build only |
