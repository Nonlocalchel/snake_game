class Tracker:
    def __init__(self, element, action):
        self.__element = element
        self.__trackable_action = action

    def track(self, element):
        self.__element = element

    def is_trackable_element(self, element):
        return self.__element == element

    def check_action(self):
        return self.__trackable_action(self.__element)
