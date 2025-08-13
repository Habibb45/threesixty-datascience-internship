
from typing import Tuple
import pandas as pd
import numpy as np

def attendance_rate(att_df: pd.DataFrame, sessions_df: pd.DataFrame) -> float:
    if att_df.empty or sessions_df.empty:
        return np.nan
    attended = (att_df['status'] == 'attended').sum()
    capacity = sessions_df['capacity'].fillna(0).sum()
    return attended / capacity if capacity else np.nan

def no_show_rate(att_df: pd.DataFrame) -> float:
    if att_df.empty:
        return np.nan
    no_shows = (att_df['status'] == 'no_show').sum()
    total = len(att_df)
    return no_shows / total if total else np.nan

def avg_dwell_minutes(att_df: pd.DataFrame) -> float:
    if att_df.empty:
        return np.nan
    t1 = pd.to_datetime(att_df['checkin_time'], errors='coerce')
    t2 = pd.to_datetime(att_df['checkout_time'], errors='coerce')
    dwell = (t2 - t1).dt.total_seconds() / 60.0
    return float(dwell.mean(skipna=True))
