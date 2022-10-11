import Aesthetics as aest
from enum import Enum


class StayWith(Enum):
    SKILLFUL: tuple = [5, [num / 100 for num in range(83, 100, 1)]]
    BRILLIANT: tuple = [4, [num / 100 for num in range(67, 83, 1)]]
    NORMAL: tuple = [3, [num / 100 for num in range(50, 67, 1)]]
    UNFAMILIAR: list = [2, [num / 100 for num in range(33, 50, 1)]]
    AWKWARD: list = [1, [num / 100 for num in range(17, 33, 1)]]
    UNSKILLFUL: list = [0, [num / 100 for num in range(0, 17, 1)]]


class Affordance:
    """
    version 1.0
    generally the same logistic process with the Aesthetics
    """

    inputIn: float
    appear: tuple

    def __init__(self, outerln: float) -> None:
        self.inputIn = outerln
        return

    def undefined(self) -> None:
        temp: float = float("{:.2f}".format(self.inputIn))
        for iterator in StayWith:
            if temp in iterator.value[1]:
                self.appear = iterator.value
                break

    def getAffor(self) -> tuple:
        self.undefined()
        return tuple([self.appear[1], self.inputIn])
