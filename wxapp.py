# -*- coding: UTF-8 -*-
from flask import Flask
from flask.ext.weixin import Weixin

WEIXIN_TOKEN="xxxxx"

app = Flask(__name__)
weixin = Weixin(app)
app.add_url_rule('/',view_func=weixin.view_func)
app.config.from_object(__name__)


@weixin('*')
def reply(**kwargs):
	username = kwargs.get('sender')
	sender = kwargs.get('receiver')
	content = kwargs.get('content')
	return weixin.reply(username,sender=sender,content=content)
@weixin(key=u'歌曲')
def reply_music(**kwargs):
	username = kwargs.get('sender')
	sender = kwargs.get('receiver')
	title='weixin music'
	description = 'weixin description'
	music_url='http://play.baidu.com/?__m=mboxCtrl.playSong&__a=257866034&__o=song/257866034||playBtn&fr=-1||www.baidu.com#'
	return weixin.reply(
		username,
		type='music',
		sender=sender,
		title=title,description=description,
		music_url=music_url,hq_music_url=music_url)

if __name__ == '__main__':
	app.run(debug=True,host="0.0.0.0")