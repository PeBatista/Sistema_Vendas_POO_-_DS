/*
Temos um script de exibição de dependências: com o script de exibição, utldtree.sql,
mostrando dentro de DEPTREE_TEMPTAB é onde são armazenadas as
estruturas de dependências e seus objetos contidos no usuário de Banco de Dados Oracle. 
*/

execute DEPTREE_FILL('table','nome_de_seu_servidor_ORA','t_produto_vendido');
select nested_level,schema,type,name,seq# from deptree order by SEQ#;
-- TABELA DEPTREE, é automaticamente atualizada, quando usamos a PROCEDURE deptree_fill