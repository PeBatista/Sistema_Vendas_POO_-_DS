-- Gerado por Oracle SQL Developer Data Modeler 22.2.0.165.1149
--   em:        2023-06-09 23:21:56 BRT
--   site:      Oracle Database 11g
--   tipo:      Oracle Database 11g



DROP TABLE t_cliente CASCADE CONSTRAINTS;

DROP TABLE t_compra CASCADE CONSTRAINTS;

DROP TABLE t_contato_cliente_virtual CASCADE CONSTRAINTS;

DROP TABLE t_contato_fornecedor CASCADE CONSTRAINTS;

DROP TABLE t_contato_funcionario CASCADE CONSTRAINTS;

DROP TABLE t_fornecedor CASCADE CONSTRAINTS;

DROP TABLE t_funcionario CASCADE CONSTRAINTS;

DROP TABLE t_produto CASCADE CONSTRAINTS;

DROP TABLE t_produto_vendido CASCADE CONSTRAINTS;

-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE t_cliente (
    cd_cliente                    NUMBER(6) NOT NULL,
    nm_cliente                    VARCHAR2(100),
    ds_tipo_cliente_virtual       VARCHAR2(100),
    ds_rg_cliente                 VARCHAR2(20),
    ds_senha_cliente_virtual      VARCHAR2(30),
    ds_cpf_cnpj_cliente           VARCHAR2(20),
    dt_nascimento_cliente_virtual DATE,
    fl_cli_fis_vir                CHAR(1) NOT NULL
);

COMMENT ON COLUMN t_cliente.cd_cliente IS
    'C�digo do cliente Fis�co';

COMMENT ON COLUMN t_cliente.nm_cliente IS
    'Nome do Cliente Fis�co';

COMMENT ON COLUMN t_cliente.ds_tipo_cliente_virtual IS
    'Tipo de pessoa do Cliente Virtual';

COMMENT ON COLUMN t_cliente.ds_rg_cliente IS
    'RG do Cliente';

COMMENT ON COLUMN t_cliente.ds_senha_cliente_virtual IS
    'Senha do Cliente';

COMMENT ON COLUMN t_cliente.ds_cpf_cnpj_cliente IS
    'CPF ou CNPJ do cliente Virtual';

COMMENT ON COLUMN t_cliente.dt_nascimento_cliente_virtual IS
    'Data de Nascimento do Cliente';

COMMENT ON COLUMN t_cliente.fl_cli_fis_vir IS
    'Cliente  F�sico ou Virtual';

ALTER TABLE t_cliente ADD CONSTRAINT pk_cliente_fisico PRIMARY KEY ( cd_cliente );

CREATE TABLE t_compra (
    cd_compra         NUMBER(6) NOT NULL,
    cd_funcionario    NUMBER(6) NOT NULL,
    cd_cliente        NUMBER(6) NOT NULL,
    dt_hora_compra    DATE NOT NULL,
    sg_status_entrega CHAR(1),
    dt_data_entrega   DATE,
    ob_observacao     VARCHAR2(100),
    vl_desconto       NUMBER(8, 2),
    vl_frete          NUMBER(8, 2),
    fl_compra_fis_vir CHAR(1) NOT NULL
);

COMMENT ON COLUMN t_compra.cd_compra IS
    'C�digo de compra fis�ca';

COMMENT ON COLUMN t_compra.dt_hora_compra IS
    'Data e Hora da compra';

COMMENT ON COLUMN t_compra.sg_status_entrega IS
    'Entregue S/N';

COMMENT ON COLUMN t_compra.dt_data_entrega IS
    'Data de entrega do Produto';

COMMENT ON COLUMN t_compra.ob_observacao IS
    'Observa��o da Compra';

COMMENT ON COLUMN t_compra.vl_desconto IS
    'Desconto Aplicado no Produto';

COMMENT ON COLUMN t_compra.vl_frete IS
    'Frete Aplicado no Produto';

COMMENT ON COLUMN t_compra.fl_compra_fis_vir IS
    'Compra Feita Fisicamente ou Virtualmente';

ALTER TABLE t_compra ADD CONSTRAINT pk_compra_fisico PRIMARY KEY ( cd_compra );

CREATE TABLE t_contato_cliente_virtual (
    cd_contato_cliente_virtual     NUMBER(10) NOT NULL,
    cd_cliente                     NUMBER(6) NOT NULL,
    ds_endereco_cliente_virtual    VARCHAR2(100) NOT NULL,
    ds_bairro_cliente_virtual      VARCHAR2(100) NOT NULL,
    ds_complemento_cliente_virtual VARCHAR2(100) NOT NULL,
    ds_estado_cliente_virtual      VARCHAR2(100) NOT NULL,
    ds_cdde_cliente_virtual        VARCHAR2(100) NOT NULL,
    ds_cel_cliente_virtual         VARCHAR2(15) NOT NULL,
    ds_cep_cliente_virtual         VARCHAR2(13) NOT NULL
);

