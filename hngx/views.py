from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "name" : "Wizz",
        "track" : "Backend",
        "Bio" : "Number One Bad Man"
    })