import psycopg
import json


def wynik():
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
        result = None

        with conn.cursor() as cur:
            cur.execute("""CREATE OR REPLACE VIEW podglad AS SELECT klienci.ID_klienta, klienci.imie, klienci.nazwisko, odczyty.Miejscowosc,
                        odczyty.Ulica, odczyty.Nr_domu, odczyty.Nr_mieszkania,
                        odczyty.wartosc, odczyty.data_odczytu FROM klienci, odczyty WHERE klienci.ID_klienta = odczyty.ID_klienta""")
            cur.execute("SELECT * FROM podglad")
            result = cur.fetchall()
        conn.commit()
    except Exception as ex:
        print("Wystapil blad podczas podgladania bazy danych: " + str(ex))
    
    conn.close()
    return result


if __name__ == '__main__':
    wynik()
