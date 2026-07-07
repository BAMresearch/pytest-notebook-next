import sys

import pytest

from pytest_notebook_next.nb_regression import NBRegressionFixture
from pytest_notebook_next.utils import autodoc


@pytest.mark.skipif(
    sys.version_info.minor >= 9, reason="Evaluates type annotations differently"
)
def test_autodoc(file_regression):
    new_class = autodoc(NBRegressionFixture)
    file_regression.check(new_class.__doc__)
