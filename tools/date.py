from datetime import date,timedelta,datetime

def date_today():
    "Retourne la date de l'ordinateur"
    return date.today().strftime("%d/%m/%Y")

def date_add(jours):
    'Rajoute x jours à la date actuelle'
    dates=datetime.now()+timedelta(days=jours)
    return dates.date().strftime("%d/%m/%Y")