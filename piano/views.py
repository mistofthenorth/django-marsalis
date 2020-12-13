from django.shortcuts import render
from django.http import HttpResponse
from xml.etree.ElementTree import Element, SubElement, Comment, tostring, ElementTree
import xml.dom.minidom
import random


def create_xml_stub():
    top = Element('score-partwise')

    top.attrib = {"version": "3.1"}
    part_list = SubElement(top, 'part-list')
    score_part = SubElement(part_list, "score-part")
    score_part.attrib = {"id": "P1"}
    part_name = SubElement(score_part, 'part-name')
    part_name.text = "MusicXML Part"
    score_instrument = SubElement(score_part, 'score-instrument')
    score_instrument.attrib = {"id": "P1-I1"}
    instrument_name = SubElement(score_instrument, 'instrument-name')
    instrument_name.text = "Instrument 1"

    return top

def add_measure_to_xml(xml):

    part = SubElement(xml, 'part')
    part.attrib = {"id": "P1"}
    measure1 = SubElement(part, 'measure')
    measure1.attrib = {"number": "1"}
    note1 = SubElement(measure1, "note")
    rest = SubElement(note1, "rest")
    rest.attrib = {"measure": "yes"}
    duration = SubElement(note1, "duration")
    duration.text = "8"
    voice = SubElement(note1, "voice")
    voice.text = "1"

    barline = SubElement(measure1, "barline")
    barline.attrib = {"location": "right"}
    bar_style = SubElement(barline, "bar-style")
    bar_style.text = "light-heavy"

def index(request):
    return HttpResponse("Hello, world. You're at the piano index.")


def page_test(request):

    top = create_xml_stub()
    add_measure_to_xml(top) 

    dom = xml.dom.minidom.parseString(tostring(top))
    pretty_xml_as_string = dom.toprettyxml()

    html = f'<textarea rows="20" cols="100"> {pretty_xml_as_string} </textarea>'

    return HttpResponse(html)
