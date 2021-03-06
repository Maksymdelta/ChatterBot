from chatterbot import ChatBot
from chatterbot.training.trainers import ChatterBotCorpusTrainer
from settings import HIPCHAT

'''
See the HipChat api documentation for how to get a user access token.
https://developer.atlassian.com/hipchat/guide/hipchat-rest-api/api-access-tokens
'''

chatbot = ChatBot(
    "HipChatBot",
    hipchat_host=HIPCHAT["HOST"],
    hipchat_room=HIPCHAT["ROOM"],
    hipchat_access_token=HIPCHAT["ACCESS_TOKEN"],
    input_adapter="chatterbot.adapters.input.HipChat",
    output_adapter="chatterbot.adapters.output.HipChat"
)

chatbot.set_trainer(ChatterBotCorpusTrainer)
chatbot.train("chatterbot.corpus.english")

# The following loop will execute each time the user enters input
while True:
    try:
        response = chatbot.get_response(None)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
