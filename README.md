## Сайт ГБУЗ МО "Ивантеевская ЦГБ"

На данный момент почти закончена работа над сайтом, в котором я постарался использовать некоторые инструменты из стека технологий DevOps инженера.

Сайт сделан на основе Wordpress с использованием балансировщика на Nginx и БД MySql. Готовый вариант можно посмотреть по ссылке [ivcgb.ru](http://94.253.92.24).

В качестве компонентов были использованы инструменты:
- Wordpress (CMS)
- MySql (Database)
- Nginx (Webserver)
- CentOS 8 minimal (Linux server)
- Docker (Docker-compose deploy)
- Python (Deploy script)

Все необходимые файлы для запуска стандартного экземпляра сборки и необходимая для развертывания информация есть в репозитории [Vera0/IVCGB](https://github.com/Vera0/IVCGB):
- Deployment.py (Скрипт развертывания на сервере)
- Docker-compose (Docker-compose манифест для запуска экземпляра сборки на сервере)
- nginx-conf (Отдельная папка с простым конфиг файлом web-сервера nginx)
- .env (Файл с вынесенными переменными для MySql и Wordpress)

Работа над сайтом в процессе, планируется добавить еще некоторые компоненты, а скрипт развертывания улчушить и проверить в работе с помощью чистого развертывания с нуля. 
Так же планируется добавить функцию резервного копирования базы данных Wordpress и систему мониторинга нагрузки сайта, на основе Prometheus + Grafana.