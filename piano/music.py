class Phrase:
	
	def __init__(self):

		self.measures = []

class Measure:
	
	def __init__(self, max_duration=8):

		self.notes = []
		self.max_duration = 8
	
	@property
	def duration(self):
		return sum([x.duration for x in self.notes])

	def add_note(self, note):
		if self.duration + note.duration > self.max_duration:
			print("Error, too many notes in this measure")
		else:
			self.notes.append(note)

	def __str__(self):
		output_string = ''
		return output_string.join([str(x) for x in self.notes])

class NoteRest:

	def __init__(self, duration, pitch):

		self.duration = duration
		self.pitch = pitch

	def __str__(self):
		return f"({self.pitch}-{self.duration})"
