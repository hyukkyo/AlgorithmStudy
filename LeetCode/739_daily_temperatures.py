class Solution(object):
    def dailyTemperatures(self, temperatures):

        # answer = []

        # for i in range(len(temperatures)):
        #     count = 1
        #     isExist = False

        #     j = i + 1
        #     while j < len(temperatures):
        #         if temperatures[i] < temperatures[j]:
        #             isExist = True
        #             break
        #         else:
        #             count += 1

        #         j += 1

        #     if isExist == False:
        #         answer.append(0)
        #     else:
        #         answer.append(count)

        # return answer
    
# time limit exceeded
# O(n^2)
    
# 스택으로 풀면 O(n)으로 풀수있음
        answer = [0] * len(temperatures)
        stack = []
        for currentDay, currentTemp in enumerate(temperatures):
            while stack and stack[-1][1] < currentTemp:
                previousDay, _ = stack.pop()
                answer[previousDay] = currentDay - previousDay
            stack.append((currentDay, currentTemp))
        return answer



            

# print(Solution.dailyTemperatures(self=Solution, temperatures = [73,74,75,71,69,72,76,73]))