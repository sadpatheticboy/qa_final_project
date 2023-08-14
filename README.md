# Это проект по автоматизации демо-сайта онлайн-магазина
Создание такого проекта было финальным заданием курса "Автоматизация тестирования с помощью Selenium и Python" ([ссылка на курс](https://stepik.org/course/575/promo)).

Проект написан в стиле Page Object Model:
- Все методы действия и проверки выделены в отдельные методы в классах PageObject; 
- Все селекторы лежат в locators.py;
- Нет assert в теле тестов.

Также в проекте есть возможность запускать тесты с параметром, а именно с заданным языком.

Во время написания проекта старался придерживаться читаемого кода, правильных коммитов и в целом логики. 

## Как запустить проект?

### Копирование репозитория
```
git clone https://github.com/sadpatheticboy/qa_final_project.git
cd qa_final_project
pip install -r requirements.txt 
```

### Запуск необходимых тестов
```
pytest -v --tb=line --language=en -m need_review
```
