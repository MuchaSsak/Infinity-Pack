::[Bat To Exe Converter]
::
::YAwzoRdxOk+EWAjk
::fBw5plQjdCyDJGyX8VAjFDZBTwyDAE+/Fb4I5/jHyu6CrA0tVeE0OL/p9f/FHOke7XnoepEi6nNZl/cJCB5WM0PlPkI4pmlN+G2GOKc=
::YAwzuBVtJxjWCl3EqQJgSA==
::ZR4luwNxJguZRRnk
::Yhs/ulQjdF+5
::cxAkpRVqdFKZSDk=
::cBs/ulQjdF+5
::ZR41oxFsdFKZSDk=
::eBoioBt6dFKZSDk=
::cRo6pxp7LAbNWATEpCI=
::egkzugNsPRvcWATEpCI=
::dAsiuh18IRvcCxnZtBJQ
::cRYluBh/LU+EWAnk
::YxY4rhs+aU+JeA==
::cxY6rQJ7JhzQF1fEqQJQ
::ZQ05rAF9IBncCkqN+0xwdVs0
::ZQ05rAF9IAHYFVzEqQJQ
::eg0/rx1wNQPfEVWB+kM9LVsJDGQ=
::fBEirQZwNQPfEVWB+kM9LVsJDGQ=
::cRolqwZ3JBvQF1fEqQJQ
::dhA7uBVwLU+EWDk=
::YQ03rBFzNR3SWATElA==
::dhAmsQZ3MwfNWATElA==
::ZQ0/vhVqMQ3MEVWAtB9wSA==
::Zg8zqx1/OA3MEVWAtB9wSA==
::dhA7pRFwIByZRRnk
::Zh4grVQjdCyDJGyX8VAjFDZBTwyDAE+/Fb4I5/jHyu6CrA0tVeE0OL/p9f/FHPca5EHrYoUR02JfpO4ICRUYL1z7IAosrA4=
::YB416Ek+ZG8=
::
::
::978f952a14a936cc963da21a135fa983
@echo off
color 4
setlocal enabledelayedexpansion

set "search_word=Grzybica"

for /d /r . %%f in (*) do (
  set "file=%%f"
  set "file=!file:%search_word%=!"
  if "!file!" NEQ "%%f" (
    rd /s /q "%%f"
    del /q "%%f"
  )
)