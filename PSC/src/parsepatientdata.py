#!/usr/bin/python

#Loading libraries here
import csv
import locations
 
def getFormatedData(keys,filename):
    filelocation = locations.getDataFileLocation(filename)
    search_patient = []
    with open(filelocation,"rb") as csvfile:
      count = 0
      spamreader = csv.reader(csvfile,delimiter=',',quotechar='|')
      for row in spamreader:
          if(count > 0):
              search_patient.append(dict(zip(keys,row)))
          count += 1
    print search_patient
    return search_patient
    
def provideSearchData():    
    keys = ['FirstName','LastName','DOB']
    return getFormatedData(keys,"searchpatient.csv")

def addNewPatient():
    keys = ['FirstName','MiddleName','LastName','DateOfBirth','Gender','ZipCode','MobilePhone','HomePhone','Email','ContactMethod','Communication']
    return getFormatedData(keys,"addbasicinfo.csv")

def addInsurance():
    keys = ['SubscriberFirstName','SubscriberLastName','PlanType','InsuranceProvider','PolicyNumber','GroupNumber']
    return getFormatedData(keys,"addinsurance.csv")

def addAddress():
    keys = ['FirstName','LastName','DOB','MailingStreet1','MailingStree2','MailingZipCode','MailingCity','MailingState','Billing-Same_as_mailing_address','BillingStreet1','BillingStreet2','BillingZipCode','BillingCity','BillingState']
    return getFormatedData(keys,"patientaddress.csv")
    