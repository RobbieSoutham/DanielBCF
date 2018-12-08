Contents {#contents .TOCHeading}
========

[Analysis 4](#analysis)

[Introduction 4](#_Toc529743193)

[Proposed solution 4](#_Toc529743194)

[Interview with client 5](#_Toc529743195)

[Current system 6](#_Toc525983234)

[Proposed system after the interview: 6](#_Toc529743197)

[Objectives of the system to be developed 6](#_Toc529743198)

[Main objectives: 6](#main-objectives)

[Auxiliary objectives 7](#_Toc529743200)

[Overview 7](#_Toc529743201)

[Stock 7](#_Toc529743202)

[Products 7](#_Toc529743203)

[Outgoing order 7](#_Toc529743204)

[History/invoices 8](#_Toc529743205)

[Statistics/dashboard 8](#_Toc529743206)

[Log 8](#_Toc529743207)

[Logistics 8](#_Toc529743208)

[To be able to order every month and schedule certain tasks I will be
using Cron as it is already integrated to 000webhost. 8](#_Toc529743209)

[Security 8](#_Toc529743210)

[To avoid the risk of SQL injections I will be using prepared
statements. Eventually I would like to add an ssl certificate to the
site. 8](#_Toc529743211)

[I will also be salting hashing the passwords before they are stored in
the database. Hashing will change the password into a long string of
different characters determined by the hashing algorithm. Salting the
passwords will add data before and/or after the data before it is hashed
so that common passwords cannot be found from their respective hashes.
The password salts will be generated for each user using
8](#_Toc529743212)

[Since the registering system could be abused by non-employees there
should also be a confirmation email sent to the manager to ensure the
registrations are legit and. 8](#_Toc529743213)

[Other inventory management software 8](#_Toc529743214)

[Algorithms 10](#_Toc525983239)

[SQL 10](#_Toc529743216)

[PHP 10](#_Toc529743217)

[I will be using MySQLi (OOP) for DB manipulation as I am using a MySQL
DB and the syntax just makes more sense to me. To use a database in PHP
you first have to connect to it. This is done by creating a connection
like so: 10](#_Toc529743218)

[This creates a new MySQLi object and stores it in the "conn" variable.
Then to test the connection, and to see what the error is if there is
one you do: 11](#_Toc529743219)

[So if the connection ("conn") fails the script exits after printing
that the connection has failed along with the error given by "
11](#_Toc529743220)

[To then use the database, you have to define a query and use the MySQLi
function "query" like so: 11](#_Toc529743221)

[Where\" 11](#_Toc529743222)

[When the script ends the connection to the DB automatically closes, but
if the script continues without using the database, it should be closed,
this can be done by using the close function " 11](#_Toc529743223)

[Passwords can be hashed with the built in hash function, which takes
two parameters: the hashing algorithm and the string to be hashed. To
generate 11](#_Toc529743224)

[To generate a CSPRN you can use the build in random string generator IN
PHP. Creating a random string of length \$length is done by the
following: 11](#_Toc529743225)

[Limitations 11](#_Toc529743226)

[Data Sources 11](#_Toc529743227)

[Data Flow Diagram 12](#_Toc525983241)

[Design 12](#design)

[File Structure 12](#_Toc529743230)

[Description of record structure: 13](#_Toc529743231)

[Stock table 13](#_Toc529743232)

[Name 13](#_Toc529743233)

[String 13](#_Toc529743234)

[None. 13](#_Toc529743235)

[Byrons 13](#_Toc529743236)

[Address 13](#_Toc529743237)

[String 13](#_Toc529743238)

[None. 13](#_Toc529743239)

[Product table 13](#_Toc529743240)

[User table 14](#_Toc529743241)

[The validation relates to the original input of the value; it is only
applicable to values that are user inputs. 14](#_Toc529743242)

[To store each month's orders there will be a text file for each site
which will reset each month. 14](#_Toc529743243)

[To test MySQL with the host I created a test database and some code.
000Webhost makes it really easy to create a database and manage it. This
is the DB that was made: 14](#_Toc529743244)

[?\> 15](#_Toc529743245)

[Bootstrap: 15](#_Toc529743246)

[For popups, including decision confirmation and data input I will be
using plugin. For validation I will be using the validator plugin.
15](#_Toc529743247)

[Validation: 15](#_Toc529743248)

[As stated previously I will be using the validator plugin, to activate
it for a given form the attribute data-toggle with the value "validator"
needs to be applied. The validation rules are as followed: I will be
using "email" and "number" value for type (standard html attributes) as
well as the "data-minlength" and "data-match attributes (non-standard).
These will need to be appended to the individual inputs with attribute
its respective value. 15](#_Toc529743249)

[Login Page 16](#_Toc529743250)

[When the web page loads the user has two options: to login, or to
register. The inputs will always be open unless either of the buttons
are pressed. 16](#_Toc529743251)

[Pseudocode: 16](#_Toc529743252)

[Retrieve Salt, Password, Email, FName, SName, IsAdmin from Users table
16](#_Toc529743253)

[givenHash = (salt + PasswordGiven) hashed with Argon2
16](#_Toc529743254)

[IF givenHash = password THEN 16](#_Toc529743255)

[Redirect to stock page 16](#_Toc529743256)

[Set session variables 16](#_Toc529743257)

[Pseudocode: 17](#_Toc529743258)

[\$\_SESSION\["FName"\] = FName 17](#_Toc529743259)

[\$\_SESSION\["SName"\] = SName 17](#_Toc529743260)

[\$\_SESSION\["IsAdmin"\] = IsAdmin 17](#_Toc529743261)

[Registration Page 18](#_Toc529743262)

[When an employee registers they will need to enter their details. If
valid, a record for the user is added into the user's database and they
will be sent a confirmation email to create their account. The manager
will also be sent an email to confirm their legitimacy. The variable
verified will be checked to see if the account has been validated by
both parties. When either the manger or the user verifies it, it will be
incremented by one, the user will then be able to use the account when
it reaches two. 18](#_Toc529743263)

[The password itself will not be stored, instead the password will be
salted and hashed, both the salt and the hashed value will be stored in
the user database. I will be using the Argon2 algorithm.
19](#_Toc529743264)

[SQL: 19](#_Toc529743265)

[Adding users to the users table: 19](#_Toc529743266)

[Stock Page: 20](#stock-page)

[SQL: 21](#_Toc529743268)

[Changing stock status: 21](#_Toc529743269)

[Pulling stock status from the table: 21](#_Toc529743270)

[Status would be the sites status e.g. ByronStatus and newStatus would
be the status that the user has just changed the item to.
21](#_Toc529743271)

[On each item of stock there will be a link to the COSSH information on
the suppliers site. 21](#_Toc529743272)

[Sketch: 21](#_Toc529743273)

[Products page: 22](#_Toc529743274)

[Here the manager will be able to change which products we use and the
order quantity for each type of product. The 22](#_Toc529743275)

[SQL: 22](#_Toc529743276)

[Pulling details from the product and stock tables: 22](#_Toc529743277)

[Log Page 22](#_Toc529743278)

[Sites Page 22](#_Toc529743279)

[SQL: 22](#_Toc529743280)

[Add the field of the sites stock status to the stock table:
22](#_Toc529743281)

[Removing the field of the sites stock status from the stock table:
22](#_Toc529743282)

[Sites: 23](#_Toc529743283)

[With the use of the \$\_SESSION variable again the manager will be able
to modify the sites here. 23](#_Toc529743284)

[When a site is added a field will be added to the stock database which
will be the stock status of that site. Likewise when a site is removed
the reverse will be true. 23](#_Toc529743285)

[Ordering: 23](#_Toc529743286)

[To make an order we will need to send the supplier an email with the
product id, order quantity and to which site it is going to.
23](#_Toc529743287)

[SQL: 23](#_Toc529743288)

[Pull the orderQty from the products table: 23](#_Toc529743289)

[Entity relationship diagram: 23](#_Toc529743290)

Analysis
========

[]{#_Toc529743193 .anchor}[Introduction:]{.underline}

Currently, I have a part time job as a cleaner for JaniKing. My manager
for the branch that I work for does not have a proper system in place to
track the stock. Because of this, there is not always the right
equipment, so the job cannot be done in the most optimal way. This is
obviously a pretty big issue, so to help our branch work more
effectively and take some load of my manager I hope to develop a system
that will solve this issue and will effectively and efficiently track
stock. The end user of the system will hopefully be everyone in our
branch and things should go a lot more smoothly when the system is in
place. Since this is pretty general use it could be implemented and used
elsewhere by anyone or any company that needs to track their inventory.

[]{#_Toc529743194 .anchor}[Proposed solution:]{.underline}

Personally, I think a web-based system would be best for this project as
it would be unnecessary to develop a standalone application for a single
or multiple platforms when I could focus on creating just one that is
cross-platform that can be accessed from anywhere a person has internet.
I think that there should be a user system where employees can register
an account and login. Once logged in there should be a list of all the
stocked products with an input for the quantity of stock remaining. The
employee could then enter the stock level at that time (whether it is
checked at the end of every month or at the start of every week, etc)
and the system will calculate whether it needs to go on the next order
or if it could wait. There should be a list of orders saved which at the
end of every month is sent to the supplier via email (or to the manager
if this is not possible). If the stock level reaches 0 or the stock is
checked before the end of the month and it is below the reorder point
(quantity at which it needs to be ordered to avoid being out of stock)
then an order should be sent straight away.

[]{#_Toc529743195 .anchor}[Interview with client:]{.underline}

**What problem would you like to solve with this new system?:**

"Just be able to easily manage the stock so I don't have to worry about
it."

**What does the current system do? (If any):**

"Employees phone me at the end of every month to tell me what they need
and then I order them from the supplier\'s website."

**What are the problems with the current system? (If any):**

"It\'s awkward. I have to search through a lot of products that we don't
use to find the few that we do."

**How would you like the system to work in terms of when purchases need
to be made? I.e. just send an alert when stock is low or create a
shopping list for every month:**

"Take a stock check every month and generate an order."

**If an item is out of stock would you like the system to automatically
order it or just send an alert?:**

"Automatically order it."

**Where is the stock purchased from?:**

"Bunzl."

**How often are products restocked? How often would you like them to be
restocked?:**

"Monthly."

**Are there any features that you would like to see in the new
system?:**

"Store COSHH (control of substances hazardous to health) of products."

**In what way would you like to stock check? I.e. Login to the site and
track when a product is used up/is in low stock or perform a weekly
check?:**

"As the product is used, as the employees probably wouldn't appreciate
doing a big stock check."

**Is the same stock used for every site?:**

"Yes."

**What would you like the domain to be?:**

"danielbcf."

**What sites do we cover?**

-   Revolution Plymouth

-   Revoloution Bristol

-   Yates

-   Revolution Swansea

-   Bedminster Family Practice

-   Gaywood Family Practice

-   Focal Point

-   The Superemere

-   Byron Hamburgers

-   Exeter FC Training ground

**Any other comments?**

"No."[]{#_Toc525983234 .anchor}

[Current system:]{.underline}

Currently there isn't an automated system in place. At the end of every
month the employees call the manager and tell him what products they
need, he then goes to the supplier's website and makes the order. The
suppliers ordering system is inefficient, making an order involves
querying their database for his item and then searching through a long
list of related products to find the one that we use. This is clearly a
bit of hassle for him, new automated system would save time and the
manager wouldn't have to worry.

[]{#_Toc529743197 .anchor}[Proposed system after the
interview:]{.underline}

Based on the interview I decided to make the system simpler by using
status values instead of actual stock levels. Employees should be able
to set the stock as "low" or "out of stock" as we agreed it should be
quick and easy, someone who has just cleaned for 2+ hours doesn't want
to sit there and stock check, and this is another reason why web-based
system is the best idea.

I was unsure as to whether I would be able to make orders to the
supplier over email. This could have been a huge limitation, and would
have caused the system to not really be optimal and lose a lot of usage
value, as this is one of the main if not the main function of the
system. Luckily, I emailed Bunzl and they confirmed that this was
possible.

[]{#_Toc529743198 .anchor}[Objectives of the system to be
developed:]{.underline}

### Main objectives:

1.  Create a user system where employees can register.

2.  Allow employees to change the stock level

3.  Generate an order for any required products at the end of the month.

4.  If an item is out of stock, then order it automatically.

5.  Have COSSH information for each product.

6.  Allow the manager to modify/add/delete the products that we use.

7.  Have order history/invoices.

[]{#_Toc529743200 .anchor}Auxiliary objectives:

1.  Have a log that tracks the changes the employees make.

2.  Have an account page for the users to change their details.

3.  Have a page where the manager can modify sites.

[]{#_Toc529743201 .anchor}[Overview:]{.underline}

What I think is most important is that the system can change the stock
or check the COSSH quickly and easily. There must be an emphasis on
simplicity so that it doesn't feel as much of a task for the employees.

The sections on the site will hopefully consist of the following:

-   Stock.

-   Products.

-   Outgoing order.

-   History/invoices.

-   (Log)

-   (Account page)

-   (Site page)

[]{#_Toc529743202 .anchor}Stock:

This section is where the employees can change the stock status. There
should be a list of products with their respective stock status and the
user should be able to easily access the COSSH information or change the
stock status to "low" or "out of stock". When a stock is set to low, it
is put on to the monthly order and when its set to out of stock it
should be ordered automatically. When the stock is changed to out the
user should be asked if they are sure to avoid any accidents. There
should also be a search bar to query the list of products. For each
product I will need to find out the order quantity so that each product
is ordered in the right amount.

[]{#_Toc529743203 .anchor}Products:

This will be a list that maps the actual products we get from the
supplier to the stock. There should be set types in the stock i.e. floor
cleaner kept in one table and this will relate to an actual product in
another. The manager should be able to change the products we use and
COSSH data for each of the product types. Creating a CMS (content
management system) for this is much more practical solution than having
to keep changing products from a DBMS (database management system).

[]{#_Toc529743204 .anchor}Outgoing order:

This should just show all of the products that are going to be ordered
at the end of the month, potentially price and cost could be shown.

[]{#_Toc529743205 .anchor}History/invoices:

This should be an easy way to keep invoices so the manager can see them
at any time without any hassle.

[]{#_Toc529743206 .anchor}Statistics/dashboard:

This section should just show statistical information about order trends
and perhaps budget information.

[]{#_Toc529743207 .anchor}Log:

In case anything goes wrong, there should be a list of all the stock
changes so we can see what happened.

[]{#_Toc529743208 .anchor}[Logistics:]{.underline}

I will be developing the system with HTML, CSS, PHP and JS as I have had
previous experience in web development in these languages and it seems
the most logical path to take.

I will also be using bootstrap an easier and more effective designing
process and to easily manipulate data pulled from the database I will be
using ajax.

We registered the domain "danielbcf.tk" for the site. However, we will
be using a subdomain for the stock as the owner wants to add a full site
eventually. I decided to use a .tk domain for now as it is free. I will
also be using the hosting service awardspace for now for both the
database and website, as again it's free.

[]{#_Toc529743209 .anchor}To be able to order every month and schedule
certain tasks I will be using Cron as it is already integrated to
awardspace.

[]{#_Toc529743210 .anchor}[Security:]{.underline}

[]{#_Toc529743211 .anchor}To avoid the risk of SQL injections I will be
using prepared statements. Eventually I would like to add an ssl
certificate to the site.

[]{#_Toc529743212 .anchor}I will also be salting hashing the passwords
before they are stored in the database. Hashing will change the password
into a long string of different characters determined by the hashing
algorithm. Salting the passwords will add data before and/or after the
data before it is hashed so that common passwords cannot be found from
their respective hashes. The password salts will be generated for each
user using a **Cryptographically Secure Pseudo-Random Number
Generator** (CSPRNG).

[]{#_Toc529743213 .anchor}Since the registering system could be abused
by non-employees there should also be a confirmation email sent to the
manager to ensure the registrations are legit and.

[]{#_Toc529743214 .anchor}[Other inventory management
software:]{.underline}

There are thousands of stock management systems out there. Many
expensive, however there are some free ones, but a lot of these offer a
lacklustre user experience and/or an ugly design and are mostly
non-web-based.

![](media/image1.png "Inserting image..."){width="5.395833333333333in"
height="3.923219597550306in"}

(Credit -- HDPOS smart)

These programs are made as a one-size fits all and in doing this
diverges from and may far exceed what the user needs.

Inventory software can cost up to \$45,000 but since these are not
bespoke programs, the company could end up investing in software that
doesn't work well for them. (Blue Link, 2018)

![](media/image2.png){width="6.260415573053368in"
height="3.5208333333333335in"}

(Credit - NetSuite)

I really like the design and functionality of oracles web-based
approach. It\'s great, but it doesn't align so nicely with my client\'s
needs. (It\'s also not specifically a stock management software)

Admittedly, there are many good inventory management software out there
that could work very well for other companies, but as for what my client
needs I don't think there is a current system.

My client would like a very simple, intuitive system with little setup
hassle or cost. He has a small business and just needs to make sure that
the stock never runs out, he\'s not running a big supermarket, so most
other things are irrelevant.

I found some information on the basics of stock management software
including terminology and quantities needed on Wikipedia.
(En.wikipedia.org, 2018)[]{#_Toc525983239 .anchor}

[Algorithms:]{.underline}

[]{#_Toc529743216 .anchor}SQL:

INSERT INTO table (field) VALUES(value)

I will be using this statement to add values (products) into the
database. Where the values are the properties of the entity in regard to
each field, i.e. if the field was ProductName, the value inserted could
be "toilet cleaner".

DELETE FROM table WHERE field=x

This statement deletes a record of certain criteria, so if the criteria
was "price \< 5" it could delete all of the products with a price below
£5

UPDATE table SET field = value WHERE field = value

This statement will be used to modify existing records. Where the first
instance of field is the property to change, and the second is the
search criteria.

SELECT field FROM table

I will be using this statement to pull information out from the
database.

ORDER BY field ASC\|DESC

This statement can be used for any ordering of the produces whether its
price or alphabetical. Using ASC (ascending) or DESC (descending)

ALTER TABLE *table* ADD field string/ALTER TABLE table DROP COLUMN field

These statements will add and remove fields from the table named "table"
respectively.

These can be combined to make composite functions and multiple pieces of
data can be manipulated together by concatenation (For example pulling
the values of two field from a database would be performed by the
following: SELECT field1, field2 FROM table).

[]{#_Toc529743217 .anchor}PHP:

[]{#_Toc529743218 .anchor}I will be using MySQLi (OOP) for DB
manipulation as I am using a MySQL DB and the syntax just makes more
sense to me. To use a database in PHP you first have to connect to it.
This is done by creating a connection like so:

\$conn = new mysqli(\$servername, \$username, \$password, \$dbname);

[]{#_Toc529743219 .anchor}This creates a new MySQLi object and stores it
in the "conn" variable. Then to test the connection, and to see what the
error is if there is one you do:

//Check connection\
if (\$conn-\>connect\_error) {\
    die(\"Connection failed: \" . \$conn-\>connect\_error);\
}

echo \"Connected succesfully\"

[]{#_Toc529743220 .anchor}So if the connection ("conn") fails the script
exits after printing that the connection has failed along with the error
given by "\$conn-\>connect\_error" otherwise it prints that it was
successful.

[]{#_Toc529743221 .anchor}To then use the database, you have to define a
query and use the MySQLi function "query" like so:

\$sql = \"\";\
\
if (\$conn-\>query(\$sql) === TRUE) {\
    echo \"Query completed successfully!\";\
} else {\
    echo \"Error: \" . \$sql . \"\<br\>\" . \$conn-\>error;\
}

[]{#_Toc529743222 .anchor}Where\" \$sql" is the query to be ran.

[]{#_Toc529743223 .anchor}When the script ends the connection to the DB
automatically closes, but if the script continues without using the
database, it should be closed, this can be done by using the close
function "\$conn-\>close();".

[]{#_Toc529743224 .anchor}Passwords can be hashed with the built in
password\_hash function, which takes two parameters: the string to be
hashed and the algorithm, which I'll be using the PASSWORD\_BYCRYPT
option which is the crypt\_blowfish algorithm. . This function makes it
really easy as it automatically salts and hashes the password. I will
also be using the standard hash function for verifying accounts.

[]{#_Toc529743226 .anchor}[Limitations:]{.underline}

Apart from the limitation I mentioned previously, I currently foresee no
limitations with the system apart from the free web hosting service, but
this should be fine.

[]{#_Toc529743227 .anchor}[Data Sources:]{.underline}

There will be one main database for all the data that needs to be
stored. This will contain 4 tables. The two main tables will be for the
products and for the stock. The products table will have the employee
side information: stock level status of each site, name, etc. and the
product table will have all the supplier side information: the actual
name of the product, brand, price, etc. The other tables will be for the
users and for the sites.

[]{#_Toc525983241 .anchor}

[Data Flow Diagram:]{.underline}

(Yourdon and Coad notation)

![C:\\Users\\Robbie
Southam\\Downloads\\Dataflow.png](media/image3.png){width="7.268055555555556in"
height="5.196978346456693in"}

To make this data flow diagram I used information from a very helpful
lucidchart.com post explaining DFDs. (Lucidchart, 2018)

Design
======

[]{#_Toc529743230 .anchor}[File Structure]{.underline}:

-   JS

-   CSS

-   Fonts

-   Invoices

-   Logs

    -   Current

    -   October18

-   login.php

-   stock.php

-   products.php

[]{#_Toc529743231 .anchor}[Description of record structure:]{.underline}

[]{#_Toc529743232 .anchor}Stock table:

This is the stock information on our side.

  Field Name   Data Type   Validation   HTML Attribute   Example         Extra info:
  ------------ ----------- ------------ ---------------- --------------- --------------------------------------------------------------------
  Alias        String      None.                         Floor Cleaner   What the actual product is.
  ProductID    Integer     N/A                                           Foreign key to product table.
  Byron        String      N/A                           Low             Stock level for each site with the field name being the site name.

Sites table:

  Field Name                          Data Type                          Validation                        HTML Attribute   Example                            Extra info:
  ----------------------------------- ---------------------------------- --------------------------------- ---------------- ---------------------------------- -----------------------------
  SiteID                              Integer                            N/A                                                1                                  Auto Increment primary key.
  []{#_Toc529743233 .anchor}Name      []{#_Toc529743234 .anchor}String   []{#_Toc529743235 .anchor}None.                    []{#_Toc529743236 .anchor}Byrons   
  []{#_Toc529743237 .anchor}Address   []{#_Toc529743238 .anchor}String   []{#_Toc529743239 .anchor}None.                                                       

[]{#_Toc529743240 .anchor}

Product table:

This is the product information on the supplier's side.

  Field Name   Data Type   Validation                                                                                                                                                     HTML Attribute   Example   Extra info:
  ------------ ----------- -------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------- --------- -----------------------------------------------------------------
  ProductID    Integer     None.                                                                                                                                                                           1         Primary key given by the supplier to allow ordering to be easy.
  OrderQty     Integer     Must be a whole number.                                                                                                                                                         True      The quantity required for an order.
  COSSH        String      Must be a URL, will use the following regex: "\^(?:http(s)?:\\/\\/)?\[\\w.-\]+(?:\\.\[\\w\\.-\]+)+\[\\w\\-\\.\_\~:/?\#\[\\\]@!\\\$&\'\\(\\)\\\*\\+,;=.\]+\$"                              

[]{#_Toc529743241 .anchor}User table:

  Field Name   Data Type   Validation                  HTML Attribute   Example             Extra info:
  ------------ ----------- --------------------------- ---------------- ------------------- -------------------------------------------------
  UserID       Integer                                                  1                   Auto increment primary key.
  Email        String      Must be an email address.   type = "email"   example\@mail.com   
  IsAdmin      Boolean                                                  True                
  Password     String                                                   "W1EH66..."         The hash of the salt prepended to the password.
  FName        String      None.                                        Robbie              
  SName        String      None.                                        Southam             
  Verified     Int                                                      1                   0-2 Incrementing when one party verifies.
  Salt         String                                                   "D4GcGs..."         

[]{#_Toc529743242 .anchor}The validation relates to the original input
of the value; it is only applicable to values that are user inputs.

[]{#_Toc529743243 .anchor}To store each month's orders there will be a
text file for each site which will reset each month.

[]{#_Toc529743244 .anchor}To test MySQL with the host I created a test
database and some code. Awardspace makes it really easy to create a
database and manage it. This is the DB that was made:

![](media/image4.png){width="7.268055555555556in"
height="0.7243055555555555in"}

\<?php\
\$servername = \"fdb24.awardspace.net\";\
\$username = \"2883969\_main\";\
\$password = \"password\";\
\$dbname = \"2883969\_main\";\
\
//Create connection\
\$conn = new mysqli(\$servername, \$username, \$password, \$dbname);

//Check connection\
if (\$conn-\>connect\_error) {\
    die(\"Connection failed: \" . \$conn-\>connect\_error);\
}

echo \"Connected succesfully\"

[]{#_Toc529743245 .anchor}?\>

After uploading the code to the site it worked as intended:

![](media/image5.png){width="2.965115923009624in"
height="0.6436832895888014in"}

[]{#_Toc529743246 .anchor}[Bootstrap:]{.underline}

[]{#_Toc529743247 .anchor}For popups, including decision confirmation
and data input I will be using plugin. For validation I will be using
the validator plugin.

[]{#_Toc529743248 .anchor}[Validation:]{.underline}

[]{#_Toc529743249 .anchor}As stated previously I will be using the
validator plugin, to activate it for a given form the attribute
data-toggle with the value "validator" needs to be applied. The
validation rules are as followed: I will be using "email" and "number"
value for type (standard html attributes) as well as the
"data-minlength" and "data-match attributes (non-standard). These will
need to be appended to the individual inputs with attribute its
respective value. Since I'm using prepared SQL statements I see no
reason to do extra server side validation

![](media/image6.png){width="4.866666666666666in"
height="7.207638888888889in"}[]{#_Toc529743250 .anchor}[Login
Page:]{.underline}

![](media/image7.jpeg){width="3.236111111111111in"
height="2.4340277777777777in"}Sketch :

[]{#_Toc529743251 .anchor}When the web page loads the user has two
options: to login, or to register. The inputs will always be open unless
either of the buttons are pressed.

If the user has chosen to login the email is validated to avoid sending
unnecessary requests. The user table is then queried to see if the email
and password combination given matches a record in the database. To
check if the password matches the salt will be prepended to the password
given and the result will be hashed and compared to the password hash
stored.

+-----------------------------------------------------------------------+
| []{#_Toc529743252 .anchor}Pseudocode:                                 |
+=======================================================================+
| []{#_Toc529743253 .anchor}Retrieve Salt, Password, Email, FName,      |
| SName, IsAdmin from Users table                                       |
|                                                                       |
| []{#_Toc529743254 .anchor}givenHash = (salt + PasswordGiven) hashed   |
| with Argon2                                                           |
|                                                                       |
| []{#_Toc529743255 .anchor}IF givenHash = password THEN                |
|                                                                       |
| []{#_Toc529743256 .anchor}Redirect to stock page                      |
|                                                                       |
| []{#_Toc529743257 .anchor}Set session variables                       |
+-----------------------------------------------------------------------+

If the data entered was incorrect the user will be given a message
otherwise they will be redirected to the stock page.

Once the user is logged in a new PHP session will start with the
function "session\_start". This will allow me to set session variables
with the \$\_SESSION variable. Following the above pseudocode, to set
the session variables would be as followed, with the assigned values
being the ones retrieved from the Users table.

+--------------------------------------------------------------+
| []{#_Toc529743258 .anchor}Pseudocode:                        |
+==============================================================+
| []{#_Toc529743259 .anchor}\$\_SESSION\["FName"\] = FName     |
|                                                              |
| []{#_Toc529743260 .anchor}\$\_SESSION\["SName"\] = SName     |
|                                                              |
| []{#_Toc529743261 .anchor}\$\_SESSION\["IsAdmin"\] = IsAdmin |
+--------------------------------------------------------------+

Inside the \$\_SESSION variable, I will be storing userID which will
allow me to check if a user is actually logged in and easily manipulate
the users details. If another page other that the login or register page
is attempted to be accessed without being logged in, they will be
redirected to the login page. Which can be done by the following PHP:
header(\"Location:http://danielbcf.tk\")

A cookie will also be stored on the user's device to allow them to use
the remember me function.

SQL:

Retrieving users details from the users table:

SELECT Email, salt, password

FROM Users

WHERE Email = given email

![](media/image8.png){width="2.0902777777777777in"
height="9.922916666666667in"}[]{#_Toc529743262 .anchor}Registration
Page[:]{.underline}

![](media/image9.jpeg){width="4.064583333333333in"
height="4.303472222222222in"} Sketch:

> []{#_Toc529743263 .anchor}When an employee registers they will need to
> enter their details. If valid, a record for the user is added into the
> user's database and they will be sent a confirmation email to create
> their account. The manager will also be sent an email to confirm their
> legitimacy. The variable verified will be checked to see if the
> account has been validated by both parties. When either the manger or
> the user verifies it, it will be incremented by one, the user will
> then be able to use the account when it reaches two.

+-----------------------------------------------+
| Pseudocode:                                   |
+===============================================+
| WHILE valid = false:                          |
|                                               |
| INPUT email, name, password, confirm password |
|                                               |
| IF entered data is accurate THEN:             |
|                                               |
| Valid = true                                  |
|                                               |
| END WHILE                                     |
|                                               |
| Send confirmation emails                      |
|                                               |
| IF email confirmed by both parties THEN:      |
|                                               |
| Insert record for the user into the database  |
|                                               |
| END IF                                        |
+-----------------------------------------------+

[]{#_Toc529743264 .anchor}The password itself will not be stored,
instead the password will be salted and hashed, tehn the resulting hash
will be stored in the user database.

+----------------------------------------+
| Pseudocode:                            |
+========================================+
| Generate salt                          |
|                                        |
| saltedPassword = salt + password       |
|                                        |
| hashedPassword = SaltedPassword hashed |
+----------------------------------------+

[]{#_Toc529743265 .anchor}SQL:

[]{#_Toc529743266 .anchor}Adding users to the users table:

INSERT INTO Users

VALUES(email, fname sname, hashedPassword)

![](media/image10.png){width="3.589583333333333in" height="8.677083333333334in"}[Stock Page]{.underline}:
---------------------------------------------------------------------------------------------------------

This page will be a list of the products for the selected site. If the
stock is changed to low, then it will be appended to the current month's
order. If the stock is changed to out, the user will be asked if they
are sure, if confirmed then the order will be sent out immediately and
the ordered flag will be set to true. When an item is set to out of
stock, the order is sent out instantly, the status is set to ordered
(this will be displayed on the stock page) and the stock level will no
longer be allowed to be changed -- this will also happen when the order
goes through at the end of the month.

+-----------------------------------------------------------------------+
| Pseudocode:                                                           |
+=======================================================================+
| WHILE not ordered:                                                    |
|                                                                       |
| IF low clicked THEN:                                                  |
|                                                                       |
| Update record in stock table                                          |
|                                                                       |
| Status = low                                                          |
|                                                                       |
| Generate log entry                                                    |
|                                                                       |
| IF normal clicked THEN:                                               |
|                                                                       |
| Update record in stock table                                          |
|                                                                       |
| Set status = normal                                                   |
|                                                                       |
| Generate log entry                                                    |
|                                                                       |
| IF Out clicked THEN:                                                  |
|                                                                       |
| PRINT "Are you sure you want to continue? This will send an order     |
| immediately."                                                         |
|                                                                       |
| IF yes THEN:                                                          |
|                                                                       |
| Update record in stock table                                          |
|                                                                       |
| Status = ordered                                                      |
|                                                                       |
| Generate order containing item                                        |
|                                                                       |
| Generate log entry                                                    |
|                                                                       |
| END IF                                                                |
|                                                                       |
| END WHILE                                                             |
+-----------------------------------------------------------------------+

After the given delivery time the stock will be set back to normal.

+------------------------------+
| Pseudocode:                  |
+==============================+
| IF delivery time passed:     |
|                              |
| Update record in stock table |
|                              |
| Status = normal              |
+------------------------------+

[]{#_Toc529743268 .anchor}SQL:

[]{#_Toc529743269 .anchor}Changing stock status:

UPDATE Stock

SET status = newStatus

WHERE StockID = ID

[]{#_Toc529743270 .anchor}Pulling stock status from the table:

SELECT status

FROM Stock

[]{#_Toc529743271 .anchor}Status would be the SiteID and newStatus would
be the status that the user has just changed the item to.

[]{#_Toc529743272 .anchor}On each item of stock there will be a link to
the COSSH information on the suppliers site.

[]{#_Toc529743273 .anchor}Sketch:

![20181010\_190304](media/image11.jpeg){width="7.270833333333333in"
height="1.625in"}

When the different sites are selected the field pulled from the database
will change accordingly.

[]{#_Toc529743274 .anchor}[Products page:]{.underline}

[]{#_Toc529743275 .anchor}Here the manager will be able to change which
products we use and the order quantity for each type of product. The
\$\_SESSION variable will be check to see if the user an admin.

[]{#_Toc529743276 .anchor}SQL:

[]{#_Toc529743277 .anchor}Pulling details from the product and stock
tables:

SELECT Stock.ItemName, Products.ProductID

FROM Stock

INNER JOIN Products ON stock.ProductID = Products.ProductID

[]{#_Toc529743278 .anchor}[Log Page:]{.underline}

When the stock of an item is changed a log entry will be added to the
log file, and when the log page is visited a list of all the log files
be displayed. When clicked the file will be displayed in a pop up.

When the stock status is changed it will be added to the log file by the
following:

\$Log = fopen(\"logs/current.txt\", \"w\")

fwrite( \$log, \$entry)

Where the entry variable will be the line added to the file. I will be
making use of the date function to fetch the date and time of each
entry.

[]{#_Toc529743279 .anchor}[Sites Page]{.underline}:

The page will show a list of all of the sites with an edit button which
will open up the input for the user and a following save and discard
button which will close the input to the user. There will also be a
delete button which will double check with the user before its deleted.

When the user clicks on the add button there will be a pop up allowing
them to add a new site, when submitted the database will have to be
checked to see if the name is unique.

+----------------------------------------------------+
| PSUEDOCODE                                         |
+====================================================+
| IF submit pressed                                  |
|                                                    |
| IF item with same name appears in database:        |
|                                                    |
| OUTPUT "This site already exists."                 |
|                                                    |
| Else:                                              |
|                                                    |
| Add site to Sites table                            |
|                                                    |
| Add field to Stock table with the name of the site |
+----------------------------------------------------+

[]{#_Toc529743280 .anchor}SQL:

[]{#_Toc529743281 .anchor}Add the field of the sites stock status to the
stock table:

> ALTER TABLE *Stock*\
> ADD SiteID string;

[]{#_Toc529743282 .anchor}Removing the field of the sites stock status
from the stock table:

ALTER TABLE Stock

DROP COLUMN SiteID

Adding the new site into the sites table (Where NULL leaves the SiteID
for auto increment):

INSERT INTO Sites

Values(NULL, Name, Address)

Removing a site from the site table:

DELETE FROM Sites

WHERE SiteID = SiteID of site selected for deletion

[]{#_Toc529743283 .anchor}[Sites:]{.underline}

[]{#_Toc529743284 .anchor}With the use of the \$\_SESSION variable again
the manager will be able to modify the sites here.

[]{#_Toc529743285 .anchor}When a site is added a field will be added to
the stock database which will be the stock status of that site. Likewise
when a site is removed the reverse will be true.

[Job Scheduling]{.underline}:

![](media/image12.png){width="6.645833333333333in" height="3.6875in"}

With 000webhost all I have to do is make the script and select when the
job should be done.[]{#_Toc529743287 .anchor}

Ordering:

To make an order we will need to send the supplier an email with the
product id, order quantity and to which site it is going to.

To do this we will need to grab the details from the sites table and the
corresponding stock status from the stock table.

+-----------------------------------------------------------+
| Psuedocode:                                               |
+===========================================================+
| Pull site details from Sites table.                       |
|                                                           |
| FOR ever record in Sites table                            |
|                                                           |
| I = \[\]                                                  |
|                                                           |
| Append Name, Adress to array I                            |
|                                                           |
| Pull details from products for all the low stock products |
|                                                           |
| Append productID and orderQty to array I                  |
+-----------------------------------------------------------+

[]{#_Toc529743288 .anchor}SQL:

Pulling the site details from the sites table:

SELECT SiteID, Address

FROM

Sites

[]{#_Toc529743289 .anchor}Pulling the details from the products table
for all the low stock products for a said site:

SELECT ProductID, OrderQty

FROM Stock

WHERE (SiteID) = "Low"

INNER JOIN Products ON stock.ProductID = Products.ProductID

[]{#_Toc529743290 .anchor}[Entity relationship
diagram:]{.underline}![C:\\Users\\robbiesoutham.AD.000\\Downloads\\Untitled
Diagram (2).png](media/image13.png){width="7.0in"
height="0.4534722222222222in"}

  Activity                                                                                     Date
  -------------------------------------------------------------------------------------------- ------------
  Finished basis of analysis, need to go into more depth.                                      24/09/2018
  Analysis nearly complete, just need to finalize with more detail.                            01/10/2018
  Finished analysis and started flow charts and pseudocode.                                    02/10/2018
  Started databases and finished pseudocode and flowcharts for the login and registry pages.   08/10/2018
  Finished DB connection design                                                                15/10/2018
  Finished basic php algs need to go over sql application on each page.                        16/10/2018

[Bibliography:]{.underline}

En.wikipedia.org. (2018). *Inventory management software*. \[online\]
Available at:
https://en.wikipedia.org/wiki/Inventory\_management\_software \[Accessed
24 Sep. 2018\].

W3schools.com. (2018). SQL Tutorial. \[online\] Available at:
https://www.w3schools.com/sql/ \[Accessed 25 Sep. 2018\].

Blue Link. (2018). So how much does Inventory Management Software cost?.
\[online\] Available at:
https://www.bluelinkerp.com/blog/2011/02/01/so-how-much-does-inventory-management-software-cost/
\[Accessed 27 Sep. 2018\].

(Lucidchart, 2018)Lucidchart. (2018). What is a Data Flow Diagram.
\[online\] Available at:
https://www.lucidchart.com/pages/data-flow-diagram \[Accessed 29 Sep.
2018\].

TODO validation

Make the order

Table for each sites orders or text file.

Redo data flow diagram

Support

Password hashing.

Analysis data dictionary

Explain cookies.

Is order amount same for each site.

If cms is added then update data flow.

<https://crackstation.net/hashing-security.htm>

Multiple tables or multiple fields

Update documentation on validation and using jquery.

Possibly change to two tables for users to increase efficiency.

Data structure and certain values based on generated from code.

SELECT table\_name FROM information\_schema.tables

WHERE table\_schema = \'danielbc\_main\';
