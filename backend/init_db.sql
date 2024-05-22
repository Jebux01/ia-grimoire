CREATE SCHEMA magic_school AUTHORIZATION postgres;

CREATE TABLE magic_school.requests (
	id SERIAL PRIMARY KEY,
	nombre varchar NOT NULL,
	apellido varchar NOT NULL,
	identificacion varchar NOT NULL,
	edad integer NOT NULL,
	afinidad_magica varchar NOT NULL,
	estado_solicitud varchar NOT NULL default 'pendiente',
	created_at timestamp default current_timestamp,
	update_at timestamp default current_timestamp,
	deleted_at timestamp
);

CREATE TABLE magic_school.grimoires (
	id SERIAL PRIMARY KEY,
	nombre varchar NOT NULL,
	autor varchar NOT NULL,
	idioma varchar NOT NULL,
	estado varchar default 'disponible',
	tipo varchar NOT NULL,
	created_at timestamp default current_timestamp,
	update_at timestamp default current_timestamp,
	deleted_at timestamp
);

CREATE TABLE magic_school.magicians (
	id SERIAL PRIMARY KEY,
	nombre varchar NOT NULL,
	apellido varchar NOT NULL,
	identificacion varchar NOT NULL,
	edad integer NOT NULL,
	afinidad_magica varchar NOT NULL,
	grimorio_id INTEGER REFERENCES magic_school.grimoires(id),
	created_at timestamp default current_timestamp,
	update_at timestamp default current_timestamp,
	deleted_at timestamp
);