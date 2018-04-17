# import re
#
# fin = open("in.txt", 'r') # in file
# fout = open("out.txt", 'w') # out file
# for line in fin:
#     p = re.compile('[-][0-9]*[.][0-9]*[,]|[-][0-9]*[,]') # pattern
#     newline = p.sub('',line) # replace matching strings with empty string
#     print (newline)
#     fout.write(newline)
# fin.close()
# fout.close()

def det_by_lu(y, x):
    y[0] = 1.

    N = x.shape[0]
    for k in range(N):
        y[0] *= x[k,k]
        for i in range(k+1, N):
            x[i,k] /= x[k,k]
            for j in range(k+1, N):
                x[i,j] -= x[i,k] * x[k,j]
det_by_lu(10, 10)