from django.shortcuts import render, redirect, HttpResponse

def index(request):
    response ="hey its views!"
    return HttpResponse(response)