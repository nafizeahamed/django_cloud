from django.shortcuts import render
from django.http import HttpResponse
import pickle
import numpy as np
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UrlDataset
import json
# Create your views here.


@csrf_exempt
def home(request):
    if request.method == "POST" :
        data = json.loads(request.body.decode('utf-8'))
        url = data['url']
        print(url)
        classifier = pickle.load(open(r"Detecting_PhishingUrls/logisticModel_savedV2", 'rb'))
        vectorizer1 = pickle.load(open(r"Detecting_PhishingUrls/vectorizer_savedv2", 'rb'))
        df1 = np.array(url)
        vect_url = vectorizer1.transform(df1.ravel())
        X_pred = vect_url

        prediction = classifier.predict(X_pred)
        print(prediction)
        if (prediction == 1):
            s = "The url is malicious"
            print(s)

        else:
            s = "The url is legitimate"
            print(s)
        return JsonResponse(data={'result': str(prediction)})
        #print(HttpResponse(json.dumps({'result': 'i love you'}), content_type='application/json'))
    return render(request,"home.html")
def result(request):
    url = request.GET['url']
    classifier = pickle.load(open(r"C:\Users\akeel\Downloads\logisticModel_savedv2", 'rb'))
    vectorizer1 = pickle.load(open(r"C:\Users\akeel\Downloads\vectorizer_savedv2",'rb'))
    df1 = np.array(url)
    print(df1)
    #vectorizer1 =TfidfVectorizer()
    #vectorizer1.fit(df1.ravel())
    vect_url = vectorizer1.transform(df1.ravel())
    X_pred = vect_url

    prediction = classifier.predict(X_pred)
    print(prediction)
    if (prediction == 1):
        s="The url is malicious"
    else:
        s="The url is legitimate"
    return render(request, "result.html",{"URL":url,"OUTPUT":s})

def report(request):
    if request.method == "POST" :
        name = request.POST['name']
        url = request.POST['url']
        url_type = request.POST['url_type']
        obj = UrlDataset()
        obj.Name = name
        obj.Url = url
        obj.Type = url_type
        obj.save()
    return render(request, "report1.html")
