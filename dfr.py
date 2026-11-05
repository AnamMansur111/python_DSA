"""

a, b = map(int, input("Enter two numbers: ").split())

print("Sum =", a + b)
"""
   for i in range (len(nums)):
            for j in range(len(nums)):
                if i!=j and abs(i - j) <= indexDiff and abs(nums[i] - nums[j]) <= valueDiff:
                    return True
        else:
            return False