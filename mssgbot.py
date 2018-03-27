#A lego'd-together chatterbot (https://chatterbot.readthedocs.io/en/stable/) 
#with github user carpedm20's fbchat, which can be found here:
#https://github.com/carpedm20/fbchat
from fbchat import log, Client
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import sys
import subprocess
import os, signal

#initialize the catterbot chatbot; not read only so machine learning is enabled
bot = ChatBot(
    'Norman',
    storage_adapter='chatterbot.storage.JsonFileStorageAdapter',
    input_adapter='chatterbot.input.VariableInputTypeAdapter',
    output_adapter="chatterbot.output.OutputAdapter",
    output_format="text",
    database='./database.json'
)

#training example to get you started when you don't already have a dataset/corpus
bot.set_trainer(ListTrainer)
bot.train([
    'How are you?',
    'I am good.',
    'That is good to hear.',
    'Thank you',
    'You are welcome.',
])


# Echobot example from fbchat, set to i/o to/from the chatterbot instance
class EchoBot(Client):
    def onMessage(self, author_id, message, thread_id, thread_type, **kwargs):
        self.markAsDelivered(author_id, thread_id)
        self.markAsRead(author_id)
        
        log.info("Message from {} in {} ({}): {}".format(author_id, thread_id, thread_type.name, message))

        # If you're not the author, echo
        if author_id != self.uid:
            bot_input = bot.get_response(message)
            self.sendMessage(bot_input, thread_id=thread_id, thread_type=thread_type)

client = EchoBot("yourfacebookemail@example.com","yourfacebookpassword")
client.listen()

#if it crashes, just start over
os.system("mssgbot.py")


