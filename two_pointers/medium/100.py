"""
"""

class Solution:
    def threeSumPartiallyCorrect(self, numbers):

        numbers.sort()

        if (len(numbers) <= 2 or
            (numbers[0] >= 0 or numbers[-1] <= 0)):
            return []


        maxneg, minpos = -1, -1
        i = 1
        while i < len(numbers):
            if numbers[i-1] < 0 and numbers[i] >= 0:
                maxneg = i-1
            if numbers[i-1] < 0 and numbers[i] > 0 or numbers[i] == 0:
                minpos = i
            i += 1

        if (minpos == -1 or
            maxneg == -1):
            return []

        res = []
        #one neg and two positives
        r = len(numbers) - 1
        for i in range(0, maxneg + 1):
            number = -numbers[i]
            if number > numbers[-2] + numbers[-1]:
                continue
            l = minpos
            while l < r:
                if number == numbers[l] + numbers[r]:
                    res.append([numbers[i], numbers[l], numbers[r]])
                if number > numbers[l] + numbers[r]:
                    l += 1
                else:
                    r -= 1
                    l = minpos

        #one pos and two negatives
        l = 0
        for i in range(len(numbers) - 1, minpos - 1, -1):
            if numbers[i] > -numbers[0] - numbers[1]:
                continue
            r = maxneg
            while l < r:
                if numbers[i] == -numbers[l] - numbers[r]:
                    res.append([numbers[l], numbers[r], numbers[i]])
                if number > -numbers[l] - numbers[r]:
                    r -= 1
                else:
                    l += 1
                    r = maxneg 
        
        return res

    def threeSum(self, numbers):
        
        numbers.sort()
        res = []
        
        for i, a in enumerate(numbers):
            
            if i > 0 and a == numbers[i-1]:
                continue
            
            l, r = i+1, len(numbers)-1
            
            while l < r:
                threeSum = a + numbers[l] + numbers[r]
                
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, numbers[l], numbers[r]])
                    
                    l += 1
                    while numbers[l] == numbers[l-1] and l < r:
                        l += 1
        return res


if __name__ == "__main__":
    tests = [
        [-5, -4, -2, -1, -1, 0, 1, 2, 2],
        [-1,-1, 2],
        [-1,0,1,1,-4]
    ]

    for test in tests:
        print(Solution().threeSum(test))


