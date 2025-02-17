import math;

def compararDis(Xa, Ya, arrC):
  d = math.sqrt(pow((0 - Xa), 2) + pow((0 - Ya), 2));

  p = 0;  
  ini = 0;
  fim = len(arrC)-1;
  
  while ini <= fim:
    meio = (ini + fim) // 2;
    if d <= arrC[meio]:
      p = len(arrC) - meio;
      fim = meio-1;
    else:
      ini = meio+1;
  
  return p;

C, T = map(int, input().split());
arrC = [];
arrT = [];

for _ in range(C):
  R = int(input());
  arrC.append(R);

p = 0;

# coords de cada tiro
for _ in range(T):
  X, Y = map(int, input().split());
  arrT.append([X, Y]);
  p += compararDis(X, Y, arrC)

print(p);