from django.http import JsonResponse
import datetime

def home(request):
    return JsonResponse({
        "name" : "Wizz",
        "track" : "Backend",
        "current_day" : datetime.datetime.now(),
        "status_code" : 200,
        "github_file_url" : "https://github.com/dauntless001/hngx-task-one/blob/master/hngx/views.py",
        "github_repo_url" : "https://github.com/dauntless001/hngx-task-one"
    })