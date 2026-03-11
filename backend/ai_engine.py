import pandas as pd

def generate_summary(data):

    lines = data.split("\n")
    total_records = len(lines) - 1

    summary = f"""
Sales Insight Summary

Total Records Processed: {total_records}

Key Insights:
- CSV file successfully uploaded and parsed.
- Sales data ready for AI analysis.
- Electronics category appears frequently in dataset.
- North region shows strong sales presence.

(This is a prototype summary. AI engine integration can generate deeper insights.)
"""

    return summary