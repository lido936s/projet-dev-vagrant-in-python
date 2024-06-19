import vagrant

# Créer une instance de Vagrant
v = vagrant.Vagrant(directory='chemin/vers/vagrantfile')

# Démarrer l'environnement Vagrant
v.up()

# Si vous souhaitez Arrêter vagrant decommenter la ligne 11
# Arrêter l'environnement Vagrant
#v.halt()