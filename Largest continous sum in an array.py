def LargeContTest(arr,arr1):
  if(sum(arr)>sum(arr1)):
    return sum(arr)
  else:
    return sum(arr1)
x = []
for i in range(len(arr)):
  x.append(LargeContTest(arr[:i],arr[i+1:]))
print(max(x))