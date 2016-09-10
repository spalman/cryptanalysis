# here is example code how to use my methods
# later there will be code of main process 

file_name = "eng.txt"
f = open(file_name)
cript = f.read().upper()

c = get_list(cript)
FD = get_freq(c)

###############################################

# method 0 for text cript
# method 1 for numeric Polybius square cript 
def get_list(cript, method=0):
    a = []
    if method==0:
        a = list(cript)
    elif method==1:
        for i,v in enumerate(l):
            if i%2==0:
                a.append(v)
            else:
                a[-1] += v
    return a

# cript must be a list from get_list method
def get_freq(cript):
    l = list(set(cript))
    clen = len(cript)+.0
    freq_dic = {}
    for x in l:
        freq_dic[x]=0
    for x in cript:
        freq_dic[x] += 1
    for x in l:
        freq_dic[x] /= clen
    return freq_dic
