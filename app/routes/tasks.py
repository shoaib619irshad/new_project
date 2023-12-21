from flask import Blueprint

from app.models.models import Tasks
from app.views.admin import AdminView
from app.views.manager import ManagerView
from app.views.employee import EmployeeView
from app.views.task_assign import *
from app.views.task_pgn import TaskPagination


tasks_bp = Blueprint('task', __name__, url_prefix='/task')

tasks_bp.add_url_rule(
     rule = '/admin',
    view_func = AdminView.as_view(
        "add_task",
        model = Tasks,
    )
)

tasks_bp.add_url_rule(
    rule = '/admin/<id>',
    view_func = AdminView.as_view(
        "display_task",
        model = Tasks
    )
)

tasks_bp.add_url_rule(
    rule = '/admin/<id>',
    view_func=AdminView.as_view(
        "update_task",
        model = Tasks
    )
)

tasks_bp.add_url_rule(
    rule = '/admin/<id>',
    view_func = AdminView.as_view(
        "delete_task",
        model = Tasks
    )
)

tasks_bp.add_url_rule(
    rule='/manager',
    view_func=ManagerView.as_view(
        "display_mgr_task",
        model = Tasks
    )
)

tasks_bp.add_url_rule(
    rule='/manager/<id>',
    view_func=ManagerView.as_view(
        "update_mgr_task",
        model = Tasks
    )
)

tasks_bp.add_url_rule(
    rule='/employee',
    view_func=EmployeeView.as_view(
        "display_emp_task",
        model = Tasks
    )
)

tasks_bp.add_url_rule(
    rule='/employee/<id>',
    view_func=EmployeeView.as_view(
        "update_emp_task",
        model = Tasks
    )
)

tasks_bp.add_url_rule(
    rule='/employee/assign/<task_id>',
    view_func=EmployeeTaskAssignView.as_view(
        "emp_task_assign",
        model = Tasks
    )
)

tasks_bp.add_url_rule(
    rule='/manager/assign/<task_id>',
    view_func=ManagerTaskAssignView.as_view(
        "mgr_task_assign",
        model = Tasks
    )
)

tasks_bp.add_url_rule(
    rule='/display/<int:no>',
    view_func=TaskPagination.as_view(
        "display_tasks",
        model = Tasks
    )
)