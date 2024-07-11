# recipe_app

## Overview
recipe_app focuses on creating a web application using the Django framework. The backend stores recipes and their respective data, and users can create their own recipes, as well as read what is already available. There is currently **no user registration available** for this application as it is out of the scope of the project requirements, so a superuser must be created in order to login to the app.

The server is deployed with Heroku, with a Postgres database, HTML, and CSS-based rendered pages at the frontend as well as Python-based Django as the web application framework.

## Features
- User Authentication: Secure user login system.

- Recipe Management: Users can create recipes and upload images for them.

- Difficulty Calculation: The application calculates the difficulty of recipes based on cooking time and number of ingredients.

- Chart Visualization: Charts show data visualization based on search criteria.

- Navbar: Each page, once logged in, has a global navbar with navigation to About, Collection, Search, Add Recipe, and Logout.

## Usage
- Home: The home page displays a welcome message and login button. Clicking Login will redirect users to the login form on a separate page.

- Collection: The Collection page displays a list of all available recipes within the app. Clicking on a recipe name or image will navigate to its Details page.

- Details: The Details page shows detailed information about a recipe, including ingredients, cooking time, difficulty, and its image.

- About: The About page shows developer contact information, including portfolio website link, LinkedIn, GitHub, Medium, and email address.

- Search: The Search page allows users to search for any and all recipes available within the database and provides chart visualizations related to recipes data.

- Add Recipe: Form for adding recipes, including fields for the name, ingredients, cooking time, and image. Difficulty is automatically calculated.

## Installation
1. Clone the repository:
    ```
    git clone <https://github.com/thompson-stephen113/recipe_app>
    ```

2. Create and activate virtual environment:
    ```
    python -m venv venv

    # For Linux Based OS Or Mac-OS
    source venv/bin/activate

    # For Windows With CMD
    .\venv\Scripts\activate.bat
    ```

3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Apply database migrations:
    ```
    py manage.py migrate
    ```

5. Run development server:
    ```
    py manage.py runserver
    ```
