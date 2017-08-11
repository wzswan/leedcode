print "enter a num"
k= int(raw_input())
l = 3*(2**k -1)
print l
print "enter a n"
n = int(raw_input())
if n <= k:
    print"A"
elif n>= (l- k):
    print"C"
else:
    div(l, n)
