import random
from typing import Optional


def afficher_message_bienvenue() -> None:
    """
    Affiche un message de bienvenue et les règles du jeu.
    """
    print("Essayez de deviner un nombre aléatoire entre 1 et 20 en un minimum d'essais.")
    print("Bonne chance!\n")


def generer_nombre_aleatoire() -> int:
    """
    Génère un nombre aléatoire entre 1 et 20.
    """
    return random.randint(1, 20)


def obtenir_deviner_utilisateur() -> int:
    """
    Demande à l'utilisateur de saisir un nombre entre 1 et 20 et le valide.
    """
    while True:
        try:
            devinette: int = int(input("Entrez votre devinette (un nombre entre 1 et 20): "))
            if 1 <= devinette <= 20:
                return devinette
            else:
                print("Le nombre doit être entre 1 et 20. Essayez encore.")
        except ValueError:
            print("Ce n'est pas un nombre valide. Essayez encore.")


def donner_indice(devinette: int, nombre_cible: int) -> None:
    """
    Fournit un indice sur la devinette : trop bas, trop haut ou correct.
    """
    if devinette < nombre_cible:
        print("Trop bas, essayez un nombre plus grand.")
    elif devinette > nombre_cible:
        print("Trop haut, essayez un nombre plus petit.")
    else:
        print("Félicitations!")


def jouer_partie() -> None:
    """
    Exécute une partie du jeu, où l'utilisateur essaie de deviner le nombre.
    """
    nombre_cible: int = generer_nombre_aleatoire()
    devinette: Optional[int] = None
    essais: int = 0

    while devinette != nombre_cible:
        devinette = obtenir_deviner_utilisateur()
        donner_indice(devinette, nombre_cible)
        essais += 1

    print(f"Vous avez trouvé le nombre en {essais} essais.\n")


def demander_si_rejouer() -> bool:
    """
    Demande à l'utilisateur s'il souhaite rejouer après une partie.
    """
    while True:
        reponse: str = input("Voulez-vous jouer à nouveau? (o/n): ").strip().lower()
        if reponse in ('o', 'n'):
            return reponse == 'o'
        print("Réponse invalide. Veuillez entrer 'o' pour oui ou 'n' pour non.")


def jeu_devinette() -> None:
    """
    Fonction principale pour lancer le jeu.
    """
    afficher_message_bienvenue()
    jouer_partie()

    while demander_si_rejouer():
        jouer_partie()

    print("Merci d'avoir joué.")


# Lancement du jeu
if __name__ == "__main__":
    jeu_devinette()
