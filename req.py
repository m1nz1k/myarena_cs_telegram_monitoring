import requests

def console_send(command):
    console_response = requests.get(f'https://www.myarena.ru/api.php?query=consolecmd&cmd={command}&token=666660f80a99eeab8298568a9ef0b374')
    print(console_response.json())

console_send('meta list')