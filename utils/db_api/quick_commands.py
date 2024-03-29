from asyncpg import UniqueViolationError
from utils.db_api.db_gino import db
from utils.db_api.schemas.user import User
from datetime import datetime, date



async def add_user(user_id: int, username: str, first_name: str, last_name: str, active_token: str):
    try:
        user = User(user_id=user_id, username=username, first_name=first_name, last_name=last_name, active_token=active_token)
        await user.create()
    except UniqueViolationError:
        print('Пользователь не добавлен.')



async def select_all_users():
    users = await User.query.gino.all()
    return users



async def count_users():
    count = await db.func.count(User.user_id).gino.scalar()
    return count


async def select_user(user_id: int):
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user


async def get_user_by_id(user_id: int):
    try:
        user = await User.query.where(User.user_id == user_id).gino.first()
        return user
    except Exception as e:
        print(f"Ошибка при получении пользователя по ID: {e}")


# обновление токена
async def update_user_active_token(user_id: int, active_token: str):
    try:

        user = await User.query.where(User.user_id == user_id).gino.first()
        if user:
            user.active_token = active_token
            await user.update(active_token=active_token).apply()
    except Exception as e:
        print(f"Ошибка при обновлении активного токена пользователя: {e}")

# достаем токен
async def get_user_active_token(user_id: int):
    try:
        user = await User.query.where(User.user_id == user_id).gino.first()
        if user:
            return user.active_token
        else:
            print(f"Пользователь с ID {user_id} не найден")
    except Exception as e:
        print(f"Ошибка при получении активного токена пользователя: {e}")

    return None


