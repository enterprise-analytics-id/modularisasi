import requests

url = 'https://detik.com'
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Success! Response = {response.status_code}')
        # print(f'Contect {response.text}')
    else:
            print('Woops, ada kesalahan request')
except Exception as e:
    print(f'There is an error {e}')
print('Program ended')