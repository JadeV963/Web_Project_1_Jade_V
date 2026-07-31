# Web Project 1 — Project Plan

## 1. Client Quote Interpretation

**Client:** Aurora Fine Arts, a small independent art gallery.

**Client need:** "We have dozens of original pieces from local artists sitting in
storage. Buying art is expensive, so a lot of potential customers — young
professionals, small business owners, interior decorators — never buy from us.
We want a way for people to rent artwork for a few months at a time instead of
buying it outright, so more people can enjoy original art and we can generate
recurring revenue from pieces that would otherwise just sit in the gallery."

## 2. Target User

Young professionals and small business owners (e.g. office managers, café
owners, interior decorators) who want to display original art in their space
without the upfront cost of buying it outright. They are comfortable ordering
online and expect a simple, visual browsing experience.

## 3. Problem Being Solved

There is no simple platform for renting original artwork the way people rent
furniture or subscribe to a service. Aurora Fine Arts currently manages rental
requests manually by phone and email, which is slow and doesn't scale. This
project provides an online catalog and rental request system so customers can
browse, select, and request artwork rentals directly.

## 4. Project Scope

### Must-have features
- Browse a catalog of available artworks (image, title, artist, monthly rental price)
- View a single artwork's detail page
- User registration and login
- Submit a rental request for an artwork with a start and end date
- View personal rental history ("My Rentals")
- Server-side validation on the rental form (valid dates, artwork availability)

### Optional / stretch features (only after core is complete)
- Filter/search the catalog by category or price
- Cancel a pending rental request
- Simple admin view to mark a rental as confirmed/completed

## 5. Chosen Frontend Track

**Track A — Flask + Jinja templates + JavaScript.**
Most pages are rendered server-side by Flask; JavaScript will be used to
enhance specific interactions (e.g. client-side validation feedback on the
rental form, dynamic availability check).

## 6. Proposed Database Models

**User**
- id (PK)
- name
- email (unique)
- password_hash
- created_at

**Artwork**
- id (PK)
- title
- artist_name
- description
- image_url
- category
- price_per_month
- is_available (boolean)

**Rental**
- id (PK)
- user_id (FK → User)
- artwork_id (FK → Artwork)
- start_date
- end_date
- status (pending / confirmed / completed)
- created_at

### Relationships
- One **User** can have many **Rentals** (1-to-many)
- One **Artwork** can have many **Rentals** over time (1-to-many)
- **Rental** is the join point connecting a User to an Artwork for a specific
  time period

## 7. Proposed Routes / Endpoints

| Route | Method | Purpose |
|---|---|---|
| `/` | GET | Artwork catalog (browse all available artworks) |
| `/artwork/<id>` | GET | Artwork detail page |
| `/rent/<id>` | POST | Submit a rental request for an artwork |
| `/my-rentals` | GET | View the logged-in user's rental history |
| `/register` | GET/POST | Create a new account |
| `/login` | GET/POST | Log in |
| `/logout` | GET | Log out |

## 8. Main User Workflow (Vertical Slice)

Browse catalog → view artwork detail → log in (if not already) → select rental
dates → submit rental request → see confirmation → view it under "My Rentals"

## 9. Initial Task Plan

See the Trello board: https://trello.com/invite/b/6a695fd1b3939959bed3c678/ATTI2b5e989a21401824537c7b8672e08c49F6270FF9/web-project-1-art-rental

## 10. Design Rationale

My design uses a white dark and yellow palette, gallery painting inspired palette(deppe charcoal background cards and ivrory pbtton) to make the artwork itself the visual focus, similar to how pieces are lit against a wall in a gallery. amuted gold accent for primary accent, dust rose tone for flags rental status.

**Color Palette**
- background white : #ffff
- Card Surface : #2C2925
- Primary text : #ffffff
- Muted text. : #594826
- Accent (primary actions): #F9F0C5
- Secondary accent (status badges): #D69A9A. #F9F0C5

**Typography:**
- Headings: Inria Serif
- Body text: Inter

See the FIGMA LINK: https://www.figma.com/design/pRxMSLYv2VnMQgBr9HtHTe/Untitled?node-id=1-2&t=uFXvz79nTU1UPoeA-1