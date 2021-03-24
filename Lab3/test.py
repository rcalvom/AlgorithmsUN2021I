ini = 0
fin = 128
x = 32
while(ini < fin):
  print("test")
  mid = int ( (ini + fin + 1)/2 )
  if(mid == x):
    break
  elif( mid > x):
    fin = mid - 1
  else:
    ini = mid