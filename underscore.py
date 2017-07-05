class Underscore(object):
    def map(self, list, action):
        # returns a new list all elements of an list according to the action argument
        new_lst = []
        for element in list:
            new_lst.append(action(element))
        return new_lst
    def reduce(self, list, action, memo):
        # applies a target operation iteratively through the list and returns the final value
        for element in list:
            memo = action(element, memo)
        return memo
    def find(self, list, rule):
        # looks through a list, finds the first value that meets a rule and returns it
        for element in list:
            if rule(element):
                return element
        return None
    def filter(self, list, rule):
        # similar to fine, but returns a list of values that meet a rule and returns all of them
        new_list = []
        for element in list:
            if rule(element):
                new_list.append(element)
        return new_list
    def reject(self, list, rule):
        # opposite of filter, returns a list with values that do NOT meet a rule
        new_list = []
        for element in list:
            if not rule(element):
                new_list.append(element)
        return new_list


_ = Underscore() # yes we are setting our instance to a variable that is an underscore

print "-" * 50
print "Map method in action - input was [1,2,3] - function was times 2"
print "-" * 50
print _.map([1,2,3], lambda x: x * 2)
print "-" * 50
print "Reduce method in action - input was [1,2,3] - function was adding"
print "-" * 50
print _.reduce([1,2,3], lambda x, m: m + x, 0)
print "-" * 50
print "Find method in action - input was [1,2,3,4] - rule was divisible by 2"
print "-" * 50
print _.find([1,2,3,4], lambda x: x%2 == 0)
print "-" * 50
print "Filter method in action - input was [1,2,3,4] - rule was divisible by 2"
print "-" * 50
print _.filter([1,2,3,4], lambda x: x%2 == 0)
print "-" * 50
print "Reject method in action - input was [1,2,3,4] - rule was divisible by 2"
print "-" * 50
print _.reject([1,2,3,4], lambda x: x%2 == 0)