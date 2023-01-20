from random import random
from random import randrange

#from abc import ABC, abstractmethod

class CoppeliaProfile:

    # the definition about 'Epistemics' part is not clear...

    COPPELIA_ON_ETHICS = "Very Kind"
    COPPELIA_ON_AFFORDANCE = "Smart"
    COPPELIA_ON_AESTHETICS = "Beautiful"
    COPPELIA_ON_AESTHETICS = "Realistic"

    PREFERENCE_ON_ETHICS = "Friendly"
    PREFERENCE_ON_AFFORDANCE = "Nutural"
    PREFERENCE_ON_AESTHETICS = "Gorgeous"
    PREFERENCE_ON_EPISTEMICS = "True"

    def factorsOnGoals(self, goal):
        return 

    def similarityOnInvl(self):
        """
            calculate the distance between Coppelia and the Agent
        """
        return 

    def similarityOnDist(self):
        """
            calculate the distance between Coppelia and the Agent
        """
        return 

    def similarityOnUI(self):
        """
            calculate the distance between Coppelia and the Agent
        """
        return 

    def getsimilarity(self):
        return

    def setIvolvement(self, involvement):
        self.involvement = involvement

    def setDistance(self, distance):
        self.distance = setDistance

    def setUseIntention(self, useIntention):
        self.useIntention = setUseIntention

    def getIvolvement(self):
        return self.involvement

    def getDistance(self):
        return self.distance

    def getUseIntention(self):
        return self.useIntention