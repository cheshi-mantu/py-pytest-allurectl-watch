import allure
import pytest
from conftest import _should_fail


@allure.feature("test results processing")
@allure.story("single api test")
@allure.title("Assert a tuple 001 and it will fail")
def test_unit_always_passing_001():
    with allure.step("Start stuff"):
        allure.global_attach("This is a global attachment", "text/plain")
        allure.global_error("This is a global error message")
        assert not _should_fail(), "Failure due to reason ODD"
    with allure.step("Click stuff"):
        assert not _should_fail(), "Failure due to reason ODD"
    with allure.step("Click stuff harder"):
        assert not _should_fail(), "Failure due to reason ODD"
    with allure.step("Czech stuff"):
        assert not _should_fail(), "Failure due to reason ODD"
    with allure.step("Check stuff"):
        assert not _should_fail(), "Failure due to reason ODD"
