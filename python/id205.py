N, F = map(int, input().split());
# capsulas | moedas
cicloN = list(map(int, input().split()));

ini = 0;
fim = int(1e8 + 1);

while ini < fim:
  meio = (ini + fim) // 2;
  res = 0;
  
  for i in range(N):
    moedas = meio // cicloN[i];
    res += moedas;
  
  if res >= F:
    fim = meio;
  else:
    ini = meio+1;

print(ini);