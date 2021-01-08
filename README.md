# ReDiscord

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a1f8c19c31ce4421a8636e828737a226)](https://app.codacy.com/gh/MATF-Computer-Networks-Projects/2020_DL_Project?utm_source=github.com&utm_medium=referral&utm_content=MATF-Computer-Networks-Projects/2020_DL_Project&utm_campaign=Badge_Grade)

## Opis projekta
**ReDiscord** je manja verzija Discord aplikacije. Simulira komunikaciju izmedju klijenata u zasebnim sobama sa mogućnostima chat-ovanja i audio poziva korišćenjem jezika **Python** i **Django** frameworka, kao i modula **Channels**.

## Instalacija

1. Klonirati repozitorijum sa gita pomoću komande `git clone https://github.com/MATF-Computer-Networks-Projects/2020_DL_Project.git` 
2. U terminalu se pozicionirati na lokaciju `2020_DL_Project/dl_project` i pokrenuti komandu `pip install -r requirements.txt `
3. Pokrenuti docker pomoću `sudo docker run -p 6379:6379 -d redis:5`, a zatim pokrenuti server pomoću `python3 manage.py runserver`