import pytest


def test_program():
    print("hello")


@pytest.mark.smoke
def test_program2():
    print("Test my name")


@pytest.mark.smoke
def test_program5():
    print("Prathyusha is my name")
