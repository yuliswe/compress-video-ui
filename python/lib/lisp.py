import traceback
import threading as T
import sys 

def memberf(f, ls):
   for x in ls:
      if f(x):
         return True
   return False

def nub(a=None):
   pass

def showError(e):
   error(str(e))
   traceback.print_exc()

def assertThreadIs(s):
   assert T.currentThread().getName() == s, \
      "Running on a wrong thread -" \
      + "\n Expected: " + s \
      + "\n Actual: " + T.currentThread().getName()

def log(s):
   print("Log - Thread "+ T.currentThread().name+": "+s, file=sys.stderr)
   
def warn(s):
   print("Warning - Thread "+ T.currentThread().name+": "+s, file=sys.stderr)
   
def error(s):
   print("Error - Thread "+ T.currentThread().name+": "+s, file=sys.stderr)
   