def retornaPao(tam):
  x = 0;
  for i in range(K):
    x += arrK[i] // tam;
  return x; # retorna a quantidade x de pães em tamanho tam

N = int(input());
K = int(input());
arrK = list(map(int, input().split()));

ini = 0;
fim = int(1e4 + 1);

res = 0;
while ini <= fim:
  meio = (ini + fim) // 2
  x = retornaPao(meio);
  
  if x >= N:
    ini = meio + 1;
    res = meio;
  else:
    fim = meio - 1;

print(res);