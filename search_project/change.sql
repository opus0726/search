ALTER TABLE book_book RENAME TO search_app_book;
ALTER TABLE book_like RENAME TO search_app_like;
ALTER TABLE book_review RENAME TO search_app_review;
UPDATE django_content_type SET app_label='search_app' WHERE app_label='book';
UPDATE django_migrations SET app='search_app' WHERE app='book';