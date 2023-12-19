from flask import jsonify, request
from flask.views import MethodView

from app.models.models import Tasks
from app.services.task_assign import assign_task, get_user_by_id
from app.services.tasks import get_task_by_id
from app.utils.decorators import *

class EmployeeTaskAssignView(MethodView):
    def __init__(self , model: Tasks = None) -> None:
        self.model = model
    
    @adm_mgr_required
    def patch(self, task_id):
        task = get_task_by_id(task_id)
        if not task:
            return jsonify({
                "message":"Task not found",
                "success":False
            })
        assigned_to = request.json.get("assigned_to")
        user = get_user_by_id(assigned_to)
        if  not user:
            return jsonify({
                "message":"Employee not found",
                "success": False
                })
        if user.role.value != "employee":
            return jsonify(message="The user is not an employee")
        assign_task(task_id, assigned_to)
        return jsonify(message="Task assigned successfully")
    

class ManagerTaskAssignView(MethodView):
    def __init__(self , model: Tasks = None) -> None:
        self.model = model
    
    @admin_required
    def patch(self, task_id):
        task = get_task_by_id(task_id)
        if not task:
            return jsonify({
                "message":"Task not found",
                "success":False
            })
        assigned_to = request.json.get("assigned_to")
        user = get_user_by_id(assigned_to)
        if  not user:
            return jsonify({
                "message":"Manager not found",
                "success": False
                })
        if user.role.value != "manager":
            return jsonify(message="The user is not a manager")
        assign_task(task_id, assigned_to)
        return jsonify(message="Task assigned successfully")