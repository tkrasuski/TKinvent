# TKinvent

## simple TKinter invent client

TKinvent is very simple client of invent module. Application handles uploads json and xlsx files to invent.

### json file format


    {"content": [
        {
            "line":{"part_no":"part 1", "description":"part 2 description", "qty":1, "price": 45.5}
        },
        {
            "line":{"part_no":"part 2", "description":"part 2 description", "qty":1,  "price": 5.0}
        },
        ]
    }

### settings

All application settings are stored in settings.py file. 

* url - invent service url
* port - port your service using
* user - service user
* sign - service user digital sign
