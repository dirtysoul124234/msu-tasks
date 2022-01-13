

def sort(p: list) -> list:
    swap = 0
    i = 0
    index = 0
    index1 = -1
    min = p[i]
    for i in range (len(a)):
      while true :
         if p[index] < min:
             swap = min
             min = p[i]
             p[index1] = min
             print ('2')
      else :
            continue
      if len(p) == i :
          print(p)
          break
    index1 = index1 + 1



def find(p: list, i) -> int:
    i = 0
    while i < len(p):
        if p[i] == self._pattern[0]:
            j = 0
            while j < len(self._pattern):
                if p[i + j] == self._pattern[j]:
                    j += 1
                else:
                    break


def my_min(p: list) -> int:
    min = p[0]
    for i in p:
        if i < min:
            min=i
    return min


def my_max(p: list) -> int:
    max = p[0]
    for i in p:
        if i > max:
            max = i
    return max

def my_sum(p: list) -> int:
    i = 0 
    for number in p:
        i += number
    print(i)


def revert(p: list) -> list:
    fun = ''
    for i in range(len(p)-1):
        fun+=p[i]
    return fun
print(fun)


def unique(p: list) -> list:
    unique_numbers =[]
    fun = set(p)
    for number in fun:
        unique_numbers.append(p)
    return unique_numbers


def capitalize(s: str) -> str:
    s.lower()  
    for word in s.split():
        if word.istitle()== False:
            word = word[0].upper() + word[1:]
        s +="".join(word)
    return s



def lower(s: str) -> str:
   print(s.casefold()) 

def upper(s: str) -> str:
    pass


def replace(s: str, old: str, new: str) -> str:
    pass


def swapcase(s: str) -> str:
    pass


def my_split(s, sep):
    pass
