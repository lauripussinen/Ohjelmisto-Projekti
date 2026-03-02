def tallenna_peli(yhteys, game_id, location, co2_consumed, current_item, attempts):
    sql = '''
        UPDATE game
        SET location = %s,
            co2_consumed = %s,
            current_item = %s,
            attempts = %s
        WHERE id = %s
    '''
    cursor = (yhteys.cursor())
    cursor.execute(sql, (location, co2_consumed, current_item, attempts, game_id))
    yhteys.commit()

import mysql.connector

yhteys = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Allu8221!",
    database="ohjelmistopeli"
)