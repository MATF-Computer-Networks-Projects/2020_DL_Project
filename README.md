# ReDiscord

## Opis projekta
**ReDiscord** je manja verzija Discord aplikacije. Simulira komunikaciju izmedju klijenata u zasebnim sobama sa mogućnostima chat-ovanja i audio poziva korišćenjem jezika **Python** i **Django** frameworka, kao i modula **Channels**.

## Instalacija

1. Klonirati repozitorijum sa gita pomoću komande `git clone https://github.com/MATF-Computer-Networks-Projects/2020_DL_Project.git` 
2. U terminalu se pozicionirati na lokaciju `2020_DL_Project/dl_project` i pokrenuti komandu `pip install -r requirements.txt `
3. Pokrenuti docker pomoću `docker run -p 6379:6379 -d redis:5`, a zatim pokrenuti server pomoću `python manage.py runserver`