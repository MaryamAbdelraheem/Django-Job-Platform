# Django-Job-Platform

## Old Structure Analysis

- The project originally had a single `job` app in `src/job/`.
- Templates for the job app were stored under `src/job/templates/job/`.
- Static assets were centralized under `src/static/assets/` with no app-specific static folders.
- The root `Templates/base.html` used hardcoded asset paths like `assets/img/...` and non-Django URL references such as `job_listing.html`.
- `project/settings.py` included only the `job` app and `project/urls.py` routed `jobs/` to `job.urls`.
- Models, views, and URLs were tightly coupled to the `job` app structure, with no separate employee app or app-specific static/template organization.

## Design Patterns Analysis

- The original architecture followed a monolithic app pattern for job functionality, which made the project harder to scale when new domain areas were needed.
- The refactor invited a more modular app design by splitting concerns into `jobs` and `employees` apps, aligning with Django's recommended app-per-domain pattern.
- Templates and static assets were also decoupled per app, improving maintainability and supporting Django's `app_name`/namespaced URL patterns.
- Using `slug` fields for job and employee detail pages follows the resource-based routing pattern, making URLs human-friendly and SEO-friendly.
- The new structure supports separation of concerns: business logic in models/views, presentation in app-specific templates, and static resources in app-specific static folders.
- This approach makes future extensions easier, such as adding an HR app, candidate profiles, or API endpoints without adding complexity to a single app.

