import sys
from pathlib import Path
import pandas as pd
import numpy as np

# Adding path to Python
project_directory = Path(__file__).resolve().parent.parent
sys.path.append(str(project_directory))

from app.services.insights.time_series_analyzer import BasicTimeSeriesAnalyzer

np.random.seed(0)
dates = pd.date_range('20210101', periods=100)
sample_series = pd.Series(np.random.randn(100), index=dates)

def test_calculate_mean() -> None:
    analyzer = BasicTimeSeriesAnalyzer(sample_series)
    mean = analyzer.calculate_mean()
    assert np.isclose(mean, sample_series.mean())

def test_calculate_standard_deviation() -> None:
    analyzer = BasicTimeSeriesAnalyzer(sample_series)
    std_dev = analyzer.calculate_standard_deviation()
    assert np.isclose(std_dev, sample_series.std())

def test_analyze_seasonality() -> None:
    analyzer = BasicTimeSeriesAnalyzer(sample_series, frequency=7)
    analyzer.analyze_seasonality()
    assert hasattr(analyzer, 'decomposition')

def test_analyze_cycles() -> None:
    analyzer = BasicTimeSeriesAnalyzer(sample_series, frequency=7)
    analyzer.analyze_cycles()
    assert hasattr(analyzer, 'decomposition')

def test_make_predictions() -> None:
    analyzer = BasicTimeSeriesAnalyzer(sample_series)
    prediction_horizon = 10
    analyzer.make_predictions(prediction_horizon)
    assert hasattr(analyzer, 'predictions')
    assert len(analyzer.predictions) == prediction_horizon