COMMENT ON COLUMN t_contato_cliente_virtual.cd_contato_cliente_virtual IS
    'C�digo de contato do Cliente Virtual';

CREATE UNIQUE INDEX t_contato_cliente_virtual__idx ON
    t_contato_cliente_virtual (
        cd_cliente
    ASC );

ALTER TABLE t_contato_cliente_virtual ADD CONSTRAINT pk_contato_cliente PRIMARY KEY ( cd_contato_cliente_virtual );

CREATE TABLE t_contato_fornecedor (
    cd_contato_fornecedor         NUMBER(6) NOT NULL,
    cd_fornecedor                 NUMBER(6) NOT NULL,
    ds_telefone_fornecedor        VARCHAR2(15),
    ds_cel_fornecedor             VARCHAR2(15) NOT NULL,
    ds_endereco_moradia_empresa VARCHAR2(100) NOT NULL
);

COMMENT ON COLUMN t_contato_fornecedor.cd_contato_fornecedor IS
    'C�digo de Contato do Fornecedor';

CREATE UNIQUE INDEX t_contato_fornecedor__idx ON
    t_contato_fornecedor (
        cd_fornecedor
    ASC );

ALTER TABLE t_contato_fornecedor ADD CONSTRAINT pk_contato_fornecedor PRIMARY KEY ( cd_contato_fornecedor );

CREATE TABLE t_contato_funcionario (
    cd_contato_funcionario     NUMBER(6) NOT NULL,
    cd_funcionario             NUMBER(6) NOT NULL,
    ds_endereco_funcionario    VARCHAR2(100) NOT NULL,
    ds_bairro_funcionario      VARCHAR2(100) NOT NULL,
    ds_complemento_funcionario VARCHAR2(100) NOT NULL,
    ds_estado_funcionario      VARCHAR2(100) NOT NULL,
    ds_cdde_funcionario        VARCHAR2(100) NOT NULL,
    ds_cel_funcionario         VARCHAR2(15) NOT NULL,
    ds_cep_funcionario         VARCHAR2(13) NOT NULL
);

COMMENT ON COLUMN t_contato_funcionario.cd_contato_funcionario IS
    'C�digo do Contato do funcion�rio';

CREATE UNIQUE INDEX t_contato_funcionario__idx ON
    t_contato_funcionario (
        cd_funcionario
    ASC );

ALTER TABLE t_contato_funcionario ADD CONSTRAINT pk_contato_funcionario PRIMARY KEY ( cd_contato_funcionario );

CREATE TABLE t_fornecedor (
    cd_fornecedor          NUMBER(6) NOT NULL,
    nm_fornecedor          VARCHAR2(100) NOT NULL,
    ds_cpf_fornecedor      VARCHAR2(14) NOT NULL,
    ds_rg_fornecedor       VARCHAR2(20) NOT NULL,
    sg_genero_fornecedor   CHAR(1) NOT NULL,
    dt_cadastro_fornecedor DATE NOT NULL
);

COMMENT ON COLUMN t_fornecedor.cd_fornecedor IS
    'C�digo do Fornecedor ';

COMMENT ON COLUMN t_fornecedor.nm_fornecedor IS
    'Nome do Fornecedor';

COMMENT ON COLUMN t_fornecedor.ds_cpf_fornecedor IS
    'CPF do Fornecedor ';

COMMENT ON COLUMN t_fornecedor.ds_rg_fornecedor IS
    'RG do Fornecedor ';

COMMENT ON COLUMN t_fornecedor.sg_genero_fornecedor IS
    'G�nero do Fornecedor';

COMMENT ON COLUMN t_fornecedor.dt_cadastro_fornecedor IS
    'Data de cadastro do Fornecedor';

ALTER TABLE t_fornecedor ADD CONSTRAINT pk_fornecedor PRIMARY KEY ( cd_fornecedor );

CREATE TABLE t_funcionario (
    cd_funcionario        NUMBER(6) NOT NULL,
    nm_funcionario        VARCHAR2(100) NOT NULL,
    ds_cargo_funcionario  VARCHAR2(100) NOT NULL,
    ds_cpf_funcionario    VARCHAR2(14) NOT NULL,
    ds_rg_funcionario     VARCHAR2(20) NOT NULL,
    dt_nascimento         DATE NOT NULL,
    dt_cadastro           DATE NOT NULL,
    sg_genero_funcionario CHAR(1) NOT NULL
);

COMMENT ON COLUMN t_funcionario.cd_funcionario IS
    'C�digo do Funcion�rio';

