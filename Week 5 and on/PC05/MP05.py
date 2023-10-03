#newnote = baseFreq * 2.0**(N/12)
def getNewNote(baseFreq,nSemitones):
      return baseFreq * 2.0 ** (nSemitones/12)

newNote = getNewNote(333,0.5)
print(newNote)