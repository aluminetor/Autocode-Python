## Two Sum (el #1 de LeetCode) ##


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

        




print(Solution().twoSum([3, 2, 4],6))



# numero palíndromo

class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        x_alrevez = int(str(x)[::-1])

        if x == x_alrevez:
            return True
        else:
            return False



print(Solution().isPalindrome(121))

#Conversion de numeros romanos a enteros

class Solution:
    def romanToInt(self, s: str) -> int:

        total = 0

        valor_simbolo = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }

        for i in range(len(s)):         
            if i + 1 < len(s) and valor_simbolo[s[i]] < valor_simbolo[s[i + 1]]:
                total -=valor_simbolo[s[i]]
            else:
                total +=valor_simbolo[s[i]]

        return total


print(Solution().romanToInt("MCMXCIV"))
