
CREATE TABLE members (
    member_id INT PRIMARY KEY,
    name VARCHAR(100),
    gender VARCHAR(10),
    subscription_id INT
);

CREATE TABLE subscriptions (
    subscription_id INT PRIMARY KEY,
    plan_name VARCHAR(50),
    duration_months INT
);

CREATE TABLE coaches (
    coach_id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE sessions (
    session_id INT PRIMARY KEY,
    member_id INT,
    coach_id INT,
    date DATE
);
