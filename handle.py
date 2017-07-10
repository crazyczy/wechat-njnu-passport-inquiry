# -*- coding: utf-8 -*-
# filename: handle.py
import hashlib
import basic
import reply
import receive
import web
import requests
import json
import os


class Handle(object):

    def POST(self):
        try:
            webData = web.data()
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.MsgType == 'text':
                    mediaId = self.getmediaid(recMsg.Content)
                    if mediaId:
                        replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                        return replyMsg.send()
                    else:
                        return reply.Msg().send()
                else:
                    return reply.Msg().send()
            else:
                return reply.Msg().send()
        except Exception, Argment:
            print Argment

    def getmediaid(self, num):
        if(os.path.isfile('img/'+num+'.jpg')):
            url = 'https://api.weixin.qq.com/cgi-bin/media/upload?access_token=' + basic.Basic().get_access_token() + '&type=image'
            files = {'media': open('img/'+num+'.jpg', 'rb')}
            r = requests.post(url, files=files)
            media_id = json.loads(r.content)['media_id']

            return media_id
        else:
            return ''
