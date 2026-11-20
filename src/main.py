# main.py

# В памяти «база данных» — список букетов
catalog = [
    {"id": 1, "name": "Ромашка", "price": 300, "quantity": 15},
    {"id": 2, "name": "Роза", "price": 500, "quantity": 8},
    {"id": 3, "name": "Тюльпан", "price": 200, "quantity": 20}
]

def display_catalog():
    print("Добро пожаловать в цветочный магазин!")
    print("Доступные букеты:")
    for i, букет in enumerate(catalog, 1):
        print(f"{i}. {buket['name']} — {buket['price']} руб. (остаток: {buket['quantity']})")

def add_to_cart(flower_id):
    if catalog[flower_id-1]["quantity"] > 0:
        catalog[flower_id-1]["quantity"] -= 1
        print(f"Добавлено в корзину: {catalog[flower_id-1]['name']}. Остаток: {catalog[flower_id-1]['quantity']}")
    else:
        print("Товар закончился. Выберите другой.")

def process_order():
    print("\n--- Оформление заказа ---")
    display_catalog()
    while True:
        try:
            choice = int(input("Введите номер букета (0 для выхода): "))
            if 1 <= choice <= len(catalog):
                add_to_cart(choice)
            else:
                print("Неверный номер. Попробуйте снова.")
        except ValueError:
            print("Пожалуйста, введите число.")

def main():
    display_catalog()
    process_order()

if __name__ == "__main__":
    main()
