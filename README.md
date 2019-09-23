# Drinks Intelligence 

A site for a marketing company dedicated to work with the drinks industry.
Users are able to see part work and purchase a variety of creative services.

 
## UX
#### Scope

Scope 1 - Beta version. 

In this version, it was decided to start with a series of pre-set packages that users can avail of.
The page collects a combination of sample of previous work that can be seen in the shape of blog posts, and a page with all the possible services on offer.

Scope 2 - Multimedia version. 

In this version, more services will eb added including podcast creation and video production.
Besides the set-price packages, users will be able to obtain bespoke quotes after filling a form thanks to authomatically generated calculation of the price created with the imput form the form.

##### User stories:
Example:
- As a user type, I want to perform an action, so that I can achieve a goal.

My user stories
- As a bar owner, I want to hire a third party to maintain my business' blog, so I can appeal to my customer base with content marketing.
- As a drinks producer, I want to request professionally written product descriptions, so I can use them on my online shop.
- As a bar manager, I want to contact someone to write press releases about my company, so I can get better media coverage of my news.
- As a brand ambassador, I want someone with knowledge of the local industry to help me organise tasting, so I can showcase my product in the best possible light
- As an author, I want assistance with research in a drinks-related area, so I can publish an investigative piece.
- As an online retailer, I want someone to edit and publish a large amount of product reviews, so I can upsell my products.
- As an event organiser, I want someone to manage the social media of the event, so I cna focus on the production side of things.

##### Mockups and wireframes

