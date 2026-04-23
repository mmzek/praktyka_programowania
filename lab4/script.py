from abc import ABC, abstractmethod

class HandlerInterface(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass

class BaseHandler(HandlerInterface):
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler

    # 4. handle
    def handle(self, request):
        if self.next_handler:
            return self.next_handler.handle(request)
        else:
            print(f"Brak zwierzęcia dla pokarmu: {request}")

class Squirrel(BaseHandler):
    def handle(self, request):
        if request == "orzech":
            print(f"Wiewiórka zje {request}")
        else:
            super().handle(request)


class Dog(BaseHandler):
    def handle(self, request):
        if request == "kosc":
            print(f"Pies zje {request}")
        else:
            super().handle(request)

def feed_animals(handler, food):
    for f in food:
        print(f"\nPodano: {f}")
        handler.handle(f)

if __name__ == "__main__":
    squirrel = Squirrel()
    dog = Dog()
    squirrel.set_next(dog)
    food = ["orzech", "mleko", "kosc"]
    feed_animals(squirrel, food)