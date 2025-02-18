import pytest
   from src.masks import get_mask_card_number, get_mask_account

   @pytest.mark.parametres("card_number, expected", [
       ("1234567812345678", "************5678"),
       ("1234-5678-1234-5678", "************5678"),
       ("123456", "******"),  # Нестандартный ввод
       ("", ""),              # Пустой ввод
   ])
   def test_get_mask_card_number(card_number, expected):
       assert get_mask_card_number(card_number) == expected

   @pytest.mark.parametres("account_number, expected", [
       ("1234567890", "**********"),  # Полный номер
       ("123", "***"),                  # Короткий номер
       ("", ""),                        # Пустой ввод
   ])
   def test_get_mask_account(account_number, expected):
       assert get_mask_account(account_number) == expected
