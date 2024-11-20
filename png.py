import requests
import base64
from pathlib import Path

def upload_image_to_imgur(image_path, client_id):
    headers = {
        'Authorization': f'Client-ID {client_id}',
    }

    # Чтение файла и кодирование в base64
    with open(image_path, 'rb') as image_file:
        image_data = base64.b64encode(image_file.read()).decode('utf-8')
        
        response = requests.post(
            'https://api.imgur.com/3/image',
            headers=headers,
            json={'image': image_data}
        )
    
    if response.status_code == 200:
        data = response.json()
        return data['data']['link']
    else:
        print('Error uploading image:', response.json())
        return None
folder_dir = "C:\\Steam\\userdata\\991345764\\760\\remote\\4000\\screenshots"
images = Path(folder_dir).glob('*.jpg')
if __name__ == '__main__':
    image_path = 'C:\\Steam\\userdata\\991345764\\760\\remote\\4000\\screenshots\\20241103210028_1.jpg'  # Укажите путь к вашему изображению
    client_id = '2ee1096b152bdbe'  # Замените на ваш Client ID

    image_url = upload_image_to_imgur(image_path, client_id)
    if image_url:
        print('Image uploaded successfully! URL:', image_url)