USE dbglobalhitss;

create table institution
(
    id           INT NOT NULL AUTO_INCREMENT,
    name         varchar(100) null,
    description  varchar(500) null,
    address      varchar(200) null,
    created_user varchar(100) null,
    created_at   DATETIME      null,
    updated_user varchar(100) null,
    updated_at   DATETIME     null,
    status       varchar(1)   null,
    PRIMARY KEY (id)
)ENGINE=InnoDB CHARACTER SET utf8;

INSERT INTO institution (id, name, description, address, created_user, created_at, updated_user, updated_at, status) VALUES (1, 'Universidad Guayaquil', 'Educacion universitaria', 'Guayaquil - Norte', 'admin', '2023-01-26 18:24:48', null, null, 'A');
INSERT INTO institution (id, name, description, address, created_user, created_at, updated_user, updated_at, status) VALUES (2, 'Universidad Agraria', 'Educacion universitaria', 'Guayaquil - Sur', 'admin', '2023-01-26 18:25:27', null, null, 'A');
INSERT INTO institution (id, name, description, address, created_user, created_at, updated_user, updated_at, status) VALUES (3, 'Ecotec', 'Educacion universitaria', 'Guayaquil - Norte', 'admin', '2023-01-26 18:25:27', null, null, 'A');