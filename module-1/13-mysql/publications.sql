SET SQL_SAFE_UPDATES = 0
;
use publications
;
------------------------------
-- Query para crear una tabla
------------------------------
-- create table store_sales_summary
select
    st.stor_id 	as store_id,
    st.stor_name as store,
    count(distinct(ord_num)) as orders,
    count(title_id) as items,
    sum(qty) as qty
from sales s
inner join stores st on s.stor_id = st.stor_id
group by store_id, store
;
------------------------------
-- Query para borrar una tabla
------------------------------
-- drop table store_sales_summary
;
------------------------------
-- Query para consultar registros de una tabla
------------------------------
select *
from store_sales_summary
;
------------------------------
-- Query para eliminar registros de una tabla
------------------------------
/*
delete 
from store_sales_summary
where qty<80
*/
;
------------------------------
-- Query para eliminar todos los registros de una tabla
------------------------------
/*
delete 
from store_sales_summary
;
*/
------------------------------
-- Query para insertar registro en una tabla
------------------------------
-- insert into store_sales_summary
select
    st.stor_id 	as store_id,
    st.stor_name as store,
    count(distinct(ord_num)) as orders,
    count(title_id) as items,
    sum(qty) as qty
from sales s
inner join stores st on s.stor_id = st.stor_id
group by store_id, store
;
------------------------------
-- Query para modificar registros en una tabla
------------------------------
update store_sales_summary
set qty = qty + 5
;

------------------------------
-- SUBCONSULTAS Y TABLAS TEMPORALES
------------------------------
-- Ventas por tienda
select 
    st.stor_name as store,
    count(distinct(ord_num)) as orders,
    count(title_id) as items,
    sum(qty) as qty
from sales s
inner join stores st on s.stor_id = st.stor_id
group by store
;
-- Número de articulos por pedido
select 
    store, 
    items/orders as avgitems,
    qty/items as avgqty
from    
	(select 
		st.stor_name as store,
		count(distinct(ord_num)) as orders,
		count(title_id) as items,
		sum(qty) as qty
	from sales s
	inner join stores st on s.stor_id = st.stor_id
	group by store) as summary
;
-- Ventas por titulo pra las tiendas que promediaron más de un articulo por pedido
select 
    store,
    ord_num,
    ord_date,
    title,
    sl.qty,
    price,
    type
from    
	(select 
        st.stor_id as store_id,
		st.stor_name as store,
		count(distinct(ord_num)) as orders,
		count(title_id) as items,
		sum(qty) as qty
	from sales s
	inner join stores st on s.stor_id = st.stor_id
	group by store
    ) as sm
inner join sales sl on sm.store_id = sl.stor_id
inner join titles t on sl.title_id = t.title_id
where items/orders > 1
;
-- realizando el mismo query con una tabla temporal
create temporary table store_sales_summary_temp
select 
	st.stor_id as store_id,
	st.stor_name as store,
	count(distinct(ord_num)) as orders,
	count(title_id) as items,
	sum(qty) as qty
from sales s
inner join stores st on s.stor_id = st.stor_id
group by store
;
-- consultando la tabla temporal
select * from store_sales_summary_temp
;
-- sustituyendo el subquery por la tabla temporal
select 
    store,
    ord_num,
    ord_date,
    title,
    sl.qty,
    price,
    type
from store_sales_summary_temp sm
inner join sales sl on sm.store_id = sl.stor_id
inner join titles t on sl.title_id = t.title_id
where items/orders > 1
;
    

