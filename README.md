# Sprint_7
	Test_API
Проект автоматизации сервиса "Самокат"
1.Фреймворк:
Pytest - основа написания тестов
Аllure-pytest - отчет тестирования
2.Необходимые установки :
pip install pytest
pip install -r requirements.txt
pip install allure-pytest
4.Команда для запуска –
pytest  -v                              # тестов
pytest --alluredir=./allure-results     # запустить все тесты и записать отчет
allure serve ./allure-results           # посмотреть отчет по прогону htm
