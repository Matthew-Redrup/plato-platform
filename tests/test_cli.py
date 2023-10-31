from plato_platform.utils.cli import MenuCLI


def test_menu_cli_initial_choice():
    cli = MenuCLI()
    assert cli.choice == ""


def test_menu_cli_initial_user_input():
    cli = MenuCLI()
    assert cli.user_input == ""


def test_menu_cli_action_with_invalid_option(capsys, monkeypatch):
    cli = MenuCLI()
    monkeypatch.setattr("builtins.input", lambda x: "5")  # Mocking user input
    cli.parse_input()
    cli.action()
    captured = capsys.readouterr()
    assert "Invalid option. Please try again." in captured.out
