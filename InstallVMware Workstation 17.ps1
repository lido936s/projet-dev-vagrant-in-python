# install VMware Workstation 17 sur Windows 10 

# Installation de VMware Workstation 17 version 17.5.2-23775571 pour Windows.

# Téléchargez le fichier d'installation depuis le site Web de VMware Workstation 17.5.2-23775571 et l'exécutez avec l'argument /S pour lancer l'installation.
$url = "https://softwareupdate.vmware.com/cds/vmw-desktop/ws/17.5.2/23775571/windows/core/VMware-workstation-17.5.2-23775571.exe.tar"
$outputFile = "C:\Users\lfrere\Downloads\VMware-workstation-full-17.5.2-23775571.exe.tar"
Invoke-WebRequest -Uri $url -OutFile $outputFile -SkipCertificateCheck 


# preparation des fichiers pour l'installation 
$installationPath = "C:\Users\lfrere\Downloads\VMware-workstation-full-17.5.2-23775571.exe.tar"
New-Item -ItemType Directory -Path "C:\Users\lfrere\Downloads\VMware-workstation-full-17.5.2-23775571" -PipelineVariable $installationPath -Force
# extraire le fichier executable d'installation 
$destinationPath = "C:\Users\lfrere\Downloads\VMware-workstation-full-17.5.2-23775571"
Expand-Archive -Path $installationPath -DestinationPath "$destinationPath"
Start-Process -FilePath "$installationPath" -ArgumentList "/S"

# Lancer le programme.

Start-Process -FilePath "C:\Program Files\Draw.io\draw.io-24.6.1-windows-installer.exe"

# astuce pour tester la variable $installationPath > qui est la variable pour pouvoir localisé notre fichier d'installation pour notre programme
