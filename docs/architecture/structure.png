
# Описание сущностей БД

## Пользователи и роли

### 1. users — пользователи

Центральная таблица. Все, кто входит в систему.

**Поля:** `id`, `email`, `password_hash`, `first_name`, `last_name`, `middle_name`, `phone`, `is_active`, `created_at`, `updated_at`.

**Связи:** → roles (M:N через `user_roles`); → teachers / students / parents (1:1).

### 2. roles — роли

Справочник ролей: админ, учитель, ученик, родитель, завуч.

**Поля:** `id`, `code`, `name`, `description`.

**Связи:** → users (M:N через `user_roles`).

### 3. user_roles — связь пользователей и ролей

Нужна, если у пользователя несколько ролей.

**Поля:** `id`, `user_id`, `role_id`, `assigned_at`.

---

## Профили

### 4. teachers — учителя

**Поля:** `id`, `user_id`, `employee_number`, `hire_date`, `is_active`.

**Связи:** → users (1:1); → subjects и classes (M:N через `teacher_subjects`); → grades (1:N).

### 5. students — ученики

**Поля:** `id`, `user_id`, `class_id`, `birth_date`, `enrollment_date`, `is_active`.

**Связи:** → users (1:1); → classes (N:1); → grades, attendance, homework_submissions (1:N); → parents (M:N через `parent_student`).

### 6. parents — родители

**Поля:** `id`, `user_id`, `contact_phone`.

**Связи:** → users (1:1); → students (M:N через `parent_student`).

### 7. parent_student — связь родителей и учеников

Нужна, если у ребёнка несколько родителей и у родителя несколько детей.

**Поля:** `id`, `parent_id`, `student_id`, `relation`.

---

## Учебный процесс

### 8. classes — классы

**Поля:** `id`, `name`, `academic_year`, `head_teacher_id`.

**Связи:** → students (1:N); → schedule (1:N); → teachers (1:1 как классный руководитель).

### 9. subjects — предметы

**Поля:** `id`, `name`, `code`, `is_active`.

**Связи:** → teachers (M:N через `teacher_subjects`); → lessons (1:N).

### 10. teacher_subjects — связь учителей, предметов и классов

Показывает, кто какой предмет ведёт в каком классе.

**Поля:** `id`, `teacher_id`, `subject_id`, `class_id`, `academic_year`.

### 11. schedule — расписание

**Поля:** `id`, `class_id`, `subject_id`, `teacher_id`, `day_of_week`, `lesson_number`, `start_time`, `end_time`, `academic_year`, `is_active`.

**Связи:** → lessons (1:N).

### 12. lessons — уроки

Конкретные уроки по датам.

**Поля:** `id`, `schedule_id`, `class_id`, `subject_id`, `teacher_id`, `lesson_date`, `topic`, `is_conducted`.

**Связи:** → grades, attendance, homework (1:N).

---

## Оценки и посещаемость

### 13. grades — оценки

**Поля:** `id`, `student_id`, `lesson_id`, `subject_id`, `teacher_id`, `value`, `grade_type`, `comment`, `graded_at`.

**Связи:** → students, lessons, teachers (N:1).

### 14. attendance — посещаемость

**Поля:** `id`, `student_id`, `lesson_id`, `status`, `reason`, `marked_by`, `marked_at`.

**Связи:** → students, lessons (N:1).

---

## Домашние задания

### 15. homework — домашние задания

**Поля:** `id`, `lesson_id`, `teacher_id`, `class_id`, `subject_id`, `description`, `due_date`, `attachment_url`, `is_published`, `created_at`.

**Связи:** → homework_submissions (1:N).

### 16. homework_submissions — сдача домашних работ

**Поля:** `id`, `homework_id`, `student_id`, `submitted_at`, `status`, `file_url`, `teacher_comment`.

**Связи:** → homework, students (N:1).

---

## Служебные

### 17. audit_log — журнал действий

**Поля:** `id`, `user_id`, `action`, `entity_type`, `entity_id`, `old_value`, `new_value`, `ip_address`, `created_at`.

**Связи:** → users (N:1).

### 18. notifications — уведомления

**Поля:** `id`, `user_id`, `type`, `title`, `message`, `is_read`, `created_at`.

**Связи:** → users (N:1).

---

## Сводная таблица связей

| Связь | Тип |
| --- | --- |
| users → teachers | 1:1 |
| users → students | 1:1 |
| users → parents | 1:1 |
| users ↔ roles | M:N |
| teachers → classes | 1:N |
| students → classes | N:1 |
| parents ↔ students | M:N |
| teachers ↔ subjects ↔ classes | M:N |
| classes → schedule | 1:N |
| schedule → lessons | 1:N |
| lessons → grades | 1:N |
| lessons → attendance | 1:N |
| lessons → homework | 1:N |
| homework → homework_submissions | 1:N |
| students → grades | 1:N |
| students → attendance | 1:N |
| users → audit_log | 1:N |
| users → notifications | 1:N |
