Feature: Checkout the item in TaniHub

    As a User, I can login and search an item (ex: Minyak Goreng Rose Brand 2 L Karton),
    Add the item into Cart, and then Checkout it.

    Scenario: Login to TaniHub
        Given I am on TaniHub Home page
        When I Click Login Button
        Then I See Login Page
            And I See Email Field
        When I Enter "testinguser@mailinator.com" to Email Field
            And I Click Selanjutnya Button
        Then I See "Password" Field
        When I Enter "admin123" to Password Field
            And I Click Masuk Button
        Then I See "Akun Saya" in Home Page
    
    Scenario: Search an Item

