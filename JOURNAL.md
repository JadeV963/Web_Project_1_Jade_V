# Daily Journal -Web project 1

## Week 1

### Monday, July 27

**Accomplished:**
Attended the project kickoff session — covered course expectations, reviewed
the project constraints (Flask backend, limited scope, required vertical
workflow). Brainstormed a project idea: an artwork rental website.

**Challenges faced:**
Difficulty pinning down the exact scope to stay within the required limits
(1 primary model, 1 secondary model, 5-8 routes) without overbuilding.

**Next step:**
Create the GitHub repository, define the fictional client and target user,
start drafting the scope for Thursday's Deliverable 1.



### Tuesday, July 28

**Accompli :**
Created the GitHub repository and cloned it locally. Wrote the initial
PROJECT_PLAN.md covering the client interpretation, target user, project
scope, database models, and proposed routes for the artwork rental site. Set
up the Trello board (Backlog, To-Do, In-progress, Testing, Done, and User
Stories) and populated it with initial tasks and user stories.

**Challenges faced:**
Accidentally started cloning the new repo inside an old project folder, which
would have created nested git directories — caught it before cloning and
fixed the local path. Also had to re-clarify project scope limits while
writing the database models to avoid overbuilding.

**Next step:**

Finalize the Figma design (desktop and mobile layouts) and write the short
design rationale before Thursday's Deliverable 1 presentation.

### Wednesday, July 29

**Accomplished:**
Continued building the Figma file — progressed from low-fidelity
wireframes to medium and high-fidelity versions for the catalog, artwork
detail, and gallery screens, including desktop and mobile layouts.

**Challenges faced:**
Balancing how much detail to put into each fidelity stage without spending
too much time refining early wireframes that would change anyway.

**Next step::**
Finalize the color palette and typography choices,  write the design
rationale, and prepare for Thursday's Deliverable 1 presentation.

## Week 2
### Tuesday, August 4

**Accomplished:**
Set up a Python virtual environment and installed Flask, Flask-SQLAlchemy, and
Flask-Login. Built a minimal Flask app and confirmed it runs correctly in the
browser. Created the initial database models (User, Artwork, Rental)

**Challenges faced**
Ran into a circular import error between app.py and models.py, since each
file was trying to import from the other.

**Next step:**
Get the app running successfully with all models created in the database,
then start building the first real route (the artwork catalog page) backed
by real database content.

### Wednesday, August 5
Debugged and fixed a circular import between app.py and models.py by moving
the db object into a separate extensions.py file. Added the Artwork model to
the database and confirmed it displays real data on the catalog route. Built
full authentication: /register (with password hashing and duplicate-email
validation), /login (with password verification via Flask-Login), and
/logout (protected with @login_required). Fixed a missing SECRET_KEY
RuntimeError that was blocking login sessions. Diagnosed a Chrome-specific
403 error (confirmed unrelated to the app by testing successfully in Safari).

**Challenges faced:**
Several blocking bugs: a route defined after app.run() , a typo (== instead of =)
, a missing SECRET_KEY needed for Flask-Login sessions,
and had perimission errors with Chrome. used Safari instead.

**Next step:**
Prepare the data flow diagram, and presentation.

### Thursday, August 6

**Accomplished:**
Presented Deliverable 2 to the class 
application: database models (User, Artwork, Rental), full authentication
(register, login, logout with password hashing and Flask-Login), the artwork catalog reading real data from the database, and the artwork User and Artwork.

**Challenges faced:**
Received feedback: the project was missing an admin-only route to review and approve rental requests.

**Next step:**
Add an admin approval workflow (a route restricted to admin users that lists pending rentals and lets them be approved), and add client-side JavaScript validation for the rental date form as a first step toward more interactive features.

### Sunday, August 9
**Accomplished:**
Added an admin-only approval workflow, linked client-side JavaScript form validation, and fixed base.html which was empty and blocking all Jinja template inheritance. 
Also improved the rental logic so an artwork's availability is set to false once a rental request is submitted, preventing duplicate requests for the same piece. 
Added the last missing route, /my-rentals, so clients can check the status of their
requests. 
Connected the artwork catalog page with clickable links to each
artwork's detail page, and configured Flask-Login to redirect unauthenticated
users to the login page (with a link to register)

**Challenges faced:**
Several small bugs compounded during testing  with browser. tried to manage with Safari instead of Google Chrome.

