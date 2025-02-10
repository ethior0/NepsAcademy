while True:
  try:
    cc = 0;
    num = int(input());
    
    while num != 2018:
      cc += 1;
      num = int(input());
    
    print(cc);
  except EOFError: 
    break;