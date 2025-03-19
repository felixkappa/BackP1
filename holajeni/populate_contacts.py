import os
import django

# Asegúrate de que Django esté configurado con tu proyecto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'holajeni.settings')  # Usa el nombre correcto de tu proyecto
django.setup()  # Configura Django

from shopApp.models import Contact  # Importa tu modelo correctamente

# Resto de tu código para poblar la base de datos con Faker
from faker import Faker
fake = Faker()



def populate_contacts():
    for _ in range(30):
        contact = Contact.objects.create(
            full_name=fake.name(),
            address=fake.address(),
            phone=fake.phone_number(),
            email=fake.email(),
            active=True
        )

if __name__ == '__main__':
    populate_contacts()

print('Empezar a poblar la base de datos')