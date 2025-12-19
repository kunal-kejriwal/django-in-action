## Core Application Setup

This project introduces a primary Django app named **`core`**, which serves as the entry point for application-level functionality.

### Changes Included
- Created a new Django app: `core`
- Defined function-based views in `core/views.py`
- Configured URL routing at both project and app levels
- Integrated the `core` app into the main project URL configuration

### Core Views
The `core` app currently exposes the following endpoints:

| URL Path | Description |
|--------|-------------|
| `/core/` | Returns a welcome message for the Core application |
| `/core/first-app/` | Demonstrates an additional view endpoint |

### Implementation Details

**Views (`core/views.py`)**
- `core_home`: Returns a basic welcome response
- `first_view`: Returns a sample response for demonstration

**URL Configuration**
- `core/urls.py` defines app-specific routes
- Project-level `urls.py` includes the `core` app using Django’s `include()` mechanism

This structure follows Django best practices by keeping application routing modular and scalable.


## Core Application – Database & Admin Integration

This update extends the `core` application by introducing persistent data storage, admin access, and dynamic data rendering.

### Changes Introduced

- Registered the `core` app in the main project settings
- Added a `Feature` model to represent application-level capabilities
- Generated and applied database migrations to create the Feature table
- Registered the Feature model in Django Admin for CRUD operations
- Created a superuser to manage application data
- Updated views to fetch and display Feature objects dynamically

### Feature Model
The `Feature` model is used to store and manage configurable features within the application and is backed by Django’s ORM.

### Admin Access
The Feature model is available in the Django Admin panel, allowing authorized users to:
- Create new features
- View existing records
- Update or remove features

### Frontend Integration
Core views now retrieve Feature records from the database and display them dynamically, demonstrating end-to-end flow from database to UI.

This setup establishes a solid foundation for building data-driven functionality within the Django-In-Action project.

