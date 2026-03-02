def tallenna_peli(tähän tarvii oikeet parametrit):
    sql = f'UPDATE game SET location = %s, player_range = %s, money = %s WHERE id = %s'
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql, (tähän samat parametrit kuin funktion kutsussa))