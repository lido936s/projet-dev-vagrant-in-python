# install draw.io sur github avec l'api web https://www.drawio.com/blog/single-repository-diagrams

https://github.com/apps/draw-io-app

# install sur windows 10 avec l'api web https://www.drawio.com/blog/single-repository-diagrams 

# Installation de Draw.io. version 24.6.1 pour Windows 10.

# Téléchargez le fichier d'installation de Draw.io à partir du site officiel.
$url = "https://github.com/jgraph/drawio-desktop/releases/download/v24.6.1/draw.io-24.6.1-windows-installer.exe"
$outputFile = "C:\Users\lfrere\Downloads\draw.io-24.6.1-windows-installer.exe"
Invoke-WebRequest -Uri $url -OutFile $outputFile

# Lancer l'installation.
$installationPath = "C:\Users\lfrere\Downloads\draw.io-24.6.1-windows-installer.exe"
Start-Process -FilePath "$installationPath" -ArgumentList "/S"

# Lancer le programme.

Start-Process -FilePath "C:\Program Files\Draw.io\draw.io-24.6.1-windows-installer.exe"

# astuce pour tester la variable $installationPath > qui est la variable pour pouvoir localisé notre fichier d'installation pour notre programme

Test-Path -Path $installationPath
