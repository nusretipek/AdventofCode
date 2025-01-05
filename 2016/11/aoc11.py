import numpy as np
import random

elementMap = {"A": "Thulium",
              "B": "Plutonium",
              "C": "Strontium",
              "D": "Promethium",
              "E": "Ruthenium"}

elements = [("A1", 1), ("A0", 1), ("B1", 1), ("C1", 1),
            ("B0", 2), ("C0", 2),
            ("D1", 3), ("D0", 3), ("E1", 3), ("E0", 3)]
verboseInitialState = False

if verboseInitialState:
    shafts = [np.array(["F1", "F2", "F3", "F4"])]
    for i in elements:
        tempShaft = []
        for j in range(4):
            if j == i[1]-1:
                tempShaft.append(i[0])
            else:
                tempShaft.append(". ")
        shafts.append(tempShaft)

    shaftPlan = np.vstack(shafts).T[::-1]
    for i in range(shaftPlan.shape[0]):
        s = ""
        for j in range(len(shaftPlan[i])):
            s += shaftPlan[i][j] + " "
        print(s.strip())


def makeMove(currentState, elevatorState):
    currentFloorItems = [_[0] for _ in currentState if _[1] == elevatorState]

    if elevatorState != 4:
        # Get carry loads to upper
        upperFloorItems = [_[0] for _ in currentState if _[1] == elevatorState + 1]
        compatibleToCarry = []
        for idx in range(len(currentFloorItems)):
            for idj in range(idx+1, len(currentFloorItems)):
                if (currentFloorItems[idx][0] == currentFloorItems[idj][0] or
                    currentFloorItems[idx][1] == currentFloorItems[idj][1]):
                    compatibleToCarry.append([currentFloorItems[idx], currentFloorItems[idj]])

        # Filter upper moves
        invalidCarryLoads = []
        for idx, carry in enumerate(compatibleToCarry):
            tempUpperFloor = upperFloorItems + carry
            pairs = []
            for idj in range(len(tempUpperFloor)):
                for idz in range(idj + 1, len(tempUpperFloor)):
                    if tempUpperFloor[idj][0] == tempUpperFloor[idz][0]:
                        pairs.append([tempUpperFloor[idj], tempUpperFloor[idz]])
            pairsSet = set([y for x in pairs for y in x])
            leftovers = [x for x in tempUpperFloor if x not in pairsSet]
            leftoversGenerator = [x[1] == "1" for x in leftovers]
            leftoversChip = [x[1] == "0" for x in leftovers]
            isValidUp = True if all(leftoversGenerator) or all(leftoversChip) else False

            tempCurrentFloor = [_ for _ in currentFloorItems if _ not in carry]
            pairs = []
            for idj in range(len(tempCurrentFloor)):
                for idz in range(idj + 1, len(tempCurrentFloor)):
                    if tempCurrentFloor[idj][0] == tempCurrentFloor[idz][0]:
                        pairs.append([tempCurrentFloor[idj], tempCurrentFloor[idz]])
            pairsSet = set([y for x in pairs for y in x])
            leftovers = [x for x in tempCurrentFloor if x not in pairsSet]
            leftoversGenerator = [x[1] == "1" for x in leftovers]
            leftoversChip = [x[1] == "0" for x in leftovers]
            isValidCurrent = True if all(leftoversGenerator) or all(leftoversChip) else False
            if not isValidUp or not isValidCurrent:
                invalidCarryLoads.append(idx)
        compatibleToCarry = [carry for idx, carry in enumerate(compatibleToCarry) if idx not in invalidCarryLoads]

        if len(compatibleToCarry) > 0:
            toCarry = random.choice(compatibleToCarry)
            nextState = currentState.copy()
            for idx in range(len(nextState)):
                if nextState[idx][0] in toCarry:
                    nextState[idx] = (nextState[idx][0], nextState[idx][1]+1)
            return nextState, elevatorState+1

    if elevatorState != 1:
        lowerFloorItems = [_[0] for _ in currentState if _[1] == elevatorState - 1]
        compatibleToStay = []
        for idx in range(len(currentFloorItems)):
            for idj in range(idx+1, len(currentFloorItems)):
                if currentFloorItems[idx][0] == currentFloorItems[idj][0]:
                    compatibleToStay.append([currentFloorItems[idx], currentFloorItems[idj]])

        pairsSet = set([y for x in compatibleToStay for y in x])
        leftovers = [x for x in currentFloorItems if x not in pairsSet]
        if len(leftovers) > 0:
            invalidCarryLoads = []
            for idx, carry in enumerate(leftovers):
                tempLowerFloor = lowerFloorItems + [carry]
                pairs = []
                for idj in range(len(tempLowerFloor)):
                    for idz in range(idj + 1, len(tempLowerFloor)):
                        if tempLowerFloor[idj][0] == tempLowerFloor[idz][0]:
                            pairs.append([tempLowerFloor[idj], tempLowerFloor[idz]])
                pairsSet = list(set([y for z in pairs for y in z]))
                leftoversTemp = [z for z in tempLowerFloor if z not in pairsSet]
                leftoversGenerator = [z[1] == "1" for z in leftoversTemp]
                leftoversChip = [z[1] == "0" for z in leftoversTemp]
                isValidDown = True if all(leftoversGenerator) or all(leftoversChip) else False

                tempCurrentFloor = [_ for _ in currentFloorItems if _ not in [carry]]
                pairs = []
                for idj in range(len(tempCurrentFloor)):
                    for idz in range(idj + 1, len(tempCurrentFloor)):
                        if tempCurrentFloor[idj][0] == tempCurrentFloor[idz][0]:
                            pairs.append([tempCurrentFloor[idj], tempCurrentFloor[idz]])
                pairsSet = set([y for x in pairs for y in x])
                leftoversTemp = [x for x in tempCurrentFloor if x not in list(pairsSet)]
                leftoversGenerator = [x[1] == "1" for x in leftoversTemp]
                leftoversChip = [x[1] == "0" for x in leftoversTemp]
                isValidCurrent = True if all(leftoversGenerator) or all(leftoversChip) else False
                if not isValidDown or not isValidCurrent:
                    invalidCarryLoads.append(idx)
            leftovers = [carry for idx, carry in enumerate(leftovers) if idx not in invalidCarryLoads]

        if len(leftovers) == 0:
            leftovers = currentFloorItems.copy()
            invalidCarryLoads = []
            for idx, carry in enumerate(leftovers):
                tempLowerFloor = lowerFloorItems + [carry]
                pairs = []
                for idj in range(len(tempLowerFloor)):
                    for idz in range(idj + 1, len(tempLowerFloor)):
                        if tempLowerFloor[idj][0] == tempLowerFloor[idz][0]:
                            pairs.append([tempLowerFloor[idj], tempLowerFloor[idz]])
                pairsSet = set([y for x in pairs for y in x])
                leftoversTemp = [x for x in tempLowerFloor if x not in pairsSet]
                leftoversGenerator = [x[1] == "1" for x in leftoversTemp]
                leftoversChip = [x[1] == "0" for x in leftoversTemp]
                isValidDown = True if all(leftoversGenerator) or all(leftoversChip) else False

                tempCurrentFloor = [_ for _ in currentFloorItems if _ not in [carry]]
                pairs = []
                for idj in range(len(tempCurrentFloor)):
                    for idz in range(idj + 1, len(tempCurrentFloor)):
                        if tempCurrentFloor[idj][0] == tempCurrentFloor[idz][0]:
                            pairs.append([tempCurrentFloor[idj], tempCurrentFloor[idz]])
                pairsSet = set([y for x in pairs for y in x])
                leftoversTemp = [x for x in tempCurrentFloor if x not in pairsSet]
                leftoversGenerator = [x[1] == "1" for x in leftoversTemp]
                leftoversChip = [x[1] == "0" for x in leftoversTemp]
                isValidCurrent = True if all(leftoversGenerator) or all(leftoversChip) else False
                if not isValidDown or not isValidCurrent:
                    invalidCarryLoads.append(idx)
            leftovers = [carry for idx, carry in enumerate(leftovers) if idx not in invalidCarryLoads]
        if len(leftovers) > 0:
            lowerFloors = []
            for idx in range(1, elevatorState):
                for element in currentState:
                    if element[1] == idx:
                        lowerFloors.append(element[0])
            generators = [x for x in lowerFloors if x[1] == "1"]
            chips = [x for x in lowerFloors if x[1] == "0"]
            if len(generators) == 0:
                leftovers = [x for x in leftovers if x[1] == "0"]
            if len(chips) == 0:
                leftovers = [x for x in leftovers if x[1] == "1"]
            if len(generators) == 1 and len(chips) == 0:
                leftovers = [generators[0][0] + "0"]
            if len(chips) == 1 and len(generators) == 0:
                leftovers = [chips[0][0] + "1"]

            toCarry = random.choice(leftovers)
            nextState = currentState.copy()
            for idx in range(len(nextState)):
                if nextState[idx][0] in toCarry:
                    nextState[idx] = (nextState[idx][0], nextState[idx][1]-1)
            return nextState, elevatorState-1
        else:
            return None, None


stepsP1 = None
while stepsP1 is None:
    s, e = elements.copy(), 1
    stepCount = 0
    try:
        while not all([_[1] == 4 for _ in s]):
            s, e = makeMove(s, e)
            stepCount += 1
        stepsP1 = stepCount
    except IndexError:
        continue
    except TypeError:
        continue
print("AoC_2016_11.1:", stepsP1)


elementMap = {"A": "Thulium",
              "B": "Plutonium",
              "C": "Strontium",
              "D": "Promethium",
              "E": "Ruthenium",
              "F": "Elerium",
              "G": "Dilithium"}
elements = [("A1", 1), ("A0", 1), ("B1", 1), ("C1", 1), ("F1", 1), ("F0", 1), ("G1", 1), ("G0", 1),
            ("B0", 2), ("C0", 2),
            ("D1", 3), ("D0", 3), ("E1", 3), ("E0", 3)]

stepsP2 = None
while stepsP2 is None:
    s, e = elements.copy(), 1
    stepCount = 0
    try:
        while not all([_[1] == 4 for _ in s]):
            s, e = makeMove(s, e)
            stepCount += 1
        stepsP2 = stepCount
    except IndexError:
        continue
    except TypeError:
        continue
print("AoC_2016_11.2:", stepsP2)
