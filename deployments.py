#Установка curl & wget on the server
yum -y update
yum install net-tools
yum install bind-utils
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
usermod -aG docker $USER
#Установка docker-compose
curl -s https://api.github.com/repos/docker/compose/releases/latest \
  | grep browser_download_url \
  | grep docker-compose-Linux-x86_64 \
  | cut -d '"' -f 4 \
  | wget -qi -
#Добавление прав для бинарного файла Docker-compose
chmod +x docker-compose-Linux-x86_64
#Копируем бинарник в /usr/local/bin с изменением названия на docker-compose
mv docker-compose-Linux-x86_64 /usr/local/bin/docker-compose
#Даем ему права
chmod +x /usr/local/bin/docker-compose
#Перемещаем бинарник docker-compose в группу docker
chgrp docker /usr/local/bin/docker-compose
#Даем ему права 750 (only User/owner and group can read&execute)
chmod 750 /usr/local/bin/docker-compose
curl -L https://raw.githubusercontent.com/docker/compose/master/contrib/completion/bash/docker-compose -o /etc/bash_completion.d/docker-compose
source /etc/bash_completion.d/docker-compose
#Установка Git и переход в ветку master для запуливания файлов с гит
yum -y install git
git init
git checkout master
git pull https://github.com/Vera0/IVCGB.git
