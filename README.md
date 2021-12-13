# **Candy Cane Coders Secret Santa's Countdown**
Candy Cane Coders is a website designed for companies that may want to do a Secret Santa in the workplace. The team signs up and as each day passes are able to choose a gift to add to their secret santa wishlist. When the countdown timer finishes the users wishlist is assigned to another user and they receive a random users wishlist in return. The user can then select 1 gift from the wishlist to send, whilst they will also receive 1 in return. 

""""""Insert amiresponsive image here""""""""""

## **Table of Contents**
* [**Planning Stage**](#planning-stage)
  * Project Goals
  * User Goals
  * User Stories
  * Design Goals
  * Design Choices
    * Font
    * Color Scheme
  * Wireframes
* [**Features**](#features)
  * Existing Features
  * Features Left to Implement
  * Languages
  * Frameworks
  * Database
  * Extensions and kits
  * Project Management
  * Tools
* [**Deployment**](#deployment)
  * Requirements
* [**Testing**](#testing)
* [**Credits**](#testing)


## **Planning Stage**

### Project Goals
The goal of this project was to create a Christmas themed site with the goal to be able to take the stress out of picking a secret santa gift. 

### User Goals
The target user is a group of people who would like to do secret santa.
 * A group of work colleagues or a specific department.
 * A group of friends.
 * A large family.
 * An online group. e.g. Reddit Secrfet Santa. 

 ### User Stories
 * As a user I want the site to be easy to use and easy to navigate.
 * As a user I want the site to get me in the Chrismas spirit.
 * As a user I want to be able to control my gift wishlist.
 * As a user I want the hassle of trying to pick a secret santa gift taken care of for me.

 ### Design Goals
 * A simple Christmas themed site that works on all devices.
 * Ease of navigation.
 * Be fun enough for users to return to the site.

### Design Choices
 
 #### Font
 Keeping in the Christmas theme we decided on the following fonts:
  * [Architects Daughter](https://fonts.google.com/specimen/Architects+Daughter?query=archite)
  * [Fuzzy Bubbles](https://fonts.google.com/specimen/Fuzzy+Bubbles?query=fuzzy+bubbles)
  * [Candyman](https://www.cdnfonts.com/candyman.font)

These fonts give the overall presentation of the site a Christmas feel, with the Candyman font being used for the site logo and for information boxes within the site. 

### **Color Scheme:**
In the spirit of Christmas, we have decided on a Red White and Green theme, with Red being the dominant color. All text on the site is easy to read with good contrast. 

### **Wireframes:**
To help keep the design scope, wireframes were created for the proposed pages of the site. There was some deviation from the initial design as each page was implemented to improve the user experience but in general it stayed true to the initial design. 

* Mobile Wireframes:
    * [Login Page](wireframes/login-page-responsive.png)
    * [Countdown Page](wireframes/countdown-responsive.png)
    * [Wishlist Page](wireframes/my-wishlist-responsive.png)
    * [Sending / Receiving Page](wireframes/secret-santa-responsive.png)

* Desktop wireframes:
     * [Login Page](wireframes/login-page.png)
    * [Countdown Page](wireframes/countdown.png)
    * [Wishlist Page](wireframes/my-wishlist.png)
    * [Sending / Receiving Page](wireframes/secret-santa.png)

## **Database & Model**

A relational database is best suited to this project given the number of relationships between the models. SQLite was used during development and Heroku Postgres in production. The diagram below may help visualise the database and relationships between each model.

![Database-schema](wireframes/database-schema.png)

### **Key Models**

#### *Countdown*

- A model for counting down the days left for the draw.

#### *Gift*

- Holds the gift information including it's name, image and which day it belongs to.

#### *Profile*

- contains the user's full name, assign it to the wishlist owner & sender, gifts recieved & sent.

#### *Wishlists*

- This model has relationship with user and gifts.

## **Features**

### **Existing Features**
  * Users are able to to view a gift and choose to add it to their wish list or not.
  * Every day a new box will open and the user can choose to add it to their wishlist.
  * On day 11 all gifts on the countdown page are no longer able to be picked. A draw is made matching users with each other.
  ![Wishlist](static/images/readme/wishlist.png)
  * Users can view their wishlist and delete items from their wishlist.
  ![My Wishlist](static/images/readme/my-wishlist.png)
  * Once matched, the user can see their matched users wishlist and can choose 1 gift from the list to send to them.
  ![My Wishlist](static/images/readme/wishlist-send.png)
  * Once a users secret santa has picked their gift, it can be seen in the gifts received page. 
  ![Wishlist Sent](static/images/readme/wishlist-sent.png)

### **Features Left to Implement**
  * Give users the option to pick 1 of 3 gifts per day with the gifts randomly chosen.
  * Hide the gift the user has received from their secret santa until Christmas day and implement a timer to replace the countdown page timer until Christmas day. 
  * Ability for the admin to add/remove gifts from the database to customise the gifts available based on budgets set.

### **Languages**

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)

- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)

- [Python](https://www.python.org/)

- [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

### **Frameworks**

- [UIkit](https://getuikit.com/)

- [Django](https://www.djangoproject.com/)


### **Database**

- [sqlite3](https://www.sqlite.org/index.html)

- [Heroku Postgres](https://www.heroku.com/postgres)

### **Extensions and kits**

- [Pillow](https://pillow.readthedocs.io/en/stable/)

### **Project Management**

- [WhiteNoise](http://whitenoise.evans.io/en/stable/index.html#)

- [Github](https://github.com/)

- [Heroku](https://heroku.com)

### **Tools**

- [Website Mockup Generator](https://websitemockupgenerator.com/)

- [Balsamiq](https://balsamiq.com/wireframes/)

- [DB Diagram](https://dbdiagram.io/home)

- [Font Awesome](https://fontawesome.com/)

- [Google Font](https://fonts.google.com/)

## **Deployment**

### **Requirements**

[Python 3](https://www.python.org/downloads/) - core code

[pipenv](https://pypi.org/project/pipenv/) - package installation and python environment control

[Git](https://git-scm.com/) - version control

[WhiteNoise](http://whitenoise.evans.io/en/stable/index.html#) - hosting static files


### **How to Candy Cane's Secret Santa and run locally**


To clone this project from its [GitHub repository](https://github.com/nazarja/candy-cane-coders):

1.From the repository, click **Code**

2.Go to the Clone >> HTTPS section, copy the clone URL for the repository

3.Go to your local IDE open your CLI

4.Change the current working directory to the location where you want the cloned directory to be made

5.Type `git clone`, and then paste the URL you copied in Step 2

```
git clone https://github.com/nazarja/candy-cane-coders
```

6.Press Enter. Your local clone will be created

7.Create a file called env.py to hold your app's environment variables, which should contain the following:

```
import os

os.environ["DEV"] = "1"
os.environ["SECRET_KEY"] = "app secret key of your choice"
os.environ["DATABASE_URL"] = ""
os.environ["HEROKU_URL"] = "*"

```
8.Make sure the following are listed in your .gitignore file to prevent any environment variables being pushed publicly:

```
env.py
__pycache__/
*.sqlite3
*.pyc
Pipfile
Pipfile.lock
.DS_Store
fixtures/
db.json
```
9.Create and activate virtual environment using:
```
pipenv shell
```

10.Install all the app requirements using:

```
pip install -r requirements.txt
```
11.Apply database migrations using:

```
python manage.py migrate
```
12.Create a new superuser and fill in your own details using:

```
python manage.py createsuperuser
```

13.The app can now be running loacally using:
```
python manage.py runserver
```

### **How to deploy to Heroku**

1.Log In to Heroku

2.Select **Create new app** from the dropdown in the Heroku dashboard

3.Choose a unique name('Kumite-dojo') for the app and the location nearest to you

4.Under **Resources** search and add **Heroku Postgres** database to your app and choose the free plan

5.Go to your CLI install **dj_database_url** and **psycopg2** so that you can sue Postges on your deployed site, commands are:
```
pipenv install dj_database_url
pipenv install Psycopg2-binary
```

6.Add those packages to requirements.txt using:
```
pip freeze > requirements.txt
```

7.Go to settings.py, setup the new database using code below:
```
import dj_database_url
```
```
if "DATABASE_URL" in os.environ:
    DATABASES = {"default": dj_database_url.parse(os.environ.get("DATABASE_URL"))}
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
```

9.Set debug using:
```
DEBUG = "DEVELOPMENT" in os.environ
```

10.Get database url from heroku settings > config vars or using:
```
heroku config
```

11.Set `DATABASE_URL` in env.py

12.Log into heroku via Heroku CLI using:
```
heroku login -i
```

13.Migrate the database into Postgres using:
```
python manage.py migrate
```

14.Import all product data using the fixtures created during development

15.Create a new superuser and fill in your own details using:
```
python manage.py createsuperuser
```

16.Install gunicorn
```
pipenv install gunicorn
```

17.Add the package into requirements
```
pip freeze > requirements.txt
```

18.Create a file call **Procfile** and include the following, making sure not to leave a blank line after it:
```
web:gunicorn candy-cane-coders.wsgi:application
```

19.Disable Heroku's static file collection (temporarily)
```
heroku config:set DISABLE_COLLECTSTATIC=1 --app candy-cane-coders
```

20.Add the hostname of your heroku app to settings.py
```
ALLOWED_HOSTS = ["candy-cane-coders.herokuapp.com", "localhost"]
```

21.Commit all changeds to github

22.Go to the **Settings** tab and under **Config Vars** choose **Reveal Config Vars** and set Django secret key where you can find in your env.py as **SECRET_KEY**

23.Initial heroku git remote using:
```
heroku git:remote -a candy-cane-coders
```

24.Deploy to Heroku using:
```
git push heroku main
```

25.Your deployed site can be launched by clicking **Open App** from its page within Heroku.

26.Back in Heroku, select the **Deploy** tab and under **Deployment method** choose GitHub

27.Go to **Connect to GitHub** enter your GitHub repository details and once found, click **Connect**, under **Automatic deploys** choose **Enable Automatic Deploys**


## **Testing**

#### **Easy navigation**

- Heading descriptive of the content displayed.

- Nabvar clearly indicates page directions.

- Logo directs user back to home page.

- Easy access to features.

#### **Consistency**

- Consistent visual effect throughout the whole site.

- Same navigation system across main pages.

- Images and elements are well contained throughout the site.

#### **Intuitive**

- Familiar icons have been used across the site for commonly expected actions.

- Toasts pop-ups alert the user when they perform actions i.e. login, errors, sucess etc.

#### **Responsiveness**

- Pages adapt a variety of screen sizes and extensive testing in Chrome Dev Tools.

- Page structure has been modified for mobile screen size to ensure readability.

#### **Secure**

- Allauth provides a robust user account system while Stripe offers secure payments, furthered by use of webhooks to ensure transactions are recorded.

#### **Appealing Visuals**

- Red and green Christmas colors throughout the whole site.

- Simple fonts ensure readability and bring content together.

**Find out how does it work**

- The about section on the home page explains to the user how the site works.

## **Credits**

* The hero image and background images were taken from [Pexels](https://www.pexels.com/)
* The falling snow animation was taken from [Giphy](https://giphy.com/explore/snow-sticker)
* The Favicon and present icon was taken from [Icons8](https://icons8.com/)
