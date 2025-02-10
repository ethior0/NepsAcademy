texto = input();
letras = input();

textoArray = texto.split();

cc = 0;
for texto in textoArray:
  for j in range(len(letras)):
    letraAtual = letras[j];
    if texto.count(letraAtual) > 0:
      cc += 1;
      break;

print(cc);