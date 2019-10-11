from pathlib import Path


this_location = Path(__file__)
root = this_location.parents[1]
data_path = root / "data"
raw_data_path = data_path / "raw"
processed_data_path = data_path / "processed"
