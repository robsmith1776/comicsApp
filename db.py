import psycopg2

# Connect to an existing database
DSN = "dbname=postgres user=postgres host=localhost port=5433 password=TxH8v16!8Vuo"


def run_insert(comic_list):
    # Expects Result Set
    conn = psycopg2.connect(DSN)
    i = 0
    with conn:
        with conn.cursor() as curs:
            curs.execute("delete from Comics.Information;")
            conn.commit()
            for comic in comic_list:
                package = (i, comic[1], comic[0], comic[2], comic[3])
                try:
                    insert_text(curs, package)
                except psycopg2.errors.InvalidTextRepresentation:
                    print(comic)
                i += 1
                conn.commit()
    conn.close()


def insert_text(curs, package):
    curs.execute(
        "INSERT INTO Comics.Information (id,cost,title,number,releasedate) VALUES (%s, %s, %s, %s, %s);",
        package)
