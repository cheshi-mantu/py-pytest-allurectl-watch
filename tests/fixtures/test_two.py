from conftest import _should_fail

def test_failing():
    assert not _should_fail(), "Failure due to reason ODD"

def test_failing_strings():
    assert not _should_fail(), "Failure due to reason ODD"

def test_failing_strings():
    assert not _should_fail(), "Failure due to reason ODD"