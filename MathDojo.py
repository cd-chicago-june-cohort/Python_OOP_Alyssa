class MathDojo(object):
    def __init__(self):
        self.total = 0
    def result(self):
        return self.total
    def add(self, *x):
        for i in range (0, len(x)):
            if type(x[i]) == list or type(x[i]) == tuple:
                for j in range(0, len(x[i])):
                    self.total += x[i][j]
            else:
                self.total += x[i]
        return self
    def subtract(self, *y):
        for k in range (0, len(y)):
            if type(y[k]) == list or type(y[k]) == tuple:
                for l in range(0, len(y[k])):
                    self.total -= y[k][l]
            else:
                self.total -= y[k]
        return self


# Testing part 1
print "Expected result for Part I is '4'"
print "Actual result =", MathDojo().add(2).add(2, 5).subtract(3, 2).result()

# Testing part 2
print "Expected result for Part II is '28.15'"
print "Actual result =", MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result()

# Testing part 3 (same as part 2, but all arguements that were lists have been changed to tuples)
print "Expected result for Part III is '28.15'"
print "Actual result =", MathDojo().add((1),3,4).add((3, 5, 7, 8), (2, 4.3, 1.25)).subtract(2, (2,3), (1.1, 2.3)).result()
