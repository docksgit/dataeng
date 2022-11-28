from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task-list.db'
db = SQLAlchemy(app)

app.app_context().push()

class TaskList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task {}>'.format(self.id)



@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = TaskList(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding the task'
    else:
        tasks = TaskList.query.order_by(TaskList.date_created).all()
        return render_template('index.html', tasks=tasks)


@app.route('/remove/<int:id>')
def remove(id):
    task_to_remove = TaskList.query.get_or_404(id)

    try:
        db.session.delete(task_to_remove)
        db.session.commit()
        return redirect('/')

    except:
        return 'There was an issue removing the task'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = TaskList.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating the task'


    else:
        return render_template('update.html', task=task)

if __name__ == "__main__":
    app.run(debug=True)