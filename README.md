<h1 align="center">Selenium Page Object</h1>
<img src="https://selenium-python.com/wp-content/uploads/2017/11/cropped-logo-mini.png" width="300">

![Python Version](https://img.shields.io/badge/python-3.7-blue)
![Selenium Version](https://img.shields.io/badge/selenium-3.14-blue)

<h2>📜Описание</h2>
<p>Представлен итоговый полноценный тестовый проект по изучению Selenium на образовательной платформе <a href="https://stepik.org" target="_blank">stepik.org</a> курса <a href="https://stepik.org/course/575/syllabus" target="_blank">Автоматизация тестирования с помощью Selenium и Python</a>.</p>
<p>В качестве тестируемого сайта был использован прототип интернет-магазина <a href="http://selenium1py.pythonanywhere.com" target="_blank">selenium1py.pythonanywhere.com</a>. В проекте использован паттерн Page Object.</p>
<p>P.S. <i>Остальная часть курса расположена в репозитории <a href="https://github.com/Delictum/selenium_and_python" target="_blank">selenium_and_python</a></i>.</p>

<h2>📑Развёртывание программного обеспечения</h2>
===========================
<ol>
  <li><a href="https://www.python.org/downloads/" target="_blank">Скачайте</a> и установите python последней версии;</li>
  <li>Склонируйте / скачайте репозиторий;</li>
  <li>Перейдите к его расположению в командной строке / терминале (например: <code>cd /d C:\Users\USER\Downloads\selenium-page-object-master</code>);</li>
  <li>Создайте виртуальное окружение: <code>python -m venv env</code> (для Unix-систем <code>python3 -m venv env</code>);</li>
  <li>Активируйте окружение командой <code>env\Scripts\activate</code> (для Unix-систем <code>. env/bin/activate</code>);</li>
  <li>Установите необходимые пакеты: <code>pip install -r requirements.txt</code>;</li>
  <li>Установите драйвер для браузера Chrome, как описано в шагах <a href="https://stepik.org/lesson/25969/step/7" target="_blank"> 7-10</a>, или для <a href="https://stepik.org/lesson/237240/step/5" target="_blank">Firefox</a>;</li>
  <li>Запустите тесты при помощи команды: <code>pytest -v --tb=line --language=en -m need_review</code> (при возникновении проблем смотрите <a href="#notes">примечания</a>);</li>
  <li>Наслаждайтесь 🎉.</li>
</ol>

<h2 id="notes">📋Примечания</h2>
===========================
<ul>
    <li>Разработка велась на python 3.7.4, убедитесь что Ваша версия >= 3.6.</li>
    <li>
        При скачивании проекта он должен успешно запуститься, однако при использовании клонирования возможно проблема с импортами пакетов. В таком случае Вы увидите приблизительно следующее: <img src="https://sun9-38.userapi.com/impf/cGTU8MZ-MyxOTXOhe3JWg-EepPvm4iMJMsOjOA/30ARZ_MwGFQ.jpg?size=1894x340&quality=96&proxy=1&sign=aabe814f316c4f1f057a429187a7f2d6&type=album">Для исправления измените группы импортов в начале файлов <i>test_main_page.py</i> и <i>test_product_page.py</i> подобно примеру снизу (Вам требуется добавить точки перед page.XXX.XXX).
        <div>
            <img src="https://sun9-57.userapi.com/impf/BypCA-H_GP7m1Eas3bLAjllc4IHK0_QRfjbAkA/dFC4CP6EgBE.jpg?size=299x63&quality=96&proxy=1&sign=e3f35aa120e7820b3c0b4700e0a5d707&type=album">
            <img height="55px" src="https://avatanplus.com/files/resources/original/5a16589dca5bc15fe74a2885.png">
            <img src="https://sun9-35.userapi.com/impf/KD2NVi9PS_YVpQ0-vadot-Kbn8qMPJi-1hZDnA/1JUHuvWwx34.jpg?size=309x65&quality=96&proxy=1&sign=0f0529269a3268c4a7030261feec8617&type=album">
        </div>
    </li>
    <li>Был создан дополнительный класс <b>WithBasketLinkPage</b>, не предусмотренный в структуре из шага "готовим код к ревью". Данный класс участвует в наследовании и предназанчен для сокращения кода. Так как ссылка перехода к корзине не находиться и не должна быть в странице с самой корзиной, для избежания дублирования был добавлен данный дополнительный класс, который может быть наследован всеми остальными страницами.</li>
</ul>
