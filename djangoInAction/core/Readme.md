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
