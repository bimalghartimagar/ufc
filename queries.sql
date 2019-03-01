CREATE TABLE IF NOT EXISTS events(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    date TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS fighters(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE join_events_fighters(
    event_id INTEGER REFERENCES events(id) ON DELETE CASCADE,
    fighter_id INTEGER REFERENCES fighters(id) ON DELETE CASCADE,
    PRIMARY KEY(event_id, fighter_id)
);