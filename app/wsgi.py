from app.main import create_app as application

if __name__ == '__main__':
    print("creating wsgi")
    app = application('dev')
    app.run()
