def dfs(x, y):
  board[x][y] = 0;
  
  if y > 0:
    if board[x][y-1] == 1:
      dfs(x, y-1);
  if y < n-1:
    if board[x][y+1] == 1:
      dfs(x, y+1);

n, m = map(int, input().split());
board = [];

for _ in range(n):
  linha = input().replace(".", "0").replace("#", "1");
  board.append([int(x) for x in list(linha)]);

k = int(input());

print("incio:", board);

res = 0;
for _ in range(k):
  l, c = map(int, input().split());
  if board[l-1][c-1] == 1:
    res += 1;
    dfs(l-1, c-1);
    print(board);

print(res);