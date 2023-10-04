import json
from .models import Robot
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import RobotSerializer

@csrf_exempt
def create_robot(request):
    if request.method == "POST":
        dt = json.loads(request.body)
        serial = dt.get('serial')
        model = dt.get('model')
        version = dt.get('version')
        created = dt.get('created')

        serializer = RobotSerializer(data=dt)

        if serializer.is_valid():

            if serial and model and version and created:
                robot = Robot(serial=serial.upper(), model=model.upper(),
                              version=version.upper(), created=created)
                robot.save()
                return JsonResponse({"success": True})
            else:
                return JsonResponse({"success": False, "error": "Invalid data"})
        else:
            return JsonResponse({"success": False, "error": serializer.errors})
    else:
        return JsonResponse({"success": False, "error": "Invalid request method"})

