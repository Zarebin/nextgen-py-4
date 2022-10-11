from .models import Shortener, VisitUrl
from django.http import JsonResponse, HttpResponseRedirect, Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.utils import timezone


@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        try:
            user = User.objects.create_user(request.data['username'], request.data['email'], request.data['password'])
            user.save()
            return JsonResponse({"result": "new account has been created"})
        except:
            return JsonResponse({"result": 'Please enter "username" , "password", "email"'})


@api_view(['GET'])
def login_user(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return JsonResponse({"result": "You have logined before!"})
        else:
            user = authenticate(username=request.data["username"], password=request.data["password"])
            if user is not None:
                login(request, user)
                result = "login successfully " + str(request.user.username) + "::"
                return JsonResponse({"result": result}, safe=False)
            else:
                return JsonResponse({"result": "username or password is wrong. Try one more time."}, safe=False)


@api_view(['GET'])
def login_state(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            logins = request.user.username + " has logined"
            return JsonResponse({"result": logins}, safe=False)
        else:
            return JsonResponse({"result": "No One"}, safe=False)


@api_view(['GET'])
def specific_url_detail(request, shortened_part):
    if request.method == 'GET':
        times_followed = 0
        unique_times_followed = 0
        long_url = ""
        try:
            shortener = Shortener.objects.get(short_url=shortened_part)
            times_followed = shortener.times_followed
            unique_times_followed = shortener.unique_times_followed
            long_url = shortener.long_url
        except:
            return JsonResponse({"result": "There isn't any long url with this shortened part"})
        try:
            visit_url = list(VisitUrl.objects.filter(short_url=shortened_part).values("ip_address", "visit_date", "device", "response_date", "browser", "browser_version", "os", "os_version", "visitor"))
            return JsonResponse({
                "times_followed": times_followed, 
                "unique_times_followed": unique_times_followed,
                "long_url": long_url,
                "visit_data": visit_url
                }, safe=False)
        except:
            return JsonResponse({"result": "No one has visited the link yet"}, safe=False)


def logout_user(request):
    logout(request)
    return JsonResponse({"result": "logout successfully"}, safe=False)


def device(request):
    if request.user_agent.is_mobile:
        return "mobile"
    if request.user_agent.is_tablet:
        return "tablet"
    if request.user_agent.is_pc:
        return "pc"
    if request.user_agent.is_bot:
        return "bot"
    return "postman"
   

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


@api_view(['GET'])
def urlshortener(request):
    if request.method == 'GET':
        # user has logined
        if request.user.is_authenticated:
            try:
                # saved before
                duplicate_url = Shortener.objects.get( long_url=request.data['long_url'] , shortner_owner=request.user.username)
                return Response({"long_url": duplicate_url.long_url,"shortUrl":duplicate_url.short_url}, status=status.HTTP_201_CREATED)
            except:
                shorturl = Shortener(long_url=request.data['long_url'], device=device(request), ip_address=get_client_ip(request),shortner_owner=request.user.username)
                shorturl.save()
                return Response({"long_url": shorturl.long_url,"shortUrl":shorturl.short_url}, status=status.HTTP_201_CREATED) 
        else:
            # anonymous user
            shorturl = Shortener(long_url=request.data['long_url'], device=device(request), shortner_owner="Unknkown", ip_address=get_client_ip(request))
            shorturl.save()
        return Response({"long_url": shorturl.long_url, "shortUrl":shorturl.short_url}, status=status.HTTP_201_CREATED) 


@api_view(['GET'])
def get_urlshortener_registerd(request):
    # Getting all the urls of customer with customer_id
    if request.method == 'GET':
        if request.user.is_authenticated:
            urls = list(Shortener.objects.filter(shortner_owner=request.user.username).values("long_url", "short_url", "times_followed", "unique_times_followed", "created_date", "device", "ip_address"))
            return JsonResponse(urls, safe=False)
        else:
            return JsonResponse({"result":"please login first"})


def create_visit_url(request, shortened_part, visitor):
    visit_url = VisitUrl(
        short_url=shortened_part,
        visitor=visitor,
        device=device(request),
        browser=request.user_agent.browser.family,
        browser_version=request.user_agent.browser.version_string,
        os=request.user_agent.os.family,
        os_version=request.user_agent.os.version_string,
        ip_address=get_client_ip(request)
    )
    visit_url.save()
    return visit_url


@api_view(['Get'])
def redirect_url_view(request, shortened_part):
    if request.method == 'GET':
        try:
            shortener = Shortener.objects.get(short_url=shortened_part)
            if request.user.is_authenticated:
                registered_visitor = VisitUrl.objects.filter(short_url=shortened_part, visitor=request.user.username)
                if not(registered_visitor):
                    # registered visitor has visited the site before
                    shortener.unique_times_followed += 1
                visit_url = create_visit_url(request, shortened_part, request.user.username)
            else:
                unknown_visitor = VisitUrl.objects.filter(
                    short_url=shortened_part,
                    visitor="unknown",
                    device=device(request),
                    browser=request.user_agent.browser.family,
                    browser_version=request.user_agent.browser.version_string,
                    os=request.user_agent.os.family,
                    os_version=request.user_agent.os.version_string,
                    ip_address=get_client_ip(request) 
                    )
                if not(unknown_visitor):
                    shortener.unique_times_followed += 1
                visit_url = create_visit_url(request, shortened_part, "unknown")
            shortener.times_followed += 1
            visit_url.response_date = timezone.now()
            visit_url.save()
            shortener.save()
            return HttpResponseRedirect(shortener.long_url)
        except Shortener.DoesNotExist:
            raise Http404("Sorry the link is broken :(( we don't have this short url ")
