def rotLeft(a, d):
    for index in range(1, d+1):
        a = a[1:]+[a[0]]
    return a
  
  
  
# Another solution
def rotLeft(a, d):
    return a[d:]+a[:d]
