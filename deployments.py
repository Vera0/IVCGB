import values
#Установка curl & wget on the server
sudo yum -y install curl
sudo yum -y install wget
#Установка Docker репозиторий
sudo curl  https://download.docker.com/linux/centos/docker-ce.repo -o /etc/yum.repos.d/docker-ce.repo
#Обновление кэша
sudo yum makecache
#Установка Docker
sudo dnf -y  install docker-ce --nobest
#Запуск Docker-compose при включении сервера
sudo systemctl enable --now docker
#Добавление пользователя докер в группу
sudo usermod -aG docker $USER
#Установка docker-compose
curl -s https://api.github.com/repos/docker/compose/releases/latest \
  | grep browser_download_url \
  | grep docker-compose-Linux-x86_64 \
  | cut -d '"' -f 4 \
  | wget -qi -
chmod +x docker-compose-Linux-x86_64
sudo mv docker-compose-Linux-x86_64 /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo chgrp docker /usr/local/bin/docker-compose
sudo chmod 750 /usr/local/bin/docker-compose
sudo curl -L https://raw.githubusercontent.com/docker/compose/master/contrib/completion/bash/docker-compose -o /etc/bash_completion.d/docker-compose
source /etc/bash_completion.d/docker-compose
#Установка Git и переход в ветку master для запуливания файлов с гит
sudo yum install git
sudo git init
git checkout master
git pull https://github.com/Vera0/IVCGB.git
