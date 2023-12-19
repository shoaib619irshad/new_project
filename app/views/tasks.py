from flask import jsonify, request
from flask.views import MethodView
from sqlalchemy.exc import IntegrityError

from app.models.models import Tasks
from app.services.tasks import *
from app.utils.decorators import token_required


class TasksView(MethodView):
    def __init__(self , model: Tasks = None) -> None:
        self.model = model

    @token_required
    def post(self):
        id = request.json.get("id",None)
        title = request.json.get("title", None)
        description = request.json.get("description", "")
        if id is None or title is None:
                return jsonify(message="Invalid Credentials") , 400
        try:
             task = create_task(
                  model = self.model,
                  id = id,
                  title = title,
                  description = description
             )
             return jsonify(message="Task added successfully")
        except IntegrityError:
             return jsonify(message="The given id already exists")
        

    @token_required
    def get(self , id):
         task = get_task_by_id(id)
         if not task:
              return jsonify({
                   "message":"Task not found",
                   "success": False
                   })
         task = {"id":task.id,
            "title":task.title,
            "description":task.description
            }
         return jsonify({
              "task": task,
              "success": True
              }) 
    
    @token_required
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
         

    @token_required
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
               "success":True})