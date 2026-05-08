create table if not exists Users(
    pk_id integer primary key,
    username text unique,
    display_name text,
    first_name text,
    last_name text,
    phone_number text,
    secret_hash text,
    password_hash text
);