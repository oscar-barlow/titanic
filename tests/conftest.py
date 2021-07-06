from pathlib import Path

import pytest
import pandas as pd

@pytest.fixture
def titanic_data(titanic_test_data_path: Path) -> pd.DataFrame:
    return pd.read_csv(titanic_test_data_path, index_col='PassengerId')

@pytest.fixture
def titanic_test_data_path() -> Path:
    tests_dir_path = Path(__file__).parent
    return tests_dir_path.joinpath("fixtures/clean.csv")
