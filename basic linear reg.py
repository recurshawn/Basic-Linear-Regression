""" BASIC LINEAR REGRESSION CODE
I wrote this to check my understanding of the basic concepts. It's pretty simple
but I needed to get my feet wet with code.

Any suggestions for modifications are welcome!

"""
#x and y datasets
x = [3,4,5,6,7,8,9,10,11,12,13,14]
y = [6,8,10,12,14,16,18,20,22,24,26,28]

#randomly chosen  initial slope and y intercept values
m = 3.0
c = 2.0

#applying gradient to modify m and c to fit the dataset
for i in xrange(100000):
    for k in range(12):
        m = m - 0.01*2*(m*x[k]+c - y[k])*x[k]
        c = c - 0.01*2*(m*x[k]+c - y[k])

#printing the proper values of m and c
print "Slope of line:", m
print "Y-intercept of line:", c

userX = float(raw_input("Enter a x value:"))
userY = m*userX + c

print "y is ",userY
