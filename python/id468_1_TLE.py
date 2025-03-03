# TLE

def lower(ini, fim, t):
  while ini < fim:
    meio = (ini + fim) // 2;
    if pref[meio] >= t:
      fim = meio;
    else:
      ini = meio + 1;
  return ini;

def upper(ini, fim, t):
  while ini < fim:
    meio = (ini + fim) // 2;
    if pref[meio] > t:
      fim = meio;
    else:
      ini = meio + 1;
  return fim;

N, K = map(int, input().split());
arrN = list(map(int, input().split()));

pref = [0] * (N + 1);

for i in range(1, N + 1):
  pref[i] = pref[i - 1] + arrN[i - 1];

# s[i..j] = pref[j] - pref[i-1]
# pref[j] - pref[i-1] = k
# pref[j] = pref[i-1] + k

ans = 0;
for i in range(1, N + 1):
  t = pref[i - 1] + K;
  ini = lower(i, N + 1, t);
  fim = upper(i, N + 1, t);
  
  ans += fim - ini;

print(ans);