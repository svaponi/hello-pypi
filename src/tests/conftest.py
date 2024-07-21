import pytest

import hello


@pytest.fixture
def greeter():
    yield hello.Greeter()
