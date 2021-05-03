/* seleccionando todo lo de la tabla actor*/
select * from actor limit 20;

select actor_id, last_name, last_update 
  from actor 
 where first_name like 'm%'
 order by first_name desc
;
-- conteo actores viaje a las vegas
 select last_name, count(actor_id) cantidad
   from actor 
  group by last_name
 having cantidad > 1
  order by cantidad desc, last_name asc
;
-- la tabla de arriba es la left y la de abajo right
select * 
  from staff s
  left join address a
    on s.address_id = a.address_id
;
select s.first_name, s.last_name, sum(p.amount) suma
  from staff s
  left join payment p
    on s.staff_id = p.staff_id
  where month(p.payment_date)=8
     and year(p.payment_date)=2005
  group by s.first_name, s.last_name
;  

select 
	c.first_name,
	c.last_name,
    c.email,
    c3.country
  from customer c
  left join address a
    on c.address_id = a.address_id
  left join city c2
    on c2.city_id= a.city_id
  left join country c3
    on c3.country_id = c2.country_id
  ;

/*
 De cada categoria de pelicula su revenu (amount)
*/
select * from category limit 10;
select * from payment limit 10;
select * from rental limit 10;

select c.name,
    sum(ifnull(p.amount,0)) total_amount
  from category c
  left join film_category fc
    on c.category_id = fc.category_id
  left join film f
    on f.film_id = fc.film_id
  left join inventory i
    on i.film_id = f.film_id
  left join rental r
    on r.inventory_id = i.inventory_id
  left join payment p
    on p.rental_id = r.rental_id
  group by c.name
  order by total_amount asc
 ;    
  

  
  