#!/usr/bin/python

#This script to add the new patient basic information

#Import the libraries
import performaction
import parsepatientdata
import searchpatient
import takescreenshot

def addNewInsurance(subscribername):
    allpatientdata = parsepatientdata.addInsurance() 
    for patient_key in range(0,len(allpatientdata)):
        clickAddInsurance()
        if not performaction.isImageDisplay("addinsurance_page.png"):
            print 'Not able to found the add insurance button'
            return False         
        performAddInsurance(patient_key,allpatientdata,subscribername)        
    return True

def clickAddInsurance():
    performaction.clickItem("addinsurance_button.png")

def performAddInsurance(patient_key,allpatientdata,subscribername):    
    if(subscribername == allpatientdata[patient_key]['SubscriberFirstName']) or (subscribername == allpatientdata[patient_key]['SubscriberLastName']) or (subscribername == 'all'):
        clickAddInsurance()
        performaction.clickItem("dropdownbox.png")
        if(allpatientdata[patient_key]['PlanType'] == 'PPO'):
            performaction.clickItem("addinsurance_ppo.png")        
        elif(allpatientdata[patient_key]['PlanType'] == 'EPO'):
            performaction.clickItem("addinsurance_epo.png")
        elif(allpatientdata[patient_key]['PlanType'] == 'HMO'):
            performaction.clickItem("addinsurance_hmo.png")
        else:
            performaction.clickItem("addinsurance_other.png")
            performaction.typeValue("addinsurance_otherplantype.png",allpatientdata[patient_key]['PlanType'])
        performaction.typeValue("addinsurance_insuranceprovider.png",allpatientdata[patient_key]['InsuranceProvider'])
        performaction.typeValue("addinsurance_policynumber.png", allpatientdata[patient_key]['PolicyNumber'])
        performaction.typeValue("addinsurance_groupnumber.png", allpatientdata[patient_key]['GroupNumber'])
        takescreenshot.takeScreenshot("addinsuranceinfo.png")
        performaction.clickItem("save.png")
            
        
        

    
    