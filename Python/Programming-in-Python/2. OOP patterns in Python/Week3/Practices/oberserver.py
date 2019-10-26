from abc import ABC, abstractmethod


class ObservableEngine(Engine):
    def __init__(self):
        self._subscribers = set()

    def subscribe(self, subscriber):
        self._subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        self._subscribers.remove(subscriber)

    def notify(self, achieve):
        for subscriber in self._subscribers:
            subscriber.update(achieve)


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, achieve):
        pass


class ShortNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = set()

    def update(self, achieve):
        self.achievements.add(achieve['title'])


class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = list()

    def update(self, achieve):
        if achieve not in self.achievements:
            self.achievements.append(achieve)
