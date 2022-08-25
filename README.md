# Performance app Backend

## Setup environment

### Requeriments

- Create a docker image from Dockerfile

´´´
docker build -t performance_app .
´´´

´´´
docker run -p 9000:8080 --rm -ti performance-app bin/sh
´´´

This will create a virtual machine (alpine) with python installed. Then the instalation of the dependencies in requirements.txt is run from a command in Dockerfile.

### Add variables

In the root directory create a file .env with these values:

...

## How to contribute to the project

Clone the repository.
From the main branch, create a new branch for each new task.
You must follow the recommended branch name like below:

...


## Commit the message:

- The project use [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) standars.
- The message should be in the following format:
    ```
    feat: PER-219 modify readme
    fix: PER-02 fix function get_example.py
    ```
- Commit types:
    - `fix` : hotfix or something that was fixed because of a bug
    - `feat` : refers to a feature, a new requirement
    - `test` : refers to test code, e.g unit testing, integration testing
    - `refactor` : refers something was modified in the code, e.g. naming

## Create the Pull Request (PR)

- Submit the feature (`git push`) and create a PR to `development` branch.
- Explain what has been done, what has been fixed or if you have created a new feature.
- Include reviewers in the PR.

## Architecture
This application is based on DDD (Domain Driven Design) for its architecture.

There is a directory for each entitiy (Employee, Bonus, Components). Each folder will have another 3 directories: application, domain and infrastructure; That is how the building blocks of the application can be separated, creating an agnostic core layer - domain - that contain all the business logic, independent from any implementation or external sources.

Refer to:
![Image about diagram architecture](https://wata.es/wp-content/uploads/2021/05/diagrama-arquitectura-hexagonal-wata-factory-1024x796.png)
