#!/usr/bin/python

#This script prforme the action as typing and clicking on perticular image

#Import libraries here
from sikuli import *
import locations
from time import sleep
import shutil

def before_starting_test():
    print 'Please make sure application screen is display on desktop'

def isImageDisplay(imagename):
    s = Screen(0)
    imagelocation = locations.getImageLocation(imagename)
    if not s.exists(imagelocation):
        print "Screen doesn't display ... Waiting for 10 seconds to display image\n"
        sleep(10)
    if s.exists(imagelocation):
        print "Screen display"
        return True
    if not s.exists(imagelocation):
        print "Screen doesn't display"
        return False

def typeValue(imagename,value):
    print "Waiting for 2 seconds before looking for the screen\n"
    sleep(2)    
    imagelocation = locations.getImageLocation(imagename)
    s = Screen(0)
    if (isImageDisplay(imagename)):
        print "Waiting for 2 seconds before typing into the text field"
        sleep(2)
        print "Clearing the text field, before enter the value"
        s.type(imagelocation,value)
    else:
        print "Not able to type on screen....as screen hasn't found\n"
    
def clickItem(imagename):
    print "Waiting for 2 seconds before looking for the screen\n"
    sleep(2)
    imagelocation = locations.getImageLocation(imagename)
    s = Screen(0)
    if(isImageDisplay(imagename)):
        print "Waiting for 2 seconds before selecting the button or image"
        sleep(2)
        s.click(imagelocation)
    else:
        print "Not able to find the scren.... as image hasn't found on screen"

def captureScreen(imagename):
    print "Waiting for 2 seconds before looking for the screen \n"
    sleep(2)
    s = Screen(0)
    print "Capturing the screen----\n"
    #Take Screen shot and move it from temp folder to new location <path>
    shutil.move(s.capture(Screen()), locations.getImageTempLocation(imagename)) 
    
def multipleImageType(imagename,imagenumber,value):
    count = 0
    s = Screen(0)
    #isImageDisplay(imagename)
    for i in s.findAll(locations.getImageLocation(imagename)):
        count += 1
        if count == imagenumber:
            typeValue(imagenumber,value)        
    print 'Number of images found ',count
    

def multipleImageClick(imagename,imagenumber):
    count = 0
    s = Screen(0)
    #isImageDisplay(imagename)
    for i in s.findAll(locations.getImageLocation(imagename)):
        count += 1
        if count == imagenumber:
            clickItem(imagenumber)        
    print 'Number of images found ',count
  

if __name__=="__main__":    
    before_starting_test()    
    typeValue("lastnamesearch.png","Germany")
    typeValue("firstnamesearch.png","Berlin")
    typeValue("searchdob.png","07/25/1970")
    clickItem("py.png")
    captureScreen("Searchpatientscreen.png")
    clickItem("searchresult_onepatient.png")
    clickItem("searchpage_next.png")
  
     

