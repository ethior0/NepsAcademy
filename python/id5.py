H, P, F, D = map(int, input().split());
lista = [0] * 16;
novaLista = [];

lista[F], lista[H], lista[P] = 1, 2, 3;

cc = F;
flag = False;
for _ in range(16):
  novaLista.append(lista[cc]);
  if D == -1:
    cc -= 1;
    if cc == -1: cc = 15;
  else:
    cc += 1;
    if cc == 16: cc = 0;
  
  if lista[cc] == 2:
    flag = True;
    break;
  elif lista[cc] == 3:
    break;

if flag:
  print("S");
else:
  print("N");