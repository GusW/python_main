# Budget Notifications

## Setup commands

* Unpack the zip contents to a folder of your choice (I guess you have done this step already...).
* (Optional) Install docker (https://docs.docker.com/get-docker/). There is a Dockerfile in the root folder which can be used to create a MySQL container and run both *db.sql* and *migration.sql* out of the box:

  ```bash
  sudo docker volume create --name myCompany-volume
  sudo docker build . -t test_db
  sudo docker run -d -p 3306:3306 \
  -v myCompany-volume:/var/lib/mysql \
  --name myCompany_db test_db
  ```

* The commands above should create a image named `test_db` and a container named `myCompany_db` exposed on local port `3306` whose data is persisted in `myCompany-volume`.

* On the root folder, create virtualenv, upgrade pip and install the requirements.txt:

  ```bash
  python3 -m venv .env
  source .env/bin/activate
  pip install --upgrade pip
  pip install -r requirements.txt
  ```
* If you need to change any DB enviroment variable (such as host and/or port) edit the file `app.env` before perfoming the next step. The Database environment variables and the CLI app can be installed running:
  ```bash
  pip install -e .
  source app.env
  ```
* *(Optional)*: Depending on your system and how the python path is configured system-wise, it may be worth to setup the PYTHONPATH of the application by running the command in the project root folder:

  ```bash
  export PYTHONPATH=$(pwd)

  # checking...

  echo $PYTHONPATH
  ```

## How to use the CLI App

The CLI App is invoked by the command **myCompany** and requires 3 different compulsory arguments and 1 optional:
* `module`
* `tooling`
* `action`
* *(optional)* `date`
```bash
myCompany <module> <tooling> <action> <date>
  ```

(Single) Usage of the CLI is:
 ```bash
myCompany budget notification run

# OR

myCompany budget notification run 20200623
  ```

## Architecture

* CLI entrypoint calls handlers
* Only one handler available => BudgetNotification
* Handler uses Services
* There are 3 different services available:
  * Budget
  * Budget Notification
  * Shop
* Services only call their own Resources and Database Interfaces
* Different Services eventually talk to each other

## Implementation assumptions

To achieve the current CLI app implementation, I had to rely on a few business assumptions. Although they eventually do not match what MyCompany's real business is, I decided to simplify some of these rules in this solution:
* All shops start the budget cycle with full product availability (online) status. No external service is responsible to set their state to "online".
  * Because of this premise, and also thinking in a pragmatic data acquisition and management, to leave an "online" parameter being updated within an Entity domain table seems dangerous. Such table (Shops) should not be updated that much and giving the fact a Shop can go offline and online multiple times within a month - due to an in-period budget amount contract increase - to handle all these events in a single column of a Shops table feels insufficient. The migration.sql is also responsible to drop that column in the Shops table and create a proper Offline Availability table.
  * In a nutshell, the service responsible to verify a Shop is offline and take its listings out of the marketplace must be refactored in order to consume the info from another source, with a slightly different logic.
* Shops whose products are already offline will not receive notifications. This is the first check being done before evaluating notifications.
* Notifications should be sent only in the current budget cumulative period.
  * When you specify a date to run the budget notification, the app will emulate a "time travel" and act as if the action is being triggered in that specific date.
  * Again, notifications will be sent **if and only if** budget thresholds are reached inside the cumulative period i.e. for that specific month.
  * If no date is passed in, the app assumes the tool is running as of today and the budget cumulative period should therefore be this month.


## Upgrades

* The solution is not using any SQL toolkit such as SQLAlchemy, peewee, etc. In one hand, the app is kept lightweight without multiple dependencies which might make development complex and dependent on many external libraries, their availability and own development lifecycle.

* In another hand, there is an inherent lack of capabilities which in the medium term (depending on how the app evolves and how many actions it is intended to do) can become unbearable.

* I also left a couple of *TODOS* in the code where apparently there is some room to easy improvement. Once the current implementation should be quick (less than 48 hrs) and simple, I decide to leave those instead of tackling every corner of the app.

* There are some security concerns in this test once we are not logged in and freely consuming internal information. The CLI should have an authentication and authorization service to manage access to all resources.

* A context manager to handle all the DB Interface cursors should be created.

* Moreover, thinking in a **Microservices** architecture, **API first** and presuming a myCompany CLI app should envolve many different modules whose developement is completely encapsulated and agnostic to each other, these DB calls should be done against an **API Gateway**. We are certainly talking about a production grade enviroment rather than a local test dev - I know ;)

## Additional thoughts

* Does your solution avoid sending duplicate notifications?
  * Yes. Only one type of notification should be sent monthly to each shop. It means that a shop can get a 50% consumption notification and another 100% spent in one month, only. There is an exception which is explained in the question below.
* How does your solution handle a budget change after a notification has already been sent?
  * Keeping track of Budget Notifications fields:
    * Shop
    * Month
    * Type
    * And Budget_Amount
  * This is the compound primary key in which the shop could eventually modify its budget_amount after getting 2 notifications and still get more 2 for the new contracted budget_amount numbers.
  * In this case, the shop **may** receive until 2 notifications per month per budget_amout.
  * It is also the underlying mechanism to avoid sending duplicated notifications.

