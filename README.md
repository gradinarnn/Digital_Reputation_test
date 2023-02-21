
## Запуск
### 1. Клонирование репозитория
```commandline
git clone <данные вашего репозитория>
```


### 2. Создание виртуального окружения
### 3. Установка пакетов Python
Если при установке возникает ошибка соединения, неоходимо производить установку с комощью команды:

```commandline
pip install -r requirements.txt
```


### 5. Выполнить миграции командой:
```commandline
python .\questionnaire\manage.py migrate
```

### 6. Создать суперпользователя командой:
```commandline
python .\questionnaire\manage.py createsuperuser
```

### 7. Запустить бэк:
```
python .\questionnaire\manage.py runserver <host:port>
```

### 8. Перейти в папку с фронтом:
```
cd .\questionnaire\questionnaire_frontend\
```

### 9. Установка пакетов js:
```
npm install
```

### 10. Запуск фронта :
```
npm run dev
```

### 11. Установка верных хостов для верного взаимодействия фронта и бэка :
В /questionnaire/questionnaire/settings.py прописываем в ALLOWED_HOSTS и CORS_ORIGIN_WHITELIST данные фронта

В /questionnaire/questionnaire_frontend/src/plugins/apollo/index.js в uri прописываем uri graphql
