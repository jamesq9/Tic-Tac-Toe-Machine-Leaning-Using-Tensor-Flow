# importing Flask
from flask import Flask, jsonify, render_template, request

import json
# import tic tac toe game 
from Train_TicTacToe_NW import *

import numpy as np


# setting up session
sess = tf.InteractiveSession()
prediction = neural_network_model(x)
saver = tf.train.Saver()
saver.restore(sess,"./model/model.ckpt")
graph = tf.get_default_graph()


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def  bestmove(input):
    global graph
    with graph.as_default():
        data = (sess.run(tf.argmax(prediction.eval(session = sess,feed_dict={x:[input]}),1)))
    return data

@app.route('/api/ticky', methods=['POST'])
def ticky_api():
    data = request.get_json()
    data = np.array(data['data'])
    data = data.tolist()
    #print('data is ')
    #print(type(data))
    #print(data)
    return jsonify(np.asscalar(bestmove(data)[0]))

# @app.after_request
# def add_header(r):
#     """
#     Add headers to both force latest IE rendering engine or Chrome Frame,
#     and also to cache the rendered page for 10 minutes.
#     """
#     r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
#     r.headers["Pragma"] = "no-cache"
#     r.headers["Expires"] = "0"
#     r.headers['Cache-Control'] = 'public, max-age=0'
#     return r

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=False)

