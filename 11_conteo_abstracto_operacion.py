# 1002 + x + 2x^2
# O(x^2)
def f(x):
  respuesta = 0 # 1

  for i in range(100): # 1000
    respuesta += 1

  for i in range(x): # x
    respuesta += x

  # 2*x^2
  for i in range(x):
    for j in range(x):
      respuesta += 1
      respuesta += 1
      # 2 operaciones

  return respuesta # 1