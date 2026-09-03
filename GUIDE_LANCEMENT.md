# Guide de lancement — `orchestrator.py`

Ce guide explique comment préparer votre machine et exécuter le script
`orchestrator.py` pour le projet `projet-dev-vagrant-in-python`.

---

## 1. Prérequis à installer

| Outil | Pourquoi | Vérifier l'installation |
|---|---|---|
| **Python 3.9+** | Exécute `orchestrator.py` et les scripts `.py` du dépôt | `python --version` |
| **pip** | Installe les paquets Python (ex. `vagrant`) | `python -m pip --version` |
| **Vagrant** | Crée/démarre les VM | `vagrant --version` |
| **VirtualBox ou VMware Workstation** | Hyperviseur utilisé par Vagrant | ouvrir le logiciel |
| **Git** | Gestion des branches et de la release | `git --version` |
| **GitHub CLI (`gh`)** *(optionnel, pour la release automatique)* | Crée la release sur GitHub sans passer par le site | `gh --version` |

Sous Windows, `python`, `pip`, `git` s'installent via leurs installateurs officiels
et s'ajoutent au `PATH` pendant l'installation (cochez la case correspondante).

---

## 2. Récupérer le projet

Si ce n'est pas déjà fait, clonez le dépôt puis placez `orchestrator.py`
et `GUIDE_LANCEMENT.md` **à la racine du dépôt**, au même niveau que
`VagrantFile`, `install_vm.py`, etc. :

```bash
git clone https://github.com/lido936s/projet-dev-vagrant-in-python.git
cd projet-dev-vagrant-in-python
# copiez orchestrator.py ici
```

---

## 3. Ouvrir un terminal au bon endroit

- **Windows** : dans l'explorateur de fichiers, ouvrez le dossier du projet,
  cliquez dans la barre d'adresse, tapez `powershell` puis Entrée.
- **macOS / Linux** : ouvrez un terminal puis :
  ```bash
  cd chemin/vers/projet-dev-vagrant-in-python
  ```

Vérifiez que vous êtes au bon endroit :

```bash
python orchestrator.py --list
```

Si la liste des étapes s'affiche, tout est en ordre.

---

## 4. Lancer le script

### Voir toutes les étapes disponibles
```bash
python orchestrator.py --list
```

### Lancer une seule étape
```bash
python orchestrator.py prereq
```
```bash
python orchestrator.py disks
```
```bash
python orchestrator.py up
```

### Enchaîner plusieurs étapes précises
```bash
python orchestrator.py disks network up
```

### Lancer tout le pipeline dans l'ordre par défaut
```bash
python orchestrator.py all
```

### Activer les logs détaillés (utile en cas de bug)
```bash
python orchestrator.py all -v
```

### Utiliser un dossier de projet différent
Si `orchestrator.py` n'est pas placé dans le dépôt lui-même :
```bash
python orchestrator.py --root "C:\chemin\vers\projet-dev-vagrant-in-python" all
```

---

## 5. Créer une release GitHub

```bash
python orchestrator.py release --version 0.1.0 --notes "Première version stable"
```

Ce que fait cette commande :
1. Vérifie que les fichiers critiques sont présents (`test`).
2. Bascule sur une branche `test`, commite les changements en cours.
3. Crée/actualise la branche `release`.
4. Crée un tag `v0.1.0` et pousse la branche + le tag sur `origin`.
5. Si `gh` (GitHub CLI) est installé et connecté (`gh auth login`), crée
   automatiquement la release sur GitHub. Sinon, un message vous explique
   comment la finaliser manuellement depuis l'onglet **Releases** du dépôt.

---

## 6. En cas d'erreur

- Le script affiche l'erreur dans le terminal **et** l'enregistre dans
  `orchestrator.log` (créé dans le dossier du projet).
- Message `L'outil requis 'vagrant' est introuvable dans le PATH` →
  installez Vagrant puis redémarrez le terminal.
- Message `Script Python/shell/PowerShell introuvable` → vérifiez que
  `orchestrator.py` est bien à la racine du dépôt cloné, à côté des
  autres fichiers du projet.
- Sous Windows, un script `.sh` sera ignoré avec un avertissement (il est
  prévu pour la VM Linux, pas pour l'hôte Windows) — c'est normal.

---

## 7. Résumé rapide (aide-mémoire)

```bash
cd projet-dev-vagrant-in-python
python orchestrator.py --list          # voir les étapes
python orchestrator.py all -v          # tout lancer avec logs détaillés
python orchestrator.py release --version 0.1.0 --notes "..."  # release GitHub
```
