from .models import Notes
from rest_framework.response import Response
from .serializers import NoteSerializer


def getNotesDetails(request):
    notes = Notes.objects.all()
    serializer = NoteSerializer(notes,many=True)
    return Response(serializer.data)

def getNoteById(request,pk):
    note = Notes.objects.get(id=pk)
    serializer = NoteSerializer(note)
    return Response(serializer.data)

def updateNote(request,pk):
    data = request.data
    note = Notes.objects.get(id=pk)
    serializer = NoteSerializer(instance=note,data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

def deleteNote(request,pk):
    note = Notes.objects.get(id=pk)
    note.delete()
    return Response('note is deleted succesfully')

def createNote(request):
    data = request.data
    note = Notes.objects.create(
        body=data['body']
    )
    serializer = NoteSerializer(note)
    return Response(serializer.data)