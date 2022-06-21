from flask import json
from flask import request
from flask import Flask

app = Flask(__name__)

@app.route('/')
def api_route():
    return 'Welcome to git-listener'

@app.route('/github',methods=['POST'])
def api_gh_mesage():
    if request.headers['Content-Type']=="application/json":
        my_info = json.dumps(request.json)
<<<<<<< HEAD
=======
        print (my_info)
>>>>>>> 55ea04dc06aae06b94b2ec9a161402f1610a158d
        return my_info

#similar to django export
if __name__ == '__main__':
    app.run(debug=True)
