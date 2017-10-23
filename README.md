# Ближайшие бары

Данный скрипт парсит файл json со списком баров и их параметрами,
после чего находит самый маленький бар и самый большой бар.

Затем запрашивает координаты и находит ближайший к этим координатам бар

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash

$ python bars.py путь_до_файла_json # Возможно потребуется использовать python3 вместо просто python

Самый большой бар:

{'geometry': {'coordinates': [37.638228501070095, 55.70111462948684], 'type': 'Point'}, 'properties': {'DatasetId': 1796, 'VersionNumber': 2, 'ReleaseNumber': 2, 'RowId': 'fbe6c340-4707-4d74-b7ca-2b84a23bf3a8', 'Attributes': {'global_id': 169375059, 'Name': 'Спорт бар «Красная машина»', 'IsNetObject': 'нет', 'OperatingCompany': None, 'AdmArea': 'Южный административный округ', 'District': 'Даниловский район', 'Address': 'Автозаводская улица, дом 23, строение 1', 'PublicPhone': [{'PublicPhone': '(905) 795-15-84'}], 'SeatsCount': 450, 'SocialPrivileges': 'нет'}}, 'type': 'Feature'}


Самый маленький бар:

{'geometry': {'coordinates': [37.35805920566864, 55.84614475898795], 'type': 'Point'}, 'properties': {'DatasetId': 1796, 'VersionNumber': 2, 'ReleaseNumber': 2, 'RowId': '17adc22c-5c41-4e4b-872f-815b521f2b53', 'Attributes': {'global_id': 20675518, 'Name': 'БАР. СОКИ', 'IsNetObject': 'нет', 'OperatingCompany': None, 'AdmArea': 'Северо-Западный административный округ', 'District': 'район Митино', 'Address': 'Дубравная улица, дом 34/29', 'PublicPhone': [{'PublicPhone': '(495) 258-94-19'}], 'SeatsCount': 0, 'SocialPrivileges': 'нет'}}, 'type': 'Feature'}


Чтобы узнать ближайший бар - укажите координаты:
Введите ширину:
52.23231
Введите долготу:
12.23232
Самый близкий бар:

{'geometry': {'coordinates': [37.92096900029184, 55.69988800002597], 'type': 'Point'}, 'properties': {'DatasetId': 1796, 'VersionNumber': 2, 'ReleaseNumber': 2, 'RowId': 'af3820bd-14ca-4a68-870d-a3c743e28819', 'Attributes': {'global_id': 281494732, 'Name': 'Таверна', 'IsNetObject': 'нет', 'OperatingCompany': None, 'AdmArea': 'Юго-Восточный административный округ', 'District': 'район Некрасовка', 'Address': 'проспект Защитников Москвы, дом 8', 'PublicPhone': [{'PublicPhone': '(977) 511-73-23'}], 'SeatsCount': 16, 'SocialPrivileges': 'нет'}}, 'type': 'Feature'}

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
