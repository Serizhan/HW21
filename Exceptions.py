class BaseError(Exception):
    message = "Ошибка"


class NotEnoughSpace(BaseError):
    message = "Нет свободного места"


class NotEnoughProduct(BaseError):
    message = "Нет свободного продукта"


class ManyProducts(BaseError):
    message = "Много товаров"


class InvalidRequest(BaseError):
    message = "Не верный запрос, повторите еще"