- See the mockup: 
    - [mockuphome](https://ibb.co/wWFDM74)
    - [mockupservices](https://ibb.co/RysjRrR)
    - The mockup for this project was created with Balsamiq.

## Features
- A blog with examples of pieces for portfolio.
- A services page with a list of available products.
- A contact form.
- Payment processing functionality using Stripe.
- A homepage with information about the company.
- A login area where users can see the status of their requests.
- An admin area where the admin can update the status of different requests.

##### Existing features

- A blog with examples of pieces for portfolio.
- A services page with a list of available products.
- A contact form.
- Payment processing functionality using Stripe.
- A homepage with information about the company.
- A login area where users can see the status of their requests.
- An admin area where the admin can update the status of different requests.


##### Desired features

- A calculator that adds on requests from a list of potential products and generates a bespoke quote for the user.
- A page dedicated to longer testimonials and case studies.


## Technologies Used

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.

- [Bootstrap 4](https://www.bootstrapcdn.com/)
    - The project uses a **Bootstrap** template for consistency or design and UX.

- [Font Awesome](https://fontawesome.com/)
    - The project uses **Font Awesome** for better design and styling.
    
- [Django](https://www.djangoproject.com/)
    - The project uses **django** to bring the backend and frontend together.

- [PostgreSQL](https://www.postgresql.org/)
    - The project uses a SQL database.
    
- [Stripe](https://stripe.com/ie)
    - Online payment processing for internet businesses.
    

## Testing

User stories reviewed:
My user stories
- **As a bar owner, I want to hire a third party to maintain my business' blog, so I can appeal to my customer base with content marketing.**
*Users can request this under the copywriting plan as part of our available services, they can also email us for a bespoke price in case of wishing an ongoing freelance relationship or a longer term project.*

- **As a drinks producer, I want to request professionally written product descriptions, so I can use them on my online shop.**
*Users can request this under the copywriting plan as part of our available services, depending on the lenght, they might want to upgrade the basic service or not.*

- **As a bar manager, I want to contact someone to write press releases about my company, so I can get better media coverage of my news.**
*Users can request this under the copywriting plan as part of our available services, depending on the lenght, they might want to upgrade the basic service or not.*

- **As a brand ambassador, I want someone with knowledge of the local industry to help me organise tasting, so I can showcase my product in the best possible light.**
*Users can request this under the events and tastings section as part of our available services.*

- **As an author, I want assistance with research in a drinks-related area, so I can publish an investigative piece.**
*Users can request this, depending on the complexity, under the copywriting or the multimedia content plan as part of our available services. For very complex projects, they can choose the bespoke option and contact me for a quote.*

- **As a retailer, I want assistance organising, so I can publish an investigative piece.**
*Users can request this, depending on the complexity, under the copywriting or the multimedia content plan as part of our available services. For very complex projects, they can choose the bespoke option and contact me for a quote.*

- **As an event organiser, I want someone to manage the social media of the event, so I can focus on the production side of things.**
*Users can request this, under the social media takeover plan as part of our available services. For very complex projects, they can choose the bespoke option and contact me for a quote.*


#### MANUAL TESTING
Below, a description of the manual tests run to ensure the site works.

*NOTE: A particularly useful form for describing your testing process is via scenarios*
*NOTE: A €1 product was created for purposes of testing which is now adjusted to normal price.*

1. Select and buy a product:
    1. Go to the services page
    2. Click on the PAY €1 button.
    3. Input correct card details.
    4. Confirm the transaction went through.

2. Try to buy a product but using incorrect card details:
    1. Go to the services page
    2. Click on the PAY €1 button.
    3. Input incorrect card details.
    4. Confirm the transaction didn't through.

3. Make sure an order is placed:
    1. Purchase a product.
    2. Confirm payment went through.
    3. Go into admin mode.
    4. Go into the category of the product just purchased.
    5. Find the details of the recently purchased product.

4. See the blog:
    1. Enter the site
    2. Go to PORTFOLIO
    3. Click on a blog post and see the content render.


##### Different screen sizes:

- The site is responsive and works best on a large to medium screen, horizontally displayed.
- On smaller screens, it works well enough, but there is a small amount of scrolling.
- The look and feel remains the same in different sizes, trying to evoke the theme, which is drinks industry.

##### Bugs and Issues
- In the future, it would be ideal to improve the way purchase flow takes place, adding individual pages to expand on each product on offer, its benefits and how does it worl, as it's unlikely that users will make a purchase of this type without gathering plenty of information first.


## Deployment

Process to deploy the project to a hosting platform:

This project was deployed on Heroku under the name of [drinks-intelligence](https://drinks-intelligenge.herokuapp.com/).
Both the deployed project on Heroku and the project ran from Cloud9 look identical and behave identically.

## Environment variables

The project uses python-decouple to separate environment variables from the settings file to a .env file.
The relevant environmnet variables are:

- Django secret key as SECRET_KEY
- Debug mode as DEBUG
- PostgreSQL database name as DB_NAME
- PostgreSQL database user as DB_USER
- PostgreSQL database password as DB_PASSWORD
- PostgreSQL database host as DB_HOST
- Allowed hosts as ALLOWED_HOSTS
- Amazon S3 bucket media storage user as AWS_S3_USER
- Amazon S3 bucket media storage access key as AWS_ACCESS_KEY_ID
- Amazon S3 bucket media storage secret access key as AWS_SECRET_ACCESS_KEY
- Amazon S3 bucket media storage bucket name as AWS_STORAGE_BUCKET_NAME
- Amazon S3 bucket media storage custom domain as AWS_S3_CUSTOM_DOMAIN

- Separate git branch: Push to Heroku --> $ git push heroku master.

## Dependencies

- Dependencies are listed in requirements.txt file.


## Credits

### Content and tools
- Help working with the views [HERE](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone)
- To optimise database queries [HERE](https://simpleisbetterthancomplex.com/tips/2016/05/16/django-tip-3-optimize-database-queries.html)
- Layout and templating reference [HERE](https://blackrockdigital.github.io/startbootstrap-agency/)
- ASCII text generator [HERE](http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20)
- Login card template [HERE](https://bootsnipp.com/snippets/vl4R7)
- Switching from SQLite3 to PostgreSQL [HERE](https://tutorial-extensions.djangogirls.org/en/optional_postgresql_installation/)
- Hiding environment varialbles [HERE](https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html)
- Deploying to Heroku [HERE](https://simpleisbetterthancomplex.com/tutorial/2016/08/09/how-to-deploy-django-applications-on-heroku.html)
- Adding AWS S3 to a Django-Heroku project [HERE](https://simpleisbetterthancomplex.com/tutorial/2017/08/01/how-to-setup-amazon-s3-in-a-django-project.html)


### Media
- The photos used in this site were obtained from sites with Creative Commons licences or belong to the public domain.
- Other images have been personally photographed by the developer, who owns all the rights of usage.

### Acknowledgements
Code Institute Tutors Nakita, Haley and Niel

Mentor Chris Zielinski

Code Insitute Alumni Andres Correa