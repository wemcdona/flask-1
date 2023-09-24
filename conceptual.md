### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
JavaScript is used mainly for frontend whild Python is used mostly for backend development and data sets, as well as server functionality

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
Can use the "get()" method, or use a "try-except" block to catch the 'KeyError' that occurs when you attempt to access a missing key in a dictionary

- What is a unit test?
Form of testing that tests individual components of code, or testing in isolated, small pieces.

- What is an integration test?
Combines units and tests them as groups in mulitple ways to make sure that they work together.

- What is the role of web application framework, like Flask?
They help provide a structured and organized way to develop web applications, allowing developers to focus on building the core functionality of their applications efficiently.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  A route URL is good for things such as link clicks or form submissions, while URL query params are better for search results and category searches and search engines such as google and reddit.

- How do you collect data from a URL placeholder parameter using Flask?
You can define a route with a placeholder in the URL, and then access that parameter within your view function. You can specify the placeholder by enclosing it in angle brackets "<>"

- How do you collect data from the query string using Flask?
You can use the "request.args" object.

- How do you collect data from the body of the request using Flask?
You can use the "request" object, which can be used for POST requests

- What is a cookie and what kinds of things are they commonly used for?
Cookies are used in order to remember data for a specific individual on a website instead of the memory restarting every time it refreshes. It can be used in order to count website visits, the amount of times an application is used, to store usernames and passwords.

- What is the session object in Flask?
Session works to save objects and values as cookies for the website.

- What does Flask's `jsonify()` do?
It is a function that allows you to create JSON responses from Python dictionaries or other data structures. It automatically sets the appropriate content type in the HTTP response headers to indicate that the response contains JSON data.