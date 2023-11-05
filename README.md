## Description
This project is intended to serve the requirements of a Backed system which are part of a task provided by BigPicture GmbH. To be able to use or review the working of the project please follow the usage section below.

## Usage
To run the project in a docker container

``` bash
cd big-picture-code-challenge/.ci-cd
```
```bash
docker-compose up
```
This creates a container with python and installs all the required python packages. Additionally setups a nginx server and serves the wsgi application on port 80.

Note: Python 3 is used to develop this project and necessary python libraries will be installed into the docker container automatically based on the provided Dockerfile. To have a detailed overview of python library requirements along with uwsgi and nginx configurations see requirements.txt and application.ini and nginx.conf files in the resources directory. The data model used to store the data is found in the model directory.

## Testing the endpoints
The backend server can be reached using http://127.0.0.1 or using http://localhost
The backend provides 3 endpoints to serve the following tasks
- **Endpoint 1**: Fetch Book Details by ISBN

      `GET /isbn/<isbn>`:
      - Returns a JSON including: author, title, summary, cover_url.
      Example: http://localhost/isbn/1878424319

    - **Endpoint 2**: Save Book Details to our Library

      `POST /books` with body `JSON: {isbn: "ISBN_NUMBER_HERE"}`:
      - This will save the book's details to our library database.

      Example: 
          http://localhost/books

          expected body:
          {
            isbn: 1878424319
          }
  
    - **Endpoint 3**: List All Books in our Library

      `GET /books`:
      - Returns a list of all books stored in our library.
      - Use a format, so the fronend can render all information from this one JSON

      Example: http://localhost/books
## Tech stack used
- Python 3
- Flask
- Flask-SQLAlchemy
- nginx
- uWSGI

# Original Instructions
## Big Picture Coding Challenge - Backend - Book Library API

**To work on this challenge, please create a fork of it to your own github account**

Our colleagues have amassed an impressive collection of books, leading to quite the bill and an unhappy boss. To keep things organized and to provide transparency into our library, we've decided to step in and help with software. Our solution: a sleek website where our intern can easily record books by their ISBN number, pulling in detailed information via an API.

**Your mission**: Build the backend to power this application.

## Overview:

- Users (in this case, our intern) can enter the ISBN number of a book.
- Our software will fetch the book's details from an external API and save it to our database.
- The frontend will then display our entire library in a user-friendly manner.

## Backend Specifications:

### Technology:

- Python (Any backend framework of your choice. E.g., Flask, Django, FastAPI, etc.)
- ORM + Database: Feel free to choose what you're comfortable with (SQLite, PostgreSQL, MongoDB, etc.)

### Features:

1. **ISBN Validation**:
    - The backend should be able to validate an ISBN number.
    - If the ISBN is not valid, it should send an appropriate response to the frontend.

2. **Fetch Book Details**:
    - The backend should get book details like author, title, summary, and cover URL from a third-party API.
    - Hint: Check out [OpenLibrary's API](https://openlibrary.org/). It's free and provides detailed information on books by ISBN.

3. **Endpoints**:

    - **Task 1**: Fetch Book Details by ISBN

      `GET /isbn/<isbn>`:
      - Returns a JSON including: author, title, summary, cover_url.

    - **Task 2**: Save Book Details to our Library

      `POST /books` with body `JSON: {isbn: "ISBN_NUMBER_HERE"}`:
      - This will save the book's details to our library database.

    - **Task 3**: List All Books in our Library

      `GET /books`:
      - Returns a list of all books stored in our library.
      - Use a format, so the fronend can render all information from this one JSON

## Documentation:

Please ensure that you document your code adequately. Proper commenting will not only help you in future modifications but will also assist any other developer who might be working with your code.

## Installation
*Please tell us how to get your code running. Do we need to install anything? Is there a database we need to create? Please provide all necessary instructions. After following these instructions the code should run!*

Good luck, and may your code run without bugs!
