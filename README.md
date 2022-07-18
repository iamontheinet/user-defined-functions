# Deploy Custom Packages from GitHub

This setup (and code) demonstrates a way to deploy custom pure-Python packages from a GitHub repo using GitHub Actions onto Snowflake.

When these packages are used to create User-Defined Functions (UDFs) this flow makes it easy to maintain and deploy custom code across several UDFs at once and automagically without manual intervention.

**NOTE** that this setup decouples the pure-Python custom package from the script that uploads the package to a stage and examines the UDFs that are affected by the updated custom package.
Setup

### GitHub Repository 1: Custom Python Package and Workflow File
* This repo contains pure-Python code that encapsulates all the logic and can be used as a package in UDFs
* This repo is also setup with GitHub Actions workflow with the following
   * Event: On push to main branch when the package code is committed  
   * GitHub Actions Workflow steps:
     * Setup Python 3.8
     * Install dependencies required to deploy the updated package code
       * requests
       * snowflake-connector-python
     * Download script (from Repo 2 – see below) that will upload the updated code to a Snowflake (stage)
     * Setup environment variables (database, warehouse, schema, user, password, and role) from GitHub Secrets that will be used by Snowflake Python Connector in the script (downloaded in step 3) to connect to Snowflake
     * Run script (downloaded in step 3) to deploy the updated code
     
***Repo 1***:  [Sample custom package](https://github.com/iamontheinet/user-defined-functions/blob/main/do_something_cool.py) and [GitHub Actions workflow file.](https://github.com/iamontheinet/user-defined-functions/blob/main/.github/workflows/python-app.yml)

### GitHub Repository 2: Python Script 
* This repo contains Python script that is downloaded and run from GitHub Actions workflow in Repo 1 when updates are made to the package in the main branch of Repo 1
* This repo also contains a JSON file that has a list of packages to be updated when this script is run
* This script 
   * Connects to Snowflake using Snowflake Python Connector and the environment variables set using GitHub Secrets
   * Downloads the latest version of the package off main branch from Repo 1 and uploads it to a Snowflake stage (where UDFs can access it)
   * Loops through all the registered UDFs that belong to the current database and schema, examines the imports, and prints out names of UDFs that are affected and use the updated package

***Repo 2***: [Script to update packages](https://github.com/iamontheinet/c-i-c-d/blob/main/update_packages.py) and [List of packages](https://github.com/iamontheinet/c-i-c-d/blob/main/packages_list.json)
