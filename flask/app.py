from flask import Flask
from flask import request
import json
from flask import make_response
from flask import abort


app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"
#curl http://192.168.0.110/test?search=2
@app.route('/test')
def test():
    search = request.args.get("search")
    print search
    return "Hello World! with test"

#curl -X POST http://192.168.0.110/test2 -d '{"thi":"aaa"}'
@app.route('/test2', methods=['POST'])
def test2():
    jbody = json.loads(request.get_data())
    print jbody['thi']
    return "Hello World! with test"

#curl -X POST http://192.168.0.110/test3  -H "User-Agent:haha"
@app.route('/test3', methods=['POST','DELETE'])
def test3():
    if request.method =="DELETE":
	print 'delete haha'
    aa = request.headers.get('User-Agent')
    print aa
    return "Hello World! with test"

#curl -X DELETE http://192.168.0.110/test4
@app.route('/test4', methods=['POST','DELETE'])
def test4():
    if request.method =="DELETE":
	print 'delete haha'
    else:
	print 'POST la'
    return "Hello World! with test"

#curl -X POST -I http://192.168.0.110/test5  where -I to get the return header
#curl -X GET http://192.168.0.110/test5
@app.route('/test5', methods=['POST','GET'])
def test5(): 
    if request.method=='POST':
	abort(404)
    else:
	return 'haha'
#curl -X POST http://192.168.0.110/test6/sasa
@app.route('/test6/<username>', methods=['POST'])
def test6(username):
    print username
    return 'haha'
    
@app.route('/test7', methods=['POST'])
@app.route('/test7/<username>', methods=['POST'])
def test7(username=None):
    print username
    return 'haha'


@app.errorhandler(404)
def not_found(error):
    resp = make_response('cannot find the service', 404)
    resp.headers['X-Something'] = 'A value'
    return resp



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)
