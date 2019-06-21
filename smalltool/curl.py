
file_name = 'abc.txt'
nids = []

with open(file_name, encoding='UTF-8') as f:
    pre_str = "nid = '"
    post_str = "';"
    for line in f:
        if line.find(pre_str) != -1 and line.find(post_str) != -1:
            pre_index = line.find(pre_str) + len(pre_str)
            post_index = line.find(post_str)
            nid = line[pre_index:post_index]
            nids.append(nid)

print(len(nids))

phone = '17717550328'
curl_postfix = '&userId=315631&sendType=sms&replaceData={"AMOUNT":"50","DAY":"1","NAME":"mario","PRODUCTNAME":"mario","CARDNO":"2850"}\' http://app-proxy-messagecenter.crephet-internal.com:9505/messagecenter/api/1.0.0/message/send'
for nid in nids:
    curl_prefix = 'curl -d \'nid=' + nid + '&phone=' + phone
    print(curl_prefix + curl_postfix)
