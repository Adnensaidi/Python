SELECT * FROM users ;
INSERT INTO users (first_name,last_name,email) VALUES ("ali","ben","ali@gmail.com"),("massoud","benmassoud","massoud@gmail.com"),("dhaw","bendhaw","dhaw@gmail.com");
SELECT * FROM users WHERE email="ali@gmail.com" ; 
SELECT * FROM users WHERE id = 3 ; 
UPDATE users SET last_name = "pancakes" WHERE id=3 ;
DELETE FROM users WHERE id = 2 ;
SELECT first_name FROM users ORDER BY first_name;
booksbooks