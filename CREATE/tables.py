from base import Database

def create_courses():
       query = f""" 
       CREATE TABLE courses (
             course_id SERIAL PRIMARY KEY,
             course_name VARCHAR(55),
             description TEXT,
             price INT,
             last_update TIMESTAMP DEFAULT NOW ())"""
       data = Database.connect("localhost", "online_oquv_kurs", "postgres", "azizbek", query)
       print(data)


def create_instructors():
    query = f""" 
       CREATE TABLE instructors(
             instructor_id SERIAL PRIMARY KEY,
             instructor_name VARCHAR(25),
             email VARCHAR(25),
             last_update TIMESTAMP DEFAULT NOW ())"""
    data = Database.connect("localhost", "online_oquv_kurs", "postgres", "azizbek", query)
    print(data)

def create_students():
    query = f""" 
       CREATE TABLE students(
             student_id SERIAL PRIMARY KEY,
             student_name VARCHAR(255),
             email VARCHAR(25),
             last_update TIMESTAMP DEFAULT NOW ())"""
    data = Database.connect("localhost", "online_oquv_kurs", "postgres", "azizbek", query)
    print(data)

def create_categories ():
    query = f""" 
       CREATE TABLE categories (
             category_id SERIAL PRIMARY KEY,
             category_name VARCHAR(25),
             last_update TIMESTAMP DEFAULT NOW ())"""
    data = Database.connect("localhost", "online_oquv_kurs", "postgres", "azizbek", query)
    print(data)

def create_enrollments():
    query = f""" 
       CREATE TABLE enrollments(
             enrollments_id SERIAL PRIMARY KEY,
             student_id INT,
             course_id INT,
              enrollment_date DATE,
             last_update TIMESTAMP DEFAULT NOW ())"""
    data = Database.connect("localhost", "online_oquv_kurs", "postgres", "azizbek", query)
    print(data)


def create_reviews ():
    query = f""" 
       CREATE TABLE reviews (
             reviews_id SERIAL PRIMARY KEY,
             student_id INT,
             course_id INT,
             rating INT,
             review_text TEXT,
             review_date DATE,
             last_update TIMESTAMP DEFAULT NOW ())"""
    data = Database.connect("localhost", "online_oquv_kurs", "postgres", "azizbek", query)
    print(data)


def create_course_materials ():
    query = f""" 
       CREATE TABLE course_materials (
             material_id SERIAL PRIMARY KEY,
             course_id INT,
             material_name VARCHAR(25),
             material_type VARCHAR(50),
             file_url VARCHAR(25),
             last_update TIMESTAMP DEFAULT NOW ())"""
    data = Database.connect("localhost", "online_oquv_kurs", "postgres", "azizbek", query)
    print(data)

def create_quizzes():
    query = f""" 
       CREATE TABLE quizzes(
             quiz_id SERIAL PRIMARY KEY,
             course_id INT,
             quiz_name VARCHAR(25),
             total_questions INT,
             duration_minutes INT,
             last_update TIMESTAMP DEFAULT NOW ())"""
    data = Database.connect("localhost", "online_oquv_kurs", "postgres", "azizbek", query)
    print(data)


def create_quiz_questions():
    query = f""" 
       CREATE TABLE quiz_questions(
             question_id SERIAL PRIMARY KEY,
             quiz_id INT,
             question_text TEXT,
             correct_answer TEXT,
             last_update TIMESTAMP DEFAULT NOW ())"""
    data = Database.connect("localhost", "online_oquv_kurs", "postgres", "azizbek", query)
    print(data)

def create_quiz_attempts ():
    query = f""" 
       CREATE TABLE quiz_attempts (
             attempt_id SERIAL PRIMARY KEY,
             student_id INT ,
             quiz_id INT,
             score INT,
             attempt_date DATE,
             last_update TIMESTAMP DEFAULT NOW ())"""
    data = Database.connect("localhost", "online_oquv_kurs", "postgres", "azizbek", query)
    print(data)

def create_discussions():
    query = f""" 
       CREATE TABLE discussions (
             discussions_id SERIAL PRIMARY KEY,
             student_id INT ,
             course_id INT,
             discussion_text TEXT,
             discussion_date DATE,
             last_update TIMESTAMP DEFAULT NOW ())"""
    data = Database.connect("localhost", "online_oquv_kurs", "postgres", "azizbek", query)
    print(data)

def create_messages():
    query = f""" 
       CREATE TABLE discussions (
             message_id SERIAL PRIMARY KEY,
             sender_id INT,
             receiver_id INT,
              message_text TEXT,
              message_date DATE,
             last_update TIMESTAMP DEFAULT NOW ())"""
    data = Database.connect("localhost", "online_oquv_kurs", "postgres", "azizbek", query)
    print(data)

def create_user_roles():
    query = f""" 
       CREATE TABLE user_roles (
             role_id SERIAL PRIMARY KEY,
             role_name VARCHAR(50),
             last_update TIMESTAMP DEFAULT NOW ())"""
    data = Database.connect("localhost", "online_oquv_kurs", "postgres", "azizbek", query)
    print(data)


def create_user_accounts():
    query = f""" 
       CREATE TABLE user_accounts(
              user_id SERIAL PRIMARY KEY,
              username VARCHAR(50),
              password VARCHAR(25),
              email VARCHAR(25),
              role_id INT,
             last_update TIMESTAMP DEFAULT NOW ())"""
    data = Database.connect("localhost", "online_oquv_kurs", "postgres", "azizbek", query)
    print(data)

if __name__ == "__main__":
    create_user_accounts()


















def create_notifications():
    query = f""" 
       CREATE TABLE notifications (
             notification_id SERIAL PRIMARY KEY,
             user_id INT,
             notification_text TEXT,
             notification_date DATE,
             last_update TIMESTAMP DEFAULT NOW ())"""
    data = Database.connect("localhost", "online_oquv_kurs", "postgres", "azizbek", query)
    print(data)

if __name__ == "__main__":
    create_messages()