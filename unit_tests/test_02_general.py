import pandas as pd

from src.general import summary


def test_on_example():
    dataset = [2, 1, 4, 3, 1, 5, 3, 3, 4, 2, 1, 1, 3, 3, 4,
               5, 5, 4, 3, 2, 2, 1, 2, 1]
    summary_stats = summary(dataset)

    assert isinstance(summary_stats, pd.DataFrame)
    assert summary_stats.loc["count", 0] == len(dataset)
    assert summary_stats.loc["min", 0] == 1
    assert summary_stats.loc["max", 0] == 5
    assert round(summary_stats.loc["mean", 0]) == sum(dataset) / len(dataset)
    assert round(summary_stats.loc["std", 0], 2) == 1.37
    assert round(summary_stats.loc["25%", 0], 2) == 1.75
    assert round(summary_stats.loc["50%", 0], 2) == 3.00
    assert round(summary_stats.loc["75%", 0], 2) == 4.00
