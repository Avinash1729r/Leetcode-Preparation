import collections

def finder1(arr1,arr2):
  arr1.sort()
  arr2.sort()

  for num1,num2 in zip(arr1,arr2):
    if num1 != num2:
      return num1
  return arr1[-1]

def finder2(arr1,arr2):

  d = collections.defaultdict(int)
  for i in arr1:
    d[i] += 1

  for num in arr1:
    if d[num] == 0:
      return num
    else:
      d[num] -= 1

      
def finder3(arr1,arr2):

  return sum(arr1)-sum(arr2)
