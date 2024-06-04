# 블루프린트 테스트
from flask import Blueprint, request

# 블루프린트 객체 등록
bp = Blueprint('bluetest', __name__, url_prefix='/')

# url 설정
@bp.route('/', methods=['GET'])
def test1(): 
    return 'test success1'

@bp.route('/test', methods=['GET'])
def test2(): 
    return 'test success2'