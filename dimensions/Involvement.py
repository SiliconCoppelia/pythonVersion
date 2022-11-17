from random import randrange
import sys
sys.path.append("..")


class Involvement:

    involvement = 0
    input_factor = ""

    aff_low, aff_mid, aff_high, eth_low, eth_mid, eth_high = ([] for i in range(6))

    def setInvolvement(self, involvement):
        self.involvement = involvement

    def setInputFactor(self, input_factor):
        self.input_factor = input_factor

    def select_factor_dic(self):
        if self.input_factor == "involvement":
            return "Inv"
        elif self.input_factor == "ethics":
            return "eth"
        else:
            pass
            # return "aest_pos/"

    def getInvolvement(self):
        # Load corpus if all variants in one dimension are used up
        if len(self.aff_low) == 0:
            self.aff_low = open("./sentences/involvement/" + self.select_factor_dic() + "_low.txt", "rb").readlines()
        if len(self.aff_mid) == 0:
            self.aff_mid = open("./sentences/involvement/" + self.select_factor_dic() + "_mid.txt", "rb").readlines()
        if len(self.aff_high) == 0:
            self.aff_high = open("./sentences/involvement/" + self.select_factor_dic() + "_high.txt", "rb").readlines()

        if self.involvement < 0.34:
            return self.aff_low.pop(randrange(len(self.aff_low))).decode("utf-8")
        elif self.involvement < 0.67:
            return self.aff_mid.pop(randrange(len(self.aff_mid))).decode("utf-8")
        else:
            return self.aff_high.pop(randrange(len(self.aff_high))).decode("utf-8")

    # def getEthics(self):
    #     # Load corpus if all variants in one dimension are used up
    #     if len(self.eth_low) == 0:
    #         self.eth_low = open("./sentences/involvement/" + self.select_factor_dic() + "_low.txt", "rb").readlines()
    #     if len(self.eth_mid) == 0:
    #         self.eth_mid = open("./sentences/involvement/" + self.select_factor_dic() + "_mid.txt", "rb").readlines()
    #     if len(self.eth_high) == 0:
    #         self.eth_high = open("./sentences/involvement/" + self.select_factor_dic() + "_high.txt", "rb").readlines()
    #
    #     if self.involvement < 0.34:
    #         return self.eth_low.pop(randrange(len(self.eth_low))).decode("utf-8")
    #     elif self.involvement < 0.67:
    #         return self.eth_mid.pop(randrange(len(self.eth_mid))).decode("utf-8")
    #     else:
    #         return self.eth_high.pop(randrange(len(self.eth_high))).decode("utf-8")


if __name__ == "__main__":
    jack = Involvement()
    jack.setInputFactor("involvement")
    jack.setInvolvement(0.6)
    print(jack.getInvolvement())


