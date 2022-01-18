from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from myapi.models import Document
from myapi.serializers import DocSerializer
from rest_framework import viewsets
from rest_framework import permissions

# Create your views here.

@csrf_exempt
def list_docs(request):
    """
    List all docs, or create a new doc.
    """
    if request.method == 'GET':
        docs = Document.objects.all()
        serializer = DocSerializer(docs, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DocSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def doc_detail(request, pk):
    """
    Retrieve, update or delete a doc.
    """
    try:
        doc = Document.objects.get(pk=pk)
    except Document.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DocSerializer(doc)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DocSerializer(doc, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        doc.delete()
        return HttpResponse(status=204)


class DocViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all().order_by('-created')
    serializer_class = DocSerializer


