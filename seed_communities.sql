DROP TABLE IF EXISTS communities;

CREATE TABLE communities (community_id SERIAL PRIMARY KEY, post_id TEXT NOT NULL, post_id VARCHAR(255) NOT NULL, comment_content TEXT NOT NULL);

-- INSERT INTO posts (post_author_id, post_author_id, post_title, post_content) VALUES ('Harry', 'harry@gmail.com', '0000');
-- INSERT INTO posts (post_author_id, post_author_id, post_title, post_content) VALUES ('Ron', 'ron@gmail.com', '0000');
-- INSERT INTO posts (post_author_id, post_author_id, post_title, post_content) VALUES ('Hermione', 'hermione@gmail.com', '0000');
-- INSERT INTO posts (post_author_id, post_author_id, post_title, post_content) VALUES ('Neville', 'Neville@gmail.com', '0000');