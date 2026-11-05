# Conversation evidence

AI-drafted task summary, not a transcript or grade. It may be public. Use actual short words or labeled paraphrases; disclose help and leave missing responses pending. The learner reviews, corrects or removes new excerpts before commit/push. Accuracy approval is not proof of understanding. Label simulated trials explicitly.

**Available conversation context:** Not recorded yet.

## APP-001

- **Prediction:** “I predict visitors will understand that CreateSpace is a platform for sharing creative work and feel encouraged to showcase their own projects.”

- **Check interpretation:** “I think these browser tests help catch problems that users might experience when viewing the website, such as the homepage not loading correctly or important content not appearing. However, they might miss issues on other devices, accessibility problems, or things that could confuse actual visitors.” (Developed with assistance.)

- **Browser observation:** “I like the clean design and the way the homepage explains what CreateSpace is for. The headline and Explore projects button make the purpose clear.”

- **Keep decision:** “Keep the current design. I like how the homepage communicates CreateSpace's purpose.”

- **Review:** Learner reviewed and approved the APP-001 decisions and evidence summary with AI assistance.

- **Help/gaps:** AI assistance helped develop the brand direction and guide repository setup and documentation. The check interpretation was developed with assistance.

- **Evidence links / next step:** [Issue #1](https://github.com/BryanF23/my-app-studio/issues/1); foundation checks passed, 2 APP-001 contract tests passed, and 2 Chromium browser journeys passed. [PR #2](https://github.com/BryanF23/my-app-studio/pull/2) merged into main; GitHub check and windows jobs passed. Next: final review and close Issue #1.

## APP-002

- **Prediction:** “I predict that if someone tries to access the private dashboard before logging in, they should receive an unauthorized response (401) and should not be able to see the private content. After successfully logging in, the request should be accepted (200), and the user should be able to access their private dashboard.” (Suggested with AI assistance and accepted by learner.)

- **Check interpretation:** “I think this check verifies that users must be logged in to access protected account information. It tests that an unauthenticated user receives a 401 response and that logging out invalidates the previous session so it cannot be reused. This is important because it helps protect private user information and prevents someone from accessing an account without permission.” (Suggested with AI assistance and accepted by learner.)

- **Browser observation:** Learner reported that account creation, login, dashboard access, and logout all worked. After logging out, attempting to access the dashboard again redirected to the login page.

- **Keep decision:** Learner chose to keep the current signup and login experience because the process worked as expected.

- **Review:** Learner reviewed and approved the APP-002 decisions and evidence summary with AI assistance.

- **Help/gaps:** AI assistance helped review the prepared authentication, database, settings, and application code; develop the implementation plan; and draft the check interpretation. Prediction wording was suggested with AI assistance and accepted by learner.

- **Evidence links / next step:** [Issue #3](https://github.com/BryanF23/my-app-studio/issues/3); branch `feature/app-002-accounts`. APP-002 scoped checks and full cumulative checks passed, including 96 foundation tests, 14 contract tests, and 2 Chromium browser journeys. Next: learner review, source review, commit, push, and pull request.

## APP-003

- Prediction: I predicted that a regular member attempting to access an admin-only URL should be denied by the server. (Discussed before implementation.)
- Check interpretation: The initial checks showed that the admin routes were missing because requests returned 404. After implementing the routes and role checks, all APP-003 contract and browser tests passed. I understand that authentication confirms who a user is, while authorization determines what that user can access.
- Browser observation: I tested with an admin account, a regular member account, and a logged-out visitor. The admin could access the admin page and API, the member was denied access, and the logged-out visitor was denied access to protected resources.
- Keep decision: I kept server-side role verification using the current database role so that being logged in alone does not grant administrator access.
- Review: I reviewed `app/features/roles.py`, `app/security.py`, and `app/templates/admin.html` to understand how the API and webpage enforce administrator permissions.