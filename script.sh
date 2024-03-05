#!/bin/bash

while :; do
	echo $(python all_kenya_market_pricelist.py);
#	python kenyan_stocks_info.py;
#	python kenya_market_summary.py;
	#sleep (360*60) for 1 hour
	sleep 21600;
	echo "kenyan_market_stocks_open [SEE PID]";
done


