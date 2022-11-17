from random import randrange


class Distance:

    # a_low, a_mid, a_high, e_low, e_mid, e_high = ([] for i in range(6))
    dis_high, dis_low, dis_mid = ([] for i in range(3))

    def setDistance(self, distance):
        self.distance = distance

    def getDistance(self):
        return self.distance

    # def setInputFactor(self, input_factor):
    #     self.input_factor = input_factor

    # def select_factor_dic(self):
    #     if self.input_factor == "ethics":
    #         return "eth/"
    #     elif self.input_factor == "affordance":
    #         return "aff/"
    #     else:
    #         pass
    #         # return "aest_pos/"

    def getDistance(self):
        # Load corpus if all variants in one dimension are used up
        if len(self.dis_low) == 0:
            self.dis_low = open("./sentences/distance/dist_low.txt", "rb").readlines()
        if len(self.dis_mid) == 0:
            self.dis_mid = open("./sentences/distance/dist_mid.txt", "rb").readlines()
        if len(self.dis_high) == 0:
            self.dis_high = open("./sentences/distance/dist_high.txt", "rb").readlines()

        if self.distance < 0.34:
            return self.dis_low.pop(randrange(len(self.dis_low))).decode("utf-8")
        elif self.distance < 0.67:
            return self.dis_mid.pop(randrange(len(self.dis_mid))).decode("utf-8")
        else:
            return self.dis_high.pop(randrange(len(self.dis_high))).decode("utf-8")

    # def getAffordance(self):
    #     # Load corpus if all variants in one dimension are used up
    #     if len(self.a_low) == 0:
    #         self.a_low = open("../sentences/distance/" + self.select_factor_dic() + "_low.txt", "r").readlines()
    #     if len(self.a_mid) == 0:
    #         self.a_mid = open("../sentences/distance/" + self.select_factor_dic() + "_mid.txt", "r").readlines()
    #     if len(self.a_high) == 0:
    #         self.a_high = open("../sentences/distance/" + self.select_factor_dic() + "_high.txt", "r").readlines()

    #     if self.distance < 0.34:
    #         return self.a_low.pop(randrange(len(self.a_low))).replace("\n", "")
    #     elif self.distance < 0.67:
    #         return self.a_mid.pop(randrange(len(self.a_mid))).replace("\n", "")
    #     else:
    #         return self.a_high.pop(randrange(len(self.a_high))).replace("\n", "")

    # def getEthics(self):
    #     if len(self.e_low) == 0:
    #         self.e_low = open("../sentences/distance/" + self.select_factor_dic() + "_low.txt", "r").readlines()
    #     if len(self.e_mid) == 0:
    #         self.e_mid = open("../sentences/distance/" + self.select_factor_dic() + "_mid.txt", "r").readlines()
    #     if len(self.e_high) == 0:
    #         self.e_high = open("../sentences/distance/" + self.select_factor_dic() + "_high.txt", "r").readlines()

    #     if self.distance < 0.34:
    #         return self.e_high.pop(randrange(len(self.e_low))).replace("\n", "")
    #     elif self.distance < 0.67:
    #         return self.e_mid.pop(randrange(len(self.e_mid))).replace("\n", "")
    #     else:
    #         return self.e_low.pop(randrange(len(self.e_high))).replace("\n", "")


# if __name__ == "__main__":
#     jack = Distance()
#     jack.setInputFactor("affordance")
#     jack.setDistance(0.6)
#     print(jack.getAffordance())

#     jack.setInputFactor("ethics")
#     jack.setDistance(0.3)
#     print(jack.getAffordance())
