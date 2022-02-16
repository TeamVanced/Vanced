echo 'Extracting apks...'
mv stock.apk base.apk
unzip base.apk resources.arsc
unzip dpi.apk -d dpi
echo 'combining resources...'
cd dpi
touch -a -m -t 198101010101.01 .
touch -a -m -t 198101010101.01 ./res
touch -a -m -t 198101010101.01 ./res/*
zip -0X ../base.apk ./res/*
zip -X ../base.apk ./res/*.xml
cd ..
cat ./dpi/resources.arsc >> ./resources.arsc
touch -a -m -t 198101010101.01 resources.arsc
zip -0X base.apk ./resources.arsc