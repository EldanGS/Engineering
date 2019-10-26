from abc import ABC, abstractmethod


class ObservableEngine:
    def __init__(self):
        self._subscribers = set()

    def subscribe(self, subscriber):
        self._subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        self._subscribers.remove(subscriber)

    def notify(self, message):
        for subscriber in self._subscribers:
            subscriber.update(message)


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, message):
        pass


class ShortNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = set()

    def update(self, achieve):
        self.achievements.add(achieve['title'])


class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = []

    def update(self, achieve):
        if achieve not in self.achievements:
            self.achievements.append(achieve)


if __name__ == '__main__':
    notify = {"title": "Покоритель",
              "text": "Дается при выполнении всех заданий в игре"}
    short = ShortNotificationPrinter()
    full = FullNotificationPrinter()
    obs_engine = ObservableEngine()
    obs_engine.subscribe(short)
    obs_engine.subscribe(full)
    obs_engine.notify(notify)

    print(short.achievements, full.achievements)