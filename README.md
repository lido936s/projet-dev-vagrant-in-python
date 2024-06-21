"# projet-dev-vagrant-in-python" 

Ce projet et en cours de dev donc pas encore terminé phase de test prévue suivant l'infrastrucutre complété 

Langage employé > Powershell, Python et dans le futur du javascript pour une application via le web pour une interface de gestion de notre VM .

Neccesite pour cela le logiciel drawio >  
- lien de l'infrastructure : infra projet.drawio > https://app.diagrams.net/#Hlido936s%2Fprojet-dev-vagrant-in-python%2Fmain%2FInfrastructure_Projet.drawio#%7B%22pageId%22%3A%22C5RBs43oDa-KdzZeNtuy%22%7D

# Prerequis : les élèments essentiel pour accomplir notre projet 

- faire un script pour creer une VM avec python sur Vagrant 
- definir le systéme d'exploitation via les Box de vagrant : https://app.vagrantup.com/m88v2/boxes/kubuntu
- installer pip 
- installer vagrant sous Python : pip install vagrant > installation via ce fichier : Install Vagrant sous Python.py
- installer python d'une version supporter par vagrant 

# création de deux repertoires DATA et OS 

- DATA : sera un répertoire de dévellopement de notre infra ainsi que la partie réseau
- OS : sera identique à celui de l'OS mais aura pour objectif de définir la machine virtuel et sont systéme d'exploitation

# Mise en place de vagrant dans notre projet pour cela on auras besoins d'une nouvelle box 
- choix de l'OS > cela dépend de votre infra qui vous auriez definit dans le cadre futur pour une mise en place de docker via un portainer.io
 vagrant init m88v2/kubuntu
 vagrant up

# Redaction du script en inserant quelques variables sympathique pour structurer notre VM 

- definir les variables essentielles 
- configurer un réseau en NAT pour une VLAN nommée LAN-DEV avec python
lien : https://github.com/lido936s/projet-dev-vagrant-in-python/blob/main/Vlan-Dev.py
- Installer sur le repertoire OS notre VM via le fichier de définitions de vagrant : Vagrantfile 

# Automatisation

- Déclarer les variables et choisir des variables critiques comme la gestion du réseau et de la RAM .
- Commenter les variables ainsi que les commandes quelles éxecutes .
- mettre en place les boucles pour l'interaction entre les differents organes de commande et d'effecteurs .

# Phase de test 

- faire un script qui fasse la vérification en cas de bug sur certaines variables critique .
- Isoler l'ensemble du projet dans une nouvelle branch nommé test .
  

# Faire une release
- Mise en production via une machine virtuel masterisé avec seulement notre projet fonctionnant dedans .


