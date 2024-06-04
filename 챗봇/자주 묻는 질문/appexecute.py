# create_factory 실행으로 서버 실행

from app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(host = '0.0.0.0', port = 80) 
"""
from app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(host = '0.0.0.0', port = 5000) """