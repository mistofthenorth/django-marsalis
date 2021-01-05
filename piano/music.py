pitch_table = {
	20 : 'Rest',
	21 : 'A0',
	22 : 'A#0/Bb0',
	23 : 'B0',
	24 : 'C1',
	25 : 'C#1/Db1',
	26 : 'D1',
	27 : 'D#1/Eb1',
	28 : 'E1',
	29 : 'F1',
	30 : 'F#1/Gb1',
	31 : 'G1',
	32 : 'G#1/Ab1',
	33 : 'A1',
	34 : 'A#1/Bb1',
	35 : 'B1',
	36 : 'C2',
	37 : 'C#2/Db2',
	38 : 'D2',
	39 : 'D#2/Eb2',
	40 : 'E2',
	41 : 'F2',
	42 : 'F#2/Gb2',
	43 : 'G2',
	44 : 'G#2/Ab2',
	45 : 'A2',
	46 : 'A#2/Bb2',
	47 : 'B2',
	48 : 'C3',
	49 : 'C#3/Db3',
	50 : 'D3',
	51 : 'D#3/Eb3',
	52 : 'E3',
	53 : 'F3',
	54 : 'F#3/Gb3',
	55 : 'G3',
	56 : 'G#3/Ab3',
	57 : 'A3',
	58 : 'A#3/Bb3',
	59 : 'B3',
	60 : 'C4',
	61 : 'C#4/Db4',
	62 : 'D4',
	63 : 'D#4/Eb4',
	64 : 'E4',
	65 : 'F4',
	66 : 'F#4/Gb4',
	67 : 'G4',
	68 : 'G#4/Ab4',
	69 : 'A4',
	70 : 'A#4/Bb4',
	71 : 'B4',
	72 : 'C5',
	73 : 'C#5/Db5',
	74 : 'D5',
	75 : 'D#5/Eb5',
	76 : 'E5',
	77 : 'F5',
	78 : 'F#5/Gb5',
	79 : 'G5',
	80 : 'G#5/Ab5',
	81 : 'A5',
	82 : 'A#5/Bb5',
	83 : 'B5',
	84 : 'C6',
	85 : 'C#6/Db6',
	86 : 'D6',
	87 : 'D#6/Eb6',
	88 : 'E6',
	89 : 'F6',
	90 : 'F#6/Gb6',
	91 : 'G6',
	92 : 'G#6/Ab6',
	93 : 'A6',
	94 : 'A#6/Bb6',
	95 : 'B6',
	96 : 'C7',
	97 : 'C#7/Db7',
	98 : 'D7',
	99 : 'D#7/Eb7',
	100 : 'E7',
	101 : 'F7',
	102 : 'F#7/Gb7',
	103 : 'G7',
	104 : 'G#7/Ab7',
	105 : 'A7',
	106 : 'A#7/Bb7',
	107 : 'B7',
	108 : 'C8'
}


class Phrase:
	
	def __init__(self):

		self.measures = []

	def get_interval_ratio(self):
		previous_pitch = 20
		note_count = 0
		pitch_distance = 0
		for measure in self.measures:
			for note in measure.notes:
				if note.pitch == 20:
					continue
				distance = abs(note.pitch - previous_pitch)
				pitch_distance = distance + pitch_distance
				note_count += 1

		if note_count > 0:
			interval_ratio = pitch_distance/note_count
		else:
			interval_ratio = 0

		return interval_ratio

	def add_measure(self, measure):
		self.measures.append(measure)

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

	@property
	def pitch_name(self):
		return pitch_table[self.pitch]
	

	def __str__(self):
		return f"({pitch_table[self.pitch]}-{self.duration})"
