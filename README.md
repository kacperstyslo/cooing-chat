# Cooing Chat
[![Build Status](https://app.travis-ci.com/kacperstyslo/cooing-chat.svg?branch=master)](https://app.travis-ci.com/kacperstyslo/cooing-chat)

## See running Cooing Chat <a href="http://cooing-chat-lb-330897751.us-east-1.elb.amazonaws.com" target="blank">here!</a>

# Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Application view](#application-view)

## General info

<details>
    <summary>Click here to see general information about application!</summary>
        <br>
        This application based on flask allows users text with other users in generated room.
        In room can be only one admin. If an external user wants to connect to the room, 
        he must know the secret key.
</details>

## Technologies

<details>
    <summary>Click here to see the technologies used!</summary>
        <ul>
            <li>AWS (ECS, ECR, FARGATE, System Manager, LB)</li>
            <li>Python 3.8.5</li>
            <li>DynamoDb</li>
            <li>Flask 1.1.2</li>
            <li>Flask-SocketIO 4.3.1</li>
            <li>Docker 20.10.5</li>
            <li>Docker-compose 1.29.0</li>
            <li>Terraform</li>
        </ul>
</details>

## Application view

### Page view "Creat room"

![image](https://user-images.githubusercontent.com/57534862/115111034-9639d400-9f7e-11eb-8ff0-14ef581b762f.png)

### Chat view

![image](https://user-images.githubusercontent.com/57534862/115111009-73a7bb00-9f7e-11eb-89ca-eed307809b0c.png)

### Page view "Connect to the room"

![image](https://user-images.githubusercontent.com/57534862/115111100-edd83f80-9f7e-11eb-8f8a-38a7b196d5d8.png)
