class EventManager:
    def __init__(self):
        self.listeners = {}

    def add_listener(self, event_name, listener):
        if event_name not in self.listeners:
            self.listeners[event_name] = []
        self.listeners[event_name].append(listener)

    def emit(self, event):
        for listener in self.listeners.get(event.name, []):
            listener(event)


class Event:
    def __init__(self, name, data=None):
        self.name = name
        self.data = data


class CharacterEnhancedEvent(Event):
    def __init__(self, character):
        super().__init__('character_enhanced', character)


class CharacterDehancedEvent(Event):
    def __init__(self, character):
        super().__init__('character_dehanced', character)


class CharacterDeathEvent(Event):
    def __init__(self, character):
        super().__init__('character_died', character)
