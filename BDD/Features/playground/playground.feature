Feature: Answering All the Questions in Selenium Playground

    As a User
    I Can Answer All the Questions in Selenium Playground

    Background:
        Given I use the Chrome Browser

    Scenario: Grab Page Title and Place Title Text in Answer Slot on first number
        Given I Navigate to Playground Homepage
        When I Get the Title of Page
            And I Enter The Title to The Answer Slot
            And I Click Check Results Button
        Then I See "OK" for First Question
    
    Scenario: Fill out name section of form
        Given I Navigate to Playground Homepage
        When I Enter "Kilgore Trout" to The Name Field
            And I Click Check Results Button
        Then I See "OK" for Second Number
