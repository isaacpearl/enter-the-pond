#Frog class

import random

class frog:
    def __init__(self, frogName, startingCode, allCodes):
        self.name = frogName
        self.code = startingCode
        self.codeDict = allCodes
        self.call = self.codeToCall()

    def getName(self):
        return self.name

    def getCode(self):
        return self.code

    def getCall(self):
        return self.call

    def refreshCall(self):
        self.call = self.codeToCall()

    def setCode(self, newCode):
        self.code = newCode
        self.refreshCall() #i think? maybe take this out

    def codeToCall(self):
        result = []
        for char in self.code:
            if char == 'x':
                randomIndex = random.randint(0, len(self.codeDict['x'])-1)
                result.append(self.codeDict['x'][randomIndex]+' ')
            else:
                result.append(self.codeDict[char]+' ')
            random.shuffle(result)
        return ''.join(result)

    def getCallList(self):
        toReturn = self.call.split(sep=' ')
        toReturn.remove('') #hacky fix for weird empty string that works
        return toReturn
