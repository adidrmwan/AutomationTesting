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
             Then I See "OK" for First Number
    
        Scenario: Fill out name section of form
            Given I Navigate to Playground Homepage
             When I Enter "Kilgore Trout" to The Name Field
              And I Click Check Results Button
             Then I See "OK" for Second Number
    
        Scenario: Set Occupation on Form
            Given I Navigate to Playground Homepage
             When I Select "Sci-Fi Author" to The Occupation Field
              And I Click Check Results Button
             Then I See "OK" for Third Number
    
        Scenario: Count Number of Blue Boxes on page after Form and Enter Into Answer
            Given I Navigate to Playground Homepage
             When I Count the Number of Blue Boxes
              And I Enter The Count to The Answer Slot
              And I Click Check Results Button
             Then I See "OK" for Fourth Number
    
        Scenario: Click Link that Says 'Click Me'
            Given I Navigate to Playground Homepage
             When I Click Link that Says "click me"
              And I Click Check Results Button
             Then I See "OK" for Fifth Number
    
        Scenario: Find Red Box Class applied to it, and Enter Into Answer Box
            Given I Navigate to Playground Homepage
             When I Get The Class of Red Box
              And I Enter The Class to The Answer Slot
              And I Click Check Results Button
             Then I See "OK" for Sixth Number

        Scenario: Run JavaScript function as: ran_this_js_function()
            Given I Navigate to Playground Homepage
             When I Run JavaScript Function "ran_this_js_function()"
              And I Click Check Results Button
             Then I See "OK" for Seventh Number
    
        Scenario: Run JavaScript function as: got_return_from_js_function()
            Given I Navigate to Playground Homepage
             When I Run JavaScript Function "got_return_from_js_function()"
              And I Enter The Return Value to The Answer Slot
              And I Click Check Results Button
             Then I See "OK" for Eight Number
        
        Scenario: Mark radio button on form for written book
            Given I Navigate to Playground Homepage
             When I Select written book on Form
              And I Click Check Results Button
             Then I See "OK" for Nineth Number
        
        Scenario: Get the text from the Red Box
            Given I Navigate to Playground Homepage
             When I Get The Text of Red Box
              And I Enter The Text to The Answer Slot
              And I Click Check Results Button
             Then I See "OK" for Ten Number
