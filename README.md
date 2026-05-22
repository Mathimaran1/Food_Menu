# Food Menu Application

Welcome to the Food Menu Application! This is a simple, easy-to-understand full-stack project built with **React** for the frontend and **FastAPI** (Python) for the backend. 

It allows users to view a restaurant menu, filter items by category (Breakfast, Lunch, Dinner, etc.), and search for specific items using their ID.

---

## Implementation Details

This project is built keeping beginners in mind. The code is stripped down to be as simple as possible.

### The Frontend (React)
- **Location:** `/web` folder
- **Key Concepts Used:** `useState`, `useEffect`, and `axios`.
- **How it works:** 
  - `ListPage.jsx` is the main file. It uses `axios` to fetch data from the Python backend.
  - When you click a category tab (like "Lunch"), it updates the `currentCategory` state and automatically fetches only the lunch items.
  - There is no complicated React Router logic; it's a true Single Page Application!

### The Backend (FastAPI + MongoDB)
- **Location:** `/app` folder
- **Key Concepts Used:** `FastAPI` routes and `pymongo` (MongoDB).
- **How it works:** 
  - `menu_routes.py` contains super simple API endpoints (like `@router.get("/menu")`).
  - It talks to a local MongoDB database to grab the menu items and categories.
  - All database IDs are simple strings (like `"1"`, `"2"`) instead of confusing MongoDB ObjectIds.

---

## How to Run the Project

Follow these simple commands to get the project running on your computer.

### 1. Clone the Repository

First, download the code to your local machine:

```bash
git clone https://github.com/Mathimaran1/Food_Menu.git
cd Food_Menu
```

### 2. Start the Backend (Python/FastAPI)

Open a terminal, go to the `app` folder, install the requirements, and start the Uvicorn server:

```bash
cd app
pip install -r requirements.txt
uvicorn main:app --reload
```
*(This will start the backend API on `http://localhost:8000`)*

**Need sample data?** If your database is empty, you can run the seed script to automatically fill it with delicious Indian food items:
```bash
cd app
python seed.py
```

### 2. Start the Frontend (React)

Open a **new, separate terminal**, go to the `web` folder, and start the React app:

```bash
cd web
npm install
npm run dev
```
*(This will start the frontend website, usually on `http://localhost:5173`)*

---


