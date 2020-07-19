def highest_even(li):
  x = 0
  for item in li:
    if(item%2==0):
      if(item>x):
        x = item
  return x


print(highest_even([100, 2, 3, 4, 8, 120]))

#find highest even