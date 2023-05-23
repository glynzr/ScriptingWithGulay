#! /bin/bash
cp ./b64.txt ./encoded.txt

for i in {1..50};do
	base64 --decode ./encoded.txt > ./decoded.txt
	mv ./decoded.txt ./encoded.txt
done
cat ./encoded.txt
