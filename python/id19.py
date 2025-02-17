MAXM = 61;
MINM = 30;

botas = [[0, 0] for _ in range(61)];

N = int(input());
for _ in range(N):
  M, L = input().split();
  if L == "D":
    botas[int(M)][1] += 1;
  else:
    botas[int(M)][0] += 1;

cc = 0;
for i in range(MINM, MAXM):
  cc += min(botas[i][0], botas[i][1]);

print(cc);