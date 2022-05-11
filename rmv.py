#Script to respiratory minute volume e on a scuba dive
#This program assumes a 232 bar tank and metric
class DiveData:
    def __init__(self, gasStart, gasEnd, diveLength, avgDepth, tankSize):
        self.gasStart = gasStart
        self.gasEnd = gasEnd
        self.diveLength = diveLength
        self.avgDepth = avgDepth
        self.tankSize = tankSize

    def __str__(self):
        print(self.gasStart)
        print(self.gasEnd)
        print(self.diveLength)
        print(self.avgDepth)
        print(self.tankSize)
        return ("")


def calculate_rmv(dive_data):
    gas_used = dive_data.gasStart - dive_data.gasEnd
    total_atmos = (dive_data.avgDepth / 10) + 1
    sac_rate = (gas_used / dive_data.diveLength) / total_atmos
    rmv = dive_data.tankSize * sac_rate
    return rmv

def userInput():
    dive_data = DiveData(int(input("Starting Gas: ")), int(input("End Gas: ")), int(input("Dive Length: ")), int(input("Average Depth: ")), int(input("Tank Size (litres): ")))
    print(round(calculate_rmv(dive_data), 1))

while True:
    if input("Type exit or hit enter to continue: ") == "exit":
        break
    userInput()




