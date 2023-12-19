from app.models.models import User
from app import db
from app.services.tasks import get_task_by_id

def get_user_by_id(id):
    user = User.query.get(id)
    return user

def assign_task(task_id, assigned_to):
    task = get_task_by_id(task_id)
    task.assigned_to = assigned_to
    db.session.commit()
