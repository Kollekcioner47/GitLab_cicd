CREATE TABLE IF NOT EXISTS deals (
    id SERIAL PRIMARY KEY,
    client_name VARCHAR(100) NOT NULL,
    amount NUMERIC(10, 2) NOT NULL,
    status VARCHAR(20) DEFAULT 'new'
);
