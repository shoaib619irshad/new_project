from flask import Blueprint

from app.models.models import Tasks
from app.views.task_assign import *

task_assign_bp = Blueprint('assigning_task', __name__, url_prefix='/task')

task_assign_bp.add_url_rule(
    rule='/employee/<task_id>',
    view_func=EmployeeTaskAssignView.as_view(
        "emp_task_assign",
        model = Tasks
    )
)

task_assign_bp.add_url_rule(
    rule='/manager/<task_id>',
    view_func=ManagerTaskAssignView.as_view(
        "mgr_task_assign",
        model = Tasks
    )
)