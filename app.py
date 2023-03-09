from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

# POST Login Controller
@app.route("/v1/api/login", methods=["POST"])
def login():
    #data 받아오기
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    # user 검증 로직, 현재는 dummy
    if username != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401
    # login 성공 시 200 code 반환
    return jsonify(""), 200

# POST Join(회원 가입)
@app.route("/v1/api/join", methods=["POST"])
def join():
    # data 받아오기
    id = request.json.get("id", None)
    password = request.json.get("password", None)
    name = request.json.get("name", None)
    email = request.json.get("email", None)
    team = request.json.get("team", None)

    # user 중복 검증 하기
    # dummy test, 만약 회원가입 요청한 id가 test 이면 회원가입 성공, 아니면 중복 인 것으로 간주
    if id != "test":
        return jsonify({"msg":"id already exist"},401)
    return jsonify({"msg":"Join Success"},200)


if __name__ == "__main__":
    app.run()