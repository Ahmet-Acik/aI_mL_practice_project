import unittest
from src.data_loader import load_csv
from pathlib import Path
import pandas as pd

class TestDataLoader(unittest.TestCase):
    def test_load_csv(self):
        # Create a dummy CSV in the data directory
        data_dir = Path(__file__).parent.parent / 'data'
        data_dir.mkdir(exist_ok=True)
        test_file = data_dir / 'test.csv'
        df = pd.DataFrame({'a': [1,2], 'b': [3,4]})
        df.to_csv(test_file, index=False)
        loaded = load_csv('test.csv')
        pd.testing.assert_frame_equal(loaded, df)
        test_file.unlink()

if __name__ == '__main__':
    unittest.main()
