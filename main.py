from Exceptions import BaseError, InvalidRequest
from Request import Request
from Shop import Shop
from Storage import Storage

storage = Storage(
    {
        "капусты": 10,
        "морковь": 20,
        "лук": 30
    }
)

shop = Shop(
    {
        "капусты": 5,
        "лук": 5
    }
)

while True:
    print(f" На складе храниться: {storage.get_items()}")
    print(f" В магазине храниться: {shop.get_items()}")
    user_input = input('\nВведите запрос в виде "Доставить 3 капусты из склад в магазин"\n'
                       'Введите "stop" или "стоп" что бы остановить ввод\n')
    if user_input in ('stop', 'стоп'):
        break
    try:
        request = Request(user_input)
    except IndexError:
        print("Не верный запрос, повторите еще")
        continue

    try:
        if request.from_ == 'склад':
            storage.remove(request.product, request.amount)
            shop.add(request.product, request.amount)
            print(f"{request.product} перемещен из {request.from_} в {request.to}")
            print(f"Курьер забрал {request.amount} {request.product} из {request.from_}")

        else:
            shop.remove(request.product, request.amount)
            storage.add(request.product, request.amount)
            print(f"{request.product} перемещен из {request.from_} в {request.to}")
            print(f"Курьер забрал  {request.amount} {request.product} из {request.from_}")
    except BaseError as error:
        print(error.message)

