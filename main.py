from app import AppFactory

app = AppFactory.initialize()

if __name__ == '__main__':
    app.run(port=1233)