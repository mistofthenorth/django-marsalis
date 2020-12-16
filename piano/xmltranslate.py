from xml.etree.ElementTree import Element, SubElement, Comment, tostring, ElementTree
import xml.dom.minidom


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


def add_note(measure, step):
    note = SubElement(measure, "note")
    pitch = SubElement(note, "pitch")
    step = SubElement(pitch, "step")
    step_choice = step
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
        add_note(measure, "A")
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
