from random import randrange


class Involvement:

    # aff_low, aff_mid, aff_high, eth_low, eth_mid, eth_high = ([] for i in range(6))
    invl_high, invl_low, invl_mid = ([] for i in range(3))

    def setInvl(self, involvement):
        self.involvement = involvement

    def getInvl(self):
        return self.involvement

    # def setInputFactor(self, input_factor):
    #     self.input_factor = input_factor

    # def select_factor_dic(self):
    #     if self.input_factor == "involvement":
    #         return "Inv"
    #     elif self.input_factor == "ethics":
    #         return "eth"
    #     else:
    #         pass
    #         # return "aest_pos/"

    def getInvolvement(self):
        # Load corpus if all variants in one dimension are used up
        if len(self.invl_low) == 0:
            self.invl_low = open("./sentences/involvement/invl_low.txt", "rb").readlines()
        if len(self.invl_mid) == 0:
            self.invl_mid = open("./sentences/involvement/invl_mid.txt", "rb").readlines()
        if len(self.invl_high) == 0:
            self.invl_high = open("./sentences/involvement/invl_high.txt", "rb").readlines()

        if self.involvement < 0.34:
            return (self.invl_low.pop(randrange(len(self.invl_low))).decode("utf-8")).replace("\n","")
        elif self.involvement < 0.67:
            return (self.invl_mid.pop(randrange(len(self.invl_mid))).decode("utf-8")).replace("\n","")
        else:
            return (self.invl_high.pop(randrange(len(self.invl_high))).decode("utf-8")).replace("\n","")

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


# if __name__ == "__main__":
#     jack = Involvement()
#     jack.setInputFactor("involvement")
#     jack.setInvolvement(0.6)
#     print(jack.getInvolvement())


