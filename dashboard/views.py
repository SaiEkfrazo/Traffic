from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Traffic
from .serializers import TrafficSerializer
from rest_framework import status
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse
from django.contrib.auth import logout
from django.shortcuts import redirect
from datetime import datetime
from django.utils import timezone

class TrafficList(APIView):
    # def get(self, request):
    #     from_date_str = request.GET.get('from_date')
    #     to_date_str = request.GET.get('to_date')
    #     location = request.GET.get('location')
    #     camera = request.GET.get('camera')

    #     from_date = datetime.strptime(from_date_str, '%Y-%m-%d') if from_date_str else None
    #     to_date = datetime.strptime(to_date_str, '%Y-%m-%d') if to_date_str else None

    #     traffic_records = Traffic.objects.all()

    #     if from_date:
    #         traffic_records = traffic_records.filter(date__gte=from_date)
    #         if to_date:
    #             traffic_records = traffic_records.filter(date__lte=to_date)
    #     if location:
    #         traffic_records = traffic_records.filter(location__icontains=location)
    #     if camera:
    #         traffic_records = traffic_records.filter(camera__icontains=camera)

    #     return render(request, 'dashboard.html', {'traffic_records': traffic_records})

    def get(self, request):
        from_date = request.query_params.get('from_date')
        to_date = request.query_params.get('to_date')
        location = request.query_params.get('location')
        camera = request.query_params.get('camera')
        violation_type = request.query_params.get('violation_type')

        traffic_records = Traffic.objects.all()

        if from_date:
            from_date = datetime.strptime(from_date, '%Y-%m-%d')
            if not from_date.tzinfo:  # Check if the datetime is naive (not timezone-aware)
                from_date = timezone.make_aware(from_date)
            start_date = from_date
            end_date = start_date + timezone.timedelta(days=1)
            traffic_records = traffic_records.filter(date__gte=start_date, date__lt=end_date)

        if to_date:
            to_date = datetime.strptime(to_date, '%Y-%m-%d')
            if not to_date.tzinfo:  # Check if the datetime is naive (not timezone-aware)
                to_date = timezone.make_aware(to_date)
            traffic_records = traffic_records.filter(date__lte=to_date)
        if location:
            traffic_records = traffic_records.filter(location__icontains=location)
        if camera:
            traffic_records = traffic_records.filter(camera__icontains=camera)
        if violation_type:
            traffic_records = traffic_records.filter(violation_type__icontains=violation_type)

        serializer = TrafficSerializer(traffic_records, many=True)
        return Response(serializer.data)




def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return JsonResponse({'redirect_url': reverse('dashboard')})  # Provide the URL name for redirection
        else:
            return JsonResponse({'error': 'Invalid username or password.'}, status=400)  # Send error response

    return render(request, 'login.html')




def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to your login URL name


def dashboard(request):
    videos = Traffic.objects.values_list('video', flat=True)
    context = {'videos': videos}
    return render(request, 'dashboard.html', context)