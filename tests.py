import pytest

from main import BooksCollector

class TestBooksCollector:

    # Тесты для add_new_book
    @pytest.mark.parametrize("book_name", ["Гордость и предубеждение", "1984"])
    def test_add_new_book_book_to_genre(self, collector, book_name):
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()

    @pytest.mark.parametrize("book_name, expected_in_genre", [
        ["Я", True],  # 1 символ — должно добавиться
        ["A" * 40, True]  # 40 символов — должно добавиться
    ])
    def test_add_new_book_boundary_values(self, collector, book_name, expected_in_genre):
        collector.add_new_book(book_name)
        assert (book_name in collector.get_books_genre()) == expected_in_genre

    @pytest.mark.parametrize("book_name, expected_in_genre", [
        ["A" * 41, False],  # 41 символ — не должно добавиться
        ["", False]  # 0 символов — не должно добавиться
    ])
    def test_add_new_book_values_outside_boundaries(self, collector, book_name, expected_in_genre):
        collector.add_new_book(book_name)
        assert (book_name in collector.get_books_genre()) == expected_in_genre

    # Тесты для set_book_genre
    def test_set_book_genre_book_in_genre_in(self, collector):
        collector.books_genre["Анора"] = ""
        collector.set_book_genre("Анора", "Комедии")
        assert collector.books_genre["Анора"] == "Комедии"

    def test_set_book_genre_book_in_genre_not_in(self, collector):
        collector.books_genre["Анора"] = ""
        collector.set_book_genre("Анора", "Драма")
        assert collector.books_genre["Анора"] == ""

    def test_set_book_genre_book_not_in_genre_in(self, collector):
        collector.set_book_genre("Неизвестная", "Комедии")
        assert "Неизвестная" not in collector.books_genre

    # Тест для get_book_genre
    def test_get_book_genre_with_genre(self, collector):
        collector.books_genre["1984"] = "Фантастика"
        assert collector.get_book_genre("1984") == "Фантастика"

    # Тест для get_books_with_specific_genre
    @pytest.mark.parametrize("book_name, genre", [
        ["1984", "Фантастика"],
        ["Король Лев", "Мультфильмы"]
    ])
    def test_get_books_with_specific_genre_true(self, collector, book_name, genre):
        collector.books_genre[book_name] = genre
        assert book_name in collector.get_books_with_specific_genre(genre)

    # Тест для get_books_for_children
    @pytest.mark.parametrize("books_genre, expected_for_children", [
        # Сценарий: книги без возрастного ограничения
        (
            {
                "Гарри Поттер": "Фантастика",
                "Король Лев": "Мультфильмы"
             },
            ["Гарри Поттер", "Король Лев"]
        )
    ])
    def test_get_books_for_children_return_list(self, collector, books_genre, expected_for_children):
        collector.books_genre = books_genre
        assert collector.get_books_for_children() == expected_for_children

    @pytest.mark.parametrize("books_genre, expected_for_children", [
        # Сценарий: книги только с возрастным ограничением
        (
            {
                "Дракула": "Ужасы",
                "Шерлок Холмс": "Детективы"
            },
            []
        )
        ])
    def test_get_books_for_children_return_empty_list(self, collector, books_genre, expected_for_children):
        collector.books_genre = books_genre
        assert collector.get_books_for_children() == expected_for_children

    # Тест для get_books_genre
    def test_get_books_genre_true(self, collector):
        expected_books_genre = {
                "1984": "Фантастика",
                "Анатомия падения": "Детективы"
            }
        collector.books_genre = expected_books_genre
        assert collector.get_books_genre() == expected_books_genre

    # Тест для add_book_in_favorites
    def test_add_book_in_favorites_successful_addition(self, collector):
        book_name = "Властелин колец"
        collector.books_genre = {book_name: "Фантастика"}
        collector.favorites = []
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.favorites

    @pytest.mark.parametrize("book_name, initial_favorites, expected_in_favorites", [
        ["Властелин колец", ["Властелин колец"], True],  # Книга уже в favorites — не добавится повторно
        ["Неизвестная книга", [], False] # Книги нет в books_genre — не добавится в favorites
    ])
    def test_add_book_in_favorites_not_added(self, collector, book_name, initial_favorites, expected_in_favorites):
        collector.books_genre = {"Властелин колец": "Фантастика"}
        collector.favorites = initial_favorites
        collector.add_book_in_favorites(book_name)
        assert (book_name in collector.favorites) == expected_in_favorites

    # Тесты для delete_book_from_favorites
    # для успешного удаления книги из избранного
    def test_delete_book_from_favorites_success_removes_book(self, collector):
        book_name = "Властелин колец"
        collector.favorites = ["Властелин колец", "Дюна"]
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.favorites

    # для проверки оставшихся книг после удаления
    def test_delete_book_from_favorites_success_remaining_books(self, collector):
        collector.favorites = ["Властелин колец", "Дюна"]
        collector.delete_book_from_favorites("Властелин колец")
        assert collector.favorites == ["Дюна"]

    # если книги нет в избранном, и список не меняется
    def test_delete_book_from_favorites_no_book_in_list(self, collector):
        book_name = "Властелин колец"
        collector.favorites = ["Властелин"]
        collector.delete_book_from_favorites(book_name)
        assert collector.favorites == ["Властелин"]

    # Тест для get_list_of_favorites_books
    def test_get_list_of_favorites_books_correct_list(self, collector):
        collector.favorites = ["Ревизор", "Вторая жизнь Уве"]
        assert collector.get_list_of_favorites_books() == ["Ревизор", "Вторая жизнь Уве"]
