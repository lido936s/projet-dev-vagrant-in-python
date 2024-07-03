# Configuration la carte NAT VMware Workstation (Windows) 

# installer VMware PowerCLI > https://blogs.vmware.com/PowerCLI/2017/04/powercli-install-process-powershell-gallery.html 
Install-Module -Name VMware.PowerCLI –Scope CurrentUser -Force 

# Creer la carte VMnet8 pour la configuration réseau en NAT avec en segment reseau 192.168.17.0/24 et en gateway 192.168.17.2 sur vmware workstation 
# https://binarynature.blogspot.com/2018/02/lan-segments-vmware-workstation-windows.html

New-NatNetwork -Name "VMnet8" -Subnet "192.168.17.0/24" -Gateway "192.168.17.2" -VMotionSubnet "192.168.17.0/24"
New-VMHostNetwork -Name "VMnet8" -Type NAT -Subnet "192.168.17.0/24" -Gateway "192.168.17.2" -VMotionSubnet "192.168.17.0/24" -VirtualSwitch LAN-SRV

$NAT = Get-NetAdapter -InterfaceIndex 25

New-VMSwitch -Name "VMnet8" -NetAdapterName $NAT.Name

# Creer une machine d'aprés un scripts python une machine Virtuel sur VMware Workstation (Windows) 

