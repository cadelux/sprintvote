#  SprintVote – Django ile Basit Oylama Sistemi

## Kurulum

```bash
git clone https://github.com/KULLANICIADIN/sprintvote.git
cd sprintvote
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


Oylanacak konular yalnızca superuser tarafından, şirket içinde genelde (teamlead, analyst) gibi pozisyonlara özel hesapla oluşturulabilir.
Bunun için url kısmına /admin ile girip djangonun admin panelinde superuser bilgileri;
username: alinu
pass: 12345678

diğer takım (örn,developer) kullanıcısı:
username: alican71
pass : 12345678.
