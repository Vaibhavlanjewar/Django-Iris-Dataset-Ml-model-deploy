from django.shortcuts import render
from joblib import load
model=load('./SavedModels/model.joblib')
# Create your views here.

def predictor(request):
    if request.method=='POST':
        seple_length=request.POST['Sepal_length']
        seple_width=request.POST['Sepal_width']
        petal_length=request.POST['Petal_length']
        petal_width=request.POST['Petal_width']
        y_pred=model.predict([[seple_length,seple_width,petal_length,petal_width]])
        if y_pred[0]==0:
           y_pred='Setosa'
        elif y_pred[0]==1:
             y_pred='Vercicolor'
        else:
            y_pred='Viriginica'     
        return render(request,'main.html',{'result':y_pred})
    return render(request,'main.html')


