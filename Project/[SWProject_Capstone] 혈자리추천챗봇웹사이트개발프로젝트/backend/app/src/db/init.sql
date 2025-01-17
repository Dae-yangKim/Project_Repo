-- Role 설정
CREATE ROLE myuser WITH LOGIN PASSWORD '1234';
ALTER ROLE myuser CREATEDB;

-- DB 생성
CREATE DATABASE capstoneDB;
GRANT ALL PRIVILEGES ON DATABASE capstoneDB TO myuser;

-- select DB
\c project_db;

-- vector extension을 가져온다.
CREATE EXTENSION IF NOT EXISTS vector;

-- 테이블 생성
CREATE TABLE documents
(
    id SERIAL PRIMARY KEY ,
    embedding vector(400) ,
    create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);