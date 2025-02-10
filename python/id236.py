N = int(input());
sqr = [[]] * 15;
soma = 0;

# checo as linhas
for i in range(1, N+1):
  sqr[i] = list(map(int, input().split()));
  
  if i == 1:
    soma = sum(sqr[i]);
  elif soma != sum(sqr[i]):
    soma = -1;

# checo as colunas
for j in range(N):
  somaCol = 0;
  for k in range(1, N+1):
    somaCol += sqr[k][j];
  if somaCol != soma:
    soma = -1;

# checar diagonais
somaDiagEsq, somaDiagDir = 0, 0;
for m in range(1, N+1):
  somaDiagEsq += sqr[m][m-1];
  somaDiagDir += sqr[m][N-m];

if somaDiagDir != soma:
  soma = -1;
if somaDiagEsq != soma:
  soma = -1;

print(soma);