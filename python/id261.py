def busca_binaria(arrN):
  ini = 0;
  fim = len(arrN)-2;
  
  while ini <= fim:
    meio = (fim + ini) // 2;
    if arrN[meio] <= forca and forca < arrN[meio+1]:
      return meio+1;
    elif arrN[meio] < forca:
      ini = meio+1;
    else:
      fim = meio-1;

N, M = map(int, input().split());
arrN = list(map(int, input().split())); # arr faixas (N-1)
arrP = list(map(int, input().split())); # arr premiaçao (N)
arrM = list(map(int, input().split())); # forca ogros (M)

res = "";

for i in range(M):
  forca = arrM[i];
  
  if forca < arrN[0]: # se ele é menor que o 1º 
    aux = arrP[0];
  elif forca >= arrN[N-2]: # se ele é maior que o ultimo
    aux = arrP[N-1];
  else:
    aux = arrP[busca_binaria(arrN)];
  
  res += str(aux) + " ";

print(res);