from django.shortcuts import render
from django.http import HttpResponse
import random


def index(request):
    return HttpResponse("Hello, world. You're at the piano index.")

def page_test(request):
	random_number = random.randint(1,100)
	return HttpResponse(str(random_number))