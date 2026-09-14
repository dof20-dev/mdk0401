# Описание сущностей БД

## Пользователи

### users — пользователи

Все, кто входит в систему.

**Поля:** `id`, `email`, `password_hash`, `first_name`, `last_name`, `role_id`, `is_active`, `created_at`.

**Связи:** → roles (N:1); → teachers / students / parents (1:1).

### roles — роли

Справочник: админ, учитель, ученик, родитель, завуч.

**Поля:** `id`, `code`, `name`.

**Связи:** → users (1:N).

---

## Профили

### teachers — учителя

**Поля:** `id`, `user_id`, `employee_number`, `hire_date`.

**Связи:** → users (1:1); → lessons (1:N).

### students — ученики

**Поля:** `id`, `user_id`, `class_id`, `parent_id`, `birth_date`.

**Связи:** → users (1:1); → classes (N:1); → parents (N:1); → grades, attendance (1:N).

### parents — родители

**Поля:** `id`, `user_id`, `contact_phone`.

**Связи:** → users (1:1); → students (1:N).

---

## Учебный процесс

### classes — классы

**Поля:** `id`, `name`, `academic_year`, `head_teacher_id`.

**Связи:** → students (1:N); → schedule (1:N).

### subjects — предметы

**Поля:** `id`, `name`, `code`, `is_active`.

**Связи:** → lessons (1:N).

### schedule — расписание

**Поля:** `id`, `class_id`, `subject_id`, `teacher_id`, `day_of_week`, `lesson_number`, `start_time`, `end_time`.

**Связи:** → lessons (1:N).

### lessons — уроки

**Поля:** `id`, `schedule_id`, `class_id`, `subject_id`, `teacher_id`, `lesson_date`, `topic`.

**Связи:** → grades, attendance, homework (1:N).

---

## Оценки и посещаемость

### grades — оценки

**Поля:** `id`, `student_id`, `lesson_id`, `teacher_id`, `value`, `grade_type`, `comment`, `graded_at`.

**Связи:** → students, lessons, teachers (N:1).

### attendance — посещаемость

**Поля:** `id`, `student_id`, `lesson_id`, `status`, `reason`, `marked_by`, `marked_at`.

**Связи:** → students, lessons (N:1).

---

## Домашние задания

### homework — домашние задания

**Поля:** `id`, `lesson_id`, `teacher_id`, `class_id`, `subject_id`, `description`, `due_date`, `is_published`.

**Связи:** → lessons (N:1).

---

## Сводная таблица связей

| Связь | Тип |
| --- | --- |
| users → roles | N:1 |
| users → teachers | 1:1 |
| users → students | 1:1 |
| users → parents | 1:1 |
| parents → students | 1:N |
| students → classes | N:1 |
| classes → schedule | 1:N |
| schedule → lessons | 1:N |
| lessons → grades | 1:N |
| lessons → attendance | 1:N |
| lessons → homework | 1:N |
| students → grades | 1:N |
| students → attendance | 1:N |

