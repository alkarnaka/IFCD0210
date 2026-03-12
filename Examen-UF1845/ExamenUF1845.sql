-- 1. Obtener el nombre y precio de venta de todos los productos.

select p.nombre, p.precio_venta  from producto p 


-- 2. Mostrar los clientes que pertenecen a España.(no especifica que datos de los clientes piden)

select * from cliente c
where c.pais = "Spain"


-- 3. Mostrar los productos ordenados por precio de venta de mayor a menor.(no especifica que datos de los clientes piden)

select p.nombre, p.precio_venta  from producto p 
order by p.precio_venta desc


-- 4. Mostrar el nombre del cliente y el código de los pedidos que ha realizado.

SELECT p.codigo_pedido , c.nombre_cliente  fROM  cliente c 
join pedido p 
order by c.codigo_cliente 

-- 5. Mostrar el nombre del cliente, el código del pedido y el nombre del producto comprado.

SELECT p.codigo_pedido , c.nombre_cliente, pro.nombre  fROM  cliente c 
join pedido p 
join producto pro
order by c.codigo_cliente


-- 6. Contar cuántos clientes hay registrados en la base de datos.

select count(c.codigo_cliente) as Conteo from cliente c 


-- 7. Calcular el precio medio de venta de los productos.

select avg(p.precio_venta) as Precio_medio from producto p 


-- 8. Mostrar cuántos productos hay en cada gama de productos.

select count(*) as conteo_producto, p.gama  from producto p
group by p.gama


-- 9. Actualizar el teléfono del cliente con código 10 a '600123456'.

update cliente c set telefono = 600123456
where c.codigo_cliente = 10


-- 10. Eliminar los pagos realizados antes del 1 de enero de 2005.

INSERT INTO Pago (Fecha_Pago, codigo_cliente, forma_pago, id_transaccion, total)
VALUES ('2004-12-15', 1, 'Transferencia','ak-std-666666', 66666);   


delete from pago WHERE fecha_pago < '2005-01-01'