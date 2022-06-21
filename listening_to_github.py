from flask import json
from flask import request
from flask import Flask

app = Flask(__name__)

@app.route('/')
def api_route():
    return 'Welcome to git-listener'

#similar to django export
if __name__ == '__main__':
    app.run(debug=True)
