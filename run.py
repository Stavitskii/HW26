from project.config import config
from project.models import Genre, Director, Movie, User
from project.server import create_app, db

app = create_app(config)


@app.shell_context_processor
def shell():
    return {
        "db": db,
        "Genre": Genre,
        "Director": Director,
        "Movie": Movie,
        "User": User
    }


if __name__ == '__main__':
    app.run(host="localhost", port=25000, debug=True)