# Ajouter une VM avec Python selon vos besoins 

import subprocess

# Chemin vers votre dossier de machine virtuelle
VM_INSTALL_DIR = "/chemin/vers/votre/dossier/de/machine/virtuelle"

# personnalisation de la machine virtuelle (VM) avec Python 
def create_vm(name, ostype, size):
    subprocess.run(["VBoxManage", "createvm", "--name", name, "--ostype", ostype, "--register"])
    subprocess.run(["VBoxManage", "createmedium", "disk", "--filename", f"{VM_INSTALL_DIR}/{name}.vdi", "--size", str(size)])
    subprocess.run(["VBoxManage", "storagectl", name, "--name", "SATA Controller", "--add", "sata", "--controller", "IntelAhci", "--portcount", "1"])
    subprocess.run(["VBoxManage", "storageattach", name, "--storagectl", "SATA Controller", "--port", "0", "--device", "0", "--type", "hdd", "--medium", f"{VM_INSTALL_DIR}/{name}.vdi"])
    subprocess.run(["VBoxManage", "modifyvm", name, "--memory", "1024", "--cpus", "1", "--hwvirtex", "on"])
    subprocess.run(["VBoxManage", "startvm", name, "--type", "headless"])
create_vm("NomDeMaVM", "Ubuntu_64", 10240)

# Pour incorporer un fichier Python pour installer une machine virtuelle (VM) sur Vagrant, il est possible de l'utiliser dans le dossier de Vagrantfile.

# Pour ajouter une VM avec Python, il suffit de l'utiliser dans le dossier de Vagrantfile.

#import subprocess

#def install_vm():
    # Exécutez la commande Vagrant pour créer une VM
    #subprocess.run(['vagrant', 'up'])

# Appelez la fonction pour installer la VM
#install_vm()

