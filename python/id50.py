A = int(input());
B = int(input());
C = int(input());
D = int(input());

cond1 = B + C + D;
cond2 = B + C;

if cond1 == A and cond2 == D and B == C:
  print("S");
else:
  print("N");