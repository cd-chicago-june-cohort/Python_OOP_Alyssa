from datetime import datetime

class Call(object):   
    counter = 10000
    def __init__(self, caller_name, caller_phone_no, call_reason, time = datetime.now().time()):
        self.id = Call.counter
        Call.counter += 1
        self.caller_name = caller_name
        self.caller_phone_no = caller_phone_no
        self.time = time
        self.reason = call_reason
        CallCenter.call_list.append(self)
    
    def display(self):
        info = self.__dict__
        order = ['id', 'caller_name', 'caller_phone_no', 'time', 'reason']
        for key in order:
            print key.upper(), '-', info[key]
        return self


class CallCenter(object):
    call_list = []
    def __init__(self):
        self.calls = CallCenter.call_list
        self.queue_size = len(CallCenter.call_list)
    def add(self, caller_name, caller_phone_no, call_reason, time = datetime.now().time()):
        Call(caller_name, caller_phone_no, call_reason, time)
        return self
    def remove(self, phone_number):
        if not phone_number:
            CallCenter.call_list.pop(0)
        else:
            i = 0
            for call in CallCenter.call_list:
                if call.caller_phone_no == phone_number:
                    CallCenter.call_list.pop(i)
                i += 1
        return self
    def info(self):
        for call in CallCenter.call_list:
            print call.id, "--- Caller Name:", call.caller_name, "--- Caller Phone Number:", call.caller_phone_no
        print "QUEUE LENGTH =", self.queue_size
        return self
    def time_order(self):
        times = []
        for call in CallCenter.call_list:
            times.append(call.time)
        CallCenter.call_list = [x for i, x in sorted(zip(times, CallCenter.call_list))]
        return CallCenter.call_list


# Testing
# Insantiate 3 calls
c1 = Call('Alyssa', '5', 'billing')
c2 = Call('Sarah', '8', 'error message')
c3 = Call('Taryn', '12', 'registration')

# Display info for a call
print "-" * 50 
print "Testing the display method for call objects by displaying Sarah's call"
print "-" * 50 
c2.display()

# Instantiate a call center
center = CallCenter()
# Create a call using the call center add method
center.add('Hailee', '3', 'change owner')
# Remove a call using the call center remove method to remove by phone number
center.remove('8')

# Try the info function (should reflect a new call from Hailee and no longer include Sarah's call)
print "-" * 50 
print "Used call center methods to add a call from Hailee and remove the call from Sarah."
print "Testing the call center info method and checking that the add and remove functions worked"
print "-" * 50 
center.info()

# Get the call list to be in the wrong time order
print "-" * 50 
print "Swapped the first and last call in the call list so the earliest call is now last"
temp = CallCenter.call_list[0]
CallCenter.call_list[0] = CallCenter.call_list[len(CallCenter.call_list)-1]
CallCenter.call_list[len(CallCenter.call_list)-1] = temp
print "-" * 50 
center.info()

# Try the time sort function to move Taryn's call to the front of the call list
print "-" * 50 
print "Used the call center time_order method to fix the error in ordering"
print "-" * 50 
center.time_order()
center.info()