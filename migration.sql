CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> 60475f1b93d5

CREATE TABLE book (
    id INTEGER NOT NULL, 
    name VARCHAR, 
    qty INTEGER, 
    PRIMARY KEY (id)
);

INSERT INTO alembic_version (version_num) VALUES ('60475f1b93d5');

-- Running upgrade 60475f1b93d5 -> 536315f7e359

CREATE TABLE user (
    id INTEGER NOT NULL, 
    username VARCHAR, 
    PRIMARY KEY (id)
);

UPDATE alembic_version SET version_num='536315f7e359' WHERE alembic_version.version_num = '60475f1b93d5';

-- Running upgrade 536315f7e359 -> 27795978db45

ALTER TABLE user ADD COLUMN age INTEGER;

UPDATE alembic_version SET version_num='27795978db45' WHERE alembic_version.version_num = '536315f7e359';

