class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        #result=[]
        # test = False
        # for x in range(len(temperatures)):
        #     count=0
        #     test = False
        #     for y in range(x+1,len(temperatures)):
        #         count+=1
        #         if temperatures[y]>temperatures[x]:
        #             test = True
        #             break
        #     if test:
        #         result.append(count)
        #     else:
        #         result.append(0)
        # return result

        result = [0]*len(temperatures)
        #extra memory
        stack = [] #pair: [temp, index]

        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stackT, stackInd = stack.pop()
                result[stackInd] = i-stackInd
            stack.append([t,i])

        return result
            




