from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from xml.etree.ElementTree import Element, SubElement, Comment, tostring, ElementTree
import xml.dom.minidom
import random
from . import xmltranslate
from . import music


def index(request):

    my_phrase = music.Phrase(4)

    for measure in my_phrase.measures:
        print(measure)

    my_phrase = music.Phrase(4)
    notes_list = []
    for measures in my_phrase.measures:
        for notes in measures.notes:
            notes_list.append(notes.pitch_name[:3])


    template = loader.get_template('piano/index.html')
    context = {'test' : 'This is my context text'}
    return HttpResponse(template.render(context, request))
