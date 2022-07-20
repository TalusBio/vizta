"""Plotly theme"""
import plotly.graph_objects as go
import plotly.io as pio


def plotly_vizta_theme():
    """Generates theme for x called 'talusbio'"""
    pio.templates["talusbio"] = go.layout.Template(
        layout={
            "title": {
                "font": {
                    "family": "Helvetica,Arial,sans-serif",
                    "size": 30,
                    "color": "#333",
                }
            },
            "font": {
                "family": "Helvetica,Arial,sans-serif",
                "size": 16,
                "color": "#333",
            },
            # Colorways
            "colorway": ["#308AAD", "#C8102E", "#96D8D8", "#B2EE79"],
        }
    )
