#!/bin/bash
#Установка curl & wget on the server
yum -y update
yum -y install net-tools
yum -y install bind-utils
yum -y install curl
yum -y install wget
#Установка Docker репозитория
curl  https://download.docker.com/linux/centos/docker-ce.repo -o /etc/yum.repos.d/docker-ce.repo
#Обновление кэша
yum makecache
#Установка Docker
dnf -y  install docker-ce --nobest
#Запуск Docker при включении сервера
systemctl enable --now docker
#Добавление пользователя в группу Docker
usermod -aG docker $(whoami)
#Установка docker-compose
curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
#Добавление прав для бинарного файла Docker-compose и создание симлинка
chmod +x /usr/local/bin/docker-compose
ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
#Перемещаем бинарник docker-compose в группу docker
chgrp docker /usr/local/bin/docker-compose
#Даем ему права 750 (only User/owner and group can read&execute)
chmod 750 /usr/local/bin/docker-compose
#Установка Git и переход в ветку master для запуливания файлов с гит
yum -y install git
git init
git checkout master
git pull https://github.com/Vera0/IVCGB.git
