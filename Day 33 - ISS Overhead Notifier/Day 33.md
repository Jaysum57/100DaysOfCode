---
tags:
  - 100_Days_of_Code
  - programming
  - python
---
# Day 33: Intermediate+ API Endpoints & API Parameters - ISS Overhead Notifier

## Notes

### Application Programming Interface (API)

- Is a set of commands, functions, protocols, and objects that programmers can use to create software or **interact with an external system**.
![[vlcsnap-2025-02-04-22h40m02s024.png|400]]

### API Endpoint
location of where the API can be found.

Example:
- `api.coinbase.com`

[Open Notify -- API Doc | ISS Current Location](http://open-notify.org/Open-Notify-API/ISS-Location-Now/)

```python
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

print(response) # Output: <Response [200]>
```

```python
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)

response.raise_for_status()
data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_postion = (longitude, latitude)

print(iss_postion)
```

### 404 Response Code
- Typically means that the thing that you are looking for doesn't exist
![[Pasted image 20250204230731.png|300]]

#### Response Code guide
`1XX`: Hold On
`2XX`: Here you Go
`3XX`: Go away
`4XX`: You screwed up
`5XX`: I screwed up

More on: [HTTP Status Codes Glossary - WebFX](https://www.webfx.com/web-development/glossary/http-status-codes/)

### API Parameters

#### Sample requests

```url
https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400
```

| Part                                  | Meaning     |
| ------------------------------------- | ----------- |
| `https://api.sunrise-sunset.org/json` | Endpoint    |
| `?`                                   | Input       |
| `lat`                                 | Param Name  |
| `=`                                   | Equals      |
| `36.7201600`                          | Value       |
| `&`                                   | More Params |

