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
        newFrob.before = atMe
        print "IF"
        temp = atMe
        found = False
        while temp.after and newFrob.name < temp.after.name:
            temp = temp.after
            print "WHILE", temp.name
            found = True
        temp.after = newFrob
        if found:
            atMe.after = newFrob
            newFrob.after = temp

    else:
        print "ELSE"
        newFrob.after = atMe
        while atMe.before and newFrob.name > atMe.before.name:
            atMe = atMe.before
            print "WHILE"
        atMe.before = newFrob

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
print martha.before, martha.after.name
print ruth.before.name, ruth.after.name





