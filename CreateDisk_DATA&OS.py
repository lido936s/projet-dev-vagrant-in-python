import os

# Chemin vers le dossier home
home_dir = os.path.expanduser("~")

# Chemin vers le répertoire machine
machine_dir = os.path.join(home_dir, "machine")

# Chemin vers le répertoire DATA dans le répertoire machine
data_dir = os.path.join(machine_dir, "DATA")

# Chemin vers le répertoire OS dans le répertoire machine
os_dir = os.path.join(machine_dir, "OS")

# Créer le répertoire machine s'il n'existe pas
if not os.path.exists(machine_dir):
    os.mkdir(machine_dir)

# Créer les répertoires DATA et OS dans le répertoire machine s'ils n'existent pas
if not os.path.exists(data_dir):
    os.mkdir(data_dir)

if not os.path.exists(os_dir):
    os.mkdir(os_dir)