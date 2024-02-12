class Patient:
    def __init__(self, patient_id, patient_name, age, gender, contact) -> None:
        self.__patient_id = patient_id
        self.__name = patient_name
        self.__age = age
        self.__gender = gender
        self.__contact = contact
    
    def get_patientDetails(self):
        return {

            'Patient_id': self.__patient_id,
            'Patient': self.__name,
            'Age': self.__age,
            'Gender': self.__gender,
            'Contact': self.__contact

        }
class Doctor:
    def __init__(self, doctor_id, name, specialisation):
        self.__doctor_id = doctor_id
        self.__name = name
        self.__specialisation = specialisation

    def get_doctorDetails(self):
        return {

            "Doctor_iD" : self.__doctor_id,
            "Name" : self.__name,
            "Specialisation" : self.__specialisation

        }
class Medical_Record():
    def __init__(self):
        self.__records = {}

    def add_record(self, patient_name, doctor_name, diagnosis, medication):
        self.__records[patient_name.get_patientDetails()['Patient']] = {"Patient" : patient_name.get_patientDetails(),
                                                                  "Doctor" : doctor_name.get_doctorDetails(),
                                                                  "Diagnosis" : diagnosis,
                                                                  "Medication" : medication}
        
    def get_records(self):
        return self.__records



# driver code
patient1 = Patient(1, "Sameer", 23, "male", "+919876567487")
patient2 = Patient(2, "Lucky", 15, "male", "+917076577485")
patient3c = Patient(3, "Sameer", 25, "male", "+917076576457")
print(patient1.get_patientDetails()['Name'])

doctor1 = Doctor(1, "Dr. RK Singh", "Neurologist")
print(doctor1.get_doctorDetails()['Name'])

record = Medical_Record()
record.add_record(patient1, doctor1, "Heart disease", "Aspirin")
print(record.get_records())

name = input("Enter Patient Name: ")
for i in record.get_records():
    if record.get_records()[i]["Patient"]['Patient_id'] == name:
        print(record.get_records()[i]["Name"])

