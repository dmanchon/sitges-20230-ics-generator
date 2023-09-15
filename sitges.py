import requests
from ics import Calendar, Event

def main():
    url = "https://sitgesfilmfestival.com/ca/service/films/2023"
    r = requests.get(url)
    body = r.json()
    c = Calendar()

    locations = {l["id"]: l["name"]["es"] for l in body["locations"]}
    for session in body["sessions"]:
        e = Event()
        e.name = session["name"]["en"]
        e.begin = session["start_date"]
        e.end = session["end_date"]
        e.location = locations[session["locations"][0]]
        e.uid = session["id"]
        c.events.add(e)

    with open('sitges.ics', 'w') as my_file:
        my_file.writelines(c.serialize_iter())
    

if __name__ == "__main__":
    main()
