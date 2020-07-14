-- change name column to utf8
ALTER TABLE hbtn_0c_0.first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4;
ALTER TABLE hbtn_0c_0.first_table MODIFY name VARCHAR(256) COLLATE utf8mb4_unicode_ci;
