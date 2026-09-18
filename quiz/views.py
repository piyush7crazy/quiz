from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Quiz
from .serializers import QuizSerializer

@api_view(['POST'])
def create_quiz_api(request):
    serializer=QuizSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors , status=400)

@api_view(['GET'])
def list_quiz_api(request):
    q=Quiz.objects.all()
    serializer=QuizSerializer(q,many=True)
    return Response(serializer.data , status=200)


@api_view(['GET'])
def detail_quiz_api(request,id):
    q=Quiz.objects.get(id=id)
    serializer=QuizSerializer(q)
    return Response(serializer.data , status=200)


@api_view(['PATCH'])
def update_quiz_api(request,id):
    q=Quiz.objects.get(id=id)
    serializer=QuizSerializer(q , data=request.data  , partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data , status=206)
    return Response(serializer.errors , status=400)


@api_view(['DELETE'])
def delete_quiz_api(request,id):
    q=Quiz.objects.get(id=id)
    q.delete()
    return Response(status=200)