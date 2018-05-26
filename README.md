# Raspberry-Pi-RFID-Proximity-Scanner-RC522-

# Türkçe

## Proje Ne yapar?
* Proje basit bir arayüze sahiptir(Python Tk)
* RFID teknolojili kartları okuyabilir( Öğrenci kartları, otobüs kartları, yoklama kartları vs. Banka kartlarının çoğunluğunu güvenlik nedeniyle okuyamaz. 'RFID ON' butonuna tıklandığında kartın okutulmasını bekleyecektir. RC522 ile okuduğu kart size bir numara verecektir, bu numara eşsizdir (unique). Eşsiz olmasının sebebi her kartın farklı bir frekansaralığına sahip olmasıdır. RC522 bu frekansı 10 tabanında bir sayıya dönüştürür. Bu sayı Primary Key olarak kullanılıp veritabanında bilgiler tutulabilir.

## Uyarılar
* Betiğin içerisinde 'pirc522'nin yolunu belirtmeniz gerekebilir. Proje dizinine bu kütüphaneyi de ekleyeceğim.

##
# English

## What this project do?
* It has a simple Tk UI
* It can read RFID keys/tags when 'RFID ON' button clicked. I set this button, when it's clicked, the program will wait for an RFID tag to read. Such as your student cards, bus cards or toll keys etc. It can't read debit cards mostly. When tag read, you'll see a 9-12 digit number. This number is unique and you can use it for primary key on your database.

## Warnings
* You may need to include 'pirc522' library in your root path (wherever it is). I included it to project.
