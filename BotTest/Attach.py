
def attachment(attach):
    attach_count = 0
    sms = ''
    for j in range(len(attach)):
        attach_type = attach[j]['type']
        if attach_type != 'sticker':
            sms = sms + attach_type + str(attach[j][attach_type]['owner_id']) + '_' + \
                  str(attach[j][attach_type]['id']) + '_' + str([j][attach_type].get('access_key'))
        elif attach[j]['type'] == 'sticker':
            sms_text = "Ты прислал стикер."
        if attach_count < len(attach):
            sms += ','
            attach_count += 1
        return sms
          #  api.messages.send(peer_id=id, message=sms_text, attachment=sms,
                #  access_token=token, random_id=random.randint(0, 15424545))