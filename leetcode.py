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

#Prefijo común mas largo
# Si no hay un prefijo común, devuelve una cadena vacía "".
# Ejemplo 1:

# Entrada: strs = ["flower","flow","flight"]
#  Salida: "fl"

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        if not strs:
            return ""
            
        strs.sort()
        Caracter1 = list(strs[0])
        Caracter2 = list(strs[len(strs)-1])
        prefijo = ""
        

        for i in range(min(len(Caracter1), len(Caracter2))):
            if Caracter1[i] == Caracter2[i]:
                prefijo += Caracter1[i]
            else:
                break

        return prefijo

            
print(Solution().longestCommonPrefix(["flower","flow","flight"]))
print(Solution().longestCommonPrefix(["perro","coche de carreras","coche"]))
print(Solution().longestCommonPrefix(["jugar","jugo","juicio"]))



"""
Para encontrar el prefijo común más largo, ordenamos alfabéticamente el array de cadenas. Luego, comparamos los caracteres 
de la primera y la última cadena del array. Si el carácter de la primera cadena se encuentra en la última en el índice correspondiente, 
también debe estar en las demás cadenas en el mismo índice, ya que el array de cadenas ya está ordenado.
"""

##Parentesis validos##




class Solution:
    def isValid(self, s: str) -> bool:


        equivalencias = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        pila = []

        for caracter in s:
            if caracter in equivalencias:
                if not pila or pila.pop() != equivalencias[caracter]:
                    return False
            else:
                pila.append(caracter)

        return len(pila) == 0




  




                 
print(Solution().isValid("([])"))





