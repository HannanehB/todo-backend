"# Todo Backend Project" 
### Hannaneh Bargi
### 1400153624151
### تمرین اول مهندسی نرمافزار 1
### استاد تقی نژاد

* کنترل نسخه با Git (Branch و Pull Request)
* پیاده‌سازی API به‌صورت اصولی (CRUD)
* اجرای پروژه داخل Docker
* استفاده از حافظه موقت (In-Memory) به‌جای دیتابیس

### زبان برنامه‌نویسی

* Python

### فریم‌ورک بک‌اند

* **FastAPI**

  * سبک و سریع
  * پشتیبانی خودکار از Swagger

### استقرار

* Docker
* Docker Compose

---

## کنترل نسخه با Git

### 1. ساخت Repository

ابتدا یک repository جدید در GitHub ساخته شد با نام:

todo-backend

سپس پروژه روی سیستم clone شد:

```bash
git clone https://github.com/HannanehB/todo-backend.git
```

---

### 2. Branching Strategy

برای رعایت اصول کنترل نسخه:

* `main` → نسخه نهایی پروژه
* `develop` → توسعه پروژه
* `feature/todo-crud` → پیاده‌سازی قابلیت CRUD

```bash
git checkout -b feature/todo-crud
```

## ساختار پروژه

ساختار نهایی پروژه به شکل زیر است:

```
todo-backend/
├── app/
│   └── main.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

توضیح فایل‌ها:

* `main.py` : کد اصلی بک‌اند
* `requirements.txt` : کتابخانه‌های پایتون
* `Dockerfile` : ساخت image داکر
* `docker-compose.yml` : اجرای سرویس

---

## پیاده‌سازی بک‌اند (main.py)

### 1. ایجاد FastAPI

```python
from fastapi import FastAPI
app = FastAPI()
```

این کد یک سرور API ایجاد می‌کند.

---

### 2. ذخیره‌سازی In-Memory

 از دیتابیس استفاده نشده و داده‌ها در حافظه ذخیره می‌شوند:

```python
tasks = []
task_id_counter = 1
```

 با ری‌استارت شدن برنامه، داده‌ها پاک می‌شوند.

---

### 3. مدل داده (Task)

```python
from pydantic import BaseModel

class Task(BaseModel):
    title: str
    completed: bool = False
```

این مدل مشخص می‌کند هر task چه فیلدهایی دارد.

---

## عملیات CRUD

### 1. Create

```python
@app.post("/tasks")
def create_task(task: Task):
```


---

### 2. Read 

```python
@app.get("/tasks")
def get_tasks():
```


---

### 3. Update 

```python
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
```


---

### 4. Delete 

```python
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
```


---

## Swagger UI 

FastAPI به‌صورت خودکار یک رابط گرافیکی برای تست API تولید می‌کند.

آدرس:

```
http://localhost:8000/docs
```

این صفحه:

* توسط خود FastAPI ساخته می‌شود
* برای تست و مستندسازی API است

---

## Docker و استقرار پروژه

### 1. Dockerfile

Dockerfile مشخص می‌کند پروژه چگونه اجرا شود:

* نصب Python
* نصب کتابخانه‌ها
* اجرای سرور

---

### 2. Docker Compose

با Docker Compose پروژه تنها با یک دستور اجرا می‌شود:

```bash
docker compose up --build
```

پس از اجرا:

```
Uvicorn running on http://0.0.0.0:8000
```

و از مرورگر:

```
http://localhost:8000/docs
```

---

## نحوه کار کلی سیستم (Flow)

1. کاربر درخواست HTTP ارسال می‌کند
2. FastAPI درخواست را دریافت می‌کند
3. عملیات CRUD اجرا می‌شود
4. پاسخ JSON برگردانده می‌شود

---

## جمع‌بندی

در این پروژه:

* یک API بک‌اند کامل پیاده‌سازی شد
* تمام عملیات CRUD انجام شد
* پروژه داخل Docker اجرا شد
* قوانین Git و Pull Request رعایت شد

---

## اجرای پروژه

```bash
docker compose up --build
```

Swagger:

```
http://localhost:8000/docs
```

---

