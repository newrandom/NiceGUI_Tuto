import psycopg2
from config import load_config

def get_parts(vendor_id):
    parts = []
    params = load_config()
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                # cur = conn.cursor()
                cur.callproc('get_parts_by_vendor', (vendor_id,))

                row = cur.fetchone()
                while row is not None:
                    parts.append(row)
                    row = cur.fetchone()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return parts
    
if __name__ == "__main__":
    parts = get_parts(1)
    print(parts)    