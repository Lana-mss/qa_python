В conftest.py инициализируется объект класса класса BooksCollector.
В test.py реализованы тесты, покрывающие методы класса BooksCollector:
1. Для метода add_new_book
   1.1. test_add_new_book_book_to_genre: позитивная проверка добавления одной книги в books_genre
   1.2. test_add_new_book_boundary_values: позитивная проверка добавления названия книг, где количество символов = допустимым граничным значениям
   1.3. test_add_new_book_values_outside_boundaries: негативная проверка добавления названия книг, где количество символов вне пределов граничных значений

2. Для метода set_book_genre
    2.1. test_set_book_genre_book_in_genre_in: проверка установления жанра, если книга есть словаре, жанр - в списке жанров
    2.2. test_set_book_genre_book_in_genre_not_in: проверка, если книга в словаре, но жанра нет в списке жанров
    2.3. test_set_book_genre_book_not_in_genre_in: проверка, если книги нет в словаре 

3. Для метода get_book_genre
    3.1. test_get_book_genre_with_genre: проверка получения жанра из словаря, если у книги есть жанр

4. Для метода get_books_with_specific_genre
    4.1. test_get_books_with_specific_genre_true: проверка, что книга возвращается для нужного жанра

5. Для метода get_books_for_children
    5.1. test_get_books_for_children_return_list: возвращаем книги, подходящие детям
    5.2. test_get_books_for_children_return_empty_list: возвращаем пустой список

6. Для метода get_books_genre
    6.1. test_get_books_genre_true: проверка, что метод возвращает правильный словарь
              
7. Для метода add_book_in_favorites
    7.1. test_add_book_in_favorites_successful_addition: книга есть в books_genre и нет в favorites - добавится
    7.2. test_add_book_in_favorites_not_added: книги нет в books_genre / книга уже в favorites - не добавится

8. Для метода delete_book_from_favorites
   8.1. test_delete_book_from_favorites_success_removes_book: тест для успешного удаления книги из избранного
   8.2. test_delete_book_from_favorites_success_remaining_books: тест для проверки оставшихся книг после удаления
   8.3. test_delete_book_from_favorites_no_book_in_list: тест если книги нет в избранном, и список не меняется

9. Для метода get_list_of_favorites_books
   9.1. test_get_list_of_favorites_books_correct_list: для проверки получения корректного списка Избранного

В тестах была использована параметризация для сокращения количества кода.