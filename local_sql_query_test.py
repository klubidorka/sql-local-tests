import pymysql
from pymysql.cursors import DictCursor

database_name = "AIRTRANS"


def execute_statement(connection, stmt, commit=False, return_result=False):
    stmt = stmt.strip()
    if len(stmt) == 0:
        return
    cursor = connection.cursor()
    cursor.execute(stmt)
    if commit:
        connection.commit()
    if return_result:
        return cursor.fetchall()


def run_query_from_file(path_to_file, connection):
    with open(path_to_file, mode='r') as sql_script:
        return execute_statement(connection, sql_script.read(), commit=True, return_result=True)


# Подключаемся к MySql, сервер с базой нужно поднять отдельно
# https://docs.oracle.com/en/java/java-components/advanced-management-console/2.20/install-guide/mysql-database-installation-and-configuration-advanced-management-console.html#GUID-12323233-07E3-45C2-B77A-F35B3BBA6592
def connect_to_airtrans_db(host='localhost', user='root', password='password'):
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        charset='utf8mb4',
        cursorclass=DictCursor
    )
    execute_statement(connection, f"CREATE DATABASE IF NOT EXISTS {database_name}")
    execute_statement(connection, f"USE {database_name}")
    with open('sql/INIT_DB.sql', mode='r') as initial_sql_script:
        sqlStatements = initial_sql_script.read().split(';')
        for statement in sqlStatements:
            execute_statement(connection, statement)
        connection.commit()
    return connection


def release_resources(connection):
    execute_statement(connection, f"DROP DATABASE {database_name}", commit=True)
    connection.close()


def run_queries():
    connection = connect_to_airtrans_db()
    try:
        # место для запуска SQL запросов
        result = run_query_from_file('sql/test.sql', connection)
        for entry in result:
            print(entry)
    finally:
        release_resources(connection)


if __name__ == '__main__':
    try:
        run_queries()
    except pymysql.err.OperationalError as e:
        print(e)
