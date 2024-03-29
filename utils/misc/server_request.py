import requests

# мониторинг сервера
async def server_monitoring(token):

    response = requests.get(f'https://www.myarena.ru/api.php?query=status&token={token}')

    if response.json()['status'] == 'OK':
        response_status = response.json()
        return await get_data(response_status)
    
    return False


async def get_data(response):

    data = {
        "online": None,		        # 0=сервер offline, 1=сервер online, 2=сервер запускается или завис
        "name":	None,               # Название сервера
        "map": None,                # карта на сервере
        "players": None,            # игроков онлайн
        "playersmax": None,         # максимальное количество слотов для игроков   	# ID сервера
        "server_address": None,     # Адрес сервера
        "server_location": None,    # Навание Локации
        "server_type": None,	    # Тип
        "server_daystoblock": None,	# Дней до окончания аренды
    }

    # статус сервера
    if response['online'] == 0:
        data.update(online='Сервер выключен ❌')
    elif response['online'] == 1:
        data.update(online='Сервер работает ✅')
    elif response['online'] == 2:
        data.update(online='Сервер запускается ⏳')
    
    # название сервера
    data.update(name=response['data']['s']['name'])
    
    # текущий онлайн игроков
    data.update(players=response['data']['s']['players'])
    
    # максимальное кол-во слотов на сервере
    data.update(playersmax=response['data']['s']['playersmax'])
    
    # карта на сервере
    data.update(map=response['data']['s']['map'])
    
    # айпи и порт сервера
    data.update(server_address=response['server_address'])
    
    # тип сервера
    data.update(server_type=response['server_type'])
    
    # осталось дней аренды
    data.update(server_daystoblock=response['server_daystoblock'])

    # локация сервера
    data.update(server_location=response['server_location'])

    return data


# получить список карт
async def get_maps(token) -> list:
    maps_response = requests.get(f'https://www.myarena.ru/api.php?query=getmaps&token={token}')
    if maps_response.json()['status'] == 'OK':
        maps_response = maps_response.json()
        maps_list = maps_response['maps']
        return maps_list
    return []


# сменить карту
async def map_change(map, token):
    change_map_response = requests.get(f'https://www.myarena.ru/api.php?query=changelevel&map={map}&token={token}')
    if change_map_response.json()['status'] == 'OK':
        return True
    return False


# запуск сервера
async def start_server(token):
    start_response = requests.get(f'https://www.myarena.ru/api.php?query=start&token={token}')
    if start_response.json()['status'] == 'OK':
        return True
    return False


# остановка сервера
async def stop_server(token):
    stop_response = requests.get(f'https://www.myarena.ru/api.php?query=stop&token={token}')
    if stop_response.json()['status'] == 'OK':
        return True
    return False


# рестарт сервера
async def restart_server(token):
    restart_response = requests.get(f'https://www.myarena.ru/api.php?query=restart&token={token}')
    if restart_response.json()['status'] == 'OK':
        return True
    return False


# отправка команды в консоль
async def console_send(command, token):
    console_response = requests.get(f'https://www.myarena.ru/api.php?query=consolecmd&cmd={command}&token={token}')
    if console_response.json()['status'] == 'OK':
        return True
    return False


# проверка токена на валидность
async def is_valid_token(token):
    response = requests.get(f'https://www.myarena.ru/api.php?query=status&token={token}')
    if response.status_code == 200:
        if response.json()['status'] == 'OK':
            return True
    return False