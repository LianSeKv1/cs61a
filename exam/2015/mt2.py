# Q1
class Ok:
    py = [3.14]

    def __init__(self, py):
        self.ok = self.py
        Ok.py.append(3 * py)

    def my(self, eye):
        print(self.my(eye))
        return self.ok.pop()
    
    def __str__(self):
        return str(self.ok)[:4]
    
class Go(Ok):
    def my(self, help):
        return [help + 3, len(Ok.py)]


#  Ok.py = [3.14,15,27] Go.py = [3,1,4] 
#  oh.ok ->Go.py
#  oh.no = {'just':Go(9)}


#oh = Go(5)               #   oh.ok = [3.14,15] -> Go.py
#Go.py = [3,1,4]          #   py = [3,1,4,27]
#oh.no = {'just':Go(9)}   #   

"""
oh.py                           [3,1,4]
oh.my(3)                        [6,3]
oh.ok + oh.no('just').ok        [3,1,4,27]
print(oh)                       [3,1,4,27]
Ok('go').my(5)                  Error
Ok.my(oh, 5)                    [8,4]   [27]

"""