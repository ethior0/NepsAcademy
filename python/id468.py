N, K = map(int, input().split());
arrN = list(map(int, input().split()));

somaN = [arrN[0]];
for i in range(1, N):
  somaN.append(somaN[i-1] + arrN[i]);

ans = 0;
for j in range(0, N):
  pass;

print(ans);