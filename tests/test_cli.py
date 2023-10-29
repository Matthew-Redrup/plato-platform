from plato_platform.utils.cli import cli


def test_cli(capsys):
    cli(["--prompt", "Testing"])
    captured = capsys.readouterr()
    result = captured.out
    assert "Testing" in result
