directions = [[0, -1], [0, 1], [-1, 0], [1, 0]];

queue = [];

def bfs(l, c):
  queue.append([l, c]);
  
  while queue:
    aux = queue.pop();
    auxL, auxC = aux[0], aux[1];
    
    if auxL < 0 or auxL > n-1 or auxC < 0 or auxC > m-1:
      continue;
    if board[auxL][auxC] != 1:
      continue;
    
    board[auxL][auxC] = qtdNavio;
    pedacos_restantes[qtdNavio] += 1;
    
    for d in directions:
      queue.append([auxL+d[0], auxC+d[1]]);

pedacos_restantes = [0] * 10000;
n, m = map(int, input().split());
board = [];

for _ in range(n):
  linha = input().replace(".", "0").replace("#", "1");
  board.append([int(x) for x in list(linha)]);

qtdNavio = 2;
for i in range(n):
  for j in range(m):
    if board[i][j] == 1:
      bfs(i, j);
      qtdNavio += 1;

k = int(input());

res = 0;
for _ in range(k):
  l, c = map(int, input().split());
  tiro = board[l-1][c-1];
  
  if tiro != 0:
    pedacos_restantes[tiro] -= 1;
    if pedacos_restantes[tiro] == 0:
      res += 1;

print(res);