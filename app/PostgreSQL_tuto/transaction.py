import psycopg2
from config import load_config

def add_part(part_name, vendor_list):
    insert_part = 'INSERT INTO parts(part_name) VALUES(%s) RETURNING part_id;'

    assign_vendor = 'INSERT INTO vendor_parts(vendor_id, part_id) VALUES (%s, %s);'

    conn  = None
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(insert_part, (part_name,))

                row = cur.fetchone()
                if row:
                    part_id = row[0]
                else:
                    raise Exception('Could not get the part id')
                
                for vendor_id in vendor_list:
                    cur.execute(assign_vendor, (vendor_id, part_id))

                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        if conn:
            conn.rollback()

        print(error)

if __name__=="__main__":
    # add_part('SIM Tray', (1, 2))
    # add_part('Speaker', (3, 4))
    # add_part('Vibrator', (5, 6))
    # add_part('Antenna', (6, 7))
    # add_part('Home Button', (1, 5))
    # add_part('LTE Modem', (1, 5))

    add_part('Power Amplifier', (99,))