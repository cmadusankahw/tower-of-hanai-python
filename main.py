#recursive solution
def tower(numRings):
    def tower1(numRings,fromPeg,toPeg,usePeg):
        if numRings > 0: #A
            tower1(numRings-1,fromPeg,usePeg,toPeg) #B
            result.append((fromPeg,toPeg)) #C
            tower1(numRings-1,usePeg,toPeg,fromPeg) #D
    result = []
    tower1(numRings,0,1,2)
    return result

#iterative solution
def tower(numRings):
    result = []
    stk = []
    def tower1(numRings):
        In, To = 0, 1
        stk.append((In,numRings,0,1,2))
        while stk:
            state,numRings,fromPeg,toPeg,usePeg = stk.pop()
            if state == In:
                if numRings != 0: #push down to 1 numRing #A
                    stk.append((To,numRings,fromPeg,toPeg,usePeg)) #B save state
                    stk.append((In,numRings-1,fromPeg,usePeg,toPeg))
            elif state == To:
                result.append((fromPeg,toPeg)) #C
                stk.append((In,numRings-1,usePeg,toPeg,fromPeg)) #D
            else:
                print('Error: logic')
                return result
    tower1(numRings)
    return result

a = [1,2,3,4]
for n in a:
    print('rings', n)
    print(tower(n))

