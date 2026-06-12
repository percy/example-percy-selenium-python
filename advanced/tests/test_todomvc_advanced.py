"""PER-8195 Phase 1 — selenium-python advanced example.

Each test exercises one row of the Advanced Feature Matrix. See
../matrix.yml for the canonical mapping of test name -> matrix row.
"""

from percy import percy_snapshot
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from conftest import TEST_URL


def _seed(driver):
    driver.get(TEST_URL)
    driver.find_element(By.CLASS_NAME, "new-todo").send_keys("Walk the dog", Keys.ENTER)


def test_exercises_widths(driver):
    _seed(driver)
    percy_snapshot(driver, "TodoMVC Advanced > exercises widths", widths=[375, 768, 1280, 1920])


def test_exercises_min_height(driver):
    _seed(driver)
    percy_snapshot(driver, "TodoMVC Advanced > exercises minHeight", min_height=2000)


def test_exercises_enable_javascript(driver):
    _seed(driver)
    percy_snapshot(
        driver,
        "TodoMVC Advanced > exercises enableJavaScript",
        enable_javascript=True,
    )


def test_exercises_responsive_snapshot_capture(driver):
    _seed(driver)
    percy_snapshot(
        driver,
        "TodoMVC Advanced > exercises responsiveSnapshotCapture",
        responsive_snapshot_capture=True,
        widths=[375, 1280],
    )


def test_exercises_readiness_preset(driver):
    _seed(driver)
    percy_snapshot(
        driver,
        "TodoMVC Advanced > exercises readiness preset",
        readiness={"preset": "strict", "timeoutMs": 5000},
    )


def test_exercises_sync(driver):
    _seed(driver)
    percy_snapshot(driver, "TodoMVC Advanced > exercises sync option", sync=False)


def test_exercises_labels(driver):
    _seed(driver)
    percy_snapshot(driver, "TodoMVC Advanced > exercises labels", labels="smoke,sdk-selenium-py")


def test_exercises_test_case(driver):
    _seed(driver)
    percy_snapshot(
        driver,
        "TodoMVC Advanced > exercises testCase",
        test_case="todomvc-advanced-suite",
    )


def test_exercises_device_pixel_ratio(driver):
    _seed(driver)
    percy_snapshot(
        driver,
        "TodoMVC Advanced > exercises devicePixelRatio",
        device_pixel_ratio=2,
    )


def test_exercises_browsers(driver):
    _seed(driver)
    percy_snapshot(
        driver,
        "TodoMVC Advanced > exercises browsers override",
        browsers=["chrome", "firefox"],
    )


def test_exercises_snake_case_camelcase_dual_naming(driver):
    """percy-selenium accepts both snake_case (Pythonic) and camelCase aliases.
    Exercise both forms in a single snapshot to verify they coexist."""
    _seed(driver)
    percy_snapshot(
        driver,
        "TodoMVC Advanced > snake_case + camelCase dual naming",
        responsive_snapshot_capture=True,
        widths=[375, 1280],
        min_height=1024,
    )
