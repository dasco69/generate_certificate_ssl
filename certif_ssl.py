# Script for create certificate ssl
# control os
import os
# check box
import inquirer
# stop script
import sys
# regex
import re


#----- Questions -----#
# start project   
def start():
    questions = [
        inquirer.List('certificat',
                    message="Voulez créer un certificat SSL ?",
                    choices=['OUI', 'NON'],
                    default= 'OUI' ),
    ]
    answers = inquirer.prompt(questions)
    # if answer egal Oui send main function (start application)
    if answers['certificat'] == 'OUI':
        main()
    #or else stop application
    else:
        return sys.exit()
    
    

def main():
    #continu question if start it's ok
    questions = [
        inquirer.Text('domain',
                    message="Nom de domaine ?") ,
        inquirer.Path('folderCertif',
                 message="Où dois-je placer le certificat ?",
                 path_type=inquirer.Path.DIRECTORY,
                )
    ]    
    answers = inquirer.prompt(questions)
    
    # catch variable
    domain = answers['domain']
    folder_certif = answers['folderCertif']
    # test string
    is_string(domain)
    is_string(folder_certif)
    
    return domain + folder_certif
#END Main



# check string
def is_string(element):
    if type(element) == str:
        # print("c'est une string")
        return True
    else:
        # print("ce n'est pas une string")
        return False
#END is_string

# a voir pour obliger "/"
def path_validate(answers, current):
    if not re.match('', current):
        raise errors.ValidationError('', reason= 'Mauvais chemin')


#----- END Question -----#

#----- START script automation -----#

def checkFolder():
    main
    


checkFolder()
#----- END script automation -----#

start()