#


csplit -z calcite_I.out /"FINAL OPTIMIZED"/ {*}
# we neglect the xx00 file....
FILES="
xx01
xx02
xx03
"

for i in ${FILES}; do
VOLUME=`grep -A4 "FINAL OPTIMIZED GEOMETRY - DIMENSIONALITY " ${i} | grep "PRIMITIVE CELL" | awk '{print $8}'`
mv ${i} ${VOLUME}.out

done

# Now we pass all these VOLUME.out to the `QHA_steping_stone_qha_outputs.py` program:
