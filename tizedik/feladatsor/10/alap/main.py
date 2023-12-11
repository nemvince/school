def hello():
  print("Hello, World!")

def add(a, b):
  return a + b

def printArray(arr):
  print(*arr, sep=", ")

def isEven(n):
  return n % 2 == 0

def reverseString(s):
  return s[::-1]

def calculateFactorial(n):
  if n == 0:
    return 1
  return n * calculateFactorial(n - 1)

def isPrime(n):
  if n < 2:
    return False
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
  return True

def sumOfList(arr):
  return sum(arr)

def findMax(arr):
  return max(arr)

def countEvenNumbers(arr):
  return sum(map(isEven, arr))

def removeDuplicates(arr):
  return list(set(arr))

def findLargestSubstring(x, y):
  m, n = len(x), len(y)

  lcs = [[0 for i in range(n + 1)] for j in range(m + 1)]

  result = 0

  r, c = 0, 0

  for i in range(m + 1):
    for j in range(n + 1):
      if i == 0 or j == 0:
        lcs[i][j] = 0
      elif x[i - 1] == y[j - 1]:
        lcs[i][j] = lcs[i - 1][j - 1] + 1
        if result < lcs[i][j]:
          result = lcs[i][j]
          r = i
          c = j
      else:
        lcs[i][j] = 0

  if result == 0:
    return ""
  
  s = ""

  while lcs[r][c] != 0:
    s = x[r - 1] + s
    r -= 1
    c -= 1

  return s

def calculatePower(x, n):
  if n == 0:
    return 1
  return x * calculatePower(x, n - 1)

def sortArray(arr):
  return sorted(arr)

def calculateAverage(arr):
  return sum(arr) / len(arr)

def findCommonElements(arr1, arr2):
  return list(set(arr1) & set(arr2))

def findMissingNumbers(arr):
  return list(set(range(1, max(arr) + 1)) - set(arr))

def swapElements(arr):
  arr[-1], arr[0] = arr[0], arr[-1]

def reverseList(arr):
  return arr[::-1]

def findPrimesInRange(a, b):
  return list(filter(isPrime, range(a, b + 1)))

def mergeArrays(arr1, arr2):
  return arr1 + arr2

def findLongestWord(arr):
  return max(arr, key=len)

