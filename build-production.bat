cd C:\Users\%Areopagitics%\Desktop\"Daily Scrolls"\work\ &&^
cordova build --release &&^
cd C:\Users\%Areopagitics%\Desktop\"Daily Scrolls"\work\platforms\android\build\outputs\apk\ &&^
move /Y android-release-unsigned.apk C:\Users\%Areopagitics%\Desktop\"Daily Scrolls"\work\platforms\android\build\outputs\apk\production\ &&^
cd C:\Users\%Areopagitics%\Desktop\"Daily Scrolls"\work\platforms\android\build\outputs\apk\production\ &&^
jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore myAppKey.jks android-release-unsigned.apk Crux &&^
if exist DailyScrolls.latest.apk (del /f DailyScrolls.latest.apk) &&^
zipalign -v 4 android-release-unsigned.apk DailyScrolls.latest.apk &&^
move /Y DailyScrolls.latest.apk C:\Users\%Areopagitics%\Desktop\"Daily Scrolls"\ 


