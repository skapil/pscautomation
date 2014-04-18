#!/usr/bin/python

#This script design to take screenshot of current screen

#Loading libararies in the script
from sikuli import *
import os
from datetime import datetime
import shutil
from time import sleep


def takeScreenshot(imagename):
    capscreen = 'ScreenShots'
    screenshot_dir_loc = os.path.join(os.getcwd(),'..','imgs',capscreen)
    if not (os.path.exists(screenshot_dir_loc)):
        os.makedirs(screenshot_dir_loc)
    currtime = datetime.now().strftime('%Y%m%d_%H_%M_%S')
    screenshot_dir = currtime+"_screenshots"
    screenshots_loc = os.path.join(screenshot_dir_loc,screenshot_dir)
    if not os.path.exists(screenshots_loc):
        os.makedirs(screenshots_loc)
    captureScreen(imagename,screenshots_loc)
    print "Screenshot taken and save here ----> ",screenshots_loc

def captureScreen(imagename,screenshot_loc):
    print "Waiting for 2 seconds before taking the screen \n"
    sleep(2)
    s = Screen(0)
    print "Capturing the screen----\n"
    #Take Screen shot and move it from temp folder to new location <path>
    shutil.move(s.capture(Screen()), screenshot_loc)  
    
    