-- Tabla universidad
CREATE TABLE university (
    id_university VARCHAR PRIMARY KEY,
    name VARCHAR NOT NULL,
    city VARCHAR,
    type VARCHAR
);
-- INSERT de universidad
INSERT INTO university (id_university, name, city, type)
VALUES ('001', 'Universidad Central', 'Quito', 'Pública');

-- Tabla estudiante
CREATE TABLE student (
    id_student VARCHAR PRIMARY KEY,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    email VARCHAR UNIQUE NOT NULL,
    password VARCHAR NOT NULL,
    registration_date TIMESTAMP,
    university_id VARCHAR REFERENCES university(id_university)
);

-- Tabla moderador
CREATE TABLE university_moderator (
    id_moderator VARCHAR PRIMARY KEY,
    name VARCHAR NOT NULL,
    email VARCHAR UNIQUE NOT NULL,
    password VARCHAR NOT NULL,
    university_id VARCHAR REFERENCES university(id_university)
);

-- Tabla publicaciones
CREATE TABLE post (
    id_post VARCHAR PRIMARY KEY,
    title VARCHAR NOT NULL,
    content TEXT NOT NULL,
    post_date TIMESTAMP WITH TIME ZONE DEFAULT now(),
    student_id VARCHAR REFERENCES student(id_student)
);

-- Tabla comentarios
CREATE TABLE comment (
    id_comment VARCHAR PRIMARY KEY,
    content TEXT NOT NULL,
    comment_date TIMESTAMP WITH TIME ZONE DEFAULT now(),
    post_id VARCHAR REFERENCES post(id_post),
    student_id VARCHAR REFERENCES student(id_student)
);

-- Tabla votos
CREATE TABLE post_vote (
    id_vote VARCHAR PRIMARY KEY,
    student_id VARCHAR REFERENCES student(id_student),
    post_id VARCHAR REFERENCES post(id_post),
    vote_type VARCHAR CHECK (vote_type IN ('upvote', 'downvote')),
    vote_date TIMESTAMP WITH TIME ZONE DEFAULT now()
);

-- Tabla para notificaciones

CREATE TABLE notifications (
    id SERIAL PRIMARY KEY,
    recipient VARCHAR(255) NOT NULL,
    subject VARCHAR(255) NOT NULL,
    message TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

--Tabla para moderacion
CREATE TABLE moderation_report (
    id_report VARCHAR PRIMARY KEY,
    content_type VARCHAR NOT NULL,         -- 'post' o 'comment'
    content_id VARCHAR NOT NULL,           -- id del post o comment
    reason TEXT NOT NULL,
    status VARCHAR DEFAULT 'PENDING',      -- 'PENDING', 'APPROVED', 'REJECTED'
    reported_by VARCHAR NOT NULL,          -- id del estudiante o moderador que reporta
    reviewed_by VARCHAR,                   -- id del moderador que revisa
    report_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    resolution_date TIMESTAMP
);

--Tabla para TAGS
CREATE TABLE tag (
    id_tag VARCHAR PRIMARY KEY,
    name VARCHAR UNIQUE NOT NULL
);

--Tabla para asociar etiquetas a las publicaciones

CREATE TABLE post_tag (
    id_post VARCHAR NOT NULL,
    id_tag VARCHAR NOT NULL,
    PRIMARY KEY (id_post, id_tag)
);
--Tabla para historial de publicaciones

CREATE TABLE post_history (
    id_history VARCHAR PRIMARY KEY,
    post_id VARCHAR NOT NULL,
    title VARCHAR NOT NULL,
    content TEXT NOT NULL,
    edited_by VARCHAR NOT NULL,
    edited_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

--Tabla para asignaturas
CREATE TABLE course (
    id_course VARCHAR PRIMARY KEY,
    name VARCHAR NOT NULL,
    description VARCHAR,
    university_id VARCHAR NOT NULL
);

--Tabla para inscripciones
CREATE TABLE enrollment (
    id_enrollment VARCHAR PRIMARY KEY,
    student_id VARCHAR NOT NULL,
    course_id VARCHAR NOT NULL,
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

--Tabla forum-link
CREATE TABLE course_forum_link (
    id_link VARCHAR PRIMARY KEY,
    course_id VARCHAR NOT NULL,
    forum_id VARCHAR NOT NULL
);
