import pytest
import os
from conftest import _should_fail

def test_unit_always_passing_001():
    assert not _should_fail(), "Failure due to reason ODD"
    assert not _should_fail(), "Failure due to reason ODD"
    assert not _should_fail(), "Failure due to reason ODD"
    assert not _should_fail(), "Failure due to reason ODD"
