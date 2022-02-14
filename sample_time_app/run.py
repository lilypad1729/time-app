from flask import Flask
import datetime
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def curr_time():
    curr_time_str = datetime.datetime.now()
    ans_str = curr_time_str.strftime('%H:%M:%S')
    return ans_str

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
