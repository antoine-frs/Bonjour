import pytest
from unittest.mock import patch, MagicMock
import random
from bonjour.Projet import (
    afficher_message_bienvenue,
    generer_nombre_aleatoire,
    obtenir_deviner_utilisateur,
    donner_indice,
    jouer_partie,
    demander_si_rejouer,
    jeu_devinette,
)


def test_afficher_message_bienvenue(capfd: pytest.CaptureFixture) -> None:
    afficher_message_bienvenue()
    captured = capfd.readouterr()
    assert "Essayez de deviner un nombre aléatoire entre 1 et 20" in captured.out
    assert "Bonne chance!" in captured.out


def test_generer_nombre_aleatoire() -> None:
    random.seed(0)  # Seed the random number generator for predictable output
    number: int = generer_nombre_aleatoire()
    assert 1 <= number <= 20


@patch("builtins.input", side_effect=["10"])
def test_obtenir_deviner_utilisateur(mock_input: MagicMock) -> None:
    devinette: int = obtenir_deviner_utilisateur()
    assert devinette == 10


@patch("builtins.input", side_effect=["30", "abc", "15"])
def test_obtenir_deviner_utilisateur_invalid_input(mock_input: MagicMock) -> None:
    devinette: int = obtenir_deviner_utilisateur()
    assert devinette == 15


def test_donner_indice_trop_bas(capfd: pytest.CaptureFixture) -> None:
    donner_indice(5, 10)
    captured = capfd.readouterr()
    assert "Trop bas" in captured.out


def test_donner_indice_trop_haut(capfd: pytest.CaptureFixture) -> None:
    donner_indice(15, 10)
    captured = capfd.readouterr()
    assert "Trop haut" in captured.out


def test_donner_indice_correct(capfd: pytest.CaptureFixture) -> None:
    donner_indice(10, 10)
    captured = capfd.readouterr()
    assert "Félicitations!" in captured.out


@patch("builtins.input", side_effect=["10", "20"])
@patch("bonjour.Projet.generer_nombre_aleatoire", return_value=15)
@patch("bonjour.Projet.donner_indice")
def test_jouer_partie(
    mock_donner_indice: MagicMock,
    mock_generer_nombre_aleatoire: MagicMock,
    mock_input: MagicMock,
) -> None:
    with patch("builtins.print") as mock_print:
        jouer_partie()
        assert mock_donner_indice.call_count == 2
        mock_print.assert_called_with("Vous avez trouvé le nombre en 2 essais.\n")


@patch("builtins.input", side_effect=["o", "n"])
def test_demander_si_rejouer_oui(mock_input: MagicMock) -> None:
    assert demander_si_rejouer() is True
    assert demander_si_rejouer() is False


@patch("builtins.input", side_effect=["o", "n"])
@patch("bonjour.Projet.jouer_partie")
def test_jeu_devinette(mock_jouer_partie: MagicMock, mock_input: MagicMock) -> None:
    with patch("builtins.print") as mock_print:
        jeu_devinette()
        assert mock_jouer_partie.call_count == 2
        mock_print.assert_called_with("Merci d'avoir joué.")
