-- Table: comics.information

-- DROP TABLE comics.information;

CREATE TABLE comics.information_backup
(
    id integer NOT NULL DEFAULT nextval('comics.information_id_seq'::regclass),
    cost money,
    title character varying(1000) COLLATE pg_catalog."default",
    "number" character varying(100) COLLATE pg_catalog."default",
    releasedate character varying(250) COLLATE pg_catalog."default",
    CONSTRAINT information_pkey2 PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE comics.information
    OWNER to postgres;

COMMENT ON COLUMN comics.information.releasedate
    IS 'String';