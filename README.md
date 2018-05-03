## Oswald

The Point of This Project:
  To fully-automate the activity of a Facebook Profile, using a combination of Web-Scraping and Neural Networks, and without using the Facebook API.  Ideally, the end-goal is to make a fully automatic, easy to use bot for Facebook, that doesn't require anything beyond a few programming dependecies except a username and password to a Facebook profile.  No API keys, no signing up for Facebook for Developers and having to "create an app", no huge libraries of scraping functions that are only really useful for static, spam bots; just a dynamically interactive bot that you can plug credentials in to and let it rock.  **This is still VERY much a WIP, so keep that in mind!**  




*Latest Update 4/25/18 - Description of NEW functionality:*


I found a decent pretrained RNN seq2seq/LSTM chatbot model here, and replaced the command line interface to input/output text with the webscraping functions of Oswald: https://github.com/pender/chatbot-rnn
(all credit for this RNN used in my project currently goes to Pender: https://github.com/pender I am actively developing my own that I will train variants of in the near future).


This newest version will comment on posts that it finds on the profile's newsfeed every 2000 seconds.  It will also listen to notifications in order to actively respond to replies to your comments on posts.  It takes the text from the posts and/or comment replies it finds/detects, skipping it if there is none (photos, memes, etc) and replaces anything outside of the BMP like emojis with a character it can handle so it doesn't crash the console or cause other problems.  It then feeds that text into pender's chatbot-rnn, which encodes/decodes it into a response, and uses functions that I modified in the rnn-script to post it back to Facebook accordingly.




Dependencies:


-Python 3.5.0  


-Dependencies for and installation of https://github.com/pender/chatbot-rnn, set up and working per the instructions with the pretrained reddit model offered by this project (at the time of this readme it uses tensorfow 1.4.1)


-Python selenium (pip3 install selenium)


-Phantom.js (make sure it is in your PATH variable):  http://phantomjs.org/



Usage:

-In the ../chatbot-rnn/chatbot-rnn-master directory of the chatbot-rnn project by pender that you install above, replace chatbot.py with multiThread.py, and copy fbbot.py to this directory as well.


-Replace "yourfacebookemail@example.com","yourfacebookpassword" in multiThread.py with your own username and password for Facebook, and then in the chatbot-rnn directory, run:


  python3 multiThread.py




BUGS: 
If you get an error where it hangs right after the logins and models load, try changing "by" in line 224 to "ca".  This element is different across profiles, and I'm working on a handler to resolve this!!




Big props to hikaruAI's work here, of which I chopped down into "fbbot.py" and have been building on top of.  It got me started on this whole thing to begin with:
https://github.com/hikaruAi/FacebookBot
