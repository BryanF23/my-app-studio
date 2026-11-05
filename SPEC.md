# App Studio Decisions

The durable agreement between learner and AI. This document records the agreed application decisions, implementation evidence, actual checks, and GitHub results. Explanations and personal learning observations are recorded in [LEARNING.md](LEARNING.md).

## Current Stage

- **Current feature:** APP-003.
- **Status:** APP-001, APP-002, and APP-003 have been implemented and merged into `main`.
- **Next step:** Final documentation review and submission.
- **Implementation marker:** `studio.json` is set to `implemented_through: 3`.

All three lesson pull requests have been merged:

- APP-001: [PR #2](https://github.com/BryanF23/my-app-studio/pull/2)
- APP-002: [PR #4](https://github.com/BryanF23/my-app-studio/pull/4)
- APP-003: [PR #6](https://github.com/BryanF23/my-app-studio/pull/6)

This repository owns application code. Server/proxy changes and production deployment are outside these three local-development lessons.

---

## APP-001 · Branded Homepage

**Scope:** Make the neutral FastAPI homepage express one chosen identity with an original SVG mark, coherent copy, navigation, and shared style tokens. Keep account actions honest about their implementation status at this lesson stage.

| Decision | Agreement |
|---|---|
| Visitor and concrete use situation | Students and independent creators showcasing digital projects, designs, artwork, and creative work. |
| Reused IS117 brand, or name / promise / primary archetype | CreateSpace / A space where creators can showcase their work, share ideas, and get discovered. / The Creator |
| One visible choice and visitor benefit | Dark navy and purple visual identity with a prominent Explore Projects call to action. The prediction was that visitors would understand they could share creative work and feel encouraged to showcase their projects. |
| Own issue / branch / PR | [Issue #1](https://github.com/BryanF23/my-app-studio/issues/1) / `feature/app-001-createspace-homepage` / [PR #2](https://github.com/BryanF23/my-app-studio/pull/2) — merged |

**Keep when:** The agreed identity is visible and usable at desktop and narrow widths; the foundation and APP-001 checks pass at the lesson stage; AI review and the learner's actual check interpretation, browser observation, and keep reason are recorded.

## APP-002 · Signup, Login and Logout

**Scope:** Add browser forms and REST behavior for member signup, login, a private dashboard, and logout backed by SQLite. Reuse the prepared password, JWT, CSRF, and session helpers. Keep data local. New accounts cannot choose their role.

| Decision | Agreement |
|---|---|
| Expected public/private behavior and account flow | Visitors can sign up and log in. Anonymous requests to private resources are rejected; authenticated members can access their dashboard. Logout revokes the server-side session. Expected API behavior: `/api/me` returns 401 before login and 200 after successful login. |
| Valid and rejected cases to demonstrate | Valid signup and login; duplicate username, malformed signup, extra signup fields, incorrect credentials, unauthenticated private request, missing CSRF token, and revoked or expired session. |
| Own issue / branch / PR | [Issue #3](https://github.com/BryanF23/my-app-studio/issues/3) / `feature/app-002-accounts` / [PR #4](https://github.com/BryanF23/my-app-studio/pull/4) — merged |

**Keep when:** The agreed forms and API work; duplicate or invalid signup and incorrect credentials are rejected; passwords are hashed; authentication uses validated, expiring JWTs with protected cookies and CSRF; private requests require a live session; and logout revokes the session. This is not a production-security certification.

## APP-003 · Server-Enforced Roles

**Scope:** Enforce a member/admin permission boundary in the API and browser. Assign roles only through the trusted local terminal command and use current server-side permissions.

| Visitor | Homepage | Member Area | Admin Area/API |
|---|---|---|---|
| Anonymous | Allowed | Login required | Login required |
| Member | Allowed | Allowed | Forbidden |
| Admin | Allowed | Allowed | Allowed |

| Decision | Agreement |
|---|---|
| Intended admin-only result | Only administrators can access the admin webpage and API. Members are denied; anonymous visitors must authenticate. |
| Actual allowed/denied request evidence | Admin accessed `/admin` and `/api/admin`; a regular member was denied; a logged-out visitor was denied access to protected resources. |
| Own issue / branch / PR | [Issue #5](https://github.com/BryanF23/my-app-studio/issues/5) / `app-003-admin-roles` / [PR #6](https://github.com/BryanF23/my-app-studio/pull/6) — merged |

**Keep when:** Direct requests cannot bypass the role boundary, permissions are checked on the server, new signup remains member-only, and cumulative checks pass. Hidden navigation alone is insufficient.

## Evidence

The following records identify the implementation files, personal issues, pull requests, actual test results, and GitHub state. Learner observations and explanations are also documented in `LEARNING.md`.

| Feature | Files / Own Issue / PR | Actual Checks and Learner Observations | Kept / GitHub State |
|---|---|---|---|
| APP-001 | `app/brand.json`, `app/static/logo.svg`, `app/static/site.css`, `app/templates/home.html`; [Issue #1](https://github.com/BryanF23/my-app-studio/issues/1); [PR #2](https://github.com/BryanF23/my-app-studio/pull/2) — merged | At the original APP-001 lesson stage, foundation checks, 2 contract tests, and 2 Chromium journeys passed. In the final cumulative APP-001 rerun, foundation checks reported 96 passed, 2 skipped, and 2 deselected; contracts reported 2 passed; Chromium reported 1 passed and 1 failed. The failure was because the historical APP-001 browser test expected `/signup` to return 404, but the completed APP-002 implementation correctly returned 200. | Learner chose to keep the design. Commit `374435b`. PR #2 merged into `main`. The original APP-001 GitHub Actions checks were recorded as passing. |
| APP-002 | Account implementation, account templates, `app/security.py`, and related application files; [Issue #3](https://github.com/BryanF23/my-app-studio/issues/3); branch `feature/app-002-accounts`; [PR #4](https://github.com/BryanF23/my-app-studio/pull/4) — merged | Foundation: 96 passed, 2 skipped, 2 deselected. APP-002 contracts: 14 passed. Chromium: 2 passed. Black and Pylint passed. Learner reported that signup, login, dashboard access, and logout worked. | Signup, login, private dashboard, and logout implemented. PR #4 merged into `main`. |
| APP-003 | `app/features/roles.py`, `app/security.py`, `app/templates/admin.html`; [Issue #5](https://github.com/BryanF23/my-app-studio/issues/5); branch `app-003-admin-roles`; [PR #6](https://github.com/BryanF23/my-app-studio/pull/6) — merged | Foundation: 96 passed, 2 skipped, 2 deselected. APP-003 contracts: 18 passed. Chromium: 2 passed. Black and Pylint passed. Manual browser checks confirmed admin access, member denial, and anonymous denial. | Server-side role verification kept. PR #6 merged into `main`. Local full APP-003 checks passed. The APP-003 evidence checker reports ready for instructor review. GitHub Actions run: [PR #6 merge workflow](https://github.com/BryanF23/my-app-studio/actions/runs/42092034801). |

## Final Repository

**Completed application repository:** [BryanF23/my-app-studio](https://github.com/BryanF23/my-app-studio)

All three lesson pull requests are merged into `main`. The repository is the requested submission URL; local development and testing were completed without requiring production deployment.

The instructor's reference branches show possible implementations. They do not establish this repository's completion or the learner's own reasoning.