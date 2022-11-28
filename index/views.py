from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from ciphey import eval_encryption

# Create views here.
def blank(request):
    url = reverse_lazy("index:index")
    return redirect(url)

def index(request):
    return render(request, "index/index.html")

def decrypt(request):
    if request.method == "POST":
        encrypted_text = str(request.POST["encrypted_text"])

        if encrypted_text == "":
            return render(request, "index/decrypt.html", 
            {"result": "*Empty string is not allowed*", "error": 1})
        
        result, error = eval_encryption(encrypted_text)
        
        if error == 0:
            return render(request, "index/decrypt.html", {"result": result})
        else:
            return render(request, "index/decrypt.html", {"result": result, "error": error})
    else:
        return render(request, "index/decrypt.html")