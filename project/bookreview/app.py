from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


## API 역할을 하는 부분
@app.route('/review', methods=['POST'])
def write_review():
	# 1. 클라이언트가 준 title, author, review 가져오기.
	# 2. DB에 정보 삽입하기
	# 3. 성공 여부 & 성공 메시지 반환하기
    post_title = request.form['title_give']
    post_author = request.form['author_give']
    post_review = request.form['review_give']

    reviewDic = {
        'title': post_title,
        'author': post_author,
        'review': post_review
    }

    db.review.insert_one(reviewDic)

    return jsonify({'result': 'success', 'msg': 'review가 성공적으로 등록되었습니다.'})


@app.route('/review', methods=['GET'])
def read_reviews():
    reviews = list(db.review.find({}, {'_id': 0}))
    print(reviews)
    return jsonify({'result': 'success', 'reviews': reviews})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)