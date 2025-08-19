wc = 0
cc = 0
cc1 = 0
with open("demo1.txt")as myfile:
   alllines = myfile.readlines()
   lc = len(alllines)
   print('total number of lines: ',lc)
   for l in alllines:
      for ch in l:
         cc+=1
      l = l.strip("/n")
      wordlist = l.split(" ")
      wc = wc +len(wordlist)
      for w in  wordlist:
         cc1 = cc1+len(w)

   print("Total number of word: ",wc)
   print('Total number of characters  with space :',cc)
   print('Total number of characters without space:',cc1)       