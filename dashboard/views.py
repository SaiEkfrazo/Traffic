from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Traffic
from .serializers import TrafficSerializer
from rest_framework import status
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect

class TrafficList(APIView):
    def get(self, request):
        traffic_records = Traffic.objects.all()
        serializer = TrafficSerializer(traffic_records, many=True)

        # Pass the data to the template and render it
        return render(request, 'dashboard.html', {'traffic_records': serializer.data})


    def post(self, request):
        serializer = TrafficSerializer(data=request.data)   
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if username and password match the static values
        if username == 'root' and password == 'root':
            # Authentication successful, redirect to the 'TrafficView' URL name
            return redirect('TrafficView')  # Redirects to the 'TrafficView' URL

    # Render the login form template if no successful login
    return render(request, 'login.html')