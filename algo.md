Question:

    -voulez vous creer un certificat ssl ?
        Oui / Non

    -Nom de domaine? (input()) # stocker dans une variable

    - Demander ou déplacer les certificat # stocker dans une variable

Code a exectuer

    - Déplacement dans /etc/ssl

    - Génération du fichier : $ sudo openssl genrsa -out nomDomaine.key 2048

    - Générer fichier demande de signature de certificat : $ sudo openssl req -new -key server.key -out server.csr

    (Question du certificat à retourner)

    - Signature du certificat : $ sudo openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt

    - Retourner : certificat auto-signé pour 365 jours (1 an) 

    - Retourer succeful ou error # print() # stopper code si error + supprimer fichier si créer

    - Déplacer les fichiers .crt + .key : cp server.crt server.key /etc/nginx/ssl

    - On verifie syntax nginx : sudo nginx -t

    - On restart systemctl : sudo systemctl restart nginx

    



