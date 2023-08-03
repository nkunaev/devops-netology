Домашнее задание 9.6 Gitlab
---

# Подготовка к выполнению

* Создайте новый репозиторий в GitLab, наполните его файлами.
![img.png](img/img.png)

# Основная часть

## DevOps
1. Образ собирается на основе centos:7.
2. Python версии не ниже 3.7.
3. Установлены зависимости: flask flask-jsonpify flask-restful.
4. Создана директория /python_api.
5. Скрипт из репозитория размещён в /python_api.
6. Точка вызова: запуск скрипта.
![img_1.png](img/img_1.png)
7. При комите в любую ветку должен собираться docker image с форматом имени hello:gitlab-$CI_COMMIT_SHORT_SHA . Образ должен быть выложен в Gitlab registry или yandex registry.
![img_2.png](img/img_2.png)
![img_3.png](img/img_3.png)
![img_4.png](img/img_4.png)

## Product Owner
Вашему проекту нужна бизнесовая доработка: нужно поменять JSON ответа на вызов метода GET `/rest/api/get_info`, необходимо создать Issue в котором указать:

1. Какой метод необходимо исправить.
2. Текст с `{ "message": "Already started" }` на `{ "message": "Running"}`.
3. Issue поставить label: feature.

![img_5.png](img/img_5.png)

## Developer

1. Создать отдельную ветку, связанную с этим Issue. 
![img_6.png](img/img_6.png)
2. Внести изменения по тексту из задания. 
![img_7.png](img/img_7.png)
3. Подготовить Merge Request, влить необходимые изменения в master, проверить, что сборка прошла успешно.
![img_8.png](img/img_8.png)


### Tester

Разработчики выполнили новый Issue, необходимо проверить валидность изменений:

1. Поднять докер-контейнер с образом `python-api:latest` и проверить возврат метода на корректность.
2. Закрыть Issue с комментарием об успешности прохождения, указав желаемый результат и фактически достигнутый.
![img_9.png](img/img_9.png)

## Итог

В качестве ответа пришлите подробные скриншоты по каждому пункту задания:

- файл [gitlab-ci.yml](./src/.gitlab-ci.yml);
- [Dockerfile](./src/Dockerfile); 
- [лог](./src/pipline.log) успешного выполнения пайплайна;
- решённый Issue..
![img_10.png](img/img_10.png)