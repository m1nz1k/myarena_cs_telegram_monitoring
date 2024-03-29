from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

server_menu = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Мониторинг', 
                                                             callback_data='server_monitoring_'),
                                        InlineKeyboardButton(text='Сменить карту', 
                                                             callback_data='server_change_map_')
                                    ],
                                    [
                                        InlineKeyboardButton(text='Запустить сервер', 
                                                             callback_data='server_start_'),
                                        InlineKeyboardButton(text='Остановить сервер', 
                                                             callback_data='server_stop_'),
                                        InlineKeyboardButton(text='Перезапустить сервер', 
                                                             callback_data='server_restart_'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='Консоль', 
                                                             callback_data='server_send_console_'),
                                        InlineKeyboardButton(text='Сервера', 
                                                             callback_data='server_list'),
                                        
                                    ],
                                    
                                ])


server_list_menu = InlineKeyboardMarkup(row_width=1,
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