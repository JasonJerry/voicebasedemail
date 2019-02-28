# voicebasedemail
Voice Based Email Client System to help the impaired. Design inspired from https://www.geeksforgeeks.org/project-idea-voice-based-email-visually-challenged/


Project Idea | Voice Based Email for Visually Challenged

Project Title: Voice based Email service for visually challenged people

We have seen that the inception of Internet has dramatically revolutionized many fields. Internet has made life of people so easy that people today have access to any information they want sitting at their home. One of the main fields that Internet has revolutionized is communication. And talking about communication over Internet, the first thing that comes in our mind is E-mail. E-mails are considered to be the most reliable way of communication over Internet, for sending or receiving some important information. But there is a special criteria for humans to access the Internet and the criteria is you must be able to see. You must be thinking that what sort of criteria is this, every one with eyes can see. But there are also specially abled people in our society who are not gifted with what you have. Yes there are some visually challenged people or blind people who can not see things and thus can not see the computer screen or keyboard.
A survey shows that there are more than 250 million visually challenged people around the globe. That is, around 250 million people are unaware of how to use Internet or E-mail. The only way by which a visually impaired person can send an E-mail is, they have to dictate the entire content of the mail to a third person( not visually challenged ) and then the third person will compose the mail and send on the behalf of the visually impaired person.
But this is not a correct way to deal with this problem. It is very less likely that every time a visually challenged person can find someone for help. Although for these reasons the specially abled people are criticized by our society.
So, for the betterment of society and giving an equal status to such specially abled people we have come up with this project idea which provides the user with ability to send mails using voice commands without the need of keyboard or any other visual things.

Introduction: As the title suggests, the application will be a web-based application for visually impaired persons using IVR- Interactive voice response, thus enabling everyone to control their mail accounts using their voice only and to be able to read,send, and perform all the other useful tasks. The system will prompt the user with voice commands to perform certain action and the user will respond to the same. The main benefit of this system is that the use of keyboard is completely eliminated, the user will have to respond through voice and mouse click only.
Now you must be thinking that how will a blind person will see the correct position on the screen for doing mouse clicks. But this system will perform actions based on the clicks only that is left click or right click, it does not depends on the portion of the screen where the cursor is placed before the click giving user the freedom to click blindly anywhere on the screen.
Design: The design of this project is divided into three phases as described below:

    UI design: In this phase the UI or the user interface of the project is developed. That is, the designing of the web pages which the user will use to interact.
    Database design: The database is considered to be the main pillars of every project. In our application, database is used to store user details such as name, age etc. Database here is also used to keep information about the emails sent or received or in draft. The complete proposed design of the database is shown in the ER-diagram below. This ER-diagram shows all the tables with all fields and also relationship between different tables.
    System design: In this phase a complete flow diagram of the working system is designed. This flow diagram will show the details of all the events like actions to be performed for an event.

After completion of the design phase, we will now start to implement our project.

Implementation


Diagrams: Below are some important diagrams which explains the working and will be used in implementing the project.
ER_Diagram_ProGeeks

ER Diagram of Proposed Project

Flow Diagram of Proposed Project

Flow Diagram of Proposed Project

The above flow diagram explains the complete working of the project and the project can be easily implemented using the above flow diagram and ER diagram. However, the project is currently under development so we are providing details of few modules which are already developed by us:

    Login: This is the very first page and will ask user to enter login credentials. It will prompt user with voice command to enter user name. After receiving user name it will prompt again for password. After receiving all of the details from user, it will encrypt and check the validity of the details entered by user. If valid, then user will be redirected to dashboard else will be sent back to login page.
    Dashboard: After successful login, user will be redirected to this page and this is the main page from where user can perform all the activities like, compose a new mail, check inbox, save to draft etc.
    Below steps specifies the operation that will be executed based on a specific click of mouse button. As the user is supposed to be blind, so it is allowed to click blindly anywhere on the screen:
        Left Click to Compose a new Mail.
        Right Click to Go to the Sent Mails.
        Double Left Click to Go to the Inbox View.
        Scroll Button Click to go to Trash Messages.
        Double Right Click to Log out of the Session.

    Below is the flowchart that explains this process:
    Login & Dashboard Flowchart

    Login & Dashboard Flowchart

    Common Rule:
    Left Click = Next Step
    Right Click = Back
    Scroll Button Click = Dashboard
    Compose a Mail: This module is used to compose a new mail. Below are the steps followed by this module to compose a new mail:
        Left Click from dashboard to Compose a new Mail.
        Give Voice Data about the Recipient, and CC, BCC, the Subject and then the body
        If satisfied with current input Left Click to go to next Stage
        In next Stage your voice will be recognized,Left Click to proceed
        In this stage your voice and input will be verified if any problem is found you are redirected to that or Left Click to proceed to Send the Mail or Right Click to Double Left Click to save as Draft
    Inbox: This page will store all of the mails received by user. Below steps explains how to access a mail from inbox:
        All the received Mails will be listed sorted in order of date
        Double left Click to give voice input to filter Mail,when Satisfied Left click to proceed
        In this Stage your mail will be read out , Double Left Click to start/pause
    Trash: This folder will store all of mails deleted by the user. Below steps provide detailed explanation about this module:
        All the deleted Mails will be listed sorted in order of date
        Double left Click to give voice input to filter Mail, when Satisfied Left click to proceed to Read Section.
        In this Stage your mail will be read out.
        Double Left Click to start/pause
        Left Click to proceed to Delete the Mail or Right Click to back
        If in Delete Section Left Click to Delete the Mail
    Sent Mail: This folder will store all of the mails sent from the user. Below steps explains the working of this module:
        All the sent Mails will be listed sorted in order of date
        Double left Click to give voice input to filter Mail, when Satisfied Left click to proceed to Read Section.
        In this Stage your mail will be read out, Double Left Click to start/pause
        Left Click to proceed to Delete the Mail or Right Click to back
        If in Delete Section Left Click to Delete the Mail

Tools Used: Apache HTTP Server, MySQL database and interpreters for scripts, PHP for handling backend of web interface, HTML and CSS for creating Web based UI, Google Speech-to-text and text-to-speech APIs.

Application:
This project is proposed for the betterment of society. This project aims to help the visually impaired people to be a part of growing digital India by using internet and also aims to make life of such people quite easy. Also, the success of this project will also encourage developers to build something more useful for visually impaired or illiterate people, who also deserves an equal standard in society.

References:

    Jagtap Nilesh, Pawan Alai, Chavhan Swapnil and Bendre M.R.. “Voice Based System in Desktop and Mobile Devices for Blind People”. In International Journal of Emerging Technology and Advanced Engineering (IJETAE), 2014 on Pages 404-407
    Ummuhanysifa U.,Nizar Banu P K , “Voice Based Search Engine and Web page Reader”. In
    International Journal of Computational Engineering Research (IJCER). Pages 1-5.
    https://cloud.google.com/speech/docs/getting-started
