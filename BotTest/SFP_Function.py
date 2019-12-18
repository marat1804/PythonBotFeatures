# This is SFP function to set the dialog as important v1.1
import vk

session = vk.Session()
api = vk.API(session, lang='ru', v=5.85)


# Так то мне вообще тут не нужна data
def SetImportant(user_id, token, data):
    conversations = api.messages.getConversations(filter='unread', access_token=token)['items']
    important = IsImportant(user_id, conversations)
    if important is None:
        api.messages.markAsImportantConversation(peer_id=user_id, important="1", access_token=token)
    return "", ""


def IsImportant(user_id, conversations):
    for i in range(len(conversations)):
        if user_id == conversations[i]['conversation']['peer']['id']:
            return conversations[i]['conversation'].get('important')


'''
elif text.lower().find("сфп") != -1 or (text.lower().find("скорая") != -1 and text.lower().find("помощь")) or 
     text.lower().find("спф") != -1:
    ____message, keyboard = SFP_Function.SetImportant(id, token, data['date'])
'''
