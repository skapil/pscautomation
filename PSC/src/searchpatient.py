#!/usr/bin/python

#This script is to search all the patient from searchpatient.csv file

#Import all the libraries to run the script
import performaction
import takescreenshot

def searchPatient(firstname,lastname,dob):
    onepatient = []
    onepatient = {'FirstName':firstname,'LastName':lastname,'DOB':dob}
    getPatientInfo(onepatient)    

def getPatientInfo(onepatient):       
    for patient_key in onepatient:
        print onepatient, onepatient["FirstName"]
        performaction.before_starting_test()    
        performaction.typeValue("lastnamesearch.png", onepatient["LastName"])
        performaction.typeValue("firstnamesearch.png",onepatient["FirstName"])
        performaction.typeValue("searchdob.png", onepatient["DOB"])
        performaction.clickItem("searchpatient.png")
        takescreenshot.takeScreenshot("searchpatientscreen.png")       
        print 'Search completed for patient \n'
        return