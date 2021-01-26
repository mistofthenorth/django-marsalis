from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from xml.etree.ElementTree import Element, SubElement, Comment, tostring, ElementTree
import xml.dom.minidom
import random
from . import xmltranslate
from . import music


def index(request):

    try:
        phrase_length = int(request.GET["phrase_length"])
    except:
        phrase_length = 8
    print(f'Phrase length is : {phrase_length}')
    my_phrase = music.Phrase(phrase_length)

    template = loader.get_template('piano/index.html')
    context = {'test' : 'This is my context text',
                'phrase' : my_phrase}
    return HttpResponse(template.render(context, request))
