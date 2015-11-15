__author__ = 'SHADOW'
from pymarkovchain import MarkovChain


mc = MarkovChain("./markov")
w = open("data", "r").read()
mc.generateDatabase(w)
print(mc.generateString())
