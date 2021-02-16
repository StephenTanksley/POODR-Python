"""
    At this point, my Wheel and Gear classes are separated and I need to figure out what messages should be passed between them. 
    The classes themselves are more visible, but I need a way of defining the value of messages that will be shared.
    Ultimately, the messages are the most important thing to get right here.


"""


class Customer:
    def __init__(self, date, difficulty, need_bike):
        self.date = date
        self.difficulty = difficulty
        self.need_bike = need_bike

    def __str__(self):
        return f'Trip date requested: {self.date}, difficulty: {self.difficulty}, customer needs bike: {self.need_bike}'

    def __repr__(self):
        return [self.date, self.difficulty, self.need_bike]


class Trip:
    def __init__(self, date, difficulty):
        self.date = date
        self.difficulty = difficulty
        self.trips = []

    def __str__(self):
        pass

    def __repr__(self):
        pass


class Bicycle:
    def __init__(self):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass


moe = Customer('01/01/2021', 'Easy', True)

print(moe.__dict__)
