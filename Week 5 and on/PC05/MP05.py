def getNewNote(baseFreq,nSemitones):
      return baseFreq*2**(nSemitones/12)

baseFrequency = 440
nSemitones = 3

print(getNewNote(baseFrequency,nSemitones))