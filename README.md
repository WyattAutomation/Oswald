## Oswald

The Point of This Project:
  To fully-automate the activity of a Facebook Profile, using a combination of Web-Scraping and a Neural Network chatbot, without using the Facebook API.  Ideally, the end-goal is to make an easy to use bot for Facebook, that doesn't require anything beyond a few programming dependecies and a username/password to a Facebook profile.  No API keys, no signing up for Facebook for Developers and having to "create an app", no huge libraries of scraping functions that are only really useful for static spam-bots; just a dynamically interactive bot that you can plug credentials in to and let it rock.  **This is still VERY much a WIP, so keep that in mind!**  


*Latest Updates 5/2/18:*

-Disabled the commenter for Timeline Posts, as it was becoming a bit of a nuisance for my friends who voluntarily befriended the profile I use for Oswald to help with testing.  **Pender's pretrained reddit model used in this project is actually quite rude and downright offensive at times**, so be aware of that before you set this up.  It lead to some awkward misunderstandings/interactions from folks seeing it's off-color comments, who weren't friends of the bot or aware of what it was, getting into some fairly heated arguments with it.  While pretty darn hilarious, I have no intent of trolling innocent strangers with this and removed this component temporarily, until I train my own model that isn't such a hot-head.

-Added the Facebook Messenger bot back into this update, using carpedm20's "fbchat".

-Added and implemented a tagReplier() function to the comment-reply listener.  Basically, this allows someone to tag Oswald and "summon" it to a thread to interact with comments wherever it was tagged.  It replies with a generic response to the tag, and subsequent comments on the thread are detected by the notification listener, which generates responses to comments using Pender's seq2seq chatbot and the other Selenium web-scraping functions for posts.

# Getting Started


## Prerequisites


-Python 3.5.0  
```
sudo apt-get install python3.5
```

-Dependencies for and working installation of https://github.com/pender/chatbot-rnn, set up per the instructions with the pretrained reddit model offered by this project (at the time of this readme it uses tensorfow 1.4.1).

For tensorflow 1.4.1, try:
```
pip3 install tensorflow==1.4.1
```

-Python selenium
```
pip3 install selenium
```


-Phantom.js (make sure it is in your PATH variable if using Windows):  http://phantomjs.org/
```
sudo apt-get install phantomjs
```

carpedm20's fbchat: https://github.com/carpedm20/fbchat
```
pip3 install fbchat
```

## Usage:

-Move Oswald.py from this Git to your local ../chatbot-rnn/chatbot-rnn-master directory of the chatbot-rnn project by pender that you install above, and copy fbbot.py to this directory as well.


-Replace all instances of ("yourfacebookemail@example.com","yourfacebookpassword") in Oswald.py with your own username and password for Facebook, and then in the chatbot-rnn directory, run:

```
python3 Oswald.py
```
BUGS: 
If you get an error where it hangs right after the logins and models load, try changing "by" in the chatbot() function of Oswald.py to "ca".  This element is different across profiles, and I'm working on a handler to resolve this!!

## Credit to others' work used in this project

-I found a decent pretrained RNN seq2seq/LSTM chatbot model here, and replaced the command line interface to input/output text with the webscraping functions of Oswald: https://github.com/pender/chatbot-rnn
(all credit for this RNN used in my project currently goes to Pender: https://github.com/pender I am actively developing my own model that I will train and use in future updates).

-carpedm20's "fbchat", which is a sort of unofficial Facebook Messenger API found here: https://github.com/carpedm20/fbchat
If you have not yet used this library/tool do yourself a favor and check it out; no official API keys needed etc.  Extremely well documented and a very solid, reliable tool.

-Big props to hikaruAI's work here, of which I chopped down into "fbbot.py" and have been building on top of.  It got me started on this whole thing to begin with:
https://github.com/hikaruAi/FacebookBot






