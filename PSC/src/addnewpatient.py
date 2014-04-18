#!/usr/bin/python

#This script to add the new patient basic information

#Import the libraries
import performaction
import parsepatientdata
import searchpatient
import takescreenshot

    
#Select Add New Patient image
def select_new_patient():
    if not performaction.isImageDisplay("addnewpatient.png"):
        print "Image not found.... skipping this user to add\n"
        return False
    performaction.clickItem("addnewpatient.png")
    return True

def addNewPatient(onepatient): 
    add_patient_info(onepatient)
    print onepatient
 
        
def deshboardScreen():
    performaction.clickItem("dashboard_button.png")

def searchNewPatient(onepatient):
    firstname = None
    lastname = None
    dob = None
    for patient_key in onepatient:
        firstname = onepatient['FirstName']
        lastname = onepatient['LastName']
        dob = onepatient['DateOfBirth']
    print 'Performing the search for the given patient'
    searchpatient.searchPatient(firstname, lastname, dob)
    print 'Search done for given patient'
        
#Provide information to patient
def add_patient_info(onepatient):
   # for patient_key in onepatient:
    performaction.before_starting_test() 
    performaction.typeValue("addnewpatient_middlename.png", onepatient['MiddleName'])
    if (onepatient['Gender'] == 'Male'):
        performaction.clickItem("addnewpatient_male.png")
    else:
        performaction.clickItem("addnewpatient_female.png")
    performaction.typeValue("addnewpatient_zipcode.png", onepatient["ZipCode"])
    performaction.typeValue("addnewpatient_mobile.png", onepatient['MobilePhone'])
    performaction.typeValue("addnewpatient_home.png", onepatient["HomePhone"])
    performaction.typeValue("addnewpatient_email.png", onepatient['Email'])
    if (onepatient['ContactMethod'] == 'Mobile'):
        performaction.typeValue("addnewpatient_mobile_preferred.png", onepatient['ContactMethod'])
    if (onepatient['ContactMethod'] == 'Phone'):
        performaction.typeValue("addnewpatient_home_preferred.png", onepatient['ContactMethod'])
    if (onepatient['ContactMethod'] == 'SMS'):
        performaction.typeValue("addnewpatient_sms_preferred.png", onepatient['ContactMethod'])
    if (onepatient['ContactMethod'] == 'Email'):
        performaction.typeValue("addnewpatient_email_preferred.png", onepatient['ContactMethod'])
    performaction.clickItem("save.png")
    print 'Taking the Screenshot of the screen'
    takescreenshot.takeScreenshot("BasicInfopage.png")
        
            
if __name__=='__main__':   
    addNewPatient()
    deshboardScreen()
    
    
    
             
        
    