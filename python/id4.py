N, M = map(int, input().split());
lista = list(map(int, input().split()));

prev = -1;
res = 0;

for i in range(N):
  mn = lista[i];
  mx = M - lista[i];
  
  if mn > mx:
    mn, mx = mx, mn;
  
  if mn >= prev:
    lista[i] = mn;
  elif mx >= prev:
    lista[i] = mx;
  else:
    res = -1;
    break;
  
  prev = lista[i];
  res += prev;

print(res);