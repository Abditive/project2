DROP TABLE IF EXISTS comments;

CREATE TABLE comments (comment_id SERIAL PRIMARY KEY, comment_author_id TEXT NOT NULL, comment_content TEXT NOT NULL);

-- INSERT INTO comments (comment_author_id, comment_content , post_content) VALUES ('Harry', 'harry@gmail.com', '0000');
-- INSERT INTO comments (comment_id, comment_author_id, comment_content , post_content) VALUES ('Ron', 'ron@gmail.com', '0000');
