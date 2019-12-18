import vk
import time
import random
import keyboard
import SFP_Function
import Config
import json

token = Config.token
session = vk.Session()
api = vk.API(session, lang='ru', v=5.85)

keyboard1 = keyboard.Keyboard(True)
keyboard1.add_button('Картинка', 'primary', 'picture')
keyboard1.add_button('Музыка', 'positive', 'music')
keyboard1.add_button('Текст', 'negative', 'text')

kb = keyboard1.get()

print(keyboard)
while True:
    time.sleep(1)
    try:
        data = api.messages.getConversations(filter='unread', access_token=token)['items']
        for j in range(len(data)):
            #print(data)
            id_message = data[j]['conversation']
            id = id_message['peer']['id']
            k = id_message['unread_count']
            message = api.messages.getHistory(user_id=id, access_token=token, count=k)['items']
            for i in range(len(message)):
                text = message[i]['text']
                print(text)
                if len(message[i]['attachments']) == 0:
                    if message[i]['text'] == "Меню" or message[i]['text'] == "меню":
                        api.messages.send(peer_id=id, message="Так и быть.", keyboard=kb,
                                          access_token=token, random_id=random.randint(0, 15424545))
                        break
                    elif message[i]['text'].lower().find("сфп") != -1 or (
                            message[i]['text'].lower().find("скорая") != -1
                            and message[i]['text'].lower().find("помощь")) or message[i]['text'].lower().find("спф") != -1:
                        ____message, keyboard = SFP_Function.SetImportant(id, token, data[j])
                        # api.messages.markAsImportantConversation(peer_id=id, important="1", access_token=token)
                        # api.messages.send(peer_id=id, message="Ага, сфп написал значит",
                        #             access_token=token, random_id=random.randint(0, 15424545))
                        break
                    elif message[i].get('payload') == '"picture"':
                        sms = "photo65554357_456245461_929699ac23fb0273fe"
                        api.messages.send(peer_id=id, message="Ха, лови пикчу", attachment=sms, keyboard=kb,
                                          access_token=token, random_id=random.randint(0, 15424545))
                        break
                    elif message[i].get('payload') == '"music"':
                        sms = "audio65554357_456239195"
                        api.messages.send(peer_id=id, message="Ну послушай", attachment=sms, keyboard=kb,
                                          access_token=token, random_id=random.randint(0, 15424545))
                        break
                    if message[i].get('payload') == '"text"':
                        api.messages.send(peer_id=id, message="Серьезно!?", keyboard=kb,
                                          access_token=token, random_id=random.randint(0, 15424545))
                        break
                    sms = "Вы зачем-то написали - " + message[i]['text']
                    if message[i]['text'] == "Привет":
                        api.messages.send(peer_id=id, message="И тебе не хворать!", attachment='',
                                          access_token=token, random_id=random.randint(0, 15424545))
                    else:
                        api.messages.send(peer_id=id, message=sms, attachment='',
                                          access_token=token, random_id=random.randint(0, 15424545))
                else:
                    if len(message[i]['text']) != 0:
                        sms_text = "Вы зачем-то написали - " + message[i]['text']
                    else:
                        sms_text = ''
                    attach = message[i]['attachments']
                    sms = ''
                    attach_count = 0
                    for j in range(len(attach)):
                        attach_type = attach[j]['type']
                        if attach_type != 'sticker':
                            sms = sms + attach_type + str(attach[j][attach_type]['owner_id']) + '_' + \
                                  str(attach[j][attach_type]['id']) + '_' + str(
                                attach[j][attach_type].get('access_key'))
                        elif attach[j]['type'] == 'sticker':
                            sms_text = "Ты прислал стикер."
                        if attach_count < len(attach):
                            sms += ','
                        attach_count += 1
                    api.messages.send(peer_id=id, message=sms_text, attachment=sms,
                                      access_token=token, random_id=random.randint(0, 15424545))

    except Exception as e:
        print("Trying again", e)
