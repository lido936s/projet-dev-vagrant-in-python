"# projet-dev-vagrant-in-python" 

Ce projet et en cours de dev donc pas encore terminé phase de test prévue suivant l'infrastrucutre complété 

Langages employées > Powershell, Python et dans le futur du javascript pour une application via le web pour une interface de gestion de notre VM .

Neccesite pour cela le logiciel drawio >  
- lien de l'infrastructure : infra projet.drawio > https://app.diagrams.net/#Hlido936s%2Fprojet-dev-vagrant-in-python%2Fmain%2FInfrastructure_Projet.drawio#%7B%22pageId%22%3A%22C5RBs43oDa-KdzZeNtuy%22%7D

# Prerequis : les élèments essentiel pour accomplir notre projet 

- faire un script pour creer une VM avec python sur Vagrant 
- definir le systéme d'exploitation via les Box de vagrant : https://app.vagrantup.com/m88v2/boxes/kubuntu
- installer pip 
- installer vagrant sous Python : pip install vagrant > installation via ce fichier : Install Vagrant sous Python.py
- installer python d'une version supporter par vagrant 
- faire un répertoire > Projet_dev_VM en local sur une machine Hôte afin d'y stocker l'ensemble des éléménts néccésaire afin d'éfféctuer les différentes taches notamment l'éditions des scripts et 
  toute autres support .

# Création de deux repertoires DATA et OS 

- DATA : sera un répertoire de dévellopement de notre infra ainsi que la partie réseau
- OS : sera identique à celui de l'OS mais aura pour objectif de définir la machine virtuel et sont systéme d'exploitation

# Mise en réseau de l'infrastructure dans le cadre du bon déroulement de notre projet 
- La machine virtuel doit étres dans un réseau qui soit excessible depuis l'extérieur pour une simple raison > Portainer.io 
- Faire un tableau d'adressage | + adresse réseau et plage attribuable | ainsi que l'équipement nommé qui distribue l'information .
- Definir le bon protocole suivant l'information transmisse : exemple > DHCP : UDP partie cliente 
-

# Mise en place de vagrant dans notre projet pour cela on auras besoins d'une nouvelle box 

- choix de l'OS > cela dépend de votre infra qui vous auriez definit dans le cadre futur pour une mise en place de docker via un portainer.io
-NewBoxe > Distribution Kubuntu 
vagrant init m88v2/kubuntu
 vagrant up

# Redaction du script en inserant quelques variables sympathique pour structurer notre VM 

- Definir le besoins essentiel en ressource mémoire et CPU dont la VM ai besoins en fonction des logiciels et conteneurs installées . 
- Mise en place d'un scripts qui gére les variables .
- Configurer un réseau en NAT pour une VLAN nommée LAN-DEV avec python > https://github.com/lido936s/projet-dev-vagrant-in-python/blob/main/Vlan-Dev.py
- Mettre en place dans un scripts la partie ssh afin que depuis l'exterieur seul les dev avec un mot de passe peuvent intéragir avec l'ensemble du projet .
- Installer sur le repertoire OS notre VM via le fichier de définitions de vagrant : Vagrantfile .
- Coté un peu délicat : le projet doit étres nommé avec un version afin de pouvoir identifié les versions du projet .

# Automatisation

- Déclarer les variables et choisir des variables critiques comme la gestion du réseau et de la RAM .
- Commenter les variables ainsi que les commandes quelles éxecutes .
- Mettre en place les boucles pour l'interaction entre les differents organes de commande et d'effecteurs .
- Mise en place de scripts dans la création de machine virtuel gràce au fichier de définitions de vagrant . 
# Phase de verifications : Etablir des regles en matiére de fonctionnement des scripts .
-
-
-
# Phase de test 

- Faire un script qui fasse la vérification en cas de bug sur certaines variables critique .
- Isoler l'ensemble du projet dans une nouvelle branch nommé test .
- Si les test sont concluant il faut mettre en place une nouvelle branch sur le github afin de la nommé "release"

# Faire une release
- Mise en production via une machine virtuel masterisé avec seulement notre projet fonctionnant dedans .


