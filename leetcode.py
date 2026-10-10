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

#26. Eliminar duplicados de un array ordenado.

# En realidad, no quieren que elimines los duplicados. Quieren que ordenes los elementos únicos al principio y luego devuelvas la longitud de la parte ordenada. Después, internamente, dividen el array en la longitud que les indiques y comprueban el resultado.

# Para que lo sepas, esta mierda me volvió loco...

# Escritor (k): Indica la posición donde escribiremos el próximo valor único que descubramos. Como nums[0] (el primer 1) ya es un elemento único garantizado, k empieza en el índice 1.

# Lector (i): Recorre el arreglo desde el índice 1 hasta el final buscando valores nuevos.
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k=1
        i=1

        for i in range(len(nums)):
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k+=1            

        return k

print(Solution().removeDuplicates([1, 1, 2]))
print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))


#27. Eliminar elemento


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k=0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1

        return k

print(Solution().removeElement([3,2,2,3],3))

#28. Find the Index of the First Occurrence in a String
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1 


print(Solution().strStr("triste pero triste","triste"))

#35. Buscar Posición de inserción

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        if target in nums:
            return nums.index(target)

        for i in range(len(nums)):
            if nums[i] < target and nums[i+1] > target:
                return i+1
        
        
        return len(nums)
                

    
print(Solution().searchInsert([1,3,5,6],2))

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left

    
print(Solution().searchInsert([1,3,5,6],2))


#58 longitud de la última palabra
#elsplit() método divide una cadena en una lista de subcadenas 
#basándose en un delimitador (separador) especificado

company = " Coding For All "

print(company.split())

palabras = company.split()

print(len(palabras[-1]))


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        palabras = s.split()

        if not palabras:
            return 0
        else:
            return len(palabras[-1])


print(Solution().lengthOfLastWord("luffy is still joyboy"))
print(Solution().lengthOfLastWord("Hola Mundo"))
print(Solution().lengthOfLastWord(" llévame a la luna "))

#66 Más uno

# range(len(digits) - 1, -1, -1)

# len(digits) - 1: empieza en el último índice, que es el ultimo.

# -1: límite final que no se incluye, para llegar hasta el índice 0.

# -1: disminuye el índice de uno en uno.

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            elif digits[i] == 9:
                digits[i] = 0
        nuevo = [0] * (len(digits) + 1)
        nuevo[0] = 1    
        return nuevo


print(Solution().plusOne([1,2,3]))
print(Solution().plusOne([1,9,9]))
print(Solution().plusOne([9]))
print(Solution().plusOne([9,9,9]))
print(Solution().plusOne([9,9,9,9]))


# 67 Agregar un binario

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        listaAu = []
        carry = 0
        
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0 or carry:
            total = carry
            if i>=0:
                total += int(a[i])
                i -=1

            if j>=0:
                total += int(b[j])
                j -=1


            listaAu.append(str(total % 2))

            carry = total // 2


        resultado = "".join(listaAu[::-1])

        return resultado

print(Solution().addBinary("1010","1"))
print(Solution().addBinary("11","1"))

#70 Subir escaleras

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2

        maneras= [0] * (n+1)
        maneras[0] = 0
        maneras[1] = 1
        maneras[2] = 2

        for i in range(3,n + 1):
            maneras[i] = maneras[i - 1] + maneras[i - 2]
        


        return maneras[-1]

print(Solution().climbStairs(3))
# len(digits) - 1: empieza en el último índice, que es el ultimo.

# -1: límite final que no se incluye, para llegar hasta el índice 0.

# -1: disminuye el índice de uno en uno.


            
#F(n)=F(n−1)+F(n−2)
# entonces ways_to(n) = ways_to(n-1) *1 + ways_to(n-2)*1
# entonces ways_to(n) = ways_to(n-1) + ways_to(n-2)
#entonces el total de maneras de llegar al punto [n] es n1 + n2


