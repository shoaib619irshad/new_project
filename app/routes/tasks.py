from flask import Blueprint

from app.models.models import Tasks
from app.views.tasks import TasksView


tasks_bp = Blueprint('task', __name__, url_prefix='/task')

tasks_bp.add_url_rule(
     rule = '/add',
    view_func = TasksView.as_view(
        "add",
        model = Tasks,
    )
)

tasks_bp.add_url_rule(
    rule = '/display/<id>',
    view_func = TasksView.as_view(
        "display",
        model = Tasks
    )
)

tasks_bp.add_url_rule(
    rule = '/update/<id>',
    view_func=TasksView.as_view(
        "update",
        model = Tasks
    )
)

tasks_bp.add_url_rule(
    rule = 'delete/<id>',
    view_func = TasksView.as_view(
        "delete",
        model = Tasks
    )
)