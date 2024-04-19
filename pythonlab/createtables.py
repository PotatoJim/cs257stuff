DROP TABLE IF EXISTS cities
CREATE TABLE cities (
    city text,
    state text,
    pop real,
    latitude real,
    longitude real
)

DROP TABLE IF EXISTS states 
CREATE TABLE states (
    code text,
    state text,
    pop real
)