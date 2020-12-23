from django.shortcuts import render
from django.http import HttpResponse
from xml.etree.ElementTree import Element, SubElement, Comment, tostring, ElementTree
import xml.dom.minidom
import random
from . import xmltranslate
from . import music

vex_flow = """

<html>
<script src="https://unpkg.com/vexflow/releases/vexflow-min.js"></script>
<body>
<div id="boo">Test</div>
<script>

VF = Vex.Flow;

// Create an SVG renderer and attach it to the DIV element named "boo".
var div = document.getElementById("boo")
var renderer = new VF.Renderer(div, VF.Renderer.Backends.SVG);

// Configure the rendering context.
renderer.resize(500, 500);
var context = renderer.getContext();
context.setFont("Arial", 10, "").setBackgroundFillStyle("#eed");

// Create a stave of width 400 at position 10, 40 on the canvas.
var stave = new VF.Stave(10, 40, 400);

// Add a clef and time signature.
stave.addClef("treble").addTimeSignature("4/4");

// Connect it to the rendering context and draw!
stave.setContext(context).draw();


var notes = [
  // A quarter-note C.
  new VF.StaveNote({clef: "treble", keys: ["c/4"], duration: "q" }),

  // A quarter-note D.
  new VF.StaveNote({clef: "treble", keys: ["d/4"], duration: "q" }),

  // A quarter-note rest. Note that the key (b/4) specifies the vertical
  // position of the rest.
  new VF.StaveNote({clef: "treble", keys: ["b/4"], duration: "qr" }),

  // A C-Major chord.
  new VF.StaveNote({clef: "treble", keys: ["c/4", "e/4", "g/4"], duration: "q" })
];

// Create a voice in 4/4 and add the notes from above
var voice = new VF.Voice({num_beats: 4,  beat_value: 4});
voice.addTickables(notes);

// Format and justify the notes to 400 pixels.
var formatter = new VF.Formatter().joinVoices([voice]).format([voice], 400);

// Render voice
voice.draw(context, stave);


</script>

</body>

</html>


"""


def index(request):
    return HttpResponse("Hello, world. You're at the piano index.")


def page_test(request):

    first_measure = music.Measure()
    note_test = music.NoteRest(4, 60)
    first_measure.add_note(note_test)

    second_measure = music.Measure()
    while second_measure.duration < second_measure.max_duration:
        second_measure.add_note(music.NoteRest(2,random.randint(21,102)))
    print(second_measure)


    notation = xmltranslate.create_xml_stub()
    xmltranslate.add_part_to_xml(notation)

    dom = xml.dom.minidom.parseString(tostring(notation))
    pretty_xml_as_string = dom.toprettyxml()

    html = f'<textarea rows="20" cols="100">{pretty_xml_as_string}</textarea> <p>{note_test.pitch_name}</p>'

    return HttpResponse(html)
