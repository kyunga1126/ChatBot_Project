"""
# create_factory 구조로 인해 서버 실행하는 테스트
from app import create_app

# 서버 실행
if __name__ == '__main__':
    app = create_app()
    app.run(host = '0.0.0.0', port = 80) """