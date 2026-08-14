#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
orchestrator.py
================
Script d'orchestration modulaire pour le projet :
https://github.com/lido936s/projet-dev-vagrant-in-python

Objectif
--------
Ce script ne remplace pas les fichiers existants du dépôt (scripts .py, .ps1,
.rb, .sh, Vagrantfile...). Il les APPELLE dans le bon ordre, étape par étape,
avec logging, gestion d'erreurs, et une commande finale pour créer une
"release" sur GitHub (tag + push + `gh release create`).

Chaque étape est une fonction indépendante enregistrée dans un dictionnaire
de "steps". Vous pouvez lancer une étape isolée, un sous-ensemble, ou tout
le pipeline.

Utilisation
-----------
    python orchestrator.py --list
    python orchestrator.py prereq
    python orchestrator.py disks vagrant network docker up
    python orchestrator.py all
    python orchestrator.py release --version 0.1.0 --notes "Première version stable"

Configuration
--------------
Adaptez la section CONFIG ci-dessous (chemins des scripts, OS cible, etc.)
avant la première exécution. Les chemins par défaut correspondent aux noms
de fichiers présents dans le dépôt GitHub cité plus haut.
"""

from __future__ import annotations

import argparse
import logging
import platform
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Dict, List, Optional


# ---------------------------------------------------------------------------
# CONFIGURATION — à adapter à votre environnement
# ---------------------------------------------------------------------------

@dataclass
class Config:
    # Racine du projet (répertoire contenant les scripts du dépôt cloné)
    project_root: Path = Path(__file__).resolve().parent

    # Fichiers du dépôt (noms tels que présents sur GitHub)
    script_install_vagrant: str = "InstallVagrantSousPython.py"
    script_create_disks: str = "CreateDisk_DATA&OS.py"
    script_vlan_dev: str = "Vlan-Dev.py"
    script_adding_vm_custom: str = "AddingVMCustom.py"
    script_install_vm: str = "install_vm.py"
    script_basculement_vmware: str = "Basculement_VMware.ps1"
    script_install_vmware: str = "InstallVMware Workstation 17.ps1"
    script_install_portainer_rb: str = "Install_portainer-io.rb"
    script_install_docker_sh: str = "Installing Docker Engine on Debian 11.sh"
    vagrantfile: str = "VagrantFile"

    # Branches utilisées pour la CI / release (voir README : test -> release)
    branch_test: str = "test"
    branch_release: str = "release"
    branch_main: str = "main"

    log_file: Path = field(default_factory=lambda: Path("orchestrator.log"))


CONFIG = Config()


# ---------------------------------------------------------------------------
# LOGGING
# ---------------------------------------------------------------------------

def setup_logging(verbose: bool = False) -> logging.Logger:
    logger = logging.getLogger("orchestrator")
    logger.setLevel(logging.DEBUG if verbose else logging.INFO)
    logger.handlers.clear()

    fmt = logging.Formatter("[%(asctime)s] %(levelname)-8s %(message)s", "%H:%M:%S")

    console = logging.StreamHandler(sys.stdout)
    console.setFormatter(fmt)
    logger.addHandler(console)

    file_handler = logging.FileHandler(CONFIG.log_file, encoding="utf-8")
    file_handler.setFormatter(fmt)
    logger.addHandler(file_handler)

    return logger


log = setup_logging()


# ---------------------------------------------------------------------------
# OUTILS BAS NIVEAU
# ---------------------------------------------------------------------------

class StepError(RuntimeError):
    """Erreur levée quand une étape échoue, pour arrêter proprement le pipeline."""


def run(cmd: List[str], cwd: Optional[Path] = None, check: bool = True) -> subprocess.CompletedProcess:
    """Exécute une commande système en loggant tout, sans jamais planter en silence."""
    log.debug("Commande: %s (cwd=%s)", " ".join(cmd), cwd or CONFIG.project_root)
    try:
        result = subprocess.run(
            cmd,
            cwd=str(cwd or CONFIG.project_root),
            check=check,
            text=True,
            capture_output=True,
        )
    except FileNotFoundError as exc:
        raise StepError(f"Commande introuvable : {cmd[0]} ({exc})") from exc

    if result.stdout:
        log.debug(result.stdout.strip())
    if result.returncode != 0:
        log.error(result.stderr.strip())
        if check:
            raise StepError(f"Échec de la commande : {' '.join(cmd)} (code {result.returncode})")
    return result


def run_python_script(relative_path: str) -> None:
    path = CONFIG.project_root / relative_path
    if not path.exists():
        raise StepError(f"Script Python introuvable : {path}")
    run([sys.executable, str(path)])


def run_shell_script(relative_path: str) -> None:
    """Exécute un .sh (bash) — pertinent surtout sous Linux/WSL."""
    path = CONFIG.project_root / relative_path
    if not path.exists():
        raise StepError(f"Script shell introuvable : {path}")
    run(["bash", str(path)])


def run_powershell_script(relative_path: str) -> None:
    """Exécute un .ps1 — pertinent sous Windows (ou pwsh sous Linux)."""
    path = CONFIG.project_root / relative_path
    if not path.exists():
        raise StepError(f"Script PowerShell introuvable : {path}")
    shell = "pwsh" if shutil.which("pwsh") else "powershell"
    run([shell, "-ExecutionPolicy", "Bypass", "-File", str(path)])


def run_ruby_script(relative_path: str) -> None:
    """Exécute un .rb (utilisé ici par Vagrant, généralement pas lancé seul)."""
    path = CONFIG.project_root / relative_path
    if not path.exists():
        raise StepError(f"Script Ruby introuvable : {path}")
    run(["ruby", str(path)])


def require_tool(tool: str, hint: str = "") -> None:
    if shutil.which(tool) is None:
        raise StepError(f"L'outil requis '{tool}' est introuvable dans le PATH. {hint}")


# ---------------------------------------------------------------------------
# ÉTAPES DU PIPELINE (une fonction = un module indépendant)
# ---------------------------------------------------------------------------

def step_prereq() -> None:
    """Vérifie/installe les prérequis : pip, vagrant via pip, etc."""
    log.info("Vérification des prérequis (pip, vagrant)...")
    run([sys.executable, "-m", "ensurepip", "--upgrade"], check=False)
    run_python_script(CONFIG.script_install_vagrant)


def step_disks() -> None:
    """Crée les répertoires/disques DATA et OS."""
    log.info("Création des répertoires DATA et OS...")
    run_python_script(CONFIG.script_create_disks)


def step_network() -> None:
    """Configure le VLAN de développement (NAT, LAN-DEV)."""
    log.info("Configuration réseau (VLAN LAN-DEV)...")
    run_python_script(CONFIG.script_vlan_dev)


def step_vm_custom() -> None:
    """Ajoute/paramètre la VM personnalisée (RAM, CPU, box)."""
    log.info("Paramétrage de la VM personnalisée...")
    run_python_script(CONFIG.script_adding_vm_custom)


def step_install_vm() -> None:
    """Lance l'installation de la VM (wrapper haut niveau du dépôt)."""
    log.info("Installation de la VM (install_vm.py)...")
    run_python_script(CONFIG.script_install_vm)


