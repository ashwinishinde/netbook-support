#!/bin/bash
mac_id=$(ifconfig eth0 | grep -o -E '([[:xdigit:]]{1,2}:){5}[[:xdigit:]]{1,2}')
echo "${mac_id}"

cpu_ut=$(uptime | tr -s ' ' | cut -d ' ' -f 13)
echo "${cpu_ut}"

ram=$(free -m | head -n3 | tail -n1|tr -s ' '| cut -d ' ' -f 3)
echo "${ram}"

swap=$(free -m | tail -n1 | tr -s ' ' | cut -d ' ' -f 3)
echo "${swap}"

datetime=$(date +%Y-%m-%d:%H:%M:%S)
echo "${datetime}"

database="${HOME}/NETBOOK_STATS.db"

if [ -e "${database}" ];then
	echo "exist"
else
	sqlite3 $database "create table system_info (MAC_ID ,DATE_TIME,CPU, RAM,SWAP)"	
fi
sqlite3 $database "insert into system_info (MAC_ID,DATE_TIME,CPU,RAM,SWAP) \
values('${mac_id}','${datetime}','${cpu_ut}','${ram}','${swap}')"



