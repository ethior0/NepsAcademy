def soma_areas(h):
  res = 0;
  for i in range(N):
    Xa, Ya, Xb, Yb = map(int, terras[i]);
    alt = abs(h - Ya);
    base = abs(Xb - Xa);
    
    res += alt * base;
  return res;

def busca_binaria(ini, fim):
  res = 0;
  while ini <= fim:
    meio = (ini + fim) // 2; # nosso h
    soma = soma_areas(meio);
    
    if soma >= K:
      res = meio;
      fim = meio - 1;
    else:
      ini = meio + 1;
  return res;

N, K = map(int, input().split());
# qtd terras | km minimo

ini = int(1e9 + 1);
fim = - int(1e9 + 1);

terras = [];
somaAreas = 0;
for _ in range(N):
  Xa, Ya, Xb, Yb = map(int, input().split());
  
  # Encontrar a altura maxima e minima
  if Ya < ini: ini = Ya;
  if Xb > fim: fim = Yb;
  
  somaAreas += (Xb - Xa) * (Yb - Ya);
  terras.append([Xa, Ya, Xb, Yb]);

# verificação pra ver se a soma das areas é maior que o K
if somaAreas < K:
  print("PERDAO MEU REI");
else: 
  print(busca_binaria(ini, fim));