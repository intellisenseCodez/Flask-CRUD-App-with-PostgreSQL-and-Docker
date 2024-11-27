# Flask REST API CRUD App with PostgreSQL

## Overview

This Docker image contains a Flask-based REST API for performing CRUD (Create, Read, Update, Delete) operations on a PostgreSQL database. It is lightweight, easy to deploy, and suitable for development or production environments.

### Key Features:
- RESTful endpoints for seamless integration with other applications.
- Powered by Flask for efficient request handling.
- PostgreSQL database support for reliable and scalable data management.
- Ideal for learning API development or integrating into larger projects.

---

## How to Run

### Prerequisites
1. Ensure Docker is installed on your system.
2. Have access to a running PostgreSQL database or start one in a Docker container. Example:

   ```bash
   docker run --name postgres_db -e POSTGRES_USER=your_user -e POSTGRES_PASSWORD=your_password -e POSTGRES_DB=your_database -p 5432:5432 -d postgres

### Steps to Run

1. Pull the Docker image:

   ```bash
   docker pull horlar/flask-restapi-crud-app:<tag>
2. Run the container with your environment variables:

   ```bash
   docker run -d --name flask_app -p 5000:5000 \
  -e DATABASE_URL=database_uri \
  horlar/flask-restapi-crud-app:<tag>

3. Access the API:
   - The API will be available at http://localhost:5000.

### Example API Endpoints
- GET: http://127.0.0.1:5000/books – Retrieve all items.
- GET: http://127.0.0.1:5000/books/<id> – Retrieve specific item.
- POST: http://127.0.0.1:5000/books/create – Create a new item.
- PUT: http://127.0.0.1:5000/books/<id> – Update specific existing item.
- DELETE: http://127.0.0.1:5000/books/<id> – Delete specific item.


### Environment Variables
<table>
  <tr>
    <th>Variable</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>POSTGRES_USER</td>
    <td>PostgreSQL username</td>
  </tr>
  <tr>
    <td>POSTGRES_PASSWORD</td>
    <td>PostgreSQL password</td>
  </tr>
<tr>
    <td>POSTGRES_DB</td>
    <td>PostgreSQL database name</td>
  </tr>
<tr>
    <td>DATABASE_URL</td>
    <td>PostgreSQL database URL PATH</td>
  </tr>
</table>

### Notes
- Replace `<tag>` with the specific version of the image you want to use (e.g., v1.0).
- Ensure that your PostgreSQL database is accessible from the container.

Feel free to explore, modify, and build upon this application! 🚀
