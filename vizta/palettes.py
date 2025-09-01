"""Plotting color palettes"""

from seaborn import palettes

# Add new color palettes here:
VIZTA_PALETTES = {
    "talusbio": ["#0086bb", "#ee8156", "#66c2a5", "#eb98b9", "#fed766"],
    "wfondrie": ["#01BCA3", "#404040"],
}

# Register palettes:
for name, colors in VIZTA_PALETTES.items():
    palettes.SEABORN_PALETTES[name] = colors
