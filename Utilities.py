
#from https://stackoverflow.com/questions/6158602/does-python-classes-support-
#events-like-other-languages (second answer)
class Event:
    def __init__(self):
        self.listeners = []

    def __iadd__(self, listener):
        """Shortcut for using += to add a listener."""
        self.listeners.append(listener)
        return self

    def notify(self, *args, **kwargs):
        """notify all the handlers"""
        for listener in self.listeners:
            listener(*args, **kwargs)