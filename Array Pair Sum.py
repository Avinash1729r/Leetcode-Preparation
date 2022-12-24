def check(arr,k):

  seen = set()
  output = set()

  for i in arr:
    target = k - i
    if target not in seen:
      seen.add(i)
    else:
      output.add((min(i,target),max(i,target)))

  print('\n'.join(map(str,list(output))))
check([1,3,2,2],4) 