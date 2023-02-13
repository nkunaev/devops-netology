Задание 1.

a=1 \
b=2 \
c=a+b \
d=$a+$b \
e=$(($a+$b))

Переменная	Значение	Обоснование \
c	        a+b	        Баш воспринимает а и b как строки, а непеременные \
d	        1+2	        Баш воспринимает записанные в переменные значения как строки \
e	        ???	        $(()) - указывает интерпритатору, что с находящимися внтури скобок знаениями
                        нужно проводить арифметические операции 

Задание 2.

while ((1==1) \
do \
	curl https://localhost:4757 \
	if (($? != 0)); then \
		date > curl.log \
    elif \
        break \
	fi \
done

Задание 3 и 4.

ip_array=(192.168.0.1 173.194.222.113 87.250.250.242) \
port=80 \
/bin/cat /dev/null > ~/test.log \
status=0 \
while :; do \
        for i in ${ip_array[@]}; do \
                for ((n=0;n<5;n+=1)); do \
                        nc -vz $i $port -w 1 &>> ~/test.log \
                done \
                if (( $? == 1 )); then \
                        echo "$i in unrichiable!" \
                        status=1 \
                        break \
                fi \
        done \
        if (($status==1)); then break; fi \
done 

