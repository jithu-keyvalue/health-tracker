CREATE TABLE IF NOT EXISTS observations (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    let-us-keep-a-better-column-name-here-for-hb-value REAL NOT NULL CHECK (hb > 0)
);
