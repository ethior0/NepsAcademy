from bisect import bisect_left, bisect_right

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
  target = pref[i - 1] + K;
  
  left = bisect_left(pref, target, i, N + 1);
  right = bisect_right(pref, target, i, N + 1);
  
  ans += right - left;

print(ans);