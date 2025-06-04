🌕 Moon Escape — Dokumentacija
Opis igre:
Moon Escape je 2D arkadna igra u kojoj igrač preuzima ulogu izvanzemaljca koji pokušava preživjeti sve intenzivniju kišu meteora. Cilj igre je izbjegavati meteore što je duže moguće, dok s vremenom postaje sve teže.

🎮 Mehanika igre
Igrač upravlja izvanzemaljcem koji se pomiče lijevo i desno po površini Mjeseca.

Meteori (neprijatelji) padaju s vrha ekrana.

Težina igre raste tijekom vremena: meteori postaju brži i češće se pojavljuju.

Igra završava kada meteorit pogodi igrača.

🧠 Tehnička struktura
1. Glavna skripta
Sav se kod nalazi u jednoj .py datoteci. Koristi se:

pygame za grafiku i unos tipki

random za nasumično generiranje meteora

sys za zatvaranje igre

2. Dimenzije ekrana
python
Kopiraj
Uredi
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
🧍 Igrač
Prikazuje se pomoću slike player.png, ili crvenim kvadratom ako slika nije dostupna.

Početni položaj: sredina po širini, 10 piksela iznad dna ekrana.

Brzina kretanja: 5 piksela po frame-u.

Kontrole:

Lijevo: strelica ←

Desno: strelica →

☄️ Meteori (neprijatelji)
Osobine:
Veličina meteora nasumično varira između 30x30 i 80x80 piksela.

Brzina meteora raste kako vrijeme prolazi.

Klasa:
python
Kopiraj
Uredi
class Enemy:
    def __init__(self, x, y, width, height, speed)
    def move(self)
    def draw(surface)
Pojavljivanje:
Meteori se nasumično pojavljuju po X osi, iznad gornjeg ruba ekrana.

Vrijeme između pojavljivanja meteora (spawn_delay) se skraćuje kako igra traje.

Minimalni interval: 5 frame-ova (~0.08s pri 60 FPS-a).

⏱️ Povećanje težine igre
Brzina meteora raste prema formuli:

python
Kopiraj
Uredi
current_enemy_speed = base_enemy_speed + speed_increase_per_second * elapsed_seconds
Interval između pojavljivanja meteora se smanjuje:

python
Kopiraj
Uredi
spawn_delay = max(base_spawn_delay - int(elapsed_seconds * 2), 5)
📦 Resursi (slike)
Očekuju se sljedeće datoteke:

background.png

player.png

enemy.png

Ako neka od slika nedostaje, koristi se zamjenska površina određene boje:

Igrač: crvena

Meteori: svijetloplava (cijan)

Pozadina: tamnoplava

🧪 Sudari
Sudar se provjerava svakim frame-om pomoću:

python
Kopiraj
Uredi
player_rect.colliderect(enemy.rect)
Ako dođe do sudara, igra završava i ispisuje se "Game Over!".

🖥️ Prikaz vremena
Vrijeme preživljavanja prikazuje se u gornjem lijevom kutu ekrana:

python
Kopiraj
Uredi
Time: Xs
▶️ Pokretanje igre
Instaliraj pygame ako već nije:

bash
Kopiraj
Uredi
pip install pygame
Pokreni igru:

bash
Kopiraj
Uredi
python moon_escape.py
