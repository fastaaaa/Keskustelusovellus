CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    content TEXT,
    user_id INTEGER REFERENCES users,
    sent_at TIMESTAMP
);

CREATE TABLE rooms (
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE admins (
    id SERIAL PRIMARY KEY,
    username TEXT
);




