import os

# Chemin vers le dossier home
home_dir = os.path.expanduser("~")

# Chemin vers le répertoire DATA
data_dir = os.path.join(home_dir, "DATA")

# Chemin vers le répertoire OS
os_dir = os.path.join(home_dir, "OS")

# Créer les répertoires s'ils n'existent pas
if not os.path.exists(data_dir):
    os.mkdir(data_dir)

if not os.path.exists(os_dir):
    os.mkdir(os_dir)