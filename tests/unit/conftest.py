import os
import random
import allure
import pytest


def _should_fail() -> bool:
    mode = os.environ.get("TESTS_SUCCESS", "random")
    if mode == "always":
        return False
    if mode == "never":
        return True
    return random.random() < 0.1


def _fixtures_count() -> int:
    try:
        return int(os.environ.get("TESTS_FIXTURES_COUNT", "0"))
    except ValueError:
        return 0


def _make_fixture(index: int):
    @allure.title(f"Fixture {index}")
    @pytest.fixture
    def _fx():
        with allure.step(f"Setup step of fixture {index}"):
            pass

        yield

        with allure.step(f"Teardown step of fixture {index}"):
            pass

    return _fx


for _i in range(1, 1001):
    globals()[f"fx_{_i}"] = _make_fixture(_i)


@pytest.fixture(autouse=True)
def _layer():
    allure.dynamic.label("layer", "unit")


@pytest.fixture(autouse=True)
def _generated_fixtures(request):
    count = _fixtures_count()
    for i in range(1, count + 1):
        request.getfixturevalue(f"fx_{i}")
