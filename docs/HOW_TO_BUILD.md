# How to build this project?

This document explains how to make an executable (or, if you prefer, a package) from the source code.

### Step 1: Clone the repository

Cloning the repository can be done with the following command:

> **git** clone *https://github.com/Cyriel1/pokemon-avonic.git*

Other possible ways are to download the source code in GitHub in a .zip file and extract it into the working directory.

### Step 2: Create a virtual environment

This is recommended, we don't want to install the dependencies globally.

To make things a bit easier I have made a Makefile, so that one can easily execute commands for this step and the following steps. The following command is used to create a virtual environment:

> **make** *create_venv*

**Note:** The following Makefile commands assumes you're in a virtual environment.

### Step 3: Install the dependencies

After activating the virtual environment, you can now install the necessary dependencies that the application needs to run. The following command is used to install the dependencies:

> **make** *install_dependencies*

### Step 4: Create an executable

The project can be run using Python, but an executable can also be created if desired. Use the following command to create an executable file:

> **make** *executable*

### Step 5 (Optional): Create a package

If desired, for any reason, one can package the source code and use the functions for one's own project. But I don't think anyone will and probably won't, but it is possible!

> **make** *package*
