-- 1.Nomes dos filmes da locadora
SELECT f.nome FROM filme f

-- 2.Nome dos clientes que já locaram o filme com nome ‘a lagoa azul’
SELECT DISTINCT c.nome FROM cliente c
JOIN locar l ON c.login = l.login_clientefk
JOIN unidade u ON u.codigo = l.codigo_unidadefk
JOIN filme f ON f.codigo=u.codigo_filmefk
WHERE f.nome='a lagoa azul'

-- 3.Nome dos filmes que possuem unidades com áudio em ‘Português’ ou ‘Inglês’

SELECT distinct f.nome FROM filme f
JOIN unidade u ON u.codigo_filmefk=f.codigo
JOIN possuir_audio pa ON pa.codigo_unidadefk=u.codigo
JOIN idioma i ON pa.codigo_idiomafk=i.codigo
WHERE i.nome='português' OR i.nome='inglês'

-- 4.O nome do(s) filme(s) que o usuário ‘Juliana Santos’ já locou. 
SELECT f.nome FROM filme f
JOIN unidade u ON u.codigo_filmefk=f.codigo
JOIN locar l ON l.codigo_unidadefk=u.codigo
JOIN cliente c ON l.login_clientefk=c.login
where c.nome='Juliana Santos'

-- 5.O nome e o código dos filmes que nunca foram alugados. 
SELECT f.nome,f.codigo from filme f
WHERE
(
    SELECT count(*) from unidade u
    JOIN locar l ON l.codigo_unidadefk=u.codigo
    where u.codigo_filmefk=f.codigo
)=0


-- 6.O nome dos clientes que nunca alugaram filme com legenda em ‘Inglês’. 
SELECT c.nome FROM cliente c
WHERE
(
    SELECT count(*) from unidade u
    JOIN locar l ON l.codigo_unidadefk=u.codigo
    JOIN possuir_legenda pl ON pl.codigo_unidadefk=u.codigo
    JOIN idioma i ON pl.codigo_idiomafk=i.codigo
    WHERE i.nome='inglês' and l.login_clientefk=c.login
)=0

-- 7.O número de unidades que existem na locadora para o filme ‘Titanic’. 
SELECT count(distinct u.codigo) FROM filme f
join unidade u ON u.codigo_filmefk=f.codigo
and f.nome='Titanic'


-- 8.O nome do(s) cliente(s) que locou mais vezes o filme ‘Titanic’

SELECT c.nome as qtd from cliente c
join locar l on l.login_clientefk=c.login
join unidade u on l.codigo_unidadefk=u.codigo
join filme f on u.codigo_filmefk=f.codigo
where f.nome='Titanic'
group by c.nome
having count(*)
=
(SELECT count(*) as qtd from cliente c
join locar l on l.login_clientefk=c.login
join unidade u on l.codigo_unidadefk=u.codigo
join filme f on u.codigo_filmefk=f.codigo
where f.nome='Titanic'
group by c.nome
order by qtd desc limit 1)

-- 9.Nome dos filmes que possuem unidades com áudio em ‘Português’ e ‘Inglês’
-- Utilizando varios joins
SELECT f.nome FROM filme f
JOIN unidade u ON f.codigo=u.codigo_filmefk
JOIN possuir_audio pa1 ON u.codigo=pa1.codigo_unidadefk
JOIN possuir_audio pa2 ON u.codigo=pa2.codigo_unidadefk
JOIN idioma i1 ON pa1.codigo_idiomafk = i1.codigo
JOIN idioma i2 ON pa2.codigo_idiomafk = i2.codigo
WHERE i1.nome='português' and i2.nome='inglês'

-- Utilizando subquery
SELECT f.nome FROM filme f
WHERE 
(
    SELECT count(distinct i.nome) from idioma i
    join possuir_audio pa on pa.codigo_idiomafk=i.codigo
    join unidade u on pa.codigo_unidadefk=u.codigo
    where (i.nome='inglês' or i.nome='português')
    and u.codigo_filmefk = f.codigo
)=2

-- 10.[DESAFIO] Os clientes que assistiram todos os filmes que o cliente de login 'phsb'. 

-- Consulto a quantidade de filmes que cada cliente viu entre os filmes que phsb viu, e depois comparo para ver se essa quantidade equivale
--  a todos os filmes vistos por phsb, se a quantidade é igual, significa que o cliente viu todos os filmes que phsb viu 
SELECT LOGIN FROM
(
    SELECT DISTINCT C.LOGIN, F.CODIGO FROM FILME F
    JOIN UNIDADE U ON U.CODIGO_FILMEFK = F.CODIGO
    JOIN LOCAR L ON L.CODIGO_UNIDADEFK = U.CODIGO
    JOIN CLIENTE C ON L.LOGIN_CLIENTEFK = C.LOGIN
)
    WHERE CODIGO IN 
    (
        SELECT DISTINCT(F.CODIGO) FROM FILME F
        JOIN UNIDADE U ON U.CODIGO_FILMEFK = F.CODIGO
        JOIN LOCAR L ON L.CODIGO_UNIDADEFK = U.CODIGO
        JOIN CLIENTE C ON L.LOGIN_CLIENTEFK = C.LOGIN
        WHERE C.LOGIN = 'phsb'
    )
GROUP BY LOGIN
HAVING COUNT(CODIGO) = 
(
    SELECT COUNT(F.CODIGO) FROM FILME F
    JOIN UNIDADE U ON U.CODIGO_FILMEFK = F.CODIGO
    JOIN LOCAR L ON L.CODIGO_UNIDADEFK = U.CODIGO
    JOIN CLIENTE C ON L.LOGIN_CLIENTEFK = C.LOGIN
    WHERE C.LOGIN = 'phsb'
)