from flaskblog import create_app

a = 1

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)