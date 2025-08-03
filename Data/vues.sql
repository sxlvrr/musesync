-- 1. Nombre d'écoutes par mois et par artiste
CREATE OR REPLACE VIEW ecoutes_par_mois_artiste AS
SELECT
  id_artiste,
  DATE_TRUNC('month', date) AS mois,
  SUM(nombre_ecoutes) AS total_ecoutes
FROM ecoutes
GROUP BY id_artiste, mois
ORDER BY id_artiste, mois;

-- 2. Fréquentation moyenne par lieu
CREATE OR REPLACE VIEW frequentation_moyenne_par_lieu AS
SELECT
  lieu,
  AVG(nb_tickets_vendus) AS frequentation_moyenne,
  COUNT(*) AS nombre_concerts
FROM concerts
GROUP BY lieu
ORDER BY frequentation_moyenne DESC;

-- 3. Fréquentation moyenne par artiste
CREATE OR REPLACE VIEW frequentation_moyenne_par_artiste AS
SELECT
  id_artiste,
  AVG(nb_tickets_vendus) AS frequentation_moyenne,
  COUNT(*) AS nombre_concerts
FROM concerts
GROUP BY id_artiste
ORDER BY frequentation_moyenne DESC;

-- 4. Croisement météo et fréquentation
CREATE OR REPLACE VIEW meteo_frequentation AS
SELECT
  meteo,
  AVG(nb_tickets_vendus) AS frequentation_moyenne,
  COUNT(*) AS nombre_concerts
FROM concerts
GROUP BY meteo
ORDER BY frequentation_moyenne DESC;

-- 5. Classement des artistes les plus écoutés
CREATE OR REPLACE VIEW artistes_plus_ecoutes AS
SELECT
  a.id,
  a.nom,
  SUM(e.nombre_ecoutes) AS total_ecoutes
FROM artistes a
JOIN ecoutes e ON a.id = e.id_artiste
GROUP BY a.id, a.nom
ORDER BY total_ecoutes DESC
LIMIT 20;

-- 6. Classement des artistes les plus vus en concert
CREATE OR REPLACE VIEW artistes_plus_vus AS
SELECT
  a.id,
  a.nom,
  SUM(c.nb_tickets_vendus) AS total_frequentation
FROM artistes a
JOIN concerts c ON a.id = c.id_artiste
GROUP BY a.id, a.nom
ORDER BY total_frequentation DESC
LIMIT 20;
