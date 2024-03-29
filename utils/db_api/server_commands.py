from asyncpg import UniqueViolationError
from utils.db_api.schemas.server import Server


async def create_server(server_name: str, server_token: str):
    try:
        server = Server(server_name=server_name, server_token=server_token)
        await server.create()
        return server.id
    except UniqueViolationError:
        print('Сервер не добавлен')
        return False
    

# функция для получения списка серверов из базы данных
async def get_all_servers():
    try:
        servers = await Server.query.gino.all()
        return servers
    except Exception as e:
        print(f"Ошибка при получении списка серверов: {e}")


async def delete_server(server_token: str):
    try:
        server = await Server.query.where(Server.server_token == server_token).gino.first()
        if server:
            await server.delete()
            return True
        else:
            return False
    except Exception as e:
        print(f"Ошибка при удалении сервера: {e}")
        return False
