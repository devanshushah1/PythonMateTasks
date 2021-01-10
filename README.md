# PythonMateTasks

All api endpoints:

#/api/token/ - 
To obtain refresh and access tokens
pass in username and password in json format

#/api/token/refresh/ - 
To obtain the access token once it has expired
pass access token in json format

#signup/ - 
to create a user
pass email, password, password2 as input of body.
added some validation to check password match and length

#shifts/ - 
to see all shifts created till now thorugh get request and to create new shifts using post request
only available to users that are logged in.

