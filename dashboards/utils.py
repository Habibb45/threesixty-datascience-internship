import pandas as pd

def format_dates(df, column):
    """Convert a column to datetime."""
    df[column] = pd.to_datetime(df[column], errors='coerce')
    return df

def percent_format(value, decimals=2):
    """Format a float as percentage string."""
    return f"{round(value*100, decimals)}%" if pd.notnull(value) else "N/A"
