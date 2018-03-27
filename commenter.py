import time
import sys
import subprocess
import os, signal
from fbbot import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

#Initialize the Chatterbot chatbot, using JSON storage adapter.  
#Chatterbot can be found here: https://chatterbot.readthedocs.io/en/stable/
#My own in-development seq2seq chatbot in Tensorflow will replace this, so hang in there 
botty = ChatBot(
    'Oswald',
    read_only=True,
    storage_adapter='chatterbot.storage.JsonFileStorageAdapter',
    input_adapter='chatterbot.input.VariableInputTypeAdapter',
    output_adapter="chatterbot.output.OutputAdapter",
    output_format="text",
    database='./database.json'
)

#Handling whatever Oswald randomly eats as input that isn't text, 
#in case it flies outside of the Basic Multilingual Plane (emojis etc)
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

#Initializes an instance of the selenium facebook bot class, and logs in, giving it time to do so.
bot=fbbot()
bot.set_page_load_timeout(15)
bot.login("yourfacebookemail@example.com","yourfacebookpassword")

#Script uses mbasic.facebook.com 
#Selenium function to navigate the bot to the mbasic homepage/timeline
bot.get("https://mbasic.facebook.com/home.php?ref_component=mbasic_home_header&ref_page=%2Fwap%2Fhome.php&refid=7")

#	Inifinite loop that scrapes posts on the timeline by xpath, in format u_0_*, 
#	just dumb-loops through u_0_8, u_0_6 and u_0_4 elements in newsfeed, sleeping 800 seconds between posts,
#	which is spread out enough to usually avoid double-posting.  It navigates to the post URL 
#	through a discovered 'Full Story' link, finds the post object 'u_0_0', looks for 
#	a 'p' css selector to find text, i/o's a response to the text through the chatbot, and 
#	posts the response as a comment.  If it fails, it prints a notification to the console
#	Will be replaced by a dynamic listener thread in an update.
while True: 
    ids = [8, 6, 4]
    for i in ids:
        t = '//*[@id="u_0_' + str(i) + '"]'
        b = bot.find_element_by_xpath(t)
        j = b.find_element_by_link_text("Full Story")
        url2 = j.get_attribute('href')
        print(url2)
        bot.get(url2)
        q = bot.find_element_by_xpath('//*[@id="u_0_0"]')
        try:
            m = bot.find_element_by_css_selector("p")
            print(m.text.translate(non_bmp_map))
            bot_input = botty.get_response(m.text.translate(non_bmp_map))
            #print(bot_input)
            bot.commentInPost(url2, str(bot_input))
            time.sleep(800)
            bot.get("https://mbasic.facebook.com/home.php?ref_component=mbasic_home_header&ref_page=%2Fwap%2Fhome.php&refid=7")
        except NoSuchElementException:
            print("post didn't have any text")
            bot.get("https://mbasic.facebook.com/home.php?ref_component=mbasic_home_header&ref_page=%2Fwap%2Fhome.php&refid=7")    
    

#"Error Handling"
os.system("commenter.py")

