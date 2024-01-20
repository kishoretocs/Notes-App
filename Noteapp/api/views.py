from rest_framework.decorators import api_view
from .utils import getNotesDetails,getNoteById,createNote,updateNote,deleteNote
# Create your views here.




@api_view(['GET','POST'])
def getNotes(request):
    if request.method == 'GET':
        return getNotesDetails(request)
    if request.method == 'POST':
        return createNote(request)

@api_view(['GET','PUT','DELETE'])
def getNote(request,pk):
    if request.method == 'GET':
        return getNoteById(request,pk)
    if request.method == 'PUT':
        return updateNote(request,pk)
    if request.method == 'DELETE':
        return deleteNote(request,pk)

# @api_view(['GET'])
# def getNotes(request):
#     if request.method == 'GET':
#         notes = Notes.objects.all()
#         serializer = NoteSerializer(notes, many=True)
#         return Response(serializer.data)
    

# @api_view(['GET'])
# def getNote(request, pk):
#     note = Notes.objects.get(id=pk)
#     serializer = NoteSerializer(note)
#     return Response(serializer.data)

# @api_view(['PUT'])
# def updateNote(request,pk):
#     data = request.data
#     note = Notes.objects.get(id=pk)
#     serializer = NoteSerializer(instance=note,data=data)
#     print(serializer,'-----------------------')
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# @api_view(['DELETE'])
# def deleteNote(request,pk):
#     note = Notes.objects.get(id=pk)
#     note.delete()
#     return Response('Note was deleted')

# @api_view(['POST'])
# def createNote(request):
#     data = request.data
#     print(data, '000000000000000000000000000')
#     note = Notes.objects.create(
#         body=data['body']
#     )
#     serializer = NoteSerializer(note,many=False)
#     return Response(serializer.data)