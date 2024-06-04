# flask에 있는 request와 Bluepoint 호출
from flask import Blueprint, request

# 블루프린트 객체 등록
bp = Blueprint('questionstart', __name__, url_prefix='/')

# url 설정
@bp.route('/question', methods=['POST'])
def questionstart():
    # 카카오챗봇에서 발화문 가져오기
    body = request.get_json()
    body=body['userRequest']['utterance']
    
    # 챗봇 입력 결과가 시작일 떄
    if body=="시작":
        # 챗봇 출력 시 textcard 설정
        responseBody={
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                    "textCard": {
                        "title": "질문 유형을 선택하세요",
                        "description": "",
                        "buttons": [
                            {
                            "action": "block",
                            "label": "계정",
                            "block": "계정"
                            },
                            {
                            "action": "block",
                            "label": "게임친구",
                            "block": "게임친구"
                            },
                            {
                            "action": "block",
                            "label": "기타",
                            "block": "기타"
                            }
                        ]
                    }
                    }
                ]
            }
        }
    return responseBody