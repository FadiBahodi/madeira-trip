# Publish online (GitHub Pages)

Goal: host this folder as a simple static site so your friend can open:
- `index.html` (landing page)
- `madeira_map.html` (interactive map)
- `itinerary.html` (markdown-rendered itinerary)

## 1) Create a new GitHub repo
On GitHub, create a new repository (recommended: **public** so your friend can view without logging in).

Example repo name: `madeira-trip-2026`

## 2) Push this folder to GitHub
From a terminal:

```bash
cd /Users/rawproductivity/Desktop/IDLE\ GEMINI/madeira_trip

git init
git add .
git commit -m "Madeira trip map + itinerary"

# replace with your repo URL from GitHub
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

If `git commit` complains about missing name/email, set them once:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

## 3) Turn on GitHub Pages
In the GitHub repo:
- **Settings → Pages**
- **Build and deployment → Source:** “Deploy from a branch”
- **Branch:** `main`
- **Folder:** `/ (root)`
- Save

Wait ~1–3 minutes. Your site URL will be shown there.

## 4) Share with your friend
Share the GitHub Pages URL, and tell them to open:
- `/` (landing page)
- `/madeira_map.html` (map)
- `/itinerary.html` (itinerary)

## Optional: preview locally before publishing
```bash
cd /Users/rawproductivity/Desktop/IDLE\ GEMINI/madeira_trip
python3 -m http.server 8000
```
Then open `http://localhost:8000/`.

