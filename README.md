# Oswald
An ongoing project to fully-automate the activity Facebook Profile, using a combination of web-scraping and Machine Learning, and without using the Facebook API.

Update 4/25/18:
-Found a pretty good pretrained RNN seq2seq/LSTM chatbot model here, and replaced the command line interface to input/output text with the webscraping functions of Oswald: https://github.com/pender/chatbot-rnn
(all credit for this RNN used in my project currently goes to Pender: https://github.com/pender I am actively developing my own that I will train variants of in the near future)



Dependencies:

-Python 3.5.0  

-tensorfow 1.4.1

-Python selenium

-phantom.js (make sure it is in your PATH variable):  http://phantomjs.org/


-Usage-

replace "yourfacebookemail@example.com","yourfacebookpassword" in multiThread.py with your own username and password for Facebook, and then run:

  python3 multiThread.py
  
in a terminal.


Big props to hikaruAI's work here, of which I chopped down into "fbbot.py" and have been building on top of.  It got me started on this whole thing to begin with:
https://github.com/hikaruAi/FacebookBot

