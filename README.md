# Web_Project_1_Jade_V
final project BLOC_3

# Aurora Fine Arts — Art Rental Platform

## Project Purpose
Aurora Fine Arts is a web platform that lets a local art gallery rent out
original artworks to clients on a monthly basis. Clients can browse the
catalog, view artwork details, and request to rent a piece for a chosen
date range. Admins review incoming requests, manage the catalog (add or
remove artworks), and approve or reject rental requests.

## Client Need
The gallery needed a way to move away from manual, in-person rental
tracking (spreadsheets, phone calls) to a self-serve online system where
clients can browse and request rentals themselves, and staff can manage
everything from a single dashboard.

## Core Features
- **Public catalog** — browse all artworks, filterable by category via
  the "Virtual Gallery" visit page
- **Artwork detail pages** — description, price, dimensions, and a Rent
  button
- **Authentication** — register/login/logout with client-side and
  server-side validation (email format, password strength)
- **Rental workflow** — clients request a rental, admins approve or
  reject it; approved rentals mark the artwork as unavailable
- **Client rental management** — clients can view and cancel their own
  pending requests from "My Rentals"
- **Admin dashboard** — a page combining: pending rental requests
  (approve/reject), an add-artwork form with image upload, and a table to
  manage/delete existing artworks
- **Responsive design** — mobile-friendly layout with a hamburger menu

## Tech Stack
- **Backend:** Python, Flask, Flask-Login, Flask-SQLAlchemy
- **Database:** SQLite
- **Frontend:** Jinja2 templates, vanilla JavaScript, custom CSS
- **Fonts:** Playfair Display, Inter, Quicksand From Google

## Project Structure
Web_Project_1_Jade_V/

- **app.py:**                  # Routes and app configuration

- **models.py:**                # SQLAlchemy models (User, Artwork,Rental)

- **extensions.py:**             # db and login_manager instances

- **seed.py:**                  # Initial data (3 artworks + admin account)

- **requirements.txt:**

- **instance/:**

- **gallery.db:**            # SQLite database (created on first run)

- **templates/:**

- **base.html:**             # Shared layout, nav, flash messages

- **home.html:**              # Public catalog

- **visit.html:**              # Virtual gallery (grouped by category)

- **artwork_detail.html:**      # Single artwork page

- **register.html / login.html:**

- **rent.html:**               # Rental request form

- **my_rentals.html:**          # Client's own rentals

- **admin_dashboard.html:**      # Unified admin panel

- **contact.html:**

- **static/:**

- **css/style.css:**

- **js/script.:**

- **images/:**                # hero, logo, pattern, uploaded artwork,images


## Installation

1. Create and activate a virtual environment:
```bash
   python3 -m venv venv
   source venv/bin/activate
```

2. Install dependencies:
```bash
   pip install -r requirements.txt
```

3. Run the app:
```bash
   python3 app.py
```
   This creates the database tables automatically on first run.

4. Seed the database with sample artworks and an admin account:
```bash
   python3 seed.py
```
   **Run this once only** — running it again will fail with a duplicate
   admin email error.

5. Visit `http://127.0.0.1:5000` in your browser.

## Test Accounts

| Role  | Email                        | Password  |
|-------|-------------------------------|-----------|
| Admin | admin@aurorafinearts.com      | admin123  |

| Role  | Email                        | Password  |
|-------|-------------------------------|-----------|
| Client | client5@google.com.com      | Password.2026  |

Client accounts can be created via the Register page.

## Known Limitations
- `admin_rentals.html` and the standalone `add_artwork.html` page are kept
  in the codebase for reference, but the admin dashboard
  (`/admin/dashboard`) is the intended single entry point for all admin
  tasks.
- The rental request form does not yet check whether the chosen date
  range overlaps with an existing rental for the same artwork — this is
  planned for a future update.
- Original seed artworks (Fractured light, Terra Rossa, Pi) do not have
  `dimensions` set, since this field was added after they were created.

## Author
Jade V. — Web Project 1 (582-32W-VA), Vanier College