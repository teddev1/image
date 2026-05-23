from .models import UploadedImage
from django.shortcuts import render
from predict import predict_image


from django.shortcuts import render

def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):

    if request.method == "POST":

        username = request.POST.get('username')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        print("\n--- New Contact Form Submission---")
        print("username:", username)
        print("email:", email)
        print("subject:", subject)
        print("message:", message)

    return render(request, 'contact.html')




 
def upload_image(request):

    result = None
    confidence = None
    uploaded_image = None

    if request.method == 'POST':

        image = request.FILES['image']

        uploaded_image = UploadedImage.objects.create(image=image)

        image_path = uploaded_image.image.path

        result, confidence = predict_image(image_path)

    return render(request, 'index.html', {
        'result': result,
        'confidence': confidence,
        'uploaded_image': uploaded_image
    })