from petpy import gardner
import numpy as np


def test_gardner():
    rhob = gardner(2000)
    assert np.testing.assert_allclose(rhob,2073.09494543)
    