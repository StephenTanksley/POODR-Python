# Learning to write classes for a bicycle
from collections import namedtuple

# USING KWARGS IN INIT FUNCTION:
# https://stackoverflow.com/questions/60418497/how-do-i-use-kwargs-in-python-3-class-init-function


class Gear:
    def __init__(self, chainring, cog, wheel):
        self._chainring = chainring
        self._cog = cog
        self.wheel = wheel

    def __str__(self):
        print(
            f'Chainring: {self.chainring}, cog: {self.cog}, ratio: {self.ratio()} ratio.')

    def __repr__(self):
        return f'({self._chainring}, {self._cog}, {self.ratio})'

    def chainring(self):
        return self._chainring

    def cog(self):
        return self._cog

    def ratio(self):
        return float(self._chainring / self._cog)

    def gear_inches(self):
        # This method doesn't actually care about self.wheel whether it's an actual Wheel object or not.
        return self.ratio() * self.wheel.diameter


class Wheel:
    def __init__(self, rim, tire):
        self.rim = rim
        self.tire = tire

    def diameter(self):
        return self.rim + (self.tire * 2)


def print_kwargs(keyword, **kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        if key == keyword:
            print(f'{keyword}: {value}')


print_kwargs("kwarg2", kwarg1="kwarg1", kwarg2="kwarg2", kwarg3="kwarg3")
