# Love to Ski-it
An app that allows users to easily view ski resort trail maps and get user submitted reviews and conditions on those trails. This Python project utilizes Flask for it's fast implementation of features like Jinja2 and flash messages. I also implemented Google Maps API in order to view resort trail maps.



# Features
* Resort trail maps automatically populate via Google Maps API based upon the resort chosen
* Trails are marked with ski trail difficulty symbols to easily differentiate between beginner, intermediate, advanced, and expert
* Ability to see user submitted reviews and conditions of individual trails
* Ability to post your review or conditions on an individual trail
* Star rating system to easily tell if a trail is worth riding
* Validations on review submissions to ensure integrity of database
* Utilized a one-to-many relationship between resorts and trails and a one-to-many relationship between trails and reviews
