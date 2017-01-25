import random
import Frog
from browser import document
from browser import timer

class storage:
    # initialize data structures
    # TODO: experiment with adding more syllables to codeList
    codeDict = {}
    codeList = []
    codeValues ={}
    frogList = []
    flCopy = []
    turn = 1
    loop = None
    pondDict = {}
    MAX_CALL_LENGTH = 11 #maybe use this

    def __init__(self):
        x = 0

    def fill(self, cDict, cList, cVals, fList, flC):
        storage.codeDict = cDict
        storage.codeList = cList
        storage.codeValues = cVals
        storage.frogList = fList
        storage.flCopy = flC

    def setLoop(self, l):
        storage.loop = l

    def setPD(self, pd):
        storage.pondDict = pd

    def getPD(self):
        return storage.pondDict

    def nextTurn(self):
        storage.turn += 1

    def getTurn(self):
        return str(storage.turn)


def main():
    # initialize data structures
    # TODO: experiment with adding more syllables to codeList
    codeList = ['קְוָה־קְוָה', 'rech', 'බක', 'rega-kvak', 'квок-квок', 'ồm-ộp', 'kum', 'qwà', 'croac', 'oac',
                     'qūr', 'kvekk', 'डरांव', 'kvā', 'кре', '개굴', 'মক মক', 'krok', 'бақ-бақ', 'tarr', 'ква', 'kre',
                     'kvæk', 'græbæk', 'kurr', 'cro', 'gribbit', 'quaaak', 'κουάξ', 'cuacs', 'krooks', 'อ๊บๆ',
                     'vrak', 'cra', 'মক', 'cva', 'kwaak', 'ribbit', 'ケロ', 'beka']

    #codeList2 = ['☉', '☆', '☺', '♾', '⚠', '♲']

    codeDict = {}  # {a,b,c,x : international frog syllable}

    createDictEntry('a', codeList, codeDict)
    createDictEntry('b', codeList, codeDict)
    createDictEntry('c', codeList, codeDict)
    createDictEntry('d', codeList, codeDict)
    createDictEntry('e', codeList, codeDict)
    createDictEntry('f', codeList, codeDict)
    # createDictEntry('g', codeList, codeDict)
    # createDictEntry('h', codeList, codeDict)
    # createDictEntry('i', codeList, codeDict)
    # createDictEntry('j', codeList, codeDict)
    # createDictEntry('k', codeList, codeDict)
    # createDictEntry('l', codeList, codeDict)
    codeDict['x'] = codeList
    codeValues = makeCodeValues(codeDict)  # {syllable : corresponding codeDict index}

    # initialize frogs & frogList
    frog1 = Frog.frog('frog1', "xxxxxxxxxx", codeDict)
    frog2 = Frog.frog('frog2', "xxxxxxxxxx", codeDict)
    frog3 = Frog.frog('frog3', "xxxxxxxxxx", codeDict)
    frog4 = Frog.frog('frog4', "xxxxxxxxxx", codeDict)
    frog5 = Frog.frog('frog5', "xxxxxxxxxx", codeDict)
    frog6 = Frog.frog('frog6', "xxxxxxxxxx", codeDict)
    frog7 = Frog.frog('frog7', "xxxxxxxxxx", codeDict)
    frog8 = Frog.frog('frog8', "xxxxxxxxxx", codeDict)
    frog9 = Frog.frog('frog9', "xxxxxxxxxx", codeDict)
    frog10 = Frog.frog('frog10', "xxxxxxxxxx", codeDict)
    frogList = [frog1, frog2, frog3, frog4, frog5, frog6, frog7, frog8, frog9, frog10]
    flCopy = [frog1, frog2, frog3, frog4, frog5, frog6, frog7, frog8, frog9, frog10]  # stays ordered for printing

    s = storage()
    s.fill(codeDict, codeList, codeValues, frogList, flCopy)

    #for i in range (1, 100):
    #    pondToString(flCopy, frogList, codeValues)
    s.setLoop(timer.set_interval(doIt, 200))

#returns a dictionary of counts for each of this frog's syllables
def getCodeCounts(frog, codeValues):
    codeCounts = {} #{syllable: counts for this frog}
    for syllable in frog.getCallList():
        if syllable in codeCounts.keys():
            codeCounts[syllable] += 1
        else:
            codeCounts[syllable] = 1
    return codeCounts

