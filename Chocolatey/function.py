import subprocess
from selection import *

list_install_choco = ["Set-ExecutionPolicy Bypass -Scope Process -Force",
                      "[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072",
                      "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))",
                      ]


#### ajouter des logiciels a cette liste


def powershellAction(my_list):
    for value in my_list:
        process = subprocess.Popen(["powershell", value], stdout=subprocess.PIPE);
        result = process.communicate()[0]
        print(result)


def install_chocolatey():
    powershellAction(list_install_choco)

def install_software():
    powershellAction(meslogiciels)

print(list_install_choco)

### fonction de changement de nom machine et mise sur le domaine
def add_to_domaine(nom_machine):
    commande_powershell1 = subprocess.Popen(["powershell", "Rename-Computer " + nom_machine ], stdout=subprocess.PIPE)
    ####commande pour l ajout sur le domaine
    commande_powershell2 = subprocess.Popen(["powershell", "Add-Computer -Domain quadra-informatique.fr -NewName $hostname -Credential Get-Credential -Restart -Force"], stdout=subprocess.PIPE);


###################################




