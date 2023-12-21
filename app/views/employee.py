from flask import jsonify, request
from flask.views import MethodView
from flask_jwt_extended import get_current_user, jwt_required

from app.models.models import Role, Tasks
from app.services.tasks import *


class EmployeeView(MethodView):
    def __init__(self, model: Tasks = None) -> None:
        self.model = model

    @jwt_required()
    def get(self):
        employee = get_current_user()
        role = employee.role.value
        if role != Role.EMPLOYEE.value:
            return jsonify(message="Only employees can view their task")
        employee_id = employee.id
        task_list = get_tasks_assign(employee_id)
        if not task_list:
            return jsonify(message="Task not assigned")
        
        tasks = []
        for task in task_list:
            tasks.append({"id":task.id,
                          "title":task.title,
                          "description":task.description
                          })
        return jsonify({
            "task": tasks,
            "success": True
            })
    
    @jwt_required()
    def patch(self, id):
        employee = get_current_user()
        role = employee.role.value
        if role != Role.EMPLOYEE.value:
            return jsonify(message="Only employees can update their task")
        employee_id = employee.id
        task_list = get_tasks_assign(employee_id)
        if not task_list:
            return jsonify(message="Task not assigned")
        task = get_task_by_id(id)
        if not task in task_list:
            return jsonify(message="This task is not assigned to you.")
        status =request.json.get("status")
        update_status(id , status)
        return jsonify(message="Task status updated successfully")