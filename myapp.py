from app import app, db
from app.models.user import User
from app.models.note import Note

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Note': Note}

if __name__ == "__main__":
    app.run(debug=True)
