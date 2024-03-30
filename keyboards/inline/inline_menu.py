from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

server_menu = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Мониторинг', 
                                                             callback_data='server_monitoring'),
                                        InlineKeyboardButton(text='Сменить карту', 
                                                             callback_data='server_change_map')
                                    ],
                                    [
                                        InlineKeyboardButton(text='Консоль', 
                                                             callback_data='server_send_console'),
                                        InlineKeyboardButton(text='Сервера', 
                                                             callback_data='server_list'),
                                        
                                    ],
                                                                        [
                                        InlineKeyboardButton(text='Запустить сервер', 
                                                             callback_data='server_start'),
                                    ],

                                                                        [
                                        InlineKeyboardButton(text='Остановить сервер', 
                                                             callback_data='server_stop'),
                                    ],

                                                                        [
                                        InlineKeyboardButton(text='Перезапустить сервер', 
                                                             callback_data='server_restart'),
                                    ],
                                    
                                ])


server_list_menu = InlineKeyboardMarkup(row_width=1,
                                resize_keyboard=True,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Добавить сервер', 
                                                             callback_data='server_add'),
                                        InlineKeyboardButton(text='Удалить сервер', 
                                                             callback_data='server_del'),
                                        InlineKeyboardButton(text='Выбрать сервер', 
                                                             callback_data='select_server'),
                                        InlineKeyboardButton(text='Назад', 
                                                             callback_data='back_to_menu'),
                                    ],              
                                ])