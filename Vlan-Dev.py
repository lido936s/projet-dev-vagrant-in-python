import subprocess

# Nom de l'interface réseau pour la VLAN LAN-DEV
interface = 'eth0'
vlan_name = 'LAN-DEV'

# Adresse IP de la VLAN LAN-DEV
vlan_ip = '192.168.1.1'
subnet_mask = '255.255.255.0'

# Commandes iptables pour configurer le NAT
commands = [
    f'iptables -t nat -A POSTROUTING -o {interface} -s {vlan_ip}/24 -j SNAT --to-source {subnet_mask}',
    'iptables -A FORWARD -i eth0 -o LAN-DEV -m state --state RELATED,ESTABLISHED -j ACCEPT',
    'iptables -A FORWARD -i LAN-DEV -o eth0 -j ACCEPT'
]

# Exécuter les commandes iptables
for cmd in commands:
    subprocess.run(cmd, shell=True)
