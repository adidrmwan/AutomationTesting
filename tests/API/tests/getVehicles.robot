*** Settings ***
Library  RequestsLibrary
Library  Collections
Library  JSONLibrary
Library  OperatingSystem

*** Variable ***
${url}=                 https://ghibliapi.herokuapp.com
${uri}=                 vehicles

*** Test Case ***
Get_Ghibli_Vehicles
    Create Session          get_ghibli_vehicles            ${url}           verify=True
    ${headers}=             create dictionary       Content-Type=application/json
    ${resp}=                get request             get_ghibli_vehicles        ${uri}          headers=${headers} 

    #Assertion
    should be equal as integers      ${resp.status_code}                        200
    FOR  ${item}    IN      @{resp.json()}
        ${id}=       Set variable    ${item['id']}
        ${name}=         Set variable    ${item['name']}
        ${description}=         Set variable    ${item['description']}
        ${vehicle_class}=         Set variable    ${item['vehicle_class']}
        ${length}=         Set variable    ${item['length']}
        ${pilot}=         Set variable    ${item['pilot']}
        ${films}=         Set variable    ${item['films']}
        ${url}=         Set variable    ${item['url']}
        Log To Console      ${id},${name},${description},${vehicle_class},${length},${pilot},${films},${url}
    END
    Should Not Be Empty         ${resp.text}