def step_vagrant_up() -> None:
    """Démarre la VM avec Vagrant à partir du Vagrantfile du dépôt."""
    log.info("Démarrage de la VM via 'vagrant up'...")
    require_tool("vagrant", "Installez Vagrant : https://developer.hashicorp.com/vagrant/downloads")
    vagrantfile = CONFIG.project_root / CONFIG.vagrantfile
    if not vagrantfile.exists():
        raise StepError(f"Vagrantfile introuvable : {vagrantfile}")
    run(["vagrant", "up"])


def step_docker_portainer() -> None:
    """Installe Docker Engine puis Portainer sur la VM cible."""
    log.info("Installation de Docker Engine...")
    system = platform.system().lower()
    if system == "linux":
        run_shell_script(CONFIG.script_install_docker_sh)
    else:
        log.warning(
            "Système '%s' détecté : le script Docker (.sh) est prévu pour Debian/Linux. "
            "Exécutez-le manuellement dans la VM (via 'vagrant ssh').",
            system,
        )

    log.info("Installation de Portainer (via provisioning Vagrant/Ruby)...")
    log.info(
        "Note : '%s' est généralement inclus comme provisioner dans le Vagrantfile "
        "et s'exécute automatiquement lors de 'vagrant up' / 'vagrant provision'.",
        CONFIG.script_install_portainer_rb,
    )


