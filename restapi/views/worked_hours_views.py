from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models.worked_hours import WorkedHour
from ..serializers.worked_hours import WorkedHourSerializer

class WorkedHoursView(APIView):
    serializer_class = WorkedHourSerializer

    def get(self, request, user_id):
        worked_hours = WorkedHour.objects.filter(user_id=user_id)
        serializer = self.serializer_class(worked_hours, many=True)
        return Response(serializer.data)

    def post(self, request, user_id):
        data = request.data
        data['id'] = user_id
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
