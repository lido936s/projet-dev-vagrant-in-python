Vagrant.configure("2") do |config|
  # https://technologie-geek.fr/installation-de-portainer-sur-docker/#Pr%C3%A9requis
  config.vm.box = "napramirez/kubuntu-14.04-LTS-amd64-lite" # https://app.vagrantup.com/napramirez/boxes/kubuntu-14.04-LTS-amd64-lite
  config.vm.hostname = "portainer-io"
  config.vm.network "private_network", type: "static", ip: "89.207.132.170"
  config.vm.provider "virtualbox" do |v|
    v.memory = 2048
    v.cpus = 2
  end

  # Ajoutez d'autres configurations supplemmentaires

  config.vm.provision "shell", inline: <<-SHELL
    # Exécutez les commandes nécessaires pour configurer Portainer.io
    # Par exemple, vous pouvez utiliser la commande `curl` pour télécharger le fichier de configuration
    curl -sSL https://raw.githubusercontent.com/portainer/portainer/master/compose/docker-compose.yml > /path/to/docker-compose.yml

    # Exécutez la commande Docker pour démarrer Portainer.io
    docker-compose -f /path/to/docker-compose.yml up -d

    # Ajoutez d'autres commandes ou scripts personnalisés pour configurer Portainer.io

    # Par exemple, vous pouvez créer un utilisateur administrateur par défaut
    docker exec -it portainer_portainer_1 /bin/sh -c "portainer-cli admin --username admin --password admin"
    
    # Créer un réseau virtuel Docker
    docker network create --subnet=172.18.0.0/16 portainer_network

    # Démarrer Portainer.io avec une adresse IP spécifique
    docker network inspect portainer_network | grep Gateway
    docker run -d --name portainer --network=portainer_network -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer --host=0.0.0.0 --host-management=172.18.0.2
    # ...

  SHELL

  # ...

end
