#!/usr/bin/python

#This script is to search all the patient from searchpatient.csv file

#Import all the libraries to run the script
import parsepatientdata
import performaction
import takescreenshot

class SearchPatientTest:
    allpatientdata = []
    
    def __init__(self):
        self.allpatientdata = parsepatientdata.provideSearchData()
    
    def getPatientInfo(self):
        for onepatient in self.allpatientdata:
            self.runTest(onepatient)
            print onepatient
    
    def runTest(self,onepatient):
        for patient_key in onepatient:
            performaction.before_starting_test()    
            performaction.typeValue("lastnamesearch.png", onepatient["LastName"])
            performaction.typeValue("firstnamesearch.png",onepatient["FirstName"])
            performaction.typeValue("searchdob.png", onepatient["DOB"])
            performaction.clickItem("searchpatient.png")
            takescreenshot.takeScreenshot("searchpatientscreen.png")
            performaction.clickItem("searchresult_onepatient.png")
            performaction.clickItem("searchpage_next.png")
            performaction.clickItem("basicpatientinfo_button.png")
            performaction.clickItem("confirm_ok_button.png")
            performaction.clickItem("dashboard_button.png")
            performaction.clickItem("confirm_ok_button.png")
            print 'Search completed for patient \n'
            return
                            
 
if __name__=='__main__':
    print "-----------------Starting the Search Patient Test-------------------"
    searchtest = SearchPatientTest()
    searchtest.getPatientInfo()
                
        
    
    
        