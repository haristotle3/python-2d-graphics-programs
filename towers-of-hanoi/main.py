from diskUtil import *
from initializationUtil import *
from mainUtil import *
from towersUtil import *

def main():
    numDisks = initializerUI()
    towersOfHanoi(numDisks)
    
main()