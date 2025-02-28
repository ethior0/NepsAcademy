MAXN = 100100;

def upd(l, r, d):
  l -= 1;
  r -= 1;
  
  f[l] += d;
  f[r+1] -= d;

f = [0] * MAXN;
dig = [0] * 10;

N, M = map(int, input().split());
arrN = list(map(int, input().split()));
arrM = list(map(int, input().split()));

last = 1;

upd(1,1,1);

for i in range(M):
  prox = arrM[i];
  l = min(last, prox);
  r = max(last, prox);
  
  upd(l, r, 1);
  upd(last, last, -1);
  
  last = prox;

for j in range(N):
  f[j] += f[j-1];
  dig[arrN[j]] += f[j];

res = "";
for k in range(10):
  res += f"{dig[k]} ";

print(res);