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