**Next step:**
Do a final full walkthrough of the entire user journey (browse → view →
rent → admin approve → my-rentals shows confirmed) before the next
deliverable.


### Monday, August 10

**Accomplished:**
Added a full CSS stylesheet matching the Figma design direction, including a
responsive nav for mobile screens. Fixed a broken UX flow where register and
login returned plain confirmation text with no navigation — both now
redirect properly (register → login → catalog).

**Challenges faced:**
Register and login originally returned raw text with no way to continue
navigating the site — realized this broke the whole user flow, not just a
cosmetic issue.

**Next step:**
Verify the interface substantially matches the
Figma design across all pages, test responsive layout on a narrow viewport,
and do a full walkthrough of error and success states.

### Tuesday, August 11

**Accomplished:**
Added artwork cards and status badges (Available/Not available,
Pending/Confirmed) across the catalog, artwork detail, and my-rentals pages.
Added client-side JavaScript validation for email format and password length
on the register/login forms.

**Challenges faced:**
bowser bugs again with chrome.

**Next step:**
Finalize the style in rent.html and admin_rentals.html

### Thursday, August 13

**Accomplished:**
Fixed login.html. Verified my_rentals.html was
already correctly structured. Added a responsive catalog grid (3 columns
desktop 2 columns mobile) and a mobile hamburger menu that toggles the nav
links on narrow screens. Reviewed the CRUD coverage of the project (Create/Read/
Update present, Delete missing) and identified a known limitation where the
admin approve route uses GET instead of POST both noted for a future fix.

**Challenges faced:**

organized file so the responsive
behavior stays predictable

**Next step:**
Add a delete/cancel workflow to complete full CRUD coverage, and change the
admin approve route from GET to a POST-protected action, before the next
deliverable.

### Monday, August 17

**Accomplished:**
Work by reworking the visual design of the site, changed the palette to: charcoal background, quartz pink accents, beige border details. Keep consistent typography system across all pages. Built out the home page hero section with a background image, heading, and an "Enter" button leading to a new virtual gallery page that groups artworks by category ("rooms").

**Challenges faced:**
Hit a database integrity error when deleting an artwork that still had rental records pointing to it, which required deleting the related rentals first.

**Next step:**
Continue improving visual consistency across remaining pages, and follow up

### Tuesday, August 18

**Accomplished:**
Added image upload functionality for artworks using Flask's request.files and secure_filename, so admins can attach real photos when adding new pieces through the form. Added a description field to the Artwork model and displayed it on the artwork detail page alongside the price and two action
buttons (Rent and View Collection). Added an admin-only DELETE feature for artworks, including cleanup of any related rental records to avoid database integrity errors. Artworks that are rented now appear shaded/grayed out in the catalog instead of disappearing, so users can still see what exists.

**Challenges faced:**
Ran into repeated issues with the Flask development server not being restarted after code or database changes, leading to confusing errors that looked like bugs but were actually stale server state. 

**Next step:**
fix the  GET/POST issue on the admin approve route, write a README with project purpose, installation instructions, and environment setup, complete a test checklist covering the
main workflows, review accessibility (form labels, color contrast), and finish the remaining unstyled pages (login, my-rentals, admin views) to match the design system.

### Wednesday, August 19

**Accomplished:**
Added a full delete workflow for artworks (admin-only), including cleanup
of related rental records before deletion to avoid a database integrity
error.
Redesigned the CSS color palette with quartz pink accents and a warmer charcoal background.
Built a unified admin dashboard combining pending rental approvals, an
add-artwork form with image upload, and a table to manage/delete existing
artworks. Fixed the admin approve route to use POST instead of GET.
Styled all remaining form pages to match the site's design system. Added
a dimensions field to artworks. Wrote the project README, generated
requirements.txt, and created a testing checklist.

**Challenges faced:**
Ran into a database integrity error when deleting an artwork still linked
to rental records — had to delete the rentals first. Also had a table
where the header and data rows didn't match in column count.

**Next step:**
Improve the rental flow based on professor feedback: the user should be
notified immediately whether their chosen date range is available before
the request goes to the admin for approval, rather than finding out only
after submitting. Also prevent users from selecting a past date when
requesting a rental. verify color contrast, improve the overall visual design
to feel more like an art gallery, and do a final review before submitting
the Feature-Complete Beta.



