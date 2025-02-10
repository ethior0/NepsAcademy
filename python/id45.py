N = int(input());
tab = [[]] * 1005;

somaLin = [0] * (N + 2);
somaCol = [0] * (N + 2);

# Soma das linhas e colunas
for i in range(1, N+1):
  tab[i] = list(map(int, input().split()));
  somaLin[i] = sum(tab[i]);
  
  for j in range(1, N+1):
    somaCol[j] += tab[i][j-1];

peso = 0;
for k in range(1, N+1):
  for l in range(N):
    numAtual = tab[k][l];
    novoPeso = (somaLin[k] + somaCol[l+1]) - (numAtual * 2);
    if novoPeso > peso:
      peso = novoPeso;

print(peso);