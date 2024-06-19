"# projet-dev-vagrant-in-python" 

# prerequis 
- faire un script pour creer une VM avec python sur Vagrant 
- installer vagrant 
- installer pip 
- installer python d'une version supporter par vagrant 

# création de deux repertoires DATA et OS 
- DATA : sera un répertoire de dévellopement de notre infra ainsi que la partie réseau
- OS : sera identique à celui de l'OS mais aura pour objectif de définir la machine virtuel et sont systéme d'exploitation


# Mise en place de vagrant dans notre projet pour cela on auras besoins d'une nouvelle box 
vagrant init m88v2/kubuntu
vagrant up

# redaction du script en inserant quelques variables sympathique pour structurer notre VM 

- definir les variables essentielles "
exemple de scripts pour déclarer les variables :
# Déclaration d'une variable pour une VM
nom_vm = "MaVM"
ip_vm = "192.168.1.10"
port_vm = 22

# Affichage des valeurs de la variable
print("Nom de la VM : ", nom_vm)
print("IP de la VM : ", ip_vm)
print("Port de la VM : ", port_vm)

-
-
-

# Faire une release

