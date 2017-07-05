class Patient(object):
    def __init__(self, name, allergies, id = None, bed_no = None):
        self.id = id
        self.name = name
        self.allergies = allergies
        self.bed_no = bed_no
class Hospital(object):
    id = 1
    bed_no = 1
    def __init__(self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity
    def admit (self, patient_name, patient_allergies):
        if len(self.patients) < self.capacity:
            new_patient = Patient(patient_name, patient_allergies, Hospital.id, Hospital.bed_no)
            self.patients.append(new_patient)
            print "{} has been admitted.  They have been placed in bed number {}".format(patient_name, Hospital.bed_no)
            Hospital.id += 1
            Hospital.bed_no += 1
        else:
            print "The hospital is full.  {} has not been admitted".format(patient_name)
        return self
    def discharge (self, patient_name):
        i = 0
        for patient in self.patients:
            if patient.name == patient_name:
                patient.bed_no = None
                self.patients.pop(i)
            i += 1
        return self

# Create an instance of hospital
LGH = Hospital("Lutheran General", 2)

# Use the admit method to create 3 patients.  3rd will be rejected for size
print "-" * 50
print "Using the admit method, we will now attempt to admit 3 patients into a hospital with capacity of 2"
print "-" * 50
LGH.admit('Alyssa', ['a', 'b', 'c'])
LGH.admit('Sarah', 'l')
LGH.admit('Taryn', 'd')

print "-" * 50
print "Here is the list of patient objects - note that there are only 2"
print "-" * 50
print LGH.patients

print "-" * 50
print "Now using the discharge method, we will discharge Alyssa and then reprint the list of patient objects with just 1 patient remaining"
print "-" * 50
LGH.discharge('Alyssa')
print LGH.patients
