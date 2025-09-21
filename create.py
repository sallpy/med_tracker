
import psycopg2

print("Тестируем подключение...")

try:

    conn = psycopg2.connect(
        "host='127.0.0.1' port=5433 dbname=postgres user=postgres password=1234"
    )

    print(" УСПЕХ! Подключение установлено")
    conn.close()

except Exception as e:
    print(f"❌ Ошибка: {e}")

    try:
        conn = psycopg2.connect(
            host='localhost',
            port=5432,
            user='postgres',
            password='1234',
            database='postgres',
            connect_timeout=5
        )

        print(" УСПЕХ с таймаутом!")
        conn.close()
    except Exception as e2:
        print(f"❌ Ошибка с таймаутом: {e2}")
