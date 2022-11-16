from random import randrange
import sys
sys.path.append("..")

class Distance:
    # distance = 0
    # input_factor = ""

    p_low, p_mid, p_high, n_low, n_mid, n_high, e_low, e_mid, e_high = ([] for i in range(9))

    def setDistance(self, distance):
        self.distance = distance

    def getDistance(self):
        return self.distance

    # def setInputFactor(self, input_factor):
    #     self.input_factor = input_factor

    # def select_factor_dic(self):
    #     if (self.input_factor == "ethics"):
    #         return "eth_pos/"
    #     elif (self.input_factor == "affordance negative"):
    #         return "aff_neg/"
    #     elif (self.input_factor == "affordance positive"):
    #         return "aff_pos/"
    #     else:
    #         pass
    #         # return "aest_pos/"

    def getPosAffordance(self):
        # Load corpus if all variants in one dimension are used up
        if len(self.p_low) == 0:
            self.p_low = open("sentences/distance/" + self.select_factor_dic() + "_low.txt", "r").readlines()
        if len(self.p_mid) == 0:
            self.p_mid = open("sentences/distance/" + self.select_factor_dic() + "_mid.txt", "r").readlines()
        if len(self.p_high) == 0:
            self.p_high = open("sentences/distance/" + self.select_factor_dic() + "_high.txt", "r").readlines()

        if self.distance < 0.34:
            return self.p_low.pop(randrange(len(self.p_low))).replace("\n", "")
        elif self.distance < 0.67:
            return self.p_mid.pop(randrange(len(self.p_mid))).replace("\n", "")
        else:
            return self.p_high.pop(randrange(len(self.p_high))).replace("\n", "")

    def getNegAffordance(self):
        # Load corpus if all variants in one dimension are used up
        if len(self.n_low) == 0:
            self.n_low = open("sentences/distance/" + self.select_factor_dic() + "_low.txt", "r").readlines()
        if len(self.n_mid) == 0:
            self.n_mid = open("sentences/distance/" + self.select_factor_dic() + "_mid.txt", "r").readlines()
        if len(self.n_high) == 0:
            self.n_high = open("sentences/distance/" + self.select_factor_dic() + "_high.txt", "r").readlines()

        if self.distance < 0.34:
            return self.n_high.pop(randrange(len(self.n_low))).replace("\n", "")
        elif self.distance < 0.67:
            return self.n_mid.pop(randrange(len(self.n_mid))).replace("\n", "")
        else:
            return self.n_low.pop(randrange(len(self.n_high))).replace("\n", "")

    def getEthics(self):
        if len(self.e_low) == 0:
            self.e_low = open("sentences/distance/" + self.select_factor_dic() + "_low.txt", "r").readlines()
        if len(self.e_mid) == 0:
            self.e_mid = open("sentences/distance/" + self.select_factor_dic() + "_mid.txt", "r").readlines()
        if len(self.e_high) == 0:
            self.e_high = open("sentences/distance/" + self.select_factor_dic() + "_high.txt", "r").readlines()

        if self.distance < 0.34:
            return self.e_high.pop(randrange(len(self.e_low))).replace("\n", "")
        elif self.distance < 0.67:
            return self.e_mid.pop(randrange(len(self.e_mid))).replace("\n", "")
        else:
            return self.e_low.pop(randrange(len(self.e_high))).replace("\n", "")

if __name__ == "__main__":
    jack = Distance()
    jack.setInputFactor("affordance positive")
    print(jack.getEthics())
