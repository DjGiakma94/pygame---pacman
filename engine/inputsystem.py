import pygame

class InputSystem:

    def __init__(self):
        self.observers = {}
        self.onPressObservers = {}
        self.prevEvents = None

    def bindToKeyboard(self, key, function, onPress=False):
        if function is not None:
            # bind a single function to multiple keys
            if onPress:
                self.onPressObservers[key] = function
            else:
                self.observers[key] = function

    def reset(self):
        self.observers.clear()
        self.onPressObservers.clear()
        self.prevEvents = None

    def process(self):
        keyboardEvents = pygame.key.get_pressed()
        
        # every single key is mapped here, with a boolean set to True for those keys that were pressed
        for key, function in self.observers.items():
            if keyboardEvents[key]:
                function(key)

        if self.prevEvents is not None:
            for key, function in self.onPressObservers.items():
                if keyboardEvents[key] and not self.prevEvents[key]:
                    function(key)

        self.prevEvents = keyboardEvents

        # we'll add later the code for joypad & joystick input


