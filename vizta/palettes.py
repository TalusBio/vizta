"""Plotting color palettes"""
import seaborn as sns

# Add new color palettes here:
VIZTA_PALETTES = {
    "talusbio": ["#308AAD", "#C8102E", "#96D8D8", "#B2EE79"],
    "wfondrie": ["#01BCA3", "#404040"],
}

# Register palettes:
for name, colors in VIZTA_PALETTES.items():
    sns.palettes.SEABORN_PALETTES[name] = colors
