"""Test matplotlib themes"""
import pytest
import vizta


def test_styles():
    """Really just check that they don't error"""
    vizta.mpl.set_theme(style="talusbio")
    vizta.mpl.set_theme(style="wfondrie")
    with pytest.raises(ValueError):
        vizta.mpl.set_theme(style="blah")


def test_contexts():
    """Test that contexts are working"""
    vizta.mpl.set_theme(context="talk")
    with pytest.raises(ValueError):
        vizta.mpl.set_theme(context="blah")


def test_font_scale():
    """Test the font_scale is working"""
    vizta.mpl.set_theme(font_scale=2)
    with pytest.raises(ValueError):
        vizta.mpl.set_theme(font_scale="blah")