#makes all frogs "tweet" (this was going to be a network of twitterbots at one point)
def everyoneTweet(frogList):
    for frog in frogList:
        print(frog.getName(), ':', frog.getCall())

#randomly adds an international frog syllable to codeList, indexed at the given code key
def createDictEntry(key, codeList, dict):
    index = random.randint(0, len(codeList)-1)
    dict[key] = codeList[index]
    #codeList.remove(codeList[index]) this line optionally disallows a,b,c from being randomly selected

#creates the inverse of codeDict ({syllable : key in codeDict})
def makeCodeValues(codeDict):
    codeValues = {}
    for key in codeDict:
        if key != 'x':
            codeValues[codeDict[key]] = key
        elif key == 'x':
            for otherSyllable in codeDict[key]:
                if otherSyllable not in codeValues.keys():
                    codeValues[otherSyllable] = key
    return codeValues

def getMostProminentSyllable(frog, codeValues):
    # gets this frog's most prominent syllable + its count
    frogMaxSyll = ''
    frogMaxCount = 0
    frogCodeCounts = getCodeCounts(frog, codeValues)  # {syllable: counts for this frog}
    for x in frogCodeCounts.keys():
        if frogCodeCounts[x] > frogMaxCount:
            frogMaxCount = frogCodeCounts[x]
            frogMaxSyll = x
    return frogMaxSyll

#finds a friend for this frog to imitate, and changes its code accordingly
def findBestMatch(frog, frogList, codeValues):
    stor = storage()
    matchCounts = {} #{syllable : number of frogs with this as their most prominent syllable}

    #populate matchCounts
    for compFrog in frogList: #every frog to compare the "main frog" to
        compFrogProminent = getMostProminentSyllable(compFrog, codeValues)
        if compFrogProminent in matchCounts.keys():
            matchCounts[compFrogProminent] += 1
        else:
            matchCounts[compFrogProminent] = 1

    max = 0
    for y in matchCounts.keys():
        if matchCounts[y] > max:
            max = matchCounts[y]
    newGoal = y  #syllable to add
    #TODO: make this dynamic, not just the same one every time (to encourage clustering/tribes instead of unison)?

    #replace an x with this syllable's key
    oldCode = list(frog.getCode())

    # this is where we can adjust rate of mimicry & all interesting things abt program behavior in general
    chance = random.randint(0, 100)
    randomRemoval = random.randint(0, (len(oldCode)-1))
    if chance > 60:
        if 'x' in oldCode: #maybe change to elif
            oldCode.remove('x')
            randomRemoval -= 1
            #TODO: add an interesting else here
        elif chance > 95 and (randomRemoval < len(oldCode) and randomRemoval > 0):
            oldCode.remove(oldCode[randomRemoval])
        if(len(oldCode) < storage.MAX_CALL_LENGTH):
            oldCode.append(codeValues[newGoal])
        newCode = ''.join(oldCode)
        frog.setCode(newCode)
        frog.refreshCall()
    return newGoal #the syllable added (or almost added)

def pondToString(orderedList, shuffleList, codeValues):
    random.shuffle(shuffleList)
    stor = storage()
    for frog in shuffleList:
        findBestMatch(frog, shuffleList, codeValues)
    s = 'Turn: ' + stor.getTurn() + '<br>'
    for frog in orderedList:
        f = ''
        f += frog.getName()
        f += ' : '
        f += frog.getCall()
        f += '\n'
        f += '<br>'
        #document[frog.getName()] <= f
        s += f #so that we can manipulate just one frog's status
    stor.nextTurn()
    return s
#      document['frog'] <= s

def pondToDict(orderedList, shuffleList, codeValues):
    pondDict = {}
    #random.shuffle(shuffleList)
    stor = storage()
    for frog in shuffleList:
        findBestMatch(frog, shuffleList, codeValues)
    for frog in orderedList:
        f = ''
        f += frog.getName()
        f += ' : '
        f += frog.getCall()
        f += '\n'
        f += '<br>'
        pondDict[frog.getName()] = f
    stor.nextTurn()
    stor.setPD(pondDict)

def doIt():
    s = storage()
    #document['frog'].html = pondToString(s.flCopy, s.frogList, s.codeValues)
    pondToDict(s.flCopy, s.frogList, s.codeValues)
    print(len(s.getPD().keys()))
    for frog in s.pondDict.keys():
        print(frog)
        document[frog].html = s.pondDict[frog]

    if s.turn > 1100:
        timer.clear_interval(s.loop)
main()