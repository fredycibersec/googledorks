#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-

# imports
from googlesearch import search

# Banner

print("   ___                _     ___          _    ")  
print("  / __|___  ___  __ _| |___|   \ ___ _ _| |__ ")
print(" | (┌ / _ \/ _ \/ _` | / -_) |) / _ \ '_| / / ")
print("  \___\___/\___/\__, |_\___|___/\___/_| |_\_\ ")
print("                |___/                         ")
print("┌─────────────────────┤ by MasterD Cibersec ├─┐")
print("└─────────────────────────────────────────────┘")
print("")
print("├ Google Hacking Dorks ┤")
print("")

# Escribimos el dominio (target)

site = input("Escribe el dominio: ")

# Dorks

list_dorks = {
        "dir_listing" : "site:"+site+" intitle:index.of",
        "conf_exposed" : "site:"+site+" ext:xml | ext:conf | ext:cnf | ext:ini | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:json | ext:yml",
        "db_exposed" : "site:"+site+" ext:sql | ext:dbf | ext:mdb",
        "log_exposed" : "site:"+site+" ext:log",
        "bk_exposed" : "site:"+site+" ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup",
        "login_page" : "site:"+site+" inurl:login",
        "sql_error" : 'site:'+site+' intext:"sql syntax near" | intext:"syntax error has ocurred"',
        "doc_exposed" : "site:"+site+" ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:xls | ext:txt",
        "php_info" : 'site:'+site+' ext:php intitle:phpinfo "published by the PHP Group"'
        }

print("──────────────────────────────")
print("1· Buscar Directory Listings")
print("2· Buscar exposed conf files")
print("3· Buscar exposed db files")
print("4· Buscar exposed log files")
print("5· Buscar exposed backup files")
print("6· Buscar login pages")
print("7· Buscar sql error pages")
print("8· Buscar exposed doc files")
print("9· Buscar php_info pages")
print("──────────────────────────────")
option = int(input("Introduce una búsqueda (1-9): "))
print("──────────────────────────────")
print("Iniciando búsqueda...")
print("")

dorks = []
for dork in list_dorks.values():
        dorks.append(dork) 
query = dorks[option-1]
my_results_list = []
for i in search(query,        # The query you want to run
                tld = 'es',   # The top level domain
                lang = 'es',  # The language
                num = 10,     # Number of results per page
                start = 0,    # First result to retrieve
                stop = None,  # Last result to retrieve
                pause = 2.0,  # Lapse between HTTP requests
               ):
        my_results_list.append(i)
        print(i)
if my_results_list :
        print("")
        print("Fin de la búsqueda.")        
else:
        print("No se encontraron resultados.")
