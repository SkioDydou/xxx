Commit initial du projet Flask de JOUSSELIN Dylan et DHAUSSY Erwan

Pour lancer le projet, il faut tout d'abord flask loaddb album.yml puis flask run.
La plupart des fonctions sur le site fonctionnent, seul la playlist ainsi que la note ne fonctionnent pas. Afin d'avoir accés à toutes les fonctionnalités, il faut s'inscrire puis se log.

Vous pouvez accéder aux détails d'un album en cliquand dessus dans "Tous les albums", ensuite si vous êtes logs vous pouvez supprimer ou modifier un album.
Sur la page "Tous les albums", vous pouvez aussi ajouter un album grâce au bouton.
Vous pouvez aussi rechercher un album par filtre en cliquant sur la petite loupe en haut à droite.

Le code n'est pas très esthétique, il n'est pas non plus optimisé car nous avons préférés que celà fonctionne le mieux possible, au vu des autres travaux que nous avions à effectuer pour notre S3 (au vu des conditions sanitaires actuelles).

Nous avons choisi de ne pas afficher le profil par exemple de l'utilisateur car celà est peu utile et ce n'était pas le plus important.