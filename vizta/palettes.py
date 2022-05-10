"""Plotting color palettes"""


def talusbio(n_colors=4):
    """A Talus Bioscience color palette.

    Parameters
    ----------
    n_colors : int
        The number of colors in the palette. This palette only reasonably
        support 4 colors.

    Returns
    -------
    tuple of str
        The HTML color codes for the palette.
    """
    colors = ["#308AAD", "#C8102E", "#96D8D8", "#B2EE79"]
    return tuple(colors[:n_colors])


def fondrie(n_colors=2):
    """Will Fondrie's personal color palette.

    Parameters
    ----------
    n_colors : int
        The number of colors in the palette. This palette only reasonably
        support 2 colors.


    Returns
    -------
    tuple of str
        The HTML color codes for the palette.
    """
    colors = ["#01BCA3", "#404040"]
    return tuple(colors[:n_colors])
