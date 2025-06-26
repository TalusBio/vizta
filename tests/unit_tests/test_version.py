"""Test that setuptools-scm is working correctly"""

import vizta


def test_version():
    """Check that the version is not None"""
    assert vizta.__version__ is not None
