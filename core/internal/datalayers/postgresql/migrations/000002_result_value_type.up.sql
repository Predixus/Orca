CREATE TYPE result_type AS ENUM ('struct', 'array', 'value');

ALTER TABLE algorithms ADD IF NOT EXISTS result_type result_type;
