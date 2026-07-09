CREATE TABLE users(
    id INTEGER PRIMARY KEY,
    username VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    role VARCHAR(50)
);

CREATE TABLE trainings(
    id INTEGER PRIMARY KEY,
    title VARCHAR(100),
    trainer_name VARCHAR(100),
    technology VARCHAR(100),
    duration VARCHAR(50),
    start_date DATE,
    end_date DATE,
    status VARCHAR(50)
);

CREATE TABLE enrollments(
    id INTEGER PRIMARY KEY,
    employee_id INTEGER,
    training_id INTEGER,
    enrollment_date DATE,
    completion_status VARCHAR(50)
);

CREATE TABLE certificates(
    id INTEGER PRIMARY KEY,
    employee_id INTEGER,
    training_id INTEGER,
    certificate_id VARCHAR(100) UNIQUE,
    issued_date DATE,
    expiry_date DATE
);
