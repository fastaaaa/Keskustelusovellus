CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);

CREATE TABLE rooms (
    id SERIAL PRIMARY KEY,
    name TEXT,
    visible BOOLEAN
);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    content TEXT,
    user_id INTEGER REFERENCES users(id),
    room_id INTEGER REFERENCES rooms(id),
    sent_at TIMESTAMP,
    visible BOOLEAN
);

CREATE TABLE admins (
    id SERIAL PRIMARY KEY,
    username TEXT REFERENCES users(username)
);

CREATE TABLE info (
    id SERIAL PRIMARY KEY,
    content TEXT,
    user_id INTEGER REFERENCES users(id),
    sent_at TIMESTAMP,
    visible BOOLEAN
);