COMMENT ON COLUMN t_funcionario.nm_funcionario IS
    'Nome do Funcion�rio';

COMMENT ON COLUMN t_funcionario.ds_cargo_funcionario IS
    'Cargo da Funcionario - Vendedor e Transportador';

COMMENT ON COLUMN t_funcionario.ds_cpf_funcionario IS
    'CPF do Funcion�rio';

COMMENT ON COLUMN t_funcionario.ds_rg_funcionario IS
    'RG do Funcion�rio';

COMMENT ON COLUMN t_funcionario.dt_nascimento IS
    'Data de Nacimento do Funcion�rio';

COMMENT ON COLUMN t_funcionario.dt_cadastro IS
    'Data do Cadastro deste Funcion�rio';

COMMENT ON COLUMN t_funcionario.sg_genero_funcionario IS
    'Sigla do G�nero do Funcion�rio';

ALTER TABLE t_funcionario ADD CONSTRAINT pk_funcionario PRIMARY KEY ( cd_funcionario );

CREATE TABLE t_produto (
    cd_produto    NUMBER(10) NOT NULL,
    cd_fornecedor NUMBER(6) NOT NULL,
    nm_produto    VARCHAR2(100) NOT NULL,
    ds_produto    VARCHAR2(300),
    vl_preco      NUMBER(9, 2) NOT NULL,
    ds_ativo      CHAR(1) NOT NULL,
    ds_fabricante VARCHAR2(100) NOT NULL,
    ds_grupo      VARCHAR2(100) NOT NULL,
    nr_estoque    NUMBER(8) NOT NULL
);

COMMENT ON COLUMN t_produto.cd_produto IS
    'C�digo do Produto ';

COMMENT ON COLUMN t_produto.nm_produto IS
    'Nome do Produto';

COMMENT ON COLUMN t_produto.ds_produto IS
    'Descri��o do Produtio';

COMMENT ON COLUMN t_produto.vl_preco IS
    'Pre�o do Custo do Produto';

COMMENT ON COLUMN t_produto.ds_ativo IS
    'Ativo do Produto,(S ou N)';

COMMENT ON COLUMN t_produto.ds_fabricante IS
    'Fabricante do Produto';

COMMENT ON COLUMN t_produto.ds_grupo IS
    'Descri��o do Grupo do Produto';

COMMENT ON COLUMN t_produto.nr_estoque IS
    'Quantidade de Estoque do Produto';

ALTER TABLE t_produto ADD CONSTRAINT pk_produto PRIMARY KEY ( cd_produto );

CREATE TABLE t_produto_vendido (
    cd_produto    NUMBER(10) NOT NULL,
    cd_compra     NUMBER(6) NOT NULL,
    ds_quantidade NUMBER(5)
);

COMMENT ON COLUMN t_produto_vendido.ds_quantidade IS
    'Quantidade de Produto Vendido Fis�camente';

ALTER TABLE t_produto_vendido ADD CONSTRAINT pk_produto_vendido_fisico PRIMARY KEY ( cd_compra,
                                                                                     cd_produto );

ALTER TABLE t_contato_cliente_virtual
    ADD CONSTRAINT fk_cli_cli_virt FOREIGN KEY ( cd_cliente )
        REFERENCES t_cliente ( cd_cliente );

ALTER TABLE t_compra
    ADD CONSTRAINT fk_cliente_compra FOREIGN KEY ( cd_cliente )
        REFERENCES t_cliente ( cd_cliente );

ALTER TABLE t_produto_vendido
    ADD CONSTRAINT fk_comp_fisi_prod FOREIGN KEY ( cd_compra )
        REFERENCES t_compra ( cd_compra );

ALTER TABLE t_contato_funcionario
    ADD CONSTRAINT fk_contato_funcionario FOREIGN KEY ( cd_funcionario )
        REFERENCES t_funcionario ( cd_funcionario );

ALTER TABLE t_produto
    ADD CONSTRAINT fk_forn_prod FOREIGN KEY ( cd_fornecedor )
        REFERENCES t_fornecedor ( cd_fornecedor );

ALTER TABLE t_compra
    ADD CONSTRAINT fk_funcio_compra FOREIGN KEY ( cd_funcionario )
        REFERENCES t_funcionario ( cd_funcionario );

ALTER TABLE t_produto_vendido
    ADD CONSTRAINT fk_prod_comp_fisiv1 FOREIGN KEY ( cd_produto )
        REFERENCES t_produto ( cd_produto );

ALTER TABLE t_contato_fornecedor
    ADD CONSTRAINT relation_5 FOREIGN KEY ( cd_fornecedor )
        REFERENCES t_fornecedor ( cd_fornecedor );



-- Relat�rio do Resumo do Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                             9
-- CREATE INDEX                             3
-- ALTER TABLE                             17
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
