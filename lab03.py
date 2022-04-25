
def integerDivision(n, k):
    if  n < k:
        return 0
    return 1 + integerDivision(n - k, k)

def collectEvenInts(listOfInt):
    if not listOfInt:
        return []
    if listOfInt[0] % 2 == 0:
        return [listOfInt[0]] + collectEvenInts(listOfInt[1:])
    return collectEvenInts(listOfInt[1:])


def countVowels(someString):
    if not someString:
        return 0
    return (1 if someString[0] in 'aeiouAEIOU' else 0) + countVowels(someString[1:])


def reverseString(s):
   if  len(s):
       return s[-1] + reverseString(s[:-1])
   else:
       return ""

def removeSubString(s,sub):
   if len(s):
       text = s[0] + removeSubString(s[1:],sub)
       if text[:len(sub)] == sub:
           return text[len(sub):]
       else:
           return text
   else:
       return ""








