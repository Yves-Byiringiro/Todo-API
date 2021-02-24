### First step

Before  using this project , you have to clone it at github using the command below:

git clone https://github.com/Yves-Byiringiro/Todo-API.git


Before run this project in your local machine, you have to install Python3, pip,venv which help to manage your dependencies and create your virtual environment.

After that you can switch to  the project directory, and run the following commands:

1. python3 -m venv env             // for creating your virtual environment
2. source env/bin/activate              // to activate your virtual environment
3. pip install -r requirements.txt      // to install the packages used in the project contained in   requirements.txt file

### Second Step

You will also need to run the following codes to start using project

1. python manage.py makemigrations             // creating tables 
2. python manage.py migrate                    // migrate tables in database
3. python manage.py createsuperuser            // to create the superuser account
4. python manage.py runserver                 //  to run the project at local server


### Third Step

To start using the project open your browser at type: [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view it in the browser.

After you can start navigate through different endpoints

Example: http://127.0.0.1:8000/api/todos/          // for listing the created todos


### NB:

if you  get any error, you can contact me via email: byiringiroyves127@gmail.com