import sys  $accesses you current path
sys.path.append('/monteCarloData/Ledger') $path where data collected is

BaseString="Ledger"
j = 2
k = 2
for i in range(25):
  for i in range(25):
    jString = input(j)
    kString = input(k)
    f = open("BaseString"+jString+kString".txt",r)  reading file Ledger22.txt
    ...insert all the manipulations
    f.close()
    j = j+2
    if j>50:
      j = 2
      k = k+2
      ...do subplots
      
main()
