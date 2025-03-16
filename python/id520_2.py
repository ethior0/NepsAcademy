fila = [];

def bfs(x):
  fila.append(x);
  
  while fila:
    aux = fila.pop();
    if vis[aux]: continue;
    vis[aux] = 1;
    
    for i in range(len(adj[aux])):
      fila.append(adj[aux][i]);

n, d = map(int, input().split());

adj = [[] for _ in range(n)]; 
vis = [0 for _ in range(n)];
arv = [];

for _ in range(n):
  x, y = map(int, input().split());
  arv.append([x, y]);

# lista de adjacencia
for i in range(n-1):
  for j in range(i+1, n):
    atual, prox = arv[i], arv[j];
    aux1 = (atual[0] - prox[0]) ** 2;
    aux2 = (atual[1] - prox[1]) ** 2;
  
    # dist^2 = (x1 - x2)^2 + (y1 - y2)^2
    if aux1 + aux2 <= d * d:
      adj[i].append(j);
      adj[j].append(i);

bfs(0);

flag = True;
for i in vis:
  if not(i):
    flag = False;

if flag:
  print("S");
else:
  print("N");