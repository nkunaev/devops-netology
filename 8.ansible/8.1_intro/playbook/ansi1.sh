#!/bin/bash
# -*- ENCODING: UTF-8 -*-

#check ansible
dpkg -s ansible &> /dev/null
if [ $? -ne 0 ]; then
    echo "Install ansible first"
    exit 1
fi

#set docker images
machines=("pycontribs/fedora" \
          "matthewfeickert/docker-python3-ubuntu" \
          "centos/python-38-centos7")

#set name of the machines to shoot them down in the end
names=("ubuntu" "centos7" "fedora")

docker_run () {
   bash -c "docker run -it --rm -d --name $1 $2 /bin/bash"
   echo "$2 containter has been started"
}

docker_stop () {
  bash -c "docker stop $1"
  echo "$1 containter has been stopped"
}

# Идем циклом по массиву из имен образов, проверяем в условии имя, и исходя из этого обхываем контейнер.
# Можно конечно было бы и задавать имена, но лень уже было фантазировать :)

for os in "${machines[@]}"; do
  case $os in
  pycontribs/fedora)
    docker_run fedora "$os"
    ;;
  matthewfeickert/docker-python3-ubuntu)
    docker_run ubuntu "$os"
    ;;
  centos/python-38-centos7)
    docker_run centos7 "$os"
    ;;
  esac
done

echo "Пароль 'netology'"

# запускаем ансамбль
ansible-playbook -i inventory/prod.yml site.yml --ask-vault-pass

# выключаем машины
for name in "${names[@]}"; do
  docker_stop "$name"
  done
