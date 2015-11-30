from flask import Flask
from mytest import Test

test = Test()

app = Flask(__name__)
app.add_url_rule('/',view_func=test.view_func)

@test
def index():
	pass

if __name__ == '__main__':
	app.run(debug=True)