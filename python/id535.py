# bfs

direction = [[1, 0], [1, -1], [1, 1], [-1, 0], [-1, -1], [-1, 1], [0, -1], [0, 1]];
queue = [];

def bfs(board, n, m, x, y, cc):
  queue.append([x, y]);
  
  while queue:
    aux = queue.pop();
    x = aux[0];
    y = aux[1];
    
    for d in direction:
      x1 = x + d[0];
      y1 = y + d[1];
      
      if x1 < 0 or x1 > n-1 or y1 < 0 or y1 > m-1:
        continue;
      
      neighbour = board[x1][y1];
      
      if neighbour == -1:
        cc += 1;
        board[x1][y1] = 1;
        queue.append([x1, y1]);
  return cc;

n, m, x, y, k = map(int, input().split()); 

board = [[-1 for _ in range(m)] for _ in range(n)];

for _ in range(k):
  a, b = map(int, input().split());
  board[a-1][b-1] = 1; # visited

cc = 1;
board[x-1][y-1] = 1;
res = bfs(board, n, m, x-1, y-1, cc);

print(res);