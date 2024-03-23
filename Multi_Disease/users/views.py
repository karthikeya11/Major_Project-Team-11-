from django.shortcuts import render, redirect
import pickle
import numpy as np
import joblib
# Create your views here.
def login(request):
    if request.method == "POST":
        admin = request.POST.get('username')
        password = request.POST.get('password')
        if admin == "admin" and password == "admin":
            return redirect('home')

    return render(request, 'login.html')

def home(request):
    if request.method == 'POST':
        # Extracting input features from the form
        gender = request.POST.get('gender')
        age = float(request.POST.get('age'))
        hemoglobin = float(request.POST.get('hemoglobin'))
        rbc = float(request.POST.get('rbc'))
        wbc = float(request.POST.get('wbc'))
        ast = float(request.POST.get('ast'))
        alt = float(request.POST.get('alt'))
        cholesterol = float(request.POST.get('cholesterol'))
        spirometry = float(request.POST.get('spirometry'))
        creatinine = float(request.POST.get('creatinine'))
        glucose = float(request.POST.get('glucose'))
        lipase = float(request.POST.get('lipase'))
        troponin = float(request.POST.get('troponin'))
        model = joblib.load("Model/model.pkl")
        input_data = np.array([gender, age, hemoglobin, rbc, wbc, ast, alt, cholesterol, spirometry, creatinine,
                                glucose, lipase, troponin])
        print(input_data)
        arr = input_data.reshape(1, -1)
        pred = round(float(model.predict(arr)))
        print(pred)
        result = ['Anemia','Asthma','Cardiovascular disease','Diabetics','Heart attack','Infection','Kidney Disease','Liver Disease','Pancreatitis']
        ans = result[pred]
        return render(request, 'result.html', {'predicted_disease': ans})
    else:
        # Render the form pagemod
        return render(request, 'home.html')