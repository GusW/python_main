# jptest - Gustavo Watanabe (gustavo.watanabe@gmail.com)

## Project structure

### lib_prices.py
Responsible to emulate basic create/read/update asset prices.

### lib_settings.py
Raw settings and ENUMs extensively used in the project. 

### portfolio.py
Classes, methods and business rules applied in this file.

### test.py
Major functionalities and vital project methods are tested using a basic python unittest framework.
Although it was explicit postulated that transaction history could be assumed as given beforehand, to the specific unittest class I decided to create objects myself and test required funcionality.

## Project assumptions:
* An asset has only one currency - Assets can NOT be traded on different currencies
* An asset has only one transaction type - Assets can NOT be traded on Stock and Bond, for instance
* A current price per asset is required to plot a portfolio consolidation
* As the functionality was tested in test.py and the variables were not reused among tests, I decided to make use of staticmethods all over to don't rely on global variables or classmethods on the unittest framework

## Running the test
1. Unpack the files in the same folder/path
2. Run '$ python /path/to/file/test.py'
3. 18 tests should be performed and the last actually prints the portfolio in a csv format

