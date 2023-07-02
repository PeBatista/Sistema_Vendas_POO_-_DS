cREATE SEQUENCE seq_cliente
	START WITH 1
	INCREMENT BY 1
	 NOCACHE
	NOCYCLE;
-- Sequência para o cd_cliente_virtual, onde teremos um AUTO_INCREMENT.
CREATE SEQUENCE seq_compra  
	START WITH 1 
	INCREMENT BY 1
	NOCACHE
	NOCYCLE;
-- Sequência para o cd_compra_fisico, onde teremos um AUTO_INCREMENT.
CREATE SEQUENCE seq_compra_virtual   
	START WITH 1 
	INCREMENT BY 1
	NOCACHE
	NOCYCLE;
-- Sequência para o cd_compra_virtual, onde teremos um AUTO_INCREMENT.
CREATE SEQUENCE seq_contato_cliente_virtual       
	START WITH 1 
	INCREMENT BY 1
	NOCACHE
	NOCYCLE;
-- Sequência para o cd_contato_cliente_virtual, onde teremos um AUTO_INCREMENT.
CREATE SEQUENCE seq_contato_fornecedor      
	START WITH 1 
	INCREMENT BY 1
	NOCACHE
	NOCYCLE;
-- Sequência para o cd_contato_fornecedor, onde teremos um AUTO_INCREMENT. 
CREATE SEQUENCE seq_contato_funcionario      
	START WITH 1 
	INCREMENT BY 1
	NOCACHE
	NOCYCLE;

CREATE SEQUENCE seq_funcionario     
	START WITH 1 
	INCREMENT BY 1
	NOCACHE
	NOCYCLE;
-- Sequência para o cd_contato_funcionario, onde teremos um AUTO_INCREMENT.
CREATE SEQUENCE seq_fornecedor       
	START WITH 1 
	INCREMENT BY 1
	NOCACHE
	NOCYCLE;
-- Sequência para o cd_fornecedor, onde teremos um AUTO_INCREMENT.

CREATE SEQUENCE seq_produto
	START WITH 1
	INCREMENT BY 1
	 NOCACHE
	NOCYCLE;

--SEQUÊNCIAS PARA CADA TIPO DE TABELA E SEUS CÓDIGOS
CREATE SEQUENCE seq_cliente_virtual
	START WITH 1
	INCREMENT BY 1
	 NOCACHE
	NOCYCLE;