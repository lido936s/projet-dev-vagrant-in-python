"# projet-dev-vagrant-in-python" 
Ce projet et en cours de dev donc pas encore terminé phase de test prévue suivant l'infrastrucutre complété 
Neccesite pour cela le logiciel drawio >  
- lien de l'infrastructure : infra projet.drawio > https://app.diagrams.net/#Hlido936s%2Fprojet-dev-vagrant-in-python%2Fmain%2FInfrastructure_Projet.drawio#%7B%22pageId%22%3A%22C5RBs43oDa-KdzZeNtuy%22%7D

# prerequis 
- faire un script pour creer une VM avec python sur Vagrant 
- definir le systéme d'exploitation via les Box de vagrant : https://app.vagrantup.com/m88v2/boxes/kubuntu
- installer pip 
- installer vagrant sous Python : pip install vagrant > installation via ce fichier : Install Vagrant sous Python.py
- installer python d'une version supporter par vagrant 

# création de deux repertoires DATA et OS 
- DATA : sera un répertoire de dévellopement de notre infra ainsi que la partie réseau
- OS : sera identique à celui de l'OS mais aura pour objectif de définir la machine virtuel et sont systéme d'exploitation

# Mise en place de vagrant dans notre projet pour cela on auras besoins d'une nouvelle box 
vagrant init m88v2/kubuntu
vagrant up

# redaction du script en inserant quelques variables sympathique pour structurer notre VM 

- definir les variables essentielles "
- configurer le réseau 
- Installer sur le repertoire OS notre VM via le fichier de définitions de vagrant : Vagrantfile 
# Automatisation
- Commenter les variables ainsi que les commandes quelle éxecute
-
-
-
-
# Faire une release

