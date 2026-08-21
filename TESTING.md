# Testing Checklist — Aurora Fine Arts

## Authentication
-  Register with valid credentials → account created, redirected to login
-  Register with invalid email, weak password, or duplicate email → error shown
-  Login with correct/incorrect credentials → redirects correctly, error on failure
-  Logout → redirected to home with confirmation

## Client — Browsing & Renting
-  Catalog displays all artworks with correct availability status
-  Rented artworks appear shaded, admin does not see Rent button
-  Rental request with invalid dates blocked (JS + server)
-  Successful rental → artwork marked unavailable, appears in My Rentals
-  Client can cancel their own pending rental (not others', not confirmed ones)

## Admin — Dashboard
-  Non-admin blocked from /admin/dashboard
-  Approve/Reject rental requests work correctly
-  Add Artwork form creates artwork with image upload
-  Delete artwork removes it and any associated rentals cleanly

## Responsive Design
-  Mobile view shows hamburger menu, catalog/detail/dashboard layouts stack correctly

## Known Gaps
- No automated/unit tests — all testing done manually via the browser
- Date-range overlap checking on rental requests not yet implemented