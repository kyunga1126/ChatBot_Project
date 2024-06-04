# 타 py이 되는지에 대한 테스트
from flask import Blueprint, request

# 블루프린트 객체 등록
bp = Blueprint('test5', __name__, url_prefix='/')

# url 설정
@bp.route('/final1', methods=['POST'])
def final1(): 
    # 카카오챗봇에서 발화문 가져오기
    body = request.get_json()
    #print(body) 
    
    # 챗봇 데이터 설정
    responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": { 
                            "text": "테스트 성공"
                        }
                    }
                ]
        }
    }
    return responseBody