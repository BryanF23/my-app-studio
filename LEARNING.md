# Conversation Evidence

This document summarizes the learner's decisions, predictions, check interpretations, browser observations, and review of the three App Studio lessons. AI assistance was used during implementation and documentation. The learner should keep only statements that accurately reflect their own experience and understanding.

## APP-001 — Branded Homepage

- **Prediction:** I predicted visitors would understand that CreateSpace is a platform for sharing creative work and feel encouraged to showcase their own projects.

- **Check interpretation:** I think these browser tests help catch problems users might experience when viewing the website, such as the homepage not loading correctly or important content not appearing. However, they might miss issues on other devices, accessibility problems, or things that could confuse actual visitors. (Developed with AI assistance.)

- **Browser observation:** I liked the clean design and the way the homepage explains what CreateSpace is for. The headline and Explore Projects button make the purpose clear.

- **Keep decision:** I chose to keep the current design because I liked how the homepage communicates CreateSpace's purpose.

- **Review:** I reviewed the APP-001 decisions and evidence summary with AI assistance.

- **Help/gaps:** AI assistance helped develop the brand direction, guide repository setup, and prepare documentation. The check interpretation was developed with assistance.

- **Evidence links:** [Issue #1](https://github.com/BryanF23/my-app-studio/issues/1); [PR #2](https://github.com/BryanF23/my-app-studio/pull/2) merged into `main`. At the original APP-001 lesson stage, the foundation checks, 2 contract tests, and 2 Chromium browser journeys passed. During the final cumulative APP-001 rerun, one historical browser assertion failed because `/signup` returned 200 after APP-002 implemented signup. The other Chromium journey passed.

## APP-002 — Signup, Login and Logout

- **Prediction:** I predicted that if someone tries to access the private dashboard before logging in, they should receive an unauthorized response (401) and should not be able to see private content. After successfully logging in, the request should be accepted (200), and the user should be able to access their private dashboard. (Suggested with AI assistance and accepted by the learner.)

- **Check interpretation:** I think this check verifies that users must be logged in to access protected account information. It tests that an unauthenticated user receives a 401 response and that logging out invalidates the previous session so it cannot be reused. This is important because it helps protect private user information and prevents someone from accessing an account without permission. (Suggested with AI assistance and accepted by the learner.)

- **Browser observation:** I reported that account creation, login, dashboard access, and logout all worked. After logging out, attempting to access the dashboard again redirected to the login page.

- **Keep decision:** I chose to keep the current signup and login experience because the process worked as expected.

- **Review:** I reviewed the APP-002 decisions and implementation evidence with AI assistance.

- **Help/gaps:** AI assistance helped review the prepared authentication, database, settings, and application code; develop the implementation plan; and draft the check interpretation. The prediction wording was suggested with AI assistance and accepted by the learner.

- **Evidence links:** [Issue #3](https://github.com/BryanF23/my-app-studio/issues/3); branch `feature/app-002-accounts`; [PR #4](https://github.com/BryanF23/my-app-studio/pull/4) merged into `main`. APP-002 checks passed, including 96 foundation tests, 14 contract tests, and 2 Chromium browser journeys. Black and Pylint passed.

## APP-003 — Server-Enforced Roles

- **Prediction:** I predicted that a regular member attempting to access an admin-only URL should be denied by the server. (Discussed before implementation.)

- **Check interpretation:** The initial checks showed that the admin routes were missing because requests returned 404. After implementing the routes and role checks, all APP-003 contract and browser tests passed. I understand that authentication confirms who a user is, while authorization determines what that user can access.

- **Browser observation:** I tested with an admin account, a regular member account, and a logged-out visitor. The admin could access the admin page and API, the member was denied access, and the logged-out visitor was denied access to protected resources.

- **Keep decision:** I kept server-side role verification using the current database role so that being logged in alone does not grant administrator access.

- **Review:** I reviewed `app/features/roles.py`, `app/security.py`, and `app/templates/admin.html` to understand how the API and webpage enforce administrator permissions.

- **Help/gaps:** AI assistance helped implement and review the role-protection feature and prepare the evidence summary. The learner performed the reported browser checks and reviewed the relevant files.

- **Evidence links:** [Issue #5](https://github.com/BryanF23/my-app-studio/issues/5); branch `app-003-admin-roles`; [PR #6](https://github.com/BryanF23/my-app-studio/pull/6) merged into `main`. Full APP-003 local checks passed, including 96 foundation tests, 18 contract tests, and 2 Chromium browser journeys. Black and Pylint passed. The APP-003 evidence checker reported that evidence was ready for instructor review.

## Overall Reflection

I completed the three App Studio lessons in order. I built the CreateSpace homepage, implemented account registration and authentication, and added server-enforced administrator permissions.

The work was completed in separate lesson branches and merged into `main` through three pull requests. I used the prepared local checks and Chromium browser tests to evaluate the application. AI assistance supported implementation, troubleshooting, and documentation, while the predictions, decisions, and browser observations were reviewed as part of the learning process.

**Repository:** [BryanF23/my-app-studio](https://github.com/BryanF23/my-app-studio)