def step_vmware_switch() -> None:
    """Bascule éventuelle vers VMware Workstation (optionnel, Windows)."""
    log.info("Bascule VMware (optionnelle)...")
    if platform.system().lower() != "windows":
        log.warning("Étape ignorée : script PowerShell prévu pour Windows uniquement.")
        return
    run_powershell_script(CONFIG.script_basculement_vmware)


def step_tests() -> None:
    """Phase de vérification : contrôle basique des variables/scripts critiques."""
    log.info("Phase de vérification (bug sur variables critiques)...")
    required_files = [
        CONFIG.vagrantfile,
        CONFIG.script_create_disks,
        CONFIG.script_vlan_dev,
    ]
    missing = [f for f in required_files if not (CONFIG.project_root / f).exists()]
    if missing:
        raise StepError(f"Fichiers critiques manquants : {missing}")
    log.info("Tous les fichiers critiques sont présents.")

    require_tool("git", "Installez git pour la gestion des branches test/release.")
    result = run(["git", "status", "--porcelain"], check=False)
    if result.stdout.strip():
        log.warning("Des modifications non commitées sont présentes.")
    log.info("Vérifications terminées avec succès.")


# ---------------------------------------------------------------------------
# RELEASE GITHUB
# ---------------------------------------------------------------------------

def git_current_branch() -> str:
    result = run(["git", "rev-parse", "--abbrev-ref", "HEAD"])
    return result.stdout.strip()


def create_release(version: str, notes: str, remote: str = "origin") -> None:
    """
    Pipeline de release conforme au README du dépôt :
      1. Isoler le projet dans une branche 'test'
      2. Si les tests sont concluants -> créer/mettre à jour la branche 'release'
      3. Créer un tag de version + push
      4. Créer la release GitHub (via 'gh' si disponible, sinon instructions manuelles)
    """
    require_tool("git")
    log.info("=== Démarrage de la release v%s ===", version)

    # 1. Vérifications préalables
    step_tests()

    # 2. Branche de test
    log.info("Passage sur la branche '%s'...", CONFIG.branch_test)
    run(["git", "checkout", "-B", CONFIG.branch_test])
    run(["git", "add", "-A"])
    commit = run(["git", "commit", "-m", f"test: préparation release v{version}"], check=False)
    if commit.returncode != 0:
        log.info("Rien à commiter sur la branche test (déjà à jour).")

    # 3. Branche de release
    log.info("Fusion vers la branche '%s'...", CONFIG.branch_release)
    run(["git", "checkout", "-B", CONFIG.branch_release, CONFIG.branch_test])

    # 4. Tag annoté
    tag = f"v{version}"
    log.info("Création du tag %s...", tag)
    run(["git", "tag", "-a", tag, "-m", notes or f"Release {tag}"])

    # 5. Push branche + tag
    log.info("Push vers '%s'...", remote)
    run(["git", "push", remote, CONFIG.branch_release])
    run(["git", "push", remote, tag])

    # 6. Release GitHub via GitHub CLI si disponible
    if shutil.which("gh"):
        log.info("Création de la release GitHub via 'gh release create'...")
        run([
            "gh", "release", "create", tag,
            "--title", tag,
            "--notes", notes or f"Release {tag}",
            "--target", CONFIG.branch_release,
        ])
        log.info("Release GitHub créée avec succès : %s", tag)
    else:
        log.warning(
            "GitHub CLI ('gh') non détectée. Le tag et la branche ont été poussés, "
            "mais la release doit être finalisée manuellement sur GitHub : "
            "onglet 'Releases' -> 'Draft a new release' -> choisir le tag '%s'.",
            tag,
        )

    log.info("=== Release v%s terminée ===", version)


