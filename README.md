
# EN: (Semi)automaticaly uploads items to the online rental shop "pujcim.to"
# CZ: Automaticky načte položky do pujcim.to z excelovské tabulky (za malé pomoci uživatele) 

Tento skript načte jednotlivé položky z Excelovského souboru, zaloguje se do uživatelského účtu na pujcim.to,
zvolí odpovídající kategorie a vyplní odpovídající políčka.
Poté čeká, až uživatel nahraje obrázek, zkontroluje obsah a položku uloží.
Následně je možné pokračovat další položkou v seznamu, nebo skript ukončit.

Původně byl tento skript vytvořen k nahrávání deskových her, ale měl by fungovat i pro jiné kategorie.

Jediný soubor, který musíte změnit, aby odpovídal vašim potřebám je user_specific_info/user_info.

Veškeré lokátory jednotlivých elementů jsou v locators/pages_locators.

### Přihášení
Na pujcim.to je nutné mít vytvořen svůj uživatelský účet.
Prihlašovací údaje je možné vložit v průběhu, nebo uložit do user_specific_info/user_info.

    class MyCredentials:
        EMAIL = "prihlasovaci@email.neco"
        PASSWORD = 'heslo'
        USERNAME = 'uzivatelske jmeno'

### Technologie 
Python 3.9.
Requirements: selenium, pandas, os, openpyxl

### Struktura EXCELového souboru
Cesta k souboru s položkami (a název listu) je uložena v user_specific_info/user_info.

    class ItemsForUpload:
        XLS_FILE = r'C: ... \nazev_souboru.xlsx'
        XLS_SHEET = 'Sheet1 ci cokoli jineho'
        USER_TEXT = 'TEXTAREA - availability info .'

Vzhledem k tomu, že původně šlo hlavně o deskové hry, tabulka obsahuje informace důležité pro popis deskových her,
ale to lze ve výsledku jednoduše upravit pro jiné kategorie.

Každý řádek tabulky je jedna položka, sloupce obsahují jednotlivé informace o položkách následovně:
(0 odpovídá sloupci A v Excelu):
- 1 (B) - název položky (hry) 
- 2 (C) - pro jaký věk
- 3 (D) - pro kolik hráčů
- 4 (E) - hrací doba 
- 6 (G) - typ
- 11 (L) - záloha
- 12 (M) - obsah balení
- 13 (N) - odkaz 
- 14 (O) - obecně o hře 
- 15 (P) - pravidla 
- 16 (Q) - komentář
- 18 (S) - cena půjčovného na týden 
- 19 (T) - název hlavní kategorie
- 20 (U)- název podkategorie 
