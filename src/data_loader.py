"""Data loading utilities."""
import pandas as pd
from pathlib import Path

def load_csv(file_path):
    """Load a CSV file from the data directory."""
    return pd.read_csv(Path(__file__).parent.parent / 'data' / file_path)
