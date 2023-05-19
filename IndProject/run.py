import sys
sys.path.append(r'C:\Users\Mateusz\IndProject\API')
sys.path.append(r'C:\Users\Mateusz\IndProject\Website testing')
from WebsiteTesting import Website_testing_script as wts    #import funkcji do testowania strony e-commerce
from API import API_testing as at

#plik do uruchamiania skryptów

#testujemy stronę e-commerce
#skrypt zawiera cały use case do automatycznego zamówienia 2 przedmiotów ze sklpeu internetgowego
wts.website_testing_script()

#próbujemy zalogować się za pomocą tokenu
at.login_with_token('special-key')

at.create_user('testuser', '123', 'test@tester.pl', 'Tester', "Testersson")

#wywołujemy funkcję wysyłajacą zdjęcie
at.upload_image()

#tworzymy 3 nowe zwierzaki
at.create_new_pets()

#wyszukujemy wszystkie zwierzaki z odpowiednim statusem
at.search_pets()

#aktualizujemy zdjęcie i nazwę zwierzaka nr. 1
at.update_pet()

#usuwamy kotka
at.delete_pet()

#składamy 2 zamówienia
at.place_orders()

#wyszsukujemy zamówienia
at.find_orders()