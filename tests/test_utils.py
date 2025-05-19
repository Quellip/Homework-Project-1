import pandas as pd
from unittest.mock import patch
import pytest
from src.utils import read_excel, time_of_day, reports_result


def test_read_excel(data):
    expected_df = pd.DataFrame(data)
    with patch("pandas.read_excel", return_value=expected_df) as mock_read_excel:
        result_df = read_excel("example.xlsx")
        mock_read_excel.assert_called_once_with("example.xlsx")
        pd.testing.assert_frame_equal(result_df, expected_df)


@pytest.mark.parametrize(
    "date, expected",
    [
        ("2021-10-12 15:13:10", "Добрый день"),
        ("2021-10-12 02:25:30", "Доброй ночи"),
        ("2021-10-12 10:20:20", "Доброе утро"),
        ("2021-10-12 20:58:16", "Добрый вечер"),
    ],
)
def test_time_of_day(date, expected):
    assert time_of_day(date) == expected


@reports_result("test_results.txt")
def sample_function(x, y):
    return x + y
