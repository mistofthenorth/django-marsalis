from django.shortcuts import render
from django.http import HttpResponse
from xml.etree.ElementTree import Element, SubElement, Comment, tostring, ElementTree
import random


def index(request):
    return HttpResponse("Hello, world. You're at the piano index.")


def page_test(request):
	random_number = random.randint(1,100)
	print("testing log to the console")

	top = Element('score-partwise')

	comment = Comment("this is a new comment")
	top.append(comment)
	top.attrib = {"version":"3.1"}


	print(tostring(top))

	return HttpResponse(str(random_number))