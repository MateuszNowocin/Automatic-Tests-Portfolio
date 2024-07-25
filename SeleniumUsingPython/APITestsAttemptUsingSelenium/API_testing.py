import requests
import json

base_url = 'https://petstore.swagger.io/v2'

def create_user(username, password, email, first_name, last_name):
    user_data = {
        'username': username,
        'password': password,
        'email': email,
        'firstName': first_name,
        'lastName': last_name
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(f'{base_url}/user', headers=headers, data=json.dumps(user_data))
    print(f'Create User - Status Code: {response.status_code}')
    if response.status_code == 200:
        print("Użytkownik został utworzony.")
        print(response.json())
    else:
        print("Nie udało się utworzyć użytkownika.")
        print(response.json())

def login_with_token(auth_token):
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {auth_token}'}
    response = requests.get(f'{base_url}/user/login', headers=headers)
    print(f'Login with Token - Status Code: {response.status_code}')
    if response.status_code == 200:
        print("Użytkownik został zalogowany za pomocą tokenu.")
    else:
        print("Nie udało się zalogować użytkownika za pomocą tokenu.")
        print(response.json())
def upload_image():
    file_path = r'C:\Users\Mateusz\Desktop\ptaszor.jpg'
    files = {'file': open(file_path, 'rb')}
    response = requests.post(f'{base_url}/pet/1/uploadImage', files=files)
    print(f'Upload Image - Status Code: {response.status_code}')
    print(response.json())

def create_new_pets():
    pet_data = [
        {
            'id': 1,
            'name': 'Dog',
            'photoUrls': ['https://www.rd.com/wp-content/uploads/2020/11/GettyImages-889552354-e1606774439626.jpg'],
            'status': 'available'
        },
        {
            'id': 2,
            'name': 'Cat',
            'photoUrls': ['https://mspmag.com/downloads/54330/download/shutterstock_1276621966.'
                          'jpg?cb=c74273ddf5fda2d66333b2f4e64d632d'],
            'status': 'available'
        },
        {
            'id': 3,
            'name': 'Bird',
            'photoUrls': ['https://media.istockphoto.com/id/986720632/photo/close-up-snowy-owl-eye-with-wooden'
                          '-background.jpg?b=1&s=170667a&w=0&k=20&c=kdES4UnIqz-o_fuq3Pz-vDE9XVrP9v9fKiulH2_N6rE='],
            'status': 'available'
        }
    ]
    headers = {'Content-Type': 'application/json'}
    for pet in pet_data:
        response = requests.post(f'{base_url}/pet', headers=headers, data=json.dumps(pet))
        print(f'Create Pet - Status Code: {response.status_code}')
        print(response.json())


def search_pets():
    response = requests.get(f'{base_url}/pet/findByStatus?status=available')
    print(f'Search Pets - Status Code: {response.status_code}')
    print(response.json())
    if response.status_code == 200:
        print("Oto wyniki wyszukiawania zwierzaków: ")
        print(response.json())
    else:
        print("Coś poszło nie tak.")
        print(response.json())

def update_pet():
    pet_id = 1
    updated_pet_data = {
        'id': pet_id,
        'name': 'Updated Dog',
        'photoUrls': ['https://i.redd.it/1akxefpzwfv21.jpg'],
        'status': 'available'
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f'{base_url}/pet', headers=headers, data=json.dumps(updated_pet_data))
    print(f'Update Pet - Status Code: {response.status_code}')
    if response.status_code == 200:
        print("Prawidłowo zaktualizowano pieseła")
        print(response.json())
    else:
        print("Coś poszło nie tak.")
        print(response.json())


def delete_pet():
    pet_id = 2
    response = requests.delete(f'{base_url}/pet/{pet_id}')
    print(f'Delete Pet - Status Code: {response.status_code}')
    response_data = response.json()
    if 'message' in response_data and response_data['message'] == '2':
        print("Kotek został usunięty :(")
        print(response_data)
    else:
        print("Coś poszło nie tak.")
        print(response_data)


def place_orders():
    order_data = [
        {
            'id': 1,
            'petId': 1,
            'quantity': 1,
            'shipDate': '2023-05-19T10:00:00.000Z',
            'status': 'placed',
            'complete': False
        },
        {
            'id': 2,
            'petId': 3,
            'quantity': 2,
            'shipDate': '2023-05-20T10:00:00.000Z',
            'status': 'placed',
            'complete': False
        }
    ]
    headers = {'Content-Type': 'application/json'}
    for order in order_data:
        response = requests.post(f'{base_url}/store/order', headers=headers, data=json.dumps(order))
        print(f'Place Order - Status Code: {response.status_code}')
        if response.status_code == 200:
            print("Zamówienie zostało złożone")
            print(response.json())
        else:
            print("Coś poszło nie tak.")
            print(response.json())


def find_orders():
    response = requests.get(f'{base_url}/store/inventory')
    print(f'Find Orders - Status Code: {response.status_code}')
    print(response.json())
    if response.status_code == 200:
        print("Oto złożone zamówienia: ")
        print(response.json())
    else:
        print("Coś poszło nie tak.")
        print(response.json())

def main():
    login_with_token('special-key')
    create_user('testuser', '123', 'test@tester.pl', 'Tester', "Testersson")
    upload_image()
    create_new_pets()
    search_pets()
    update_pet()
    delete_pet()
    place_orders()
    find_orders()

if __name__ == '__main__':
    main()