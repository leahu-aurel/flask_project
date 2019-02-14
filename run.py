from flaskblog import create_app

a = 2

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)