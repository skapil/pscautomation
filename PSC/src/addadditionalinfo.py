#!/usr/bin/python

#This to add the mailing address, Billing Address, Guardian Info and Emergency Contact

import performaction
import locations

def addPatientAddress(patientaddress):
    if(performaction.isImageDisplay("additionalinfopage.png")):
        performaction.typeValue("additionalinfo_street1_mailing.png", patientaddress['MailingStreet1'])
        performaction.multipleImageType("additionalinfo_street2", 2, patientaddress['MailingStreet2'])
        performaction.multipleImageType("additionalinfo_zipcode.png", 2, patientaddress['MailingZipCode'])
        performaction.multipleImageType("additionalinfo_city.png", 2, patientaddress['MailingCity'])
        performaction.multipleImageType("additionalinfo_state.png", 2, patientaddress['MailingState'])
        if (patientaddress['Billing-Same_as_mailing_address'] == 'yes') or (patientaddress['Billing-Same_as_mailing_address'] == 'Yes'):
            performaction.clickItem("sameasmailingaddress.png")
        else:
            performaction.typeValue("additionalinfo_street1_billing.png", patientaddress['MailingStreet1'])
            performaction.multipleImageType("additionalinfo_street2", 1, patientaddress['MailingStreet2'])
            performaction.multipleImageType("additionalinfo_zipcode.png", 1, patientaddress['MailingZipCode'])
            performaction.multipleImageType("additionalinfo_city.png", 1, patientaddress['MailingCity'])
            performaction.multipleImageType("additionalinfo_state.png", 1, patientaddress['MailingState'])
    