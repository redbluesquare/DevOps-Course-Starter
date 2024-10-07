from flask import Flask, redirect, render_template, request
from todo_app.data.db_items import add_item, get_items, update_item
#from todo_app.data.trello_items import add_item, get_items, update_item
from todo_app.data.view_model import ViewModel

from todo_app.flask_config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    @app.route('/')
    def index():
        items = get_items()
        item_view_model = ViewModel(items)
        return render_template('index.html', view_model = item_view_model)

    @app.route('/add-todo', methods=['POST'])
    def add_todo():
        title = request.form.get('title')
        add_item(title)
        return redirect('/')

    @app.route('/close-todo', methods=['POST'])
    def close_todo():
        id = request.form.get('id')
        update_item(id, True)
        return redirect('/')
    
    return app