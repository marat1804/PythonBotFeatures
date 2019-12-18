# This is SFP function to set the dialog as important v1.1
import vk

session = vk.Session()
api = vk.API(session, lang='ru', v=5.85)


def SetImportant(user_id, token, data):
    important = data['conversation'].get('important')
    if important is None:
        api.messages.markAsImportantConversation(peer_id=user_id, important="1", access_token=token)
    return "", ""


'''
elif text.lower().find("сфп") != -1 or (text.lower().find("скорая") != -1 and text.lower().find("помощь")) or 
     text.lower().find("спф") != -1:
    ____message, keyboard = SFP_Function.SetImportant(id, token, data[j])
'''
