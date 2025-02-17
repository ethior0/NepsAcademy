# é o mesmo problema do id 255

casas = [];

N = int(input());

for _ in range(N):
  casa = int(input());
  casas.append(casa);

K = int(input());

ini = 0;
fim = N-1;

while fim - ini > 1:
  if casas[ini] + casas[fim] == K:
    break;
  elif casas[ini] + casas[fim] > K:
    fim -= 1;
  else:
    ini += 1;

print(casas[ini], casas[fim]);