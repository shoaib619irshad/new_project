from flask import Blueprint

from app.models.models import Tasks
from app.views.admin import AdminView
from app.views.manager import ManagerView
from app.views.employee import EmployeeView
from app.views.task_assign import *


tasks_bp = Blueprint('task', __name__, url_prefix='/task')

tasks_bp.add_url_rule(
     rule = '/admin/add',
    view_func = AdminView.as_view(
        "add",
        model = Tasks,
    )
)

tasks_bp.add_url_rule(
    rule = '/admin/display/<id>',
    view_func = AdminView.as_view(
        "display",
        model = Tasks
    )
)

tasks_bp.add_url_rule(
    rule = '/admin/update/<id>',
    view_func=AdminView.as_view(
        "update",
        model = Tasks
    )
)

tasks_bp.add_url_rule(
    rule = '/admin/delete/<id>',
    view_func = AdminView.as_view(
        "delete",
        model = Tasks
    )
)

tasks_bp.add_url_rule(
    rule='/manager/display',
    view_func=ManagerView.as_view(
        "display_mgr",
        model = Tasks
    )
)

tasks_bp.add_url_rule(
    rule='/manager/update/<id>',
    view_func=ManagerView.as_view(
        "update_mgr",
        model = Tasks
    )
)

tasks_bp.add_url_rule(
    rule='/employee/display',
    view_func=EmployeeView.as_view(
        "display_emp",
        model = Tasks
    )
)

tasks_bp.add_url_rule(
    rule='/employee/update/<id>',
    view_func=EmployeeView.as_view(
        "update_emp",
        model = Tasks
    )
)

tasks_bp.add_url_rule(
    rule='/employee/<task_id>',
    view_func=EmployeeTaskAssignView.as_view(
        "emp_task_assign",
        model = Tasks
    )
)

tasks_bp.add_url_rule(
    rule='/manager/<task_id>',
    view_func=ManagerTaskAssignView.as_view(
        "mgr_task_assign",
        model = Tasks
    )
)