"""Test plotly theme"""
import pytest
import vizta


def test_plotly_styles():
    """Really just check that theme doesn't error"""
    vizta.plotly.plotly_vizta_theme()
    with pytest.raises(ValueError):
        vizta.mpl.set_theme(style="blah")
