def memberf(f, ls):
   for x in ls:
      if f(x):
         return True
   return False
