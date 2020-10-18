from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/order', methods=['POST'])
def post_order():
    post_name = request.form['name']
    post_count = request.form['count']
    post_address = request.form['address']
    post_phone = request.form['phone']

    print(post_name, post_count, post_address, post_phone)

    order = {
        'name': post_name,
        'count': post_count,
        'address': post_address,
        'phone': post_phone
    }

    db.order.insert_one(order)
    return jsonify({'result': 'success', 'msg': 'order 성공적으로 등록되었습니다.'})

@app.route('/order', methods=['GET'])
def get_order():
    order_list = list(db.order.find({}, {'_id': 0}))
    print(order_list)
    return jsonify(({'result': 'success', 'order': order_list}))

if __name__ == '__main__':
    app.run('0.0.0.0', port=5600, debug=True)