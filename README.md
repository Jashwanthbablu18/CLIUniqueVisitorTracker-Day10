# 🌐 Day 10 - Unique Visitor Tracker (Sets & Frozensets)

Hey there! 👋  
Welcome to **Day 10** of my **#30DaysOfPythonChallenge**. Today’s project is all about tracking **unique data** using `set` and `frozenset` — powerful tools for handling duplicates and immutable collections.

---

## 📌 What’s This About?
Today’s focus: **Sets and Frozensets** in Python — ideal for deduplicating data and capturing immutable records.

---

## 💭 Why Sets & Frozensets?
- `set` helps track unique values like visitor IDs or names.
- `frozenset` creates unchangeable snapshots of data — perfect for archival or logging.
- Set operations (`|`, `&`, `-`) let you compare collections easily.

---

## ✨ Features

Here’s what the app does:
- 👥 Adds daily unique visitors using `set.add()`
- 🧊 Converts each day’s set to a `frozenset` (immutable snapshot)
- 📊 Compares visitor data across days using:
  - `|` Union
  - `&` Intersection
  - `-` Difference
- 🔄 Interactive CLI with input validation

---

## 🛠️ Tech Stuff

Built with:
- 🐍 **Python 3**
- 🔁 `set()` and `frozenset()`
- 🔎 Set operations for data comparison
- 🛡️ Error handling and input validation

---

## 🚀 Getting It Running

### ✅ What You’ll Need
Just Python 3!  
Run the code using:
```bash
python Day-10Code.py
