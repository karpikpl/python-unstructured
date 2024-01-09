from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from langchain.document_loaders import UnstructuredWordDocumentLoader, UnstructuredPowerPointLoader, UnstructuredExcelLoader
import logging

def index(request):
    print('Request for index page received')
    return render(request, 'hello_azure/index.html')

@csrf_exempt
def hello(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        
        if name is None or name == '':
            print("Request for hello page received with no name or blank name -- redirecting")
            return redirect('index')
        else:
            print("Request for hello page received with name=%s" % name)
            context = {'name': name }
            return render(request, 'hello_azure/hello.html', context)
    else:
        return redirect('index')
    
@csrf_exempt
def word(request):
    # loader = Docx2txtLoader("example_data/fake.docx")
    loader = UnstructuredWordDocumentLoader("example_data/sample4.docx")

    data = loader.load()
    logging.info("UnstructuredWordDocumentLoader: %s", data[-1])
    return render(request, 'hello_azure/word.html', {'data': data})

@csrf_exempt
def powerpoint(request):
    loader = UnstructuredPowerPointLoader("example_data/Paris.pptx")

    data = loader.load()
    logging.info("UnstructuredPowerPointLoader: %s", data[-1])
    return render(request, 'hello_azure/powerpoint.html', {'data': data})

@csrf_exempt
def excel(request):
    loader = UnstructuredExcelLoader("example_data/Paris.xlsx")

    data = loader.load()
    logging.info("UnstructuredExcelLoader: %s", data[-1])
    return render(request, 'hello_azure/excel.html', {'data': data})