

def containsMoreThanOne(sequence, of):
#    print("seq: " + ",".join(sequence))
#    print("of: " + ",".join(of))
    found = False
    for it in of:
        if sequence.count(it) == 1 and found == False:
#            print("first found: " + it)
            found = True
        elif sequence.count(it) == 1 and found == True:
#            print("secound found: " + it)
            return True
    return False