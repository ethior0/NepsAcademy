A, B, C, D = map(int, input().split());

if (B == D and A != C and A != B and C != B) or (A == C and B != D and B != A and D != A):
  print("V");
else:
  print("F");