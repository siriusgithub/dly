# duplicates allowed

def permute(lisstr,staidx,endidx):
    if staidx == endidx:
       print(''.join(lisstr))
    else:
        for idx in range(staidx,endidx+1):
            lisstr[staidx] , lisstr[idx] = lisstr[idx] , lisstr[staidx]
            permute(lisstr,staidx+1,endidx)
            lisstr[staidx] , lisstr[idx] = lisstr[idx] , lisstr[staidx]

string = 'hi!'
lenstr = len(string)
lisstr = list(string)
permute(lisstr,0,lenstr-1)
