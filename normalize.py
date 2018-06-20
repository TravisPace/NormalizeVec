def infNorm(vector):
  result = 0
  for i in range(len(vector)):
    if result <= abs(vector[i]):
      result = abs(vector[i])
  return result

def scalarMultVec(scalar,vector):
  A = [ ]
  for i in range(len(vector)):
    A.append(vector[i] * scalar)
  return A

def normalize(vector):
  result = infNorm(vector)
  if result == 1 or result == 0:
    return vector
  scalar = 1/result
  B = scalarMultVec(scalar,vector)
  return B

  



vector = [0,0,-1]
print(normalize(vector))
