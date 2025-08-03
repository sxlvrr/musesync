-- ===============================
-- 🔥 Suppression des tables existantes
-- ===============================
DROP TABLE IF EXISTS ecoutes CASCADE;
DROP TABLE IF EXISTS concerts CASCADE;
DROP TABLE IF EXISTS meteo CASCADE;
DROP TABLE IF EXISTS artistes CASCADE;

-- ===============================
-- 🎤 Table artistes
-- ===============================
CREATE TABLE artistes (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    genre VARCHAR(50),
    bpm_moyen INTEGER CHECK (bpm_moyen >= 30 AND bpm_moyen <= 250),
    energie FLOAT CHECK (energie >= 0 AND energie <= 1),
    popularite INTEGER CHECK (popularite >= 0 AND popularite <= 100)
);

-- ===============================
-- 🎫 Table concerts
-- ===============================
CREATE TABLE concerts (
    id SERIAL PRIMARY KEY,
    id_artiste INTEGER NOT NULL REFERENCES artistes(id) ON DELETE CASCADE,
    lieu VARCHAR(100),
    date DATE NOT NULL,
    genre VARCHAR(50),
    meteo VARCHAR(50),
    prix INTEGER CHECK (prix >= 0),
    nb_tickets_vendus INTEGER CHECK (nb_tickets_vendus >= 0)
);

-- ===============================
-- 🎧 Table écoutes
-- ===============================
CREATE TABLE ecoutes (
    id SERIAL PRIMARY KEY,
    id_artiste INTEGER NOT NULL REFERENCES artistes(id) ON DELETE CASCADE,
    date DATE NOT NULL,
    nombre_ecoutes INTEGER CHECK (nombre_ecoutes >= 0),
    plateforme VARCHAR(50)
);

-- ===============================
-- ☀️ Table météo
-- ===============================
CREATE TABLE meteo (
    id SERIAL PRIMARY KEY,
    lieu VARCHAR(100),
    date DATE NOT NULL,
    temperature INTEGER,
    meteo VARCHAR(50)
    -- Pas de clé étrangère directe, mais lieu+date peut être utilisé pour jointures
);
