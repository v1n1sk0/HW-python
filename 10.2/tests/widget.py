import pytest
from src.widget import mask_account_card
@pytest.mark.parametrize("input_data, expected", [
    ("card", "Masked card"),
    ("account", "Masked account"),
    ("invalid", "Error"),  # неверные данные
])
def test_mask_account_card(input_data, expected):
    assert mask_account_card(input_data) == expected
