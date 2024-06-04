# 블루프린트 테스트

from flask import Blueprint

# 블루프린트 객체 등록
bp = Blueprint('test3', __name__, url_prefix='/')

# url 설정
@bp.route('/hello0',methods=['GET'])
def hello_pybo():
    return 'Hello0'


@bp.route('/',methods=['GET'])
def index():
    return 'Pybo indexer'