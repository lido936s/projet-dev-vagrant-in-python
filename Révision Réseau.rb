#Pour configurer le réseau sur Vagrant, vous pouvez utiliser le fichier Vagrantfile pour définir les paramètres de votre réseau. Voici un exemple de configuration réseau pour Vagrant :

Vagrant.configure("2") do |config| # Version 2 de Vagrant 
  config.vm.network "private_network", ip: "192.168.33.10" 
end


#Dans cet exemple, nous utilisons le réseau privé (private_network) avec l'adresse IP 192.168.33.10. Vous pouvez ajuster cette configuration en fonction de vos besoins.

#Assurez-vous d'avoir installé Vagrant et de disposer d'une machine virtuelle (par exemple, VirtualBox) configurée pour fonctionner avec Vagrant.