from flask import Flask,flash,redirect,render_template,request,session,abort
from flask import jsonify

app=Flask(__name__)



products=[

{	
	'id':1,
	'title':u'first element',
	'quantity':4
},
{
	'id':2,
	'title': u'second element',
	'quantity':3
}

]


#@app.route("/products",methods=['GET'])
#def index():
#	return jsonfy({'products':products})
	#return render_template('layout.html')


@app.route('/products', methods=['GET'])
def get_products():
    return jsonify({'products': products})

#@app.route("/hello")
#def hello():
#	return "hello world"


#@app.route("/hello/<string:name>/")
#def hello(name):
#	return render_template('layout.html',name=name)




if __name__=="__main__":
	app.run()



