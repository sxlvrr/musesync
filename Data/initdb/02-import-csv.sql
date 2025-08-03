-- Attention : le chemin est relatif dans le conteneur
\copy artistes FROM '/docker-entrypoint-initdb.d/artistes.csv' WITH (FORMAT csv, HEADER true, DELIMITER ',');
\copy concerts FROM '/docker-entrypoint-initdb.d/concerts.csv' WITH (FORMAT csv, HEADER true, DELIMITER ',');
\copy ecoutes FROM '/docker-entrypoint-initdb.d/ecoutes.csv' WITH (FORMAT csv, HEADER true, DELIMITER ',');
\copy meteo FROM '/docker-entrypoint-initdb.d/meteo.csv' WITH (FORMAT csv, HEADER true, DELIMITER ',');
