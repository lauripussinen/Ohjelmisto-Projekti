MariaDB [ohjelmistopeli]> describe airport;
+-------------------+-------------+------+-----+---------+-------+
| Field             | Type        | Null | Key | Default | Extra |
+-------------------+-------------+------+-----+---------+-------+
| id                | int(11)     | NO   |     | NULL    |       |
| ident             | varchar(40) | NO   | PRI | NULL    |       |
| type              | varchar(40) | YES  |     | NULL    |       |
| name              | varchar(40) | YES  |     | NULL    |       |
| latitude_deg      | double      | YES  |     | NULL    |       |
| longitude_deg     | double      | YES  |     | NULL    |       |
| elevation_ft      | int(11)     | YES  |     | NULL    |       |
| continent         | varchar(40) | YES  |     | NULL    |       |
| iso_country       | varchar(40) | YES  | MUL | NULL    |       |
| iso_region        | varchar(40) | YES  |     | NULL    |       |
| municipality      | varchar(40) | YES  |     | NULL    |       |
| scheduled_service | varchar(40) | YES  |     | NULL    |       |
| gps_code          | varchar(40) | YES  |     | NULL    |       |
| iata_code         | varchar(40) | YES  |     | NULL    |       |
| local_code        | varchar(40) | YES  |     | NULL    |       |
| home_link         | varchar(40) | YES  |     | NULL    |       |
| wikipedia_link    | varchar(40) | YES  |     | NULL    |       |
| keywords          | varchar(40) | YES  |     | NULL    |       |
+-------------------+-------------+------+-----+---------+-------+