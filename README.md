# cities2map
A function that converts an input file with data into a map.

## Input file
The input file should look like something like this. See file `staff.txt` for a full example.

```
Name,Position,City,Province,Country
Erin,Staff,Pittsburgh,Pennsylvania,United States
Samantha,Staff,Youngstown,Ohio,United States
Ivan,Staff,Buenos Aires,Buenos Aires,Argentina
```

## Example
```
python3 cities2map.py -f staff.txt -o map.eps -t "CBD World Map" -m 'v' -c 'red'
```

where 

* `-m`/`--marker`
* `-t`/`--title`
* `-c`/`--color`
* `-f`/`--file`
* `-o`/`--output`
