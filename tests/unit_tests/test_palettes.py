"""Check that our palettes work"""


def test_vizta_first():
    """Test when importing vizta before seaborn"""
    import vizta
    import seaborn as sns

    sns.color_palette("talusbio")
    sns.color_palette("wfondrie")


def test_vizta_first():
    """Test when importing vizta before seaborn"""
    import seaborn as sns
    import vizta

    sns.color_palette("talusbio")
    sns.color_palette("wfondrie")
