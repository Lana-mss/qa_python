import pytest

from main import BooksCollector

# Фикстура для инициализации объекта BooksCollector
@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector
