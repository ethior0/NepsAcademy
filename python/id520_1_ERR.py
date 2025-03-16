# com dfs dá erro por conta do limite de recursao, entao tentamos com bfs

def dfs(x):
  if vis[x]: return;
  vis[x] = 1;
  for i in range(len(adj[x])):
    dfs(adj[x][i]);

n, d = [int(x) for x in input().split()];

adj = [[] for _ in range(n)];
vis = [0] * n;
arv = [];

for _ in range(n):
  x, y = map(int, input().split());
  arv.append([x, y]);

# lista de adjacencia
for i in range(n):
  for j in range(i+1, n):
    aux1 = (arv[i][0] - arv[j][0]) ** 2;
    aux2 = (arv[i][1] - arv[j][1]) ** 2
    # dist = sqrt((x1 - x2)^2 + (y1 - y2)^2);
    # dist^2 = (x1 - x2)^2 + (y1 - y2)^2
    if (aux1 + aux2) <= d*d:
      adj[i].append(j);
      adj[j].append(i);

dfs(0); # começo do vértice 0

flag = True;
for i in range(n):
  if not(vis[i]):
    flag = False;

if flag:
  print("S");
else:
  print("N");