T = int(input()); # arvores dia 0
M = int(input()); # mudas por dia
A = int(input()); # número alvo de árvores

dias = 0;

while T < A:
  T += T * M;
  dias += 1;

print(dias);
