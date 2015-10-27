class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None

    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before

    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after

    def getBefore(self):
        return self.before

    def getAfter(self):
        return self.after

    def myName(self):
        return self.name

def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links?
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.
    """
    print atMe.name, newFrob.name
    if atMe.name < newFrob.name:
        print "IF"
        newFrob.before = atMe
        temp = atMe
        found = False
        while temp.after and newFrob.name > temp.after.name:
            temp = temp.after
            found = True
        print temp.name
        if found:
            newFrob.before = temp
            newFrob.after  = temp.after
            if temp.after:
                temp.after.before = newFrob
            temp.after = newFrob
        else:
            newFrob.before = atMe
            newFrob.after = atMe.after
            if atMe.after:
                atMe.after.before = newFrob
            atMe.after = newFrob
        # if found:
        #     atMe.after = newFrob
        #     temp.before = newFrob
        #     newFrob.after = temp
        # else:
        #     temp.after = newFrob
    else:
        print "IF"
        newFrob.after = atMe
        temp = atMe
        found = False
        while temp.before and newFrob.name < temp.before.name:
            temp = temp.before
            found = True
        print temp.name
        if found:
            newFrob.after = temp
            newFrob.before = temp.before
            if temp.before:
                temp.before.after = newFrob
            temp.before = newFrob
        else:
            newFrob.after = atMe
            newFrob.before = atMe.before
            if atMe.before:
                atMe.before.after = newFrob
            atMe.before = newFrob

def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list
    """
    if not start.before:
        return start
    return findFront(start.before)

eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
martha = Frob('martha')

insert(eric, andrew)
insert(eric, ruth)
insert(eric, fred)
insert(ruth, martha)
print "*******************************"
print andrew.before, andrew.after.name
print eric.before.name, eric.after.name
print fred.before.name, fred.after.name
print martha.before.name, martha.after.name
print ruth.before.name, ruth.after
print "*******************************"

allison = Frob('allison')
lyla = Frob("lyla")
christina =Frob("christina")
ben = Frob("ben")
#insert(allison, lyla)
#insert(allison, christina)
#insert(allison, ben)
#print "*******************************"
#print allison.before, allison.after.name
#print ben.before.name, ben.after.name
#print christina.before.name, christina.after.name
#print lyla.before.name, lyla.after
#print "*******************************"

lenoid = Frob('leonid')
a = Frob('amara')
j1 = Frob('jennifer')
j2 = Frob('jennifer')
s = Frob('scott')

insert(lenoid, s)
insert(s, j1)
print "*******************************"
print j1.before, j1.after.name
print lenoid.before.name, lenoid.after.name
print s.before.name, s.after
print "*******************************"



