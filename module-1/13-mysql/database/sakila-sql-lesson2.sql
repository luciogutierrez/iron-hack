use sakila;
-------------------------------
Select * 
from film
limit 10
;
-------------------------------
Create table conteo_top_movies
Select 
	f.title, 
    count(r.rental_id) as 'rentas_totales',
    count(distinct(c.customer_id)) as 'customer_totales'
from film f 
	join inventory i on f.film_id = i.film_id
	left join rental r on r.inventory_id=i.inventory_id
	left join customer c on c.customer_id = r.customer_id
group by f.title
order by rentas_totales desc
limit 20
;
-------------------------------
select * from conteo_top_movies
;
SET SQL_SAFE_UPDATES = 0;
DELETE from conteo_top_movies
where rentas_totales<30
;
DROP TABLE conteo_top_movies;
-------------------------------
create table datos_clientes_confidencial
select 
	c.customer_id,
    date_format(c.create_date,'%Y-%m'),
    co.country
from customer c
left join address a on c.address_id = a.address_id
left join city ci on ci.city_id = a.city_id
left join country co on ci.country_id = co.country_id
limit 20
;
-------------------------------
select distinct(country)
from datos_clientes_confidencial
;
DELETE from datos_clientes_confidencial
where country not in ('Japan','United States')
;
select *
from datos_clientes_confidencial
where country = 'Japan'
;
-------------------------------
-- Subqueries
-------------------------------
-- CREATE TABLE monto_por_pelicula
select 
	r_sub.title,
    p.amount,
    sum(p.amount) as monto_total
from
	(select 
		r.rental_id,
		f.title
	from film f
		left join inventory i on f.film_id = i.film_id
		left join rental r on r.inventory_id = i.inventory_id) r_sub
left join payment p on r_sub.rental_id = p.rental_id
group by 1
order by 2 desc
;
select * from
monto_por_pelicula
;
UPDATE monto_por_pelicula
SET monto_total = monto_total *21
;
select * from
monto_por_pelicula
;
-------------------------------
-- Insert
-------------------------------
insert INTO monto_por_pelicula(title, amount, monto_total)
values('El señor de los anillos', 13.5, 3151351)
;
select * from monto_por_pelicula
where title like 'El señor'
;