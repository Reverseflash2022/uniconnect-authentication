# UniConnect Authentication and Authorization Microservice

Welcome to UniConnect's Authentication and Authorization microservice. This repository contains the necessary modules for authenticating students and moderators and authorizing them based on their roles. Designed with scalability and security in mind, this service uses Flask, MySQL, Docker, and JWT-based authentication, among other technologies.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Dockerization](#dockerization)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- JWT-based Authentication for students and moderators.
- Role-Based Access Control for resources.
- MySQL database for data persistence.
- Docker containerization for consistent development and production environments.
- Custom error handlers for meaningful error messages.
- CI/CD workflow with GitHub Actions.

## Getting Started

### Prerequisites

- Python 3.8+
- Docker and Docker Compose
- MySQL

### Installation

1. **Clone the Repo**:
    ```bash
    git clone https://github.com/Reverseflash2022/uniconnect-authentication.git
    cd uniconnect-authentication
    ```

2. **Set up Environment Variables**:
    - Copy the `.env.example` to `.env` and adjust the values to match your local setup.
    ```bash
    cp .env.example .env
    ```

3. **Install Python Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Start Docker Services**:
    ```bash
    docker-compose up --build
    ```

## Usage

Once the application is running, you can access the following routes:

- **Student Signup**: POST `/signup/student`
- **Moderator Signup**: POST `/signup/moderator`
- **Login**: POST `/login`
- **Logout**: POST `/logout`
- **User Profile CRUD Operations**: Various routes (please see the routes documentation for further details)

## Testing

Unit tests are located in the `tests/` directory. To run them:

```bash
python -m unittest tests/test_auth.py
```

## Dockerization

The UniConnect Authentication and Authorization Microservice leverages Docker for seamless development and deployment. Below are steps to use the Dockerized application:

1. **Build the Docker Containers**:

    Ensure you have Docker and Docker Compose installed. Then, run the following command from the root directory:

    ```bash
    docker-compose build
    ```

2. **Start the Services**:

    This will start both the application and its associated MySQL server.

    ```bash
    docker-compose up
    ```

    You can stop the services anytime using:

    ```bash
    docker-compose down
    ```

## Contributing

We greatly appreciate contributions. Whether it's a bug fix, new feature, or simply correcting a typo, your help is welcomed and valued.

1. **Fork the Project**:
2. Create a new Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## License

Distributed under the MIT License. See the `LICENSE` file for more information.

## Contact

Okechukwu Uzukwu - ouzukwu@gmail.com

Project Link: [https://github.com/your_username_/uniconnect-authentication](https://github.com/your_username_/uniconnect-authentication)
