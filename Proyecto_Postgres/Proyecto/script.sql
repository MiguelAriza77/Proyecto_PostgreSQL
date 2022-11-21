DROP DATABASE "bd_users";
CREATE DATABASE "bd_users5";
\l
\c bd_users
CREATE TABLE _users_5 (
    id_user SERIAL PRIMARY KEY,
    name_user VARCHAR(30) NOT NULL,
    lastname_user VARCHAR(30) NOT NULL,
    numberuser INT NOT NULL,
    age__user INT NOT NULL 
);
\dt

