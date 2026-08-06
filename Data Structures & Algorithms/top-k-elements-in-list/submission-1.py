from collections import defaultdict

class Solution:




    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # def findMin(inpList):
        #     # returns the index of smallest item in list
        #     smallest = inpList[0]
        #     smallestInd = 0
        #     for i in range(len(inpList)):
        #         if inpList[i] < smallest:
        #             smallestInd = i

        #     return smallestInd


        numDict = defaultdict(int)
        for num in nums:
            numDict[num] += 1
        # return numDict
        topK = []

        for key, val in numDict.items():
            if len(topK) < k: # just append key to list
                topK.append((key, val)) # [(1, 4), (2, 6), (3, 1)]
            else: # check for update to list
                if val > min([i[1] for i in topK]): # if there needs to be an update
                    smallestValInd = 0
                    smallestVal = topK[0][1]
                    for i in range(len(topK)):
                        if topK[i][1] < smallestVal:
                            smallestValInd = i
                            smallestVal = topK[i][1]
                    topK[smallestValInd] = (key, val)



        return [i[0] for i in topK]



                # if val > min(topK):
                #     minIndex = -1
                #     minVal = topK[0]
                #     for j in range(len(topK)):
                #         if topK[j] < minVal:
                #             minIndex = j
                #     topK[j] = val


        