# Creer une VM 

https://portal.cloud.hashicorp.com/vagrant/discover/gutehall/ubuntu24-10

1.creer un répertoire pour la box > gutehall/ubuntu24-10 

projet_VM_Vubuntu

mkdir C:\projet_VM_Vubuntu

2.Se rendre dans se répertoire

cd C:\projet_VM_Vubuntu

3.faire vagrant init de la box > gutehall/ubuntu24-10 # Etre bien dans le répertoire C:\projet_VM_Vubuntu

vagrant init gutehall/ubuntu24-10

4.Ouvrir ensuite dans le répertoire projet_VM_Vubuntu le fichier "Vagrantfile"

5.Supprimer tous les commentaire en vert et ensuite insérer le bon provider dessus 

6.Attention avant d'ajouter le provider il faut éfféctué l'installation du plugin VMware intégrer à Vagrant > https://developer.hashicorp.com/vagrant/docs/providers/vmware/installation


7.POur des raison de configuration en manuel il faudrat passer par utilitaire et un service  "Vagrant VMware Utility"

Pour Windows 

Installation > Vagrant VMware Utility > https://developer.hashicorp.com/vagrant/install/vmware > https://releases.hashicorp.com/vagrant-vmware-utility/1.0.22/vagrant-vmware-utility_1.0.22_windows_amd64.msi

C:\ProgramData\HashiCorp\vagrant-vmware-desktop\certificates

Vagrant VMware Utility Service

net.exe start vagrant-vmware-utility


8.vous pouvez ajouter le provider ensuite avec la commande vagrant up --provider "provider ciblé"

vagrant up --provider vmware_desktop




