SELECT * from users;
SELECT * from books;
SELECT * from favorites;



INSERT into users (first_name, last_name) VALUES ("Jane", "Amsden"), ("Emily", "Dixon"), ("Theodore", "Dostoevsky"), ("William", "Shapiro"), ("Lao", "Xiu");


INSERT into books (title, num_of_pages) VALUES ("C Sharp", 200), ("Java", 300), ("Python", 100), ("PHP", 500), ("Ruby", 150);



UPDATE books SET title = "C#" WHERE title = "C Sharp";



UPDATE users SET first_name = "Bill" WHERE id = 4;


INSERT into favorites (user_id, book_id) VALUES(1, 1), (1, 2) ;
INSERT into favorites (user_id, book_id) VALUES (2, 1), (2, 2), (2, 3) ;
INSERT into favorites (user_id, book_id) VALUES(3, 1), (3, 2), (3, 3), (3, 4) ;
INSERT into favorites (user_id, book_id) VALUES(4, 1),(4, 2), (4, 3), (4, 4), (4,5);
-- Retrieve all the users who favorited the 3rd book
SELECT name FROM users
JOIN favorites ON users.id = user_id
JOIN books ON favorites.book_id = books.id
WHERE books.id = 3;


DELETE from favorites where book_id = 3 AND user_id = 1;


INSERT into favorites (user_id, book_id)  VALUES (5, 2);

SELECT books.title FROM books
JOIN favorites ON books.id = favorites.book_id WHERE favorites.user_id = 3;


SELECT name from users
JOIN favorites on users.id = favorites.user_id
WHERE favorites.book_id = 5;