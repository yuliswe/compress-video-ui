import traceback

def memberf(f, ls):
   for x in ls:
      if f(x):
         return True
   return False

def nub(a=None):
   pass

def showError(e):
   print e
   traceback.print_exc()
