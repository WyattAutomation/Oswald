#This is a class with some of the method's copied from hikaruAI's work here:
#https://github.com/hikaruAi/FacebookBot/blob/master/FacebookWebBot.py
#I've rebuilt it to fit my purposes of passing text i/o through a chatbot 

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import os
import json
import sys

#anything outside the BMP like emojis etc can cause issues; this is for handling that
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

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
    
    #logout method
    def logout(self):
        url = "https://mbasic.facebook.com/logout.php?h=AffSEUYT5RsM6bkY&t=1446949608&ref_component=mbasic_footer&ref_page=%2Fwap%2Fhome.php&refid=7"
        try:
            self.get(url)
            return True
        except Exception as e:
            print("Failed to log out ->\n", e)
        return False

    #comment in post method.
    #returns an error message with the post url if it can't comment
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

    #comment reply commenter method.
    #Grabs text from the latest comment in a comment reply.
    #Navigates to the URL gathered from a "replied to your comment" notification
    #will use commentInPost once I've built my own RNN
    def commentReplyCommenter(self, comRepUrl, msg = None):
        #navigate to the current link
        self.get(comRepUrl)
        #skip to the latest reply in the thread        
        t = self.find_element_by_class_name("z")
        fg = t.find_elements_by_xpath("//div[@class='bj']")
        p = fg[-1]
        self.msg = p.text
        #print it to the console, translating any emjoi's 
        print(p.text.translate(non_bmp_map))

#tag replier functions, to get the direct url to respond to tags in a comment-reply
#Duplicate to handle alternate occurances of .cx/.co css selector element
    def tagReplier(self, tagRepUrl, repUrl = None):
        self.get(tagRepUrl)
        fg = self.find_elements_by_css_selector(".cx")
        print(fg)
        p = fg[-1]
        gg = p.find_element_by_link_text("Reply")     
        self.repUrl = gg.get_attribute("href")
        e = gg.get_attribute("href")
        print(e)

    def tagReplier2(self, tagRepUrl, repUrl = None):
        self.get(tagRepUrl)
        fg = self.find_elements_by_css_selector(".co")
        print(fg)
        p = fg[-1]
        gg = p.find_element_by_link_text("Reply")      
        self.repUrl = gg.get_attribute("href")
        e = gg.get_attribute("href")
        print(e)

    #currently inactive method for listener, for when I replace pender's RNN chatbot with my own
#    def listenForNotifications(self, notifurl):        
#        last_link = (None)
#        while True:
#            self.get(notifurl)
#            b = self.find_element_by_xpath('//*[@id="notifications_list"]')
#            link = self.find_element_by_class_name("by")
#            #self.url = self.link.get_attribute("href")
#            #self.last_link = self.url
#            url1 = link.get_attribute("href")
#            txt = link.text
#            if last_link != url1:
#                print(url1)
#                if 'replied' in txt and url1 != (None):
#                    self.commentReplyCommenter(url1)
#            time.sleep(10)
#            last_link = url1
    


