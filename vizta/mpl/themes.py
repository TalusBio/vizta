"""Matplotlib Themes

New themes are defined at the bottom of this file.
"""

from dataclasses import dataclass
from typing import List, Tuple, Dict, Any, Optional, Union

import seaborn as sns

from .. import palettes  # Needed to edit seaborn palette dict # noqa: F401


def set_theme(
    context: Union[str, Dict] = "notebook",
    style: str = "talusbio",
    font_scale: float = 1,
) -> None:
    """Get the parameters that control the general style of the plots.

    This function can also be used as a context manager to temporarily
    alter the global defaults.

    Parameters
    ----------
    context : str or dict, optional
        The scaling parameters. Can be one of `paper` `notebook`, `talk`, or
        `poster`. See [seaborn.plotting_context][].
    style : str, optional
        The name of a preconfigured style. Currently either `talusbio` or
        `wfondrie`.
    font_scale : float, optional
        Separate scaling factor to independently scale the size of the font
        elements

    Returns
    -------
    primary_color : str
        The primary color for the plot elements.
    accent_color : str
        The accent color for the plot elements.

    """
    try:
        theme = VIZTA_STYLES[style]
    except KeyError as err:
        raise ValueError(f"Unrecognized style: '{style}'") from err

    sns.set_theme(
        context=context,
        palette=theme.palette,
        font_scale=font_scale,
        rc=theme.style_dict,
    )

    return theme.primary, theme.accent


@dataclass
class MplTheme:
    """A class for matplotlib themes.

    Parameters
    ----------
    palette : str, optional
        A vizta, seaborn, or matplotlib color palette.
    primary : str, optional
        The primary color
    accent : str, optional
        The accent color
    rc_params : dict, optional
        Update the style with matplotlib rc_params.
    """

    palette: Optional[str] = None
    primary: str = "#000000"
    accent: str = "#000000"
    rc_params: Optional[Dict[str, Any]] = None

    def __post_init__(self) -> None:
        """Initialize the MplThemeBase"""

        # The base style:
        self.style_dict = {
            "figure.facecolor": "white",
            "xtick.direction": "out",
            "ytick.direction": "out",
            "axes.axisbelow": True,
            "grid.linestyle": "-",
            "font.family": ["sans-serif"],
            "lines.solid_capstyle": "round",
            "patch.edgecolor": "w",
            "patch.force_edgecolor": True,
            "image.cmap": "viridis",
            "xtick.top": False,
            "ytick.right": False,
            "axes.facecolor": "white",
            "axes.spines.left": True,
            "axes.spines.bottom": True,
            "axes.spines.right": True,
            "axes.spines.top": True,
            "xtick.bottom": True,
            "ytick.left": True,
            "legend.frameon": False,
            # Colors:
            "axes.edgecolor": self.primary,
            "axes.labelcolor": self.primary,
            "text.color": self.primary,
            "xtick.color": self.primary,
            "ytick.color": self.primary,
        }

        if self.rc_params is not None:
            self.style_dict.update(self.rc_params)

    @property
    def palette(self) -> List[Tuple[float, float, float]]:  # noqa: F811
        """The color palette"""
        return self._palette

    @palette.setter
    def palette(self, pal: str) -> None:
        """Set the palette"""
        self._palette = sns.color_palette(pal)


# Themes defined by in vizta:
VIZTA_STYLES = {
    "talusbio": MplTheme(
        palette="talusbio",
        primary="#0C015B",
        accent="#64C0CA",
        rc_params={
            "font.family": "sans-serif",
            "font.sans-serif": ["Host Grotesk", "Arial", "Helvetica"],
        },
    ),
    "wfondrie": MplTheme(
        palette="wfondrie",
        primary="#404040",
        accent="#01BCA3",
        rc_params={"font.family": "sans-serif", "font.sans-serif": ["Roboto"]},
    ),
}
