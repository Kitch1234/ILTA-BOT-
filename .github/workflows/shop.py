```python
from card_generator import create_lol_card

class CardShop:
    def __init__(self):
        self.inventory = {
            "Yasuo": {"price": 100, "skins": [0, 1]},
            "Ahri": {"price": 80, "skins": [0]},
            "Jinx": {"price": 120, "skins": [0, 5]},
        }
    
    def buy_card(self, champion_name: str, skin_num: int = 0):
        if champion_name in self.inventory:
            print(f"Куплена карточка {champion_name}!")
            return create_lol_card(champion_name, skin_num)
        else:
            print("Такого чемпиона нет в магазине!")
            return None

# Пример использования
if __name__ == "__main__":
    shop = CardShop()
    shop.buy_card("Yasuo")
