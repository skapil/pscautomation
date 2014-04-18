#!/usr/bin/python

#This script is to test the psc

#Import the libraries
import performaction
import takescreenshot
import addnewpatient
import addinsurance
import parsepatientdata
import addadditionalinfo
from datetime import datetime

def runTest():    
    allpatientdata = parsepatientdata.addNewPatient()
    for onepatient in allpatientdata:
        addAdditionalInformation(onepatient['FirstName'],onepatient['LastName'],onepatient['DateOfBirth'])              
        performaction.clickItem("dashboard_button.png")
        if(performaction.isImageDisplay("confirm_ok_button.png")):
            performaction.clickItem("confirm_ok_button.png")
        addnewpatient.searchNewPatient(onepatient)
        if not (performaction.isImageDisplay("nopatientfound.png")):
            print "Patient already exist...Search for other patient\n"
            continue
        flag = addnewpatient.select_new_patient()
        if not flag:
            print 'Not able to add the patient because not able to found the Add Patient image'
            print 'Exiting form the test'
            exit()    
        addnewpatient.addNewPatient(onepatient)   
        allpatientdata = parsepatientdata.addInsurance()  
        addinsurance.clickAddInsurance()
        if not performaction.isImageDisplay("addinsurance_page.png"):
            print 'Not able to found the add insurance button'
            continue  
        addinsurance.addNewInsurance('all')
        takescreenshot.takeScreenshot('insuranceadded_'+str(datetime.now().strftime('%Y%m%d_%H_%M_%S'))+'.png')
        performaction.clickItem("next.png")
        addAdditionalInformation(onepatient['FirstName'],onepatient['LastName'],onepatient['DateOfBirth'])
        addnewpatient.deshboardScreen()
        if(performaction.isImageDisplay("confirm_ok_button.png")):
            performaction.clickItem("confirm_ok_button.png")

def addAdditionalInformation(firstname,lastname,dob):
    flag = False
    allrecords = parsepatientdata.addAddress()
    for single_record in allrecords:
        if(firstname == single_record['FirstName']) and (lastname == single_record['LastName']) and (dob == single_record['DateOfBirth']):
            addadditionalinfo.addPatientAddress(single_record)
            flag = True
            break
    if flag == False:
        for single_record in allrecords:
            if('' == single_record['FirstName']) and ('' == single_record['LastName']) and ('' == single_record['DOB']):
                print "This is default address for all the patient"
                addadditionalinfo.addPatientAddress(single_record)
                break

        
        

if __name__=='__main__':
    runTest()