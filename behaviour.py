error_message = 'Я вас не понимаю'

start_message_id = 'familiarity'
first_message_id = 'familiarity'

behavior = {
    'familiarity': {
        'text': 'Привет! Я шаблонный бот, созданный пользователями https://vk.com/perfectrum и https://vk.com/simplesavely. Можете посмотреть мои исходники или написать мне что-нибудь в базу данных.',
        'type': 1,
        'expect': ['Покажи исходники', 'Запиши в БД'],
        'children': ['code', 'db']
        },
    'options': {
        'text': 'Можете посмотреть мои исходники или написать мне что-нибудь в базу данных.',
        'type': 1,
        'expect': ['Покажи исходники', 'Запиши в БД'],
        'children': ['code', 'db']
        },
    'code': {
        'text':'А вот и не покажу',
        'type': 1,
        'expect':['назад'],
        'children':['options']
        },
    'db':{
        'text':'Что мне записать?',
        'type': 2,
        'expect':[],
        'children':['got_it']
            },
    'got_it': {
        'text': 'Записал, спасибо!',
        'type': 1,
        'expect': ['Назад'],
        'children': ['options']
        }
    }
