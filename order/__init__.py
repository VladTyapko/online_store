class OrderStatus:
    NEW = "новий"
    IN_PROCESS = "готується"
    SUCCESSFUL = "виконано"
    CANCEL = "відміна"


    CHOICES = [
        (
            NEW,
            "новий"
        ),
        (
            IN_PROCESS,
            "готується"
        ),
        (
            SUCCESSFUL,
            "виконано"
        ),
        (
            CANCEL,
            "відміна"
        ),
    ]


class MethodPayment:
    CASH = "готівка"
    ONLINE = "онлайн"

    CHOICES = [
        (
            CASH,
            "готівка"
        ),
        (
            ONLINE,
            "онлайн"
        ),
    ]