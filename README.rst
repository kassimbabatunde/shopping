********
Products
********

Products is a Django Web app to conduct to view the list of 
available products.Customer are able to view the list of available
product and quantity of each product with price tag.
Also, the customer can add a new set of Gift to the existing list.
The list of purchased product can view and see the quantity bought 
for each gift.

The application trys to Answer the following questions::

    - Add a gift to the list (Link: 'Add New Gift')
    - Remove a gift from the list (Button: 'On Products Page as a button')
    - List the already added gifts of the list (Link: 'Products')
    - Purchase a gift from the list (Button: 'On Products Page as a button')
    - Generate a report from the list which will print out the gifts and their statuses.(Link: 'Product Report')
    - The report must include 2 sections: (Link: 'Product Report')
    - Purchased gifts: each purchased gift with their details.(Link: 'Purchase Item')
    - Not purchased gifts: each available gift with their details. (Link: 'Product Report')


.. note::
   This application is built with::
   
   - Python 3
   - Ubuntu OS 16.04 LTS
   - VSCode
   - Docker

App development
---------------
The application is run using two approach::

    - Development Approach
    - Docker Compose 

Development Approach
--------------------

1. To run the app create virtualenv::

    python -m venv venv

2. Change directory to the venv and create a folder::

    cd venv && mkdir <folder_name>

3. Within the venv, activate the virtualenv::

    source bin/activate

4. Change into <folder_name> and copy the application to directory within the virtualenv::

    cd <folder_name> && cp /root/project_folder /venv/<folder_name>

5. In order to have required dependency, install the requirements.txt file::

    pip install -r requirements.txt

6. Run ``python manage.py runserver`` to start the application in development.

7. Visit http://127.0.0.1:8000/ to view the landing page and links to other pages.


Using Docker
------------

1. Make sure you have Docker Engine and Docker Compose run on your local host

2. Once this done, a docker-compose.yaml file is created to help you run the application

3. Run the following command to start the docker image::

    - docker-compose up


.. note::
    Depending on how you install the docker, if get an error
    [Permission Denide 13] run you command with `sudo docker-compose  up`
       
This should build without any error

Visit http://127.0.0.1:8000/ to view the landing page and links to other pages.
