casas = [];

N = int(input());

for _ in range(N):
  casas.append(int(input()));

K = int(input());

inicio = 0;
fim = N-1;

while inicio < fim:
  if casas[inicio] + casas[fim] == K:
    break;
  elif casas[inicio] + casas[fim] > K:
    fim -= 1;
  else:
    inicio += 1;

print(casas[inicio], casas[fim]);