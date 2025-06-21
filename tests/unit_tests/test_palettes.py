"""Check that our palettes work"""


def test_vizta_first():
    """Test when importing vizta before seaborn"""
    import vizta  # noqa: F401
    import seaborn as sns

    sns.color_palette("talusbio")
    sns.color_palette("wfondrie")


def test_vizta_second():
    """Test when importing vizta after seaborn"""
    import seaborn as sns
    import vizta  # noqa: F401

    sns.color_palette("talusbio")
    sns.color_palette("wfondrie")
