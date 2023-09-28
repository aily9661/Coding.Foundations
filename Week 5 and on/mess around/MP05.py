def getNewNote(baseFreq,nSemitones):
	newFreq = float(baseFreq) * (float(nSemitones)/12)**2
	return newFreq

baseFrequency = 440
nSemitones = 3
print(getNewNote(baseFrequency,nSemitones))