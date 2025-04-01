#¿Cuál es la salida del siguiente código?
n = 3

while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)

print("\n############")
#¿Cuál es la salida del siguiente código?
n = range(4)

for num in n:
    print(num - 1)
else:
    print(num)

print("\n############")
#¿Cuál es la salida del siguiente código?
for i in range(0, 6, 4): ###El primer valor es 0 pero como incrementa en 3 es 0,3 ya que al sumar 3 mas el rango se sale 
    print(i)