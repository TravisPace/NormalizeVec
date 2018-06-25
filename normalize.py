def infNorm(vector):
  '''
  This takes the infinity norm of the vector.
  '''
  result = 0
  #Result is equal to no integer.
  for i in range(len(vector)):
  #For every element in the vector.
    if result <= abs(vector[i]):
    #This takes each element of the vector and sees if it greater than or equal to the previous element in the vector list.
      result = abs(vector[i])
      #If the result is greater than or equal to than the previous element, then the element becomes the result.
  return result
  #This returns the integer as the result.

def scalarMultVec(scalar,vector):
  A = [ ]
  for i in range(len(vector)):
    A.append(vector[i] * scalar)
  return A

def normalize(vector):
  '''
  This function normalizes the vector
  '''
  result = infNorm(vector)
  if result == 1 or result == 0:
    return vector
  #If the result is equal to 1 or zero from the infinity norm function, then this will return the vector.
  scalar = 1/result
  B = scalarMultVec(scalar,vector)
  #This takes the scalar multiplication vector function and runs it to get B, B is the vector and scalar is scalar.
  return B
  #This returns the vector B.

  



vector = [0,0,-1]
print(normalize(vector))
