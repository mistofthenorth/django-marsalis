class Phrase:
	
	def __init__(self):

		self.measures = []

class Measure:
	
	def __init__(self):

		self.notes = []
		self.duration = 0

	def add_note(self, note):
		self.notes.append(note)
		self.duration += note.duration

class NoteRest:

	def __init__(self, duration, pitch):

		self.duration = duration
		self.pitch = pitch

