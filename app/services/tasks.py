from typing import Any
from flask import jsonify

from app import db
from app.models.models import Tasks


def create_task(model: Any, id: int, title: str, description: str):
    task = model(
        id = id,
        title = title,
        description = description
    )
    db.session.add(task)
    db.session.commit()

    return task

def get_task_by_id(id):
    task = Tasks.query.get(id)
    return task

def update_task(data ,id):
    task = get_task_by_id(id)
    if "title" in data:
        if  data["title"].isspace() or data["title"] == "":
            return jsonify(message="Title cannot be empty")
        task.title = data["title"]
    if "description" in data:
        task.description = data["description"] 
    db.session.commit()

def delete_task(task):
    db.session.delete(task)
    db.session.commit()