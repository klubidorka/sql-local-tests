# Репозиторий для тестирования SQL-скриптов

Репозиторий создан для участников SQL-соревнований ИТ школы. С его помощью участники могут протестировать свои SQL запросы на данных, близких к тем, которые используются в тестирующей системе на Степике.

### Отладка SQL скриптов

1. [Поднять](https://docs.oracle.com/en/java/java-components/advanced-management-console/2.20/install-guide/mysql-database-installation-and-configuration-advanced-management-console.html#GUID-12323233-07E3-45C2-B77A-F35B3BBA6592) локальный сервер с MySql. Рекомендуется версия MySQL 5.7.12, так как именно эта версия используется в тестирующей системе Степика
2. Отредактировать функцию `run_queries()` в файле `local_sql_query_test.py`. Не забудьте передать нужные параметры в функцию `connect_to_airtrans_db()` в соответствии с настройками вашего сервера базы данных. База создается при помощи `sql/INIT_DB.sql`. В примере запускается скрипт из `sql/test.sql`
3. Запустить скрипт в IDE или при помощи  `python3 local_sql_query_test.py`
