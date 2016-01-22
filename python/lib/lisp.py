import traceback
import threading as T

def memberf(f, ls):
   for x in ls:
      if f(x):
         return True
   return False

def nub(a=None):
   pass

def showError(e):
   print(e)
   traceback.print_exc()


def assertThreadIs(s):
   assert T.currentThread().getName() == s, \
      "Running on a wrong thread -" \
      + "\n Expected: " + s \
      + "\n Actual: " + T.currentThread().getName()
