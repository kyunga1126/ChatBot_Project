from flask import Flask


# route 팩토리
def create_app():
    app = Flask(__name__)
    
    #각 파일 호출
    import questionstart
    import questionusers
    import questionfriends
    import questionother
    
    # 블루프린트 객체 등록
    app.register_blueprint(questionstart.bp)
    app.register_blueprint(questionusers.bp)
    app.register_blueprint(questionfriends.bp)
    app.register_blueprint(questionother.bp)
    
    return app 
    
    """

def create_app():
    app = Flask(__name__)
    
    #각 파일 호출 blueprinttest
    import blueprinttest
    #import questionstart
    #import questionusers
    #import questionfriends
    #import questionother
    
    # 블루프린트 객체 등록
    app.register_blueprint(blueprinttest.bp)
    #app.register_blueprint(questionusers.bp)
    #app.register_blueprint(questionfriends.bp)
    #app.register_blueprint(questionother.bp)
    
    return app """