# -*- coding: utf-8 -*-

from flask import Flask,request,make_response
import time
import hashlib
import xml.etree.ElementTree as ET
from message import xml_rep

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def index():
	if request.method =="GET":
		token = "wx92768dacc032b64c"
		signature = request.args.get('signature','')
		timestamp = request.args.get('timestamp','')
		nonce = request.args.get('nonce','')
		echostr = request.args.get('echostr','')
		s = [timestamp,nonce,token]
		s.sort()
		s = ''.join(s)
		if (hashlib.sha1(s).hexdigest()==signature):
			return make_response(echostr)
	else:
		rec = request.data
        xml_rec = ET.fromstring(rec)
        tou = xml_rec.find('ToUserName').text
        fromu = xml_rec.find('FromUserName').text
        content = "欢迎来到luna的微信号"
        #加上xml_rep
        response = make_response(xml_rep % (fromu,tou,str(int(time.time())), content))
        response.content_type='application/xml'
        return response
@app.route('/test')
def test():
	return "Hello."

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0')