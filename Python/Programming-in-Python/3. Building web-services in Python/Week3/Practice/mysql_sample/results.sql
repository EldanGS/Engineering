use test;
set names utf8;

-- 1. Выбрать все товары (все поля)
SELECT * FROM product;

-- 2. Выбрать названия всех автоматизированных складов
SELECT name FROM store;

-- 3. Посчитать общую сумму в деньгах всех продаж
SELECT sum(total) as total FROM sale;

-- 4. Получить уникальные store_id всех складов, с которых была хоть одна продажа
SELECT DISTINCT(store_id) FROM sale WHERE quantity > 0;

-- 5. Получить уникальные store_id всех складов, с которых не было ни одной продажи
SELECT DISTINCT(store.store_id) FROM store
LEFT JOIN sale on sale.store_id = store.store_id
WHERE quantity is NULL;

-- 6. Получить для каждого товара название и среднюю стоимость единицы товара avg(total/quantity), если товар не продавался, он не попадает в отчет.
SELECT product.name, AVG(sale.total / sale.quantity) average FROM product
NATURAL JOIN sale
GROUP BY product.name;

-- 7. Получить названия всех продуктов, которые продавались только с единственного склада
SELECT product.name FROM product
JOIN sale ON product.product_id = sale.product_id
GROUP BY sale.product_id
HAVING COUNT(DISTINCT(sale.store_id)) = 1;

-- 8. Получить названия всех складов, с которых продавался только один продукт
SELECT store.name FROM STORE
JOIN sale ON store.store_id = sale.store_id
GROUP BY sale.store_id
HAVING COUNT(DISTINCT(sale.product_id)) = 1;

-- 9. Выберите все ряды (все поля) из продаж, в которых сумма продажи (total) максимальна (равна максимальной из всех встречающихся)
SELECT * FROM sale
WHERE total = (SELECT MAX(total) FROM SALE);

-- 10. Выведите дату самых максимальных продаж, если таких дат несколько, то самую раннюю из них
SELECT date FROM sale
GROUP BY date
ORDER BY sum(total) DESC, date
LIMIT 1;