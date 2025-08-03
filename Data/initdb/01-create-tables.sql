CREATE TABLE IF NOT EXISTS artistes (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(100),
    genre VARCHAR(50),
    bpm_moyen INT,
    énergie FLOAT,
    popularité INT
);

CREATE TABLE IF NOT EXISTS concerts (
    id SERIAL PRIMARY KEY,
    artiste VARCHAR(100),
    date DATE,
    lieu VARCHAR(100),
    genre VARCHAR(50),
    météo VARCHAR(50),
    prix FLOAT,
    nb_tickets_vendus INT
);

CREATE TABLE IF NOT EXISTS ecoutes (
    id SERIAL PRIMARY KEY,
    artiste VARCHAR(100),
    date DATE,
    nb_écoutes INT,
    plateforme VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS meteo (
    date DATE,
    lieu VARCHAR(100),
    température INT,
    météo VARCHAR(50),
    PRIMARY KEY(date, lieu)
);
