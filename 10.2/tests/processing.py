import pytest
from src.processing import filter_by_state, sort_by_date

@pytest.fixture
def sample_data():
    return [
        {"state": "active", "date": "2023-01-01"},
        {"state": "inactive", "date": "2023-01-02"},
       {"state": "active", "date": "2023-01-03"},
   ]

def test_filter_by_state(sample_data):
    assert filter_by_state(sample_data, "active") == [
        {"state": "active", "date": "2023-01-01"},
        {"state": "active", "date": "2023-01-03"},
    ]

def test_sort_by_date(sample_data):
    assert sort_by_date(sample_data) == [
        {"state": "active", "date": "2023-01-03"},
        {"state": "inactive", "date": "2023-01-02"},
        {"state": "active", "date": "2023-01-01"},
    ]
