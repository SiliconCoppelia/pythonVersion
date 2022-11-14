from enum import Enum

class Appearance(Enum):
    """
    Aesthetics is designed for a auction to represent robot's reflect
    on agent's appearance, generally there are three level

    version 1.0
    noted: Enum.auto() will generate a unique number. I planing use this to present
    position of corresponding sentence in database
    """
    BEAUTY: list = [5, [num / 100 for num in range(67, 100, 1)]]
    PRETTY: list = [4, [num / 100 for num in range(34, 67, 1)]]
    ORDINARY: list = [3, [num / 100 for num in range(0, 34, 1)]]
    BLEMISH: list = [2, [(-1)*(num / 100) for num in range(0, 34, 1)]]
    UGLY: list = [1, [(-1)*(num / 100) for num in range(34, 67, 1)]]
    APPALLING: list = [0, [(-1)*(num / 100) for num in range(67, 100, 1)]]


class Aesthetics:
    """
    Description of the class:
    according to paper, the Aesthetics is more like a judging database
    this class wont process some calculate algorithm.

    version 1.0
    features :var, determine the future receive value since from initial dataset
    the value received would be JSON format
    """

    features: dict
    accuracy: float
    appear: tuple

    def __init__(self, accuracy: float):
        self.accuracy = accuracy

    def judge(self):
        temp: float = float("{:.2f}".format(self.accuracy))
        for iterator in Appearance:
            if temp in iterator.value[1]:
                self.appear = iterator.value
                break

    def getAest(self) -> tuple:
        self.judge()
        # a print statement should present here
        return tuple([self.appear[0], self.accuracy])


if __name__ == "__main__":
    Aesthetics(0.35).getAest()
