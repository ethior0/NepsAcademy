E = int(input()); # 2
A = int(input()); # 3
C = int(input()); # 5

soma = (E * 2) + (A * 3) + (C * 5);

if soma < 100:
  print("N");
elif soma < 150:
  print("B");
elif soma < 200:
  print("S");
else:
  print("O");