# ---------------------------------------------------------------------------
# REGISTRE DES ÉTAPES (permet d'ajouter facilement de nouvelles étapes)
# ---------------------------------------------------------------------------

STEPS: Dict[str, Callable[[], None]] = {
    "prereq": step_prereq,
    "disks": step_disks,
    "network": step_network,
    "vmcustom": step_vm_custom,
    "vmware": step_vmware_switch,
    "installvm": step_install_vm,
    "up": step_vagrant_up,
    "docker": step_docker_portainer,
    "test": step_tests,
}

# Ordre par défaut du pipeline complet ("all")
DEFAULT_ORDER: List[str] = [
    "prereq", "disks", "network", "vmcustom", "installvm", "up", "docker", "test",
]


def run_pipeline(step_names: List[str]) -> None:
    log.info("Pipeline demandé : %s", " -> ".join(step_names))
    for name in step_names:
        func = STEPS.get(name)
        if func is None:
            raise StepError(f"Étape inconnue : '{name}' (voir --list)")
        log.info("--- Étape : %s ---", name)
        try:
            func()
        except StepError as exc:
            log.error("Échec sur l'étape '%s' : %s", name, exc)
            raise
    log.info("Pipeline terminé avec succès.")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="orchestrator.py",
        description="Orchestrateur modulaire pour le projet projet-dev-vagrant-in-python",
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="Logs détaillés")
    parser.add_argument("--list", action="store_true", help="Liste les étapes disponibles et quitte")
    parser.add_argument(
        "--root", type=Path, default=None,
        help="Chemin vers le dossier du dépôt cloné (par défaut : dossier de ce script)",
    )

    sub = parser.add_subparsers(dest="command")

    sub.add_parser("all", help="Exécute le pipeline complet dans l'ordre par défaut")

    for name in STEPS:
        sub.add_parser(name, help=f"Exécute uniquement l'étape '{name}'")

    release_parser = sub.add_parser("release", help="Crée une release sur GitHub")
    release_parser.add_argument("--version", required=True, help="Numéro de version, ex: 0.1.0")
    release_parser.add_argument("--notes", default="", help="Notes de version")
    release_parser.add_argument("--remote", default="origin", help="Nom du remote git (défaut: origin)")

    parser.add_argument(
        "steps", nargs="*", default=[],
        help="Liste d'étapes à enchaîner (ex: disks network up). Ignoré si une sous-commande est utilisée.",
    )

    return parser


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    global log
    log = setup_logging(args.verbose)

    if args.root:
        CONFIG.project_root = args.root.resolve()

    if args.list:
        print("Étapes disponibles :")
        for name in STEPS:
            print(f"  - {name}")
        print("  - all      (toutes les étapes dans l'ordre par défaut)")
        print("  - release  (crée une release GitHub)")
        return 0

    try:
        if args.command == "release":
            create_release(args.version, args.notes, args.remote)
        elif args.command == "all":
            run_pipeline(DEFAULT_ORDER)
        elif args.command in STEPS:
            run_pipeline([args.command])
        elif args.steps:
            run_pipeline(args.steps)
        else:
            parser.print_help()
            return 1
    except StepError as exc:
        log.error("Arrêt du pipeline : %s", exc)
        return 2
    except KeyboardInterrupt:
        log.warning("Interrompu par l'utilisateur.")
        return 130

    return 0


if __name__ == "__main__":
    sys.exit(main())
