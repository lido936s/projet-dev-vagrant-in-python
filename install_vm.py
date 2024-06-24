# Assurez-vous d'avoir Vagrant installé sur votre système. Vous pouvez le télécharger et l'installer à partir du site officiel de Vagrant.
# Créez un nouveau fichier Python avec l'extension .py (par exemple, install_vm.py).
# Dans ce fichier, vous pouvez utiliser la bibliothèque subprocess pour exécuter des commandes de ligne. 

# Voici un exemple de code qui utilise Vagrant pour installer une VM :
import subprocess

def install_vm():
    # Exécutez la commande Vagrant pour créer une VM
    subprocess.run(['vagrant', 'up'])

# Appelez la fonction pour installer la VM
install_vm()

# Enregistrez le fichier Python.
# Ouvrez une invite de commandes ou un terminal et naviguez jusqu'au répertoire où vous avez enregistré le fichier Python.
# Exécutez le fichier Python en utilisant la commande python suivie du nom du fichier (par exemple, python install_vm.py).
# Cela exécutera le script Python et appellera la fonction install_vm(), qui utilise Vagrant pour installer la VM.

# Assurez-vous d'avoir les fichiers de configuration Vagrant appropriés dans le même répertoire que le fichier Python pour que Vagrant puisse utiliser les informations nécessaires pour installer la VM.