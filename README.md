<h1 align="center">Selenium Page Object</h1>
<img src="https://selenium-python.com/wp-content/uploads/2017/11/cropped-logo-mini.png" width="300">

<h2>Описание</h2>
<p>Представлен итоговый полноценный тестовый проект по изучению Selenium на образовательной платформе <a href="https://stepik.org">stepik.org</a> курса <a href="https://stepik.org/course/575/syllabus">Автоматизация тестирования с помощью Selenium и Python</a>.</p>
<p>В качестве тестируемого сайта был использован прототип интернет-магазина <a href="http://selenium1py.pythonanywhere.com">selenium1py.pythonanywhere.com</a>. В проекте использован паттерн Page Object.</p>
<p>P.S. <i>Остальная часть курса расположена в репозитории <a href="https://github.com/Delictum/selenium_and_python">selenium_and_python</a></i>.</p>

<h2>Развёртывание программного обеспечения</h2>
===========================
<ol>
  <li>Склонируйте / скачайте репозиторий;</li>
  <li>Перейдите к его расположению в командной строке / терминале (например: <code>cd /d C:\Users\USER\Downloads\selenium-page-object-master</code>);</li>
  <li>Создайте виртуальное окружение: <code>python -m venv env</code> (для Unix-систем <code>python3 -m venv env</code>);</li>
  <li>Активируйте окружение командой <code>env\Scripts\activate</code> (для Unix-систем <code>. env/bin/activate</code>);</li>
  <li>Установите необходимые пакеты: <code>pip install -r requirements.txt</code>;</li>
  <li>Установите драйвер для браузера Chrome, как описано в шагах <a href="https://stepik.org/lesson/25969/step/7"> 7-10</a>, или для <a href="https://stepik.org/lesson/237240/step/5">Firefox</a>;</li>
  <li>Запустите тесты при помощи команды: <code>pytest -v --tb=line --language=en -m need_review</code>;</li>
  <li>Наслаждайтесь 🎉.</li>
</ol>