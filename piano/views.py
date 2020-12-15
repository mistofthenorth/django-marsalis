from django.shortcuts import render
from django.http import HttpResponse
from xml.etree.ElementTree import Element, SubElement, Comment, tostring, ElementTree
import xml.dom.minidom
import random

note_names = ["A", "B", "C", "D", "E", "F", "G"]

def create_xml_stub():
    xml = Element('score-partwise')

    xml.attrib = {"version": "3.1"}
    part_list = SubElement(xml, 'part-list')
    score_part = SubElement(part_list, "score-part")
    score_part.attrib = {"id": "P1"}
    part_name = SubElement(score_part, 'part-name')
    part_name.text = "MusicXML Part"
    score_instrument = SubElement(score_part, 'score-instrument')
    score_instrument.attrib = {"id": "P1-I1"}
    instrument_name = SubElement(score_instrument, 'instrument-name')
    instrument_name.text = "Instrument 1"

    return xml


def add_note(measure):
    note = SubElement(measure, "note")
    pitch = SubElement(note, "pitch")
    step = SubElement(pitch, "step")
    step_choice = random.choice(note_names)
    step.text = step_choice
    octave = SubElement(pitch, "octave")
    octave.text = "4"
    duration = SubElement(note, "duration")
    duration.text = "1"
    voice = SubElement(note, "voice")
    voice.text = "1"
    note_type = SubElement(note, "type")
    note_type.text = "eighth"


def add_measure(part, measure_number, final=False):
    measure = SubElement(part, 'measure')
    measure.attrib = {"number": str(measure_number)}
    for i in range(8):
        add_note(measure)
    """
    note1 = SubElement(measure, "note")
    rest = SubElement(note1, "rest")
    rest.attrib = {"measure": "yes"}
    duration = SubElement(note1, "duration")
    duration.text = "8"
    voice = SubElement(note1, "voice")
    voice.text = "1"
    """
    if final:
        barline = SubElement(measure, "barline")
        barline.attrib = {"location": "right"}
        bar_style = SubElement(barline, "bar-style")
        bar_style.text = "light-heavy"


def add_part_to_xml(xml):

    part = SubElement(xml, 'part')
    part.attrib = {"id": "P1"}
    add_measure(part, 1)
    add_measure(part, 2)


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

    notation = create_xml_stub()
    add_part_to_xml(notation)

    dom = xml.dom.minidom.parseString(tostring(notation))
    pretty_xml_as_string = dom.toprettyxml()

    html = f'<textarea rows="20" cols="100">{pretty_xml_as_string}</textarea>'

    return HttpResponse(vex_flow)
