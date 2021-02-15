INTRO_TEXT = 'Привет! Я покажу тебе информацию, связанную с поступлением в МГТУ имени Николая Эрнестовича Баумана.Ты можешь спросить меня о таких вещах, как приемная комиссия, факультеты, день открытых дверей, общежития, стипендии, студенческая жизнь. Для завершения навыка скажите "Спасибо"'
ERROR_TEXT = 'Извините не поняла вас. Я могу дать информацию только на такие темы, как приемная комиссия, факультеты, день открытых дверей, общежития, стипендии, студенческая жизнь. Пожалуйста, спрашивайте только о них.'


def handler(event, context):
    """
    Entry-point for Serverless Function.
    :param event: request payload.
    :param context: information about current execution context.
    :return: response to be serialized as JSON.
    """
    text = INTRO_TEXT
    if 'request' in event and \
            'original_utterance' in event['request'] \
            and event['request']['original_utterance'].lower() in ['факультеты']:
        text = 'У нас 6 направлений обучения и более 12 факультетов. Поближе познакомиться с ними ты сможешь по ссылке https://bmstu.ru/abitur/general/presentations/'
    elif 'request' in event and \
            'original_utterance' in event['request'] \
            and event['request']['original_utterance'].lower() in ['приемная комиссия']:
        text = 'Вы можете позвонить по номеру (499) 263-6541 или же написать на почту abiturient@bmstu.ru'
    elif 'request' in event and \
            'original_utterance' in event['request'] \
            and event['request']['original_utterance'].lower() in ['день открытых дверей']:
        text = 'Два раза в год двери нашего Университета открываются для Абитуриентов. Подробнее о датах можно узнать на сайте МГТУ'
    elif 'request' in event and \
            'original_utterance' in event['request'] \
            and event['request']['original_utterance'].lower() in ['общежития']:
        text = 'Общежития имеются на ряде факультетов МГТУ им. Н.Э. Баумана:МТ, СМ, РК, Э, ИУ, РЛ, БМТ, кафедрах "Интеллектуальная собственность" и "Цифровая криминалистика", а также в Калужском и Мытищинском филиалах.На факультетах ИБМ, ФН, Л, АК, ПС, РКТ, РТ, ОЭП, СГН общежитий нет. При зачислении в учебные группы этих факультетов общежитие не предоставляется.'
    elif 'request' in event and \
            'original_utterance' in event['request'] \
            and event['request']['original_utterance'].lower() in ['стипендии']:
        text = 'Кроме обычной стипендии, учащиеся Университета могут получать повышенные стипендии за хорошую учебу, вуз оказывает материальную поддержку нуждающимся студентам.'
    elif 'request' in event and \
            'original_utterance' in event['request'] \
            and event['request']['original_utterance'].lower() in ['студенческая жизнь']:
        text = 'В нашем Университете очень интересная и насыщенная студенческая жизнь. Вуз организует различные студенческие мероприятия, предлагает доступ к огромному объему научной литературы, предлагает вкусное и полезное питание своим учащимся.'
    elif 'request' in event and \
            'original_utterance' in event['request'] \
            and event['request']['original_utterance'].lower() in ['спасибо']:
        text = 'Рада, что помогла. Желаю вам успешного поступления!'
        url = 'https://bmstu.ru/'
        buttons = 'buttons'
        return {
            'version': event['version'],
            'session': event['session'],
            'response': {
                'text': text,
                'url': url,
                'buttons': [
                    {
                        'title': 'Cайт МГТУ',
                        'payload': {},
                        'url': 'https://bmstu.ru/',
                    }
                ],
                'end_session': 'true'
            },
        }
    elif 'request' in event and \
            'original_utterance' in event['request'] \
            and len(event['request']['original_utterance']) > 0:
        text = ERROR_TEXT

    return {
        'version': event['version'],
        'session': event['session'],
        'response': {
            'text': text,
            'end_session': 'false'
        },
    }
