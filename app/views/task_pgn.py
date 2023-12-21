from flask import jsonify, render_template, request, url_for
from flask.views import MethodView

from app.models.models import Tasks

class TaskPagination(MethodView):
     def __init__(self, model: Tasks = None) -> None:
          self.model = model
          
     def get(self, no):
          per_page = request.args.get('param')
          tasks = Tasks.query.paginate(page=no, per_page=per_page)
          task_list = []
          for task in tasks.items:
               task_list.append({
                   "id":task.id,
                   "title":task.title,
                   "description":task.description,
                   "status":task.status.value
               })

          if tasks.has_next:
               next_url = "http://127.0.0.1:5000" + url_for('task.display_tasks', no=no+1)
               return jsonify({"Tasks":task_list, "Next":next_url})
          
          return jsonify(tasks=task_list)