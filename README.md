States & Cities.
===================


Providing a public API for states and cities in Nigeria


----------

About.
-------------

It just a simple API that lets you get a list of states, cities and local government areas in Nigeria. In JSON duh. It's made for the developer who wants to make a simple drop down list of Nigerian locations for any app in any language. (It's also not limited to that developer's use case).

It's built in Python with Flask using Parse as a data store.
More on getting the information directly from Parse below.


URI and Versioning.
-------------

We hope to improve this API over time, and these changes won't always be backward compatible, so we're going to version the API. This first iteration will be live at states-and-cities.com/api/v1/ and is structured as described below.


----------


## States

To get a list of all states in Nigeria, call the endpoint at http://states-and-cities.com/api/v1/states.

All states have the following properties:

Field | Description
------|------------
name | The name of the state.
capital | The capital of the state.
latitude | It's longitude.
longitude | It's latitude.
minLat | The minimum latitude of it's boundary.
minLong | The minimum longitude of it's boundary.
maxLat | The maximum latitude of it's boundary.
maxLong | The maximum longitude of it's boundary.


States are identified using their names or a code, which are unique.
For example, a state: http://states-and-cities.com/api/v1/state/lagos

```json
{
  "name": "Lagos",
  "maxLat": 6.7027984,
  "minLong": 3.0982732,
  "longitude": 3.3792057,
  "maxLong": 3.696727799999999,
  "minLat": 6.3936419,
  "latitude": 6.5243793,
  "capital": "Ikeja"
}
```



## Local Government Areas (LGAs)

LGAs belong to a state and they are identified by their names. 
All LGAs have the following properties:

Field | Description
------|------------
name | The name of the LGA.

For example, LGAs in Kaduna: http://states-and-cities.com/api/v1/state/kaduna/lgas

```json
[
  {
    "name": "Birnin Gwari"
  },
  {
    "name": "Chikun"
  },
  {
    "name": "Giwa"
  },
  {
    "name": "Ikara"
  },
  {
    "name": "Igabi"
  },
  {
    "name": "Jaba"
  },
  {
    "name": "Jema'a"
  },
  {
    "name": "Kachia"
  },
  {
    "name": "Kaduna North"
  },
  {
    "name": "Kaduna South"
  },
  {
    "name": "Kagarko"
  },
  {
    "name": "Kajuru"
  },
  {
    "name": "Kaura"
  },
  {
    "name": "Kauru"
  },
  {
    "name": "Kubau"
  },
  {
    "name": "Kudan"
  },
  {
    "name": "Lere"
  },
  {
    "name": "Makarfi"
  },
  {
    "name": "Sabon Gari"
  },
  {
    "name": "Sanga"
  },
  {
    "name": "Soba"
  },
  {
    "name": "Zangon Kataf"
  },
  {
    "name": "Zaria"
  }
]
```



## Cities

Cities belong to a state and they are identified by their names.
All cities have the following properties:

Field | Description
------|------------
name | The name of the city.

For example, Cities in Ogun:http://states-and-cities.com/api/v1/state/ogun/cities

```json
[
  {
    "name": "Ijebu Ode"
  },
  {
    "name": "Shagamu"
  }
]
```


List of endpoints
-------------

This is just a summary of all four endpoints you can call.
- `GET /states` returns a list of all states in Nigeria.
- `GET /state/<state_name_or_code>` returns one state. You can either pass in the state name i.e `lagos` or the state code i.e `LA`.
- `GET /state/<state_name_or_code>/lgas` returns a list of LGAs in a state. You can either pass in the state name i.e `lagos` or the state code i.e `LA`.
- `GET /state/<state_name_or_code>/cities` returns a list of cities in a state. You can either pass in the state name i.e `lagos` or the state code i.e `LA`.


Using Parse SDKs
--------------------

Since this is a Parse backed application, you can skip the API, if say, you're already using Parse in your application or you'd just rather use Parse's SDK than the API.

You can find the parse keys in `/app/__init__.py` and can use them to only read data. Attempting to write anything to our db is a declaration of eternal war with the Knights of Devcenter Square.

There are two classes of concern if you're using any of the Parse SDKs.
- `State` there are 36 of them...actually, no 37 of them. LOL. Do with them you what you may.
- `LGA` These are the local government areas. A city is just a local government area with `city = true`.


Contributing
--------------------

We welcome any and all contributions, code cleanups and feature requests.

1. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug.
2. Fork the repository on GitHub to start making your changes to the **master** branch (or branch off of it).
3. Send a pull request and bug the maintainer until it gets merged and published. :).

