# App Studio decisions

The durable agreement between learner and AI. Update only agreed decisions and actual evidence; pending is a valid state. Keep explanations/help in [LEARNING.md](LEARNING.md), not a second copy here.

## Current stage

- **Current feature:** APP-001.
- **Status:** APP-001 CreateSpace homepage implemented; full APP-001 checks passed. Learner review and final GitHub workflow remain in progress.
- **Next step:** Finish learner evidence review, verify the implementation marker, and complete the APP-001 commit and pull request.
- **Implementation marker:** `studio.json` is set to `implemented_through: 1` after the APP-001 checks passed.

This repository owns application code. Server/proxy changes and production deployment are outside these three local-development lessons. Prepared helpers are reusable foundations, not evidence that unfinished routes are implemented.

## APP-001 · Branded homepage

**Scope:** make the neutral FastAPI homepage express one chosen identity with a simple original SVG mark, coherent copy, navigation and shared style tokens. Keep account actions honest about their unfinished state.

| Decision | Agreement |
|---|---|
| Visitor and concrete use situation | Students and independent creators showcasing digital projects, designs, artwork, and creative work |
| Reused IS117 brand, or name / promise / primary archetype | CreateSpace / A space where creators can showcase their work, share ideas, and get discovered. / The Creator |
| One visible choice and visitor benefit | Dark navy and purple visual identity with a prominent Explore projects call to action; predicts visitors will understand they can share creative work and feel encouraged to showcase their own projects. |
| Own issue / branch / PR | [Issue #1](https://github.com/BryanF23/my-app-studio/issues/1) / `feature/app-001-createspace-homepage` / PR pending |

**Keep when:** the agreed identity is visible and usable at desktop/narrow widths; full foundation + APP-001 checks pass; AI review and the learner's actual check interpretation/browser observation/keep reason are recorded; reviewed evidence and verified GitHub state are linked below.

## APP-002 · Signup, login and logout

**Scope:** add browser forms and REST behavior for member signup, login, a private dashboard and logout backed by SQLite. Reuse the prepared password/JWT/CSRF/session helpers; keep data local. New accounts cannot choose their role.

| Decision | Agreement |
|---|---|
| Expected public/private behavior and account flow | Pending |
| Valid and rejected cases to demonstrate | Pending |
| Own issue / branch / PR | Pending |

**Keep when:** the agreed forms/API work; duplicate/invalid signup and wrong credentials are rejected; passwords are hashed; authentication uses validated, expiring JWTs with protected cookies and CSRF; private requests require a live session and logout revokes it. Full cumulative checks, AI review, actual learner contributions and GitHub state are recorded. This is not a production-security certification.

## APP-003 · Server-enforced roles

**Scope:** enforce a small member/admin boundary in the API and browser. Assign roles only through the trusted local terminal command; use current server-side permissions, including for an existing session after a role change.

| Visitor | Homepage | Member area | Admin area/API |
|---|---|---|---|
| Anonymous | Allowed | Login required | Login required |
| Member | Allowed | Allowed | Forbidden |
| Admin | Allowed | Allowed | Allowed |

| Decision | Agreement |
|---|---|
| Intended admin-only result | Pending |
| Actual allowed/denied request evidence | Pending |
| Own issue / branch / PR | Pending |

**Keep when:** a direct request cannot bypass the role boundary, role changes take effect as specified, new signup remains member-only, and full cumulative checks plus AI review pass. Link the learner's actual interpretation/observation, reviewed record and verified GitHub result. Hidden navigation alone is insufficient.

## Evidence

Link actual files/checks and the student's own issues/PRs. No fabricated URLs, customer research or claims that a timestamp proves learning.

| Feature | Files / own issue / PR | Actual checks and learner observations | Kept / GitHub state |
|---|---|---|---|
| APP-001 | `app/brand.json`, `app/static/logo.svg`, `app/static/site.css`, `app/templates/home.html`; [Issue #1](https://github.com/BryanF23/my-app-studio/issues/1); PR pending | Foundation checks passed; APP-001 contract tests: 2 passed; Chromium browser journeys: 2 passed. Learner browser observation and check interpretation recorded in LEARNING.md (interpretation developed with assistance). | Learner chose to keep the design; commit/PR/merge pending |
| APP-002 | Pending | Unfinished; explicit contracts not yet passed | Pending |
| APP-003 | Pending | Unfinished; explicit contracts not yet passed | Pending |

The instructor's reference branches show possible implementations. They do not establish this repository's completion or the learner's own reasoning.