#!/usr/bin/python

#This file will return the current location, image location and log file location.

#Importing the libararies
import os
import yaml

def getCurrentLocation():
    return os.getcwd() 

def getImageLocation(imagename):
    return os.path.abspath(os.path.join(getCurrentLocation(),'..','imgs',imagename))

def getDataLocation():
    return os.path.abspath(os.path.join((os.getcwd()),'..','data'))

def getDataFileLocation(nameoffile):
    return (os.path.join(getDataLocation(),nameoffile))

def getImageTempLocation(imagename):
    return os.path.abspath(os.path.join(getCurrentLocation(),'..','imgs','temp'))





