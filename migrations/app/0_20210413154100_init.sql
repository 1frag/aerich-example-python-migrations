-- upgrade --
CREATE TABLE IF NOT EXISTS "genre" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(200) NOT NULL
);
CREATE TABLE IF NOT EXISTS "music" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(63) NOT NULL UNIQUE,
    "duration" DOUBLE PRECISION NOT NULL,
    "path" VARCHAR(127) NOT NULL UNIQUE,
    "genre_id" INT REFERENCES "genre" ("id") ON DELETE SET NULL
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" JSONB NOT NULL
);
