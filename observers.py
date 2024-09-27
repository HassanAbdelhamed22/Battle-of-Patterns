from abc import ABC, abstractmethod

# Observer interface
class Observer(ABC):
    @abstractmethod
    def notify(self, message):
        pass

# Subject interface
class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify_observers(self, message):
        pass

# Concrete Observer
class GameLogObserver(Observer):
    def notify(self, message):
        print(f"{message}")

# Concrete Subject
class GameSubject(Subject):
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.notify(message)