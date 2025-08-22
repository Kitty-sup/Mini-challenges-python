#!/usr/bin/env python
# coding: utf-8

# In[8]:


import csv,os



# In[2]:


class Patient:
    def __init__(self, idd, name, age, gender, disease):
        self.idd = idd
        self.name = name
        self.age = age
        self.gender = gender
        self.disease = disease
    def add_patient(self):
        return f"Patient {self.name} (ID: {self.idd}) added successfully"
    def update_patient(self,name=None,age=None,gender=None,disease=None):
        if name:
            self.name = name
        if age:
            self.age = age
        if gender:
            self.gender = gender
        if disease:
            self.disease =  disease
        return f"Patient {self.idd} is updatedddddd"
    def view_patient(self):
        return f"{self.idd} | Name: {self.name} | Age: {self.age} | Gender: {self.gender} | Disease: {self.disease}"


# In[1]:


class Doctor:
    def __init__(self, idd, name, specialization):
        self.idd = idd
        self.name = name
        self.specialization = specialization
        
    def add_doctor(self):
        return f"Doctor {self.name} (ID: {self.idd}) added successfully"
    def update_doctor(self,name=None,specialization=None):
        if name:
            self.name = name
        if specialization:
            self.specialization = specialization
        return f"Doctor {self.idd} is updatedddddd"
    def view_doctor(self):
        return f"{self.idd} | Name: {self.name} | specialization: {self.specialization}"


# In[4]:


class Appointment:
    def __init__(self, idd ,patient_id, doctor_id, date, status="scheduled"):
        self.idd = idd
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.status = status
    def schedule(self):
        self.status = "Scheduled"
        return f"{self.patient_id} is appointed to {self.doctor_id} on {self.date}"
    def cencal(self):
        self.status = "Cencal"
        return f"{self.idd} appointment has been cencallllllllll"
    def view_appointment(self):
        return f"Appointment id {self.idd} | Patient id: {self.patient_id} | : Doctor id: {self.doctor_id} | Date: {self.date} | Status: {self.status}"


# In[ ]:





# In[5]:


class Hospital_System:
    def __init__(self):
        self.patients = {}
        self.doctors = {}
        self.appointments = {}
        
    def save_patients(self):
        with open("patients.csv","w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID","Name","Age","Gender","Disease"])
            for p in self.patients.values():
                writer.writerow([p.idd,p.name,p.age,p.gender,p.disease])
    
    def save_doctors(self):
        with open("doctors.csv","w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID","Name","Specialization"])
            for d in self.doctors.values():
                writer.writerow([d.idd,d.name,d.specialization])
    
    def save_appointments(self):
        with open("appointments.csv","w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID" ,"Patient ID","Doctor ID","Date", "Status"])
            for a in self.appointments.values():
                writer.writerow([a.idd ,a.patient_id, a.doctor_id, a.date, a.status])
    
    def add_patient(self,patient):
        self.patients[patient.idd] = patient
        return f"Patient idd {patient.idd} is addeddddd"
    def view_patients(self):
        if not self.patients:
            return "No Patients Foundddd"
        return "\n". join([p.view_patient() for p in self.patients.values()])
    
    def add_doctor(self,doctor):
        self.doctors[doctor.idd] = doctor
        return f"Docter {doctor.idd} is addddddddd"
    def view_doctor(self):
        if not self.doctors:
            return "No Doctor related data is foundddddddd"
        return "\n".join(d.view_doctor() for d in self.doctors.values())
    
    def schedule_appointment(self, appointment):
        if appointment.patient_id not in self.patients:
            return "No patient found"
        if appointment.doctor_id not in self.doctors:
            return "No doctor found"
        self.appointments[appointment.idd] = appointment
        return appointment.schedule()
    def view_appointment(self):
        if not self.appointments:
            return "No data in appointment"
        return "\n".join(a.view_appointment() for a in self.appointments.values())
    

