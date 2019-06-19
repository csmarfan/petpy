import pytest
import sys
import os

pytest.main(['--cov','petpy'])

#sys.path.append(os.getcwd())
#pytest.main(['petpy'])