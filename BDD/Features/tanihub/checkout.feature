Feature: Checkout the item in TaniHub

    As a User
    I can login and search an item (ex: Minyak Goreng Rose Brand 2 L Karton),
    Add the i
    tem into Cart, and then Checkout it.

    Background:
        Given I use the Chrome Browser
            And I Navigate to TaniHub Homepage

    Scenario: Search an Item and Checkout it
        Given I am logged in as "testinguser@mailinator.com"
        When I Enter "Minyak Goreng Rose Brand 2 L Karton" to Search Field
        Then I See the Result of "Rose Brand Minyak Goreng 2 L Karton" on Page
        When I Add The Item to Cart
            And I Click Checkout Button
        Then I See The Summary Page of Checkout
