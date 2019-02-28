CREATE TABLE IF NOT EXISTS events(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    date DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS fighters(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE join_events_fighters(
    event_id INTEGER REFERENCES events(id),
    fighter_id INTEGER REFERENCES fighters(id),
    PRIMARY KEY(event_id, fighter_id)
);