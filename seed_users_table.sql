DROP TABLE IF EXISTS users;

CREATE TABLE users (user_id SERIAL PRIMARY KEY, user_name TEXT NOT NULL, user_email VARCHAR(255) NOT NULL, user_password TEXT NOT NULL);

INSERT INTO users (user_name, user_email, user_password) VALUES ('Harry', 'harry@gmail.com', '$2b$12$/sqi7WgpcbJ.aD0gBv2//u9HiZ3PDTBv9NXvhsbVtF8snuNhomotu');
INSERT INTO users (user_name, user_email, user_password) VALUES ('Ron', 'ron@gmail.com', '$2b$12$/sqi7WgpcbJ.aD0gBv2//u9HiZ3PDTBv9NXvhsbVtF8snuNhomotu');
INSERT INTO users (user_name, user_email, user_password) VALUES ('Hermione', 'hermione@gmail.com', '$2b$12$/sqi7WgpcbJ.aD0gBv2//u9HiZ3PDTBv9NXvhsbVtF8snuNhomotu');
INSERT INTO users (user_name, user_email, user_password) VALUES ('Neville', 'Neville@gmail.com', '$2b$12$/sqi7WgpcbJ.aD0gBv2//u9HiZ3PDTBv9NXvhsbVtF8snuNhomotu');