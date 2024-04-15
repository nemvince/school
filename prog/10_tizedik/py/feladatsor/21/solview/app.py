import os
from flask import Flask, render_template, send_file, request

app = Flask(__name__)

TASKS_DIR = 'tasks'

def is_valid_task_name(task_name):
    return all(c.isalnum() or c in ['_', '-'] for c in task_name)

@app.route('/')
def index():
    tasks = [d.name for d in os.scandir(TASKS_DIR) if d.is_dir()]
    if not tasks:
        return 'No tasks found', 404
    return render_template('index.html', tasks=tasks)

@app.route('/task/<task_name>')
def task(task_name):
    if not is_valid_task_name(task_name):
        return 'Invalid task name', 400

    task_path = os.path.join(TASKS_DIR, task_name)
    sol_file = os.path.join(task_path, 'sol.py')
    tsk_file = os.path.join(task_path, 'tsk.pdf')

    if not os.path.exists(task_path):
        return 'Not found', 404
    elif not os.path.exists(sol_file):
        return 'Not solved', 404
    elif not os.path.exists(tsk_file):
        return 'Tasksheet not found', 404

    with open(sol_file, 'r', encoding="utf-8") as f:
        solText = f.read().strip()
    return render_template('task.html', task_name=task_name, solText=solText)

@app.route('/tasksheet/<task_name>')
def tasksheet(task_name):
    if not is_valid_task_name(task_name):
        return 'Invalid task name', 400

    task_path = os.path.join(TASKS_DIR, task_name)
    tsk_file = os.path.join(task_path, 'tsk.pdf')

    if not os.path.exists(tsk_file):
        return 'Not found', 404

    as_attachment = request.args.get('asAttachment', default=False, type=bool)
    download_name = f'{task_name}_tasksheet.pdf'

    return send_file(tsk_file, download_name=download_name, as_attachment=as_attachment)

@app.route('/solution/<task_name>')
def solution(task_name):
    if not is_valid_task_name(task_name):
        return 'Invalid task name', 400

    task_path = os.path.join(TASKS_DIR, task_name)
    sol_file = os.path.join(task_path, 'sol.py')

    if not os.path.exists(sol_file):
        return 'Not found', 404
    
    download_name = f'{task_name}_solution.py'
    return send_file(sol_file, download_name=download_name, as_attachment=True)

if __name__ == '__main__':
    print(f"Running with debug server, this is not recommended for production!")
    app.run(debug=True)
