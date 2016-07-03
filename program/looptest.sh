#!/bin/bash
echo "hi"

declare -i counter 
declare -i increment
declare -i counterMain
declare -i incrementMain
counter=1000
increment=50

counterMain=500000
incrementMain=50000

while :
do
	#loop infinity
	if [ $counter -ge 2000 ]; then
		increment=-50 #reverse
	elif [ $counter -le 1000 ]; then
		increment=50 #forward
	fi
	counter+=increment
 	#echo "$counter"
	pigs SERVO 19 $counter
	#sleep 0.5

	if [ $counterMain -ge 800000 ]; then
		incrementMain=-50000 #reverse
	elif [ $counterMain -le 500000 ]; then
		incrementMain=50000 #forward
	fi
	counterMain+=incrementMain
	pigs hp 18 100 $counterMain
	#echo $counterMain
	sleep 0.5
done	


exit 0
