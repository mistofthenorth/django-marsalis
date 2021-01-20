from django.shortcuts import render
from django.http import HttpResponse
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

    vex_flow = f"""

    <html>
    <script src="https://unpkg.com/vexflow/releases/vexflow-min.js"></script>
    <body>
    <div id="boo"></div>
    <script>

    const VF = Vex.Flow;

    // Create an SVG renderer and attach it to the DIV element named "boo".
    var vf = new VF.Factory({{renderer: {{elementId: 'boo'}}}});
    var score = vf.EasyScore();
    var system = vf.System();

    system.addStave({{
      voices: [score.voice(score.notes('{notes_list[0]}/q, {notes_list[1]}, {notes_list[2]}, {notes_list[3]}'))]
    }}).addClef('treble').addTimeSignature('4/4');

    system.addStave({{
      voices: [score.voice(score.notes('{notes_list[4]}/q, {notes_list[5]}, {notes_list[6]}, {notes_list[7]}'))]
    }}).addClef('treble').addTimeSignature('4/4');

    vf.draw();



    </script>

    </body>

    </html>


    """

    return HttpResponse(vex_flow)
