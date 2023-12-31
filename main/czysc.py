import psycopg
import json


def czysc():
    try:
    # Odczytaj plik JSON
        with open("database_creds.json", "r") as json_file:
            dane = json.loads(json_file.read())
        # Polacz sie z baza danych
        conn = psycopg.connect(dbname=dane["db_name"],
                                user=dane["user_name"],
                                password=dane["password"],
                                host=dane["host_name"],
                                port=dane["port_number"]
                               )

        with conn.cursor() as cur:
            cur.execute("DROP TABLE IF EXISTS klienci CASCADE")
            cur.execute("DROP TABLE IF EXISTS odczyty")
        conn.commit()
    except Exception as ex:
        print("Wystapil blad podczas czyszczenia bazy danych: " + str(ex))
    
    conn.close()
    return


if __name__ == '__main__':
    czysc()
