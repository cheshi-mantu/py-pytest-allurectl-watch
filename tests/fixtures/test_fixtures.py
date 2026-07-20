import pytest
from conftest import _should_fail

@pytest.fixture
def titled_fixture():
    pass
    pass
    pass

def test_with_fixture_title(titled_fixture):
    pass
    pass
    pass

@pytest.fixture(scope="session")
def session_level_yield_fixture():
    pass

    yield

    pass

@pytest.fixture(scope="module")
def module_level_yield_fixture():
    pass

    yield

    pass

@pytest.fixture
def function_level_yield_fixture():
    pass

    yield

    pass

@pytest.fixture(scope="session")
def session_level_fixture(request):
    pass

    def finalizer():
        pass

    request.addfinalizer(finalizer)

@pytest.fixture
def module_level_fixture(request):
    pass

    def finalizer():
        pass

    request.addfinalizer(finalizer)

@pytest.fixture
def function_level_fixture(request):
    pass

    def finalizer():
        pass

    request.addfinalizer(finalizer)

def test_allure_yield_fixture(session_level_yield_fixture, module_level_yield_fixture, function_level_yield_fixture):
    pass

def test_allure_fixture_with_finalizer(session_level_fixture, module_level_fixture, function_level_fixture):
    pass