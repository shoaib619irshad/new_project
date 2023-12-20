from flask import request, jsonify
from flask.views import MethodView
from sqlalchemy.exc import IntegrityError

from app.models.models import Tasks
from app.services.tasks import *
from app.utils.decorators import admin_required


class AdminView(MethodView):
    def __init__(self, model: Tasks = None) -> None:
        self.model = model

    @admin_required
    def post(self):
        id = request.json.get("id",None)
        title = request.json.get("title", None)
        description = request.json.get("description", "")
        status = "unassigned"
        if id is None or title is None:
            return jsonify(message="Invalid Credentials") , 400
        try:
            task = create_task(
                model = self.model,
                id = id,
                title = title,
                description = description,
                status = status
                )
            return jsonify(message="Task added successfully")
        except IntegrityError:
            return jsonify(message="The given id already exists")
        
    @admin_required   
    def get(self , id):
         task = get_task_by_id(id)
         if not task:
              return jsonify({
                   "message":"Task not found",
                   "success": False
                   })
         task = {"id":task.id,
            "title":task.title,
            "description":task.description,
            "status":task.status.value
            }
         return jsonify({
              "task": task,
              "success": True
              })
    
    @admin_required
    def patch(self , id):
        data = request.json
        task = get_task_by_id(id)
        if not task:
            return jsonify({
                "message":"Task not found",
                "success": False
                })
        update_task(data,id)
        return  jsonify({
              "message":"Task updated succesfully",
              "success":True
              })
    
    @admin_required
    def delete(self , id):
        task = get_task_by_id(id)
        if not task:
            return jsonify({
                "message":"Task not found",
                "success": False
                })
        delete_task(task)
        return jsonify({
            "message":"Task deleted sucessfully",
            "success":True
            })