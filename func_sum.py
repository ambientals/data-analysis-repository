"""Function that calculates the sum of all numbers from 0 to (its argument - 1). Next implementation for this code: calculate sums from 0 to their arguments, instead. This code has educational purposes; no copyright infringement is intended."""

def sum(x):
  res = 0
  for i in range(x):
    res += i
  return res

print(sum(9)) # calculates 9 iterations: from 0 to 8 instead (not to 9!!!)
print(sum(10)) # calculates 10 iterations: from 0 to 9 instead (not to 10!!!)