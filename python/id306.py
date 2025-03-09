n = int(input());
arr = [int(x) for x in input().split()]; # n

# -2 5 -1 8 -11 7 3
# -2 5 4 12 1 8 11 (kadane)

maior = 0;
atual = arr[0];

for i in range(1, n):
  if atual + arr[i] > arr[i]:
    atual += arr[i];
  else:
    atual = arr[i];
  maior = max(maior, atual);

print(maior);