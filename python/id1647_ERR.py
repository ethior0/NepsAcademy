# o site simplesmente nao avalia minha resposta '-'

N = int(input());

ini = 0;
fim = N;
ans = 0;

while ini <= fim:
  meio = (ini + fim) // 2;
  gaussAnt = meio * (meio-1) // 2;
  gauss = (meio + 1) * meio // 2;
  
  if N >= gaussAnt:
    if N < gauss: 
      ans = meio-1;
    ini = meio + 1;
  else:
    fim = meio - 1;

print(ans);