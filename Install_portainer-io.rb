#Pour installer Portainer sur Vagrant depuis le shell, vous pouvez suivre les étapes suivantes :

#1. Assurez-vous d'avoir Vagrant et VirtualBox installés sur votre système.

#2. CCréez un dossier pour votre projet Vagrant et accédez-y dans votre terminal.

#3. Initialisez un nouveau projet Vagrant en exécutant la commande suivante :

# vagrant init

#4. Modifiez le fichier Vagrantfile pour ajouter la configuration nécessaire pour installer Portainer. Voici un exemple de configuration :

Vagrant.configure("2") do |config| # Utilisez la version 2 de Vagrant
  config.vm.box = "ubuntu/focal64" # Utilisez la version 20.04 LTS de Ubuntu pour la machine virtuelle Vagrant

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y docker.io
    systemctl start docker
    docker run -d -p 9000:9000 --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker:/var/lib/docker portainer/portainer-ce
  SHELL

  config.vm.provider "virtualbox" do |vb| # vb = VirtualBox = hypervisor de Virtual Machine 
    vb.memory = "2048"
    vb.cpus = 2
  end
end

#5. Enregistrez le fichier Vagrantfile et exécutez la commande suivante pour démarrer la machine virtuelle :

#vagrant up

#Une fois que la machine virtuelle est démarrée, vous pouvez accéder à Portainer en ouvrant votre navigateur et en visitant http://localhost:9000.

#6. Cela devrait installer Portainer sur votre machine virtuelle Vagrant à l'aide de la commande shell dans le fichier Vagrantfile.


