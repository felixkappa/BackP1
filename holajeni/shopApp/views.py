from django.shortcuts import render
from django.http import HttpResponse
from django.templatetags.static import static
from shopApp.models import Product
from shopApp.models import Contact 

def about(request):
    active_contacts = Contact.objects.filter(active=True)  
    print("Contactos activos en la vista:", active_contacts)  # Agregar este print para depurar
    return render(request, 'shopApp/about.html', {'contacts': active_contacts})



def home(request):
    product_list = Product.objects.all()
    special_offers = Product.objects.filter(product_is_offer=True)
    my_context = {
    'user': 'guest',
    'message': 'Largo de aqui',
    'special_offers': special_offers,
    'product_list' : product_list,
    'special_offers_2': [
        {
            'img': static('shopApp/img/nintendo_pikachu.jpg'),
            'name': 'Mascarilla hidratante de sábila',
            'cost': '14'
        },
        {
            'img': 'https://ditecmex.com/cdn/shop/files/D_NQ_NP_721807-MLM44961459768_022021-O.webp?v=1717356354',
            'name': 'Consola de videojuegos portátil XE150',
            'cost': '450'
        },
        {
            'img': 'https://steamuserimages-a.akamaihd.net/ugc/290853501092266364/59A3601E5ABD191F07E5F7A021EA4C6B4364793D/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false',
            'name': 'Reloj gótico de Luffy',
            'cost': '130'
        },
        {
            'img': 'https://steamuserimages-a.akamaihd.net/ugc/481146537293937796/7CC1B266722534B3738949D66AD02573C1700478/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false',
            'name': 'Muñeco de Batman tamaño real',
            'cost': '14438'
        },
        {
            'img': 'https://pbs.twimg.com/profile_images/1452465225374916609/uzuLkaEW_200x200.jpg',
            'name': 'Otros',
            'cost': '23'
        },
    ]
}

    return render(request, 'shopApp/index.html', my_context)
  #  return HttpResponse("<h1>¡Bienvenido a ShopApp!</h1>")

def about(request):
    return render(request, 'shopApp/about.html')