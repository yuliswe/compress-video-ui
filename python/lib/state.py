class State(object):

   class Await():
      """State"""
   class Success():
      stdout = ""
   class Failure():
      pass
   class Running():
      """State"""

   def __init__(self):
      self.state = State.Await()

   def setRunning(self):
      self.state = State.Running()

   def setFailure(self, e):
      self.state = State.Failure()
      self.exception = e

   def setSuccess(self):
      self.state = State.Success()

   def setAwait(self):
      self.state = State.Await()

   def isRunning(self):
      return isinstance(self.state, State.Running)

   def isFailure(self):
      return isinstance(self.state, State.Failure)

   def isSuccess(self):
      return isinstance(self.state, State.Success)

   def isAwait(self):
      return isinstance(self.state, State.Await)


   def getException(self):
      assert self.isFailure(), \
         "State: attempted to call getException when the state is " \
         + str(self.state)
      return self.state.exception
