# sql_to_json
JSON dict of dicts based on the revenue table in this session_2.db database.

From terminal
```bash
sqlite> SELECT *FROM revenue;
company            state  cost 
-----------------  -----  -----
Haddad's           PA     239.5
Westfield          NJ     53.9 
The Store          NJ     211.5
Hipster's          NY     11.98
Dothraki Fashions  NY     5.98 
Awful's            PA     23.95
The Clothiers      NY     115.2
Acme Inc.          AL     35.98
```

From revenue.json
```json
{
     "Haddad's": {
          "name": "Haddad's",
          "state": "PA",
          "cost": 239.5
     },
     "Westfield": {
          "name": "Westfield",
          "state": "NJ",
          "cost": 53.9
     },
     "The Store": {
          "name": "The Store",
          "state": "NJ",
          "cost": 211.5
     },
     "Hipster's": {
          "name": "Hipster's",
          "state": "NY",
          "cost": 11.98
     },
     "Dothraki Fashions": {
          "name": "Dothraki Fashions",
          "state": "NY",
          "cost": 5.98
     },
     "Awful's": {
          "name": "Awful's",
          "state": "PA",
          "cost": 23.95
     },
     "The Clothiers": {
          "name": "The Clothiers",
          "state": "NY",
          "cost": 115.2
     },
     "Acme Inc.": {
          "name": "Acme Inc.",
          "state": "AL",
          "cost": 35.98
     }
}
```
