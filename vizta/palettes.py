"""Plotting color palettes"""

from seaborn import palettes

# Add new color palettes here:
VIZTA_PALETTES = {
    "talusbio": ["#64C0CA", "#0086BB", "#0049BE", "#684AE1"],
    "wfondrie": ["#01BCA3", "#404040"],
}

# Register palettes:
for name, colors in VIZTA_PALETTES.items():
    palettes.SEABORN_PALETTES[name] = colors
