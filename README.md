###### In this project I worked on a real time application. I used its database to retrieve information that is needed by using some sql queries. I worked with status codes, which a server would record.
In order to work with these I should be having some pre-requisites installed in our system.
          •	Python (version 2.7 or version 3.6)
          •	Virtual Box
          •	Vagrant
Steps for entering into vagrant environment:
  	I installed virtual box for creating a new environment.
  	I installed vagrant.
  	I created a new folder with any name(most suitable is vagrant) and open the terminal or command prompt from that folder path.
  	Then I ran the following two commands:
                      •	vagrant init ubuntu/trusty64
                      •	vagrant up
                      •	vagrant ssh
Then I will enter into vagrant environment and it looks like vagrant@vagrant......
I  installed required packages like postgresql if not installed in our system with the      following command:
                	sudo apt-get update
                	sudo apt-get install postgresql postgresql-contrib
 Now I have enter into the user postgres with the following command:
                •	sudo –i –u postgres
                •	psql
Now that I have entered into the user postgres I can create my own user by the following command:
                •	create user username with password ‘password’
I altered the user inorder to get our own access by the following commands:
                •	alter user  username with Superuser
                •	alter user  username with Createrole
                •	alter user  username with Createdb
Then I have created a database in that vagrant user.
                •	createdb databasename;
Then I have  quit the postgres user and enter into vagrant user with the above mentioned command for postgres.
Then I created another database named news in the user vagrant with the following command:
                •	create database databasename;
Then I entered into news database from vagrant databse by following command:
                 •	\c news
I downloaded the sql file and placed it in the folder I have created for vagrant.
Now inorder to import the file into news database we have to first quit the database and enter into vagrant file path and execute the following command.
                •	sudo –d news –f  sqlfilename
Now that the file has been imported into news database we can access its data by running the sql queries.

The below are the queries for creating views that I used to get the solution:
Views related to most popular articles:
To create art_view:
create view art_view as(select title,count(*) as count from articles join log on log.path like concat('/article/%',articles.slug) or    log.status like concat('200','OK') group by articles.title order by count desc; 
Views related to most popular authors:
To create author_view:
create view author_view as select articles.author,count(*) as count from articles join log on log.path like concat('/article/%',articles.slug) natural join art_view where art_view.title=articles.title group by articles.author order by count desc;
To create author_view2:
create view author_view2 as select authors.name,author_view.count from author_view natural join authors where                  author_view.author=authors.id group by authors.name,author_view.count order by author_view.count desc;

Views related to days leading to more than 1% errors:
To create view_total:
      create view view_total as select date(time),count(status) as total from log group by date(time) order by total;
To create view_error:
    create view view_error as select date(time),count(status) as errors where status like ‘404 NOT FOUND’ group by date(time) order by       errors desc;
To create combined_view:
create view combined_view as select view_total.date,errors,total from view_total left join view_error on                 view_total.date=view_erroe.date group by view_total.date,errors,total order by errors desc;
To create the view error_percent:
  create view error_percent as select date,(errors*100.00/total) as error_cent from combined_view group by date,error_cent order by       error_cent desc;
#	After creating the above views we have to the python file in which we have written the main queries to get the solution .
#	The pythom file must be stored in the vagrant folder.
The python is run by the following command:
		python log.py.

