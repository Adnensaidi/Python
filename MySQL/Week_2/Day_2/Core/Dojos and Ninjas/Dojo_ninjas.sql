SELECT * FROM dojos;

INSERT INTO dojos (name) VALUES("Group1"), ("Group2"), ("Group3");
DELETE FROM dojos WHERE id > 0;
INSERT INTO dojos (name) VALUES ("Group4"), ("Group5"), ("Group6") ;



SELECT * FROM ninjas;

INSERT INTO ninjas (first_name, last_name, age,dojo_id) VALUES ("Adnen","Saidi",30,40),("Ali","Ben",31,40),("Samir","rhouma",32,40) ; 
INSERT INTO ninjas (first_name, last_name, age,dojo_id) VALUES ("Abdallah","Salami",33,41),("Adel","Badri",34,41),("Sami","rayes",35,41);
INSERT INTO ninjas (first_name, last_name, age,dojo_id) VALUES ("Abir","Salemli",36,42),("Atef","Baji",37,42),("Sawssen","raji",38,42);

SELECT * FROM ninjas WHERE dojo_id = 40 ;
SELECT * FROM ninjas WHERE dojo_id = 48 ;
SELECT * FROM ninjas ORDER BY id DESC limit 1 ;  



SELECT ninjas.id, ninjas.first_name, ninjas.last_name, ninjas.age, ninjas.create_at, ninjas.update_at, ninjas.dojo_id, dojos.id, dojos.name, dojos.created_at, dojos.updated_at
from ninjas 
JOIN dojos ON ninjas.dojo_id = dojos.id
WHERE ninjas.id = 39;
SELECT ninjas.id, ninjas.first_name, ninjas.last_name, ninjas.age, ninjas.create_at, ninjas.update_at, ninjas.dojo_id, dojos.id, dojos.name, dojos.created_at, dojos.updated_at
FROM ninjas
JOIN dojos ON ninjas.dojo_id = dojos.id;






 
