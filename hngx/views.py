from django.http import JsonResponse

from datetime import timezone
import datetime


def home(request):
    return JsonResponse({
        "slack_name" : "Wizz",
        "track" : "backend",
        "current_day" : "Tuesday",
        "utc_time" : datetime.datetime.now(timezone.utc),
        "status_code" : 200,
        "github_file_url" : "https://github.com/dauntless001/hngx-task-one/blob/master/hngx/views.py",
        "github_repo_url" : "https://github.com/dauntless001/hngx-task-one"
    })