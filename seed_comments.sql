DROP TABLE IF EXISTS comments;

CREATE TABLE comments (comment_id SERIAL PRIMARY KEY, comment_author_id INTEGER, comment_content TEXT NOT NULL);

INSERT INTO comments (comment_author_id, comment_content ) VALUES (1, 'hey');
-- INSERT INTO comments (comment_id, comment_author_id, comment_content , post_content) VALUES ('Ron', 'ron@gmail.com', '0000');
