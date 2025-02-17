N = int(input());
tam = list(map(int, input().split()));
tamOrd = sorted(tam);
desord = [0] * N;

cc = 0;
sen = "";
for i in range(N):
  if tam[i] != tamOrd[i]:
    desord[cc] = tamOrd[i];
    sen += str(desord[cc]) + " ";
    cc += 1;

print(cc);
if cc > 0: print(sen);