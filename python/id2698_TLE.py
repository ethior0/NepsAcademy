# TLE

def checaMaior(i, j, array, n, m):
  maior = array[i][j];
  
  for k in range(i, n):
    linha = array[k][j:m];
    maior = max(maior, max(linha));
  
  return maior;

n, m = map(int, input().split());
M = [];

for _ in range(n):
  linha = list(map(int, input().split()));
  M.append(linha);

maxFrutas = 0;
for i in range(n):
  for j in range(m):
    frutasAtual = M[i][j];
    maiorArray = checaMaior(i, j, M, n, m);
    
    if maiorArray > frutasAtual:
      res = maiorArray - frutasAtual;
      if res > maxFrutas:
        maxFrutas = res;

print(maxFrutas);

