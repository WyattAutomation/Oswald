#This is a class with methods copied directly from hikaruAI's work here (all comments are my own):
#https://github.com/hikaruAi/FacebookBot/blob/master/FacebookWebBot.py

#It got me started on building Oswald, and these worked well enough that
#I found it pointless to change them into "my own", so I just chopped it down
#to a couple bare neccessities for my project.  Kudos to hikaruAI for getting 
#me addicted to making bots with Selenium! 

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import os
import json

#url for your own profile
selfProfile = "https://mbasic.facebook.com/profile.php?fref=pb"

#phantom.js settings
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
    "(KHTML, like Gecko) Chrome/15.0.87"
)

#class for the selenium bot, with methods for login and comments 
class fbbot(webdriver.PhantomJS):

    #initialize the phantom.js webdriver
    def __init__(self):
        webdriver.PhantomJS.__init__(self, desired_capabilities=dcap)

    #login method, returns false on an exception
    def login(self, email, password):
        url = "https://mbasic.facebook.com"
        self.get(url)
        email_element = self.find_element_by_name("email")
        email_element.send_keys(email)
        pass_element = self.find_element_by_name("pass")
        pass_element.send_keys(password)
        pass_element.send_keys(Keys.ENTER)
        try:
            print("Logged in")
            return True
        except NoSuchElementException as e:
            print("Fail to login")
            return False

    #comment method, returns an error message with the post url if it can't comment
    def commentInPost(self, postUrl, text):
        """Comment a text(str) in a post(str)"""
        try:
            self.get(postUrl)
            tb = self.find_element_by_name("comment_text")
            tb.send_keys(text)
            tb.send_keys(Keys.ENTER)
            return True
        except Exception as e:
            print("Can't comment in ", postUrl, "\n->", e)