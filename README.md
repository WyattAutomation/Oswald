# Oswald
An ongoing project to fully-automate the activity Facebook Profile, using a combination of web-scraping and Machine Learning, and without using the Facebook API.

Update 4/25/18:
-Found a pretty good pretrained RNN seq2seq/LSTM chatbot model here, and replaced the command line interface to input/output text with the webscraping functions of Oswald: https://github.com/pender/chatbot-rnn
(all credit for this RNN used in my project currently goes to Pender: https://github.com/pender I am actively developing my own that I will train variants of in the near future)



Dependencies:

-Python 3.5.0  

-Dependencies for and installation of https://github.com/pender/chatbot-rnn, set up and working per the instructions with the pretrained reddit model offered by this project (at the time of this readme it uses tensorfow 1.4.1)

-Python selenium (pip3 install selenium)

-Phantom.js (make sure it is in your PATH variable):  http://phantomjs.org/


-Usage-

In the /chatbot-rnn directory of the chatbot-rnn project by pender that you install above, replace chatbot.py with multiThread.py, and copy fbbot.py to this directory as well.

Replace "yourfacebookemail@example.com","yourfacebookpassword" in multiThread.py with your own username and password for Facebook, and then run:

  python3 multiThread.py
  
in a terminal.

This will post a comment as a reply to your friends posts every so often, and listen to notifications in order to reply to other profiles responses to your comments.  It takes the text from the posts and comment replies, skipping it if there is none, feeds it into the chatbot-rnn which encodes/decodes it into a response, which it then posts back to Facebook accordingly.

Big props to hikaruAI's work here, of which I chopped down into "fbbot.py" and have been building on top of.  It got me started on this whole thing to begin with:
https://github.com/hikaruAi/FacebookBot

