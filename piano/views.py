from django.shortcuts import render
from django.http import HttpResponse
from xml.etree.ElementTree import Element, SubElement, Comment, tostring, ElementTree
import xml.dom.minidom
import random


def index(request):
    return HttpResponse("Hello, world. You're at the piano index.")


def page_test(request):
    random_number = random.randint(1, 100)
    print("testing log to the console")

    top = Element('score-partwise')

    comment = Comment("this is a new comment")
    top.append(comment)
    top.attrib = {"version": "3.1"}
    part_list = SubElement(top, 'part-list')
    part_name = SubElement(part_list, 'part_name')
    part_name.text = "MusicXML Part"

    print(tostring(top))

    dom = xml.dom.minidom.parseString(tostring(top))
    pretty_xml_as_string = dom.toprettyxml()

    print(pretty_xml_as_string)

    return HttpResponse(str(random_number))
