# helloworld

## Начало работы

Ведите разработку новой функциональности (feature), исправление ошибок (bugfix) и рефакторинг (refactoring) в отдельных ветках git.
```
git checkout -b branch_name
```

Cоздавайте Merge Request.
Общее владение кодом важный аспект в командной разработке. Качество кода может регламентироваться стандартами разработки и контролироваться путем проведения ревью.

### Запуск/остановка на локальной машине
Запуск:
```
docker-compose up -d
```
Остановка:
```
docker-compose down
```

### Ссылки
* [swagger T1](https://swagger.edu.scibox.tech/docs)
* [swagger docker-compose](http://127.0.0.1:8000/docs)
* [pgadmin docker-compose](http://127.0.0.1:5050)

### Доступы
* Postgres: postgres/mysecretpassword
* PgAdmin: admin@admin.com/root


### Развертывание в Т1
- Добавьте Deploy Key в настройках проекта (Settings -> Repository). Можно взять из настроек проектов с уже работающим cicd.
- Создайте файл .gitlab-ci.yml с конфигурацией сборки и развертывания. Можно взять из проекта с уже работающим cicd.
- Не забывайте про конфигурирование работы с proxy (proxy.vtb.t1cloud:3128). Это особенность работы в облаке Т1. 

### Работа с Poetry
- Установка пакета poetry ```pip install poetry```
- Создание нового проекта ```poetry new helloworld```
- Добавление нового пакета в проект ```poetry add fastapi```
- Запуск сервиса с помощью poetry ```poetry run uvicorn helloworld.app:app --reload```

### Начало работа с миграциями БД (Alembic)
- Устанавливаем пакеты alembic (sqlalchemy, sqlmodel)
```poetry add alembic``` (Если возникает несовместимость версии sqlmodel, то следует снизить версию sqlalchemy до 1.4.41)
- Инициализация скриптов миграций ```alembic init migrations```
- добавить в migrations/script.py.mako ```import sqlmodel``` 
- Добавить в migrations/env.py импорт моделей БД
```
from helloworld.models import *
from helloworld.settings import settings
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)
```

### Создание и применение миграций БД
- Генерация файла миграции ```alembic revision --autogenerate -m 'имя_миграции'```
- Проверить генерацию кода в migrations/versions.
- Применить миграцию на БД ```alembic upgrade head```
- Откатить последнюю миграцию на БД ```alembic downgrade -1```
- Для генерации инициализирующего скрипта для существующей БД, нужно создать пустую БД и сгенерировать миграцию на ней (alembic stamp head позволит начать с существующей миграции на целевой БД).

## Полезные ссылки
### Взаимодействие в команде

- [ ] [Invite team members and collaborators](https://docs.gitlab.com/ee/user/project/members/)
- [ ] [Create a new merge request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
- [ ] [Automatically close issues from merge requests](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)
- [ ] [Enable merge request approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/)
- [ ] [Automatically merge when pipeline succeeds](https://docs.gitlab.com/ee/user/project/merge_requests/merge_when_pipeline_succeeds.html)

### Тестирование и CICD


- [ ] [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/quick_start/index.html)
- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing(SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)
- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/ee/topics/autodevops/requirements.html)
- [ ] [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/ee/user/clusters/agent/)
- [ ] [Set up protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)
