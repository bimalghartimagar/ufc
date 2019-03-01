INSERT_FIGHTER = "INSERT INTO fighters (name) values (%s) ON CONFLICT(name) DO UPDATE SET name=EXCLUDED.name RETURNING id;"
INSERT_EVENT = "INSERT INTO events (name, date) values (%s,%s)  RETURNING id;"
INSERT_RELATION = "INSERT INTO join_events_fighters(event_id, fighter_id) values (%s, %s);"