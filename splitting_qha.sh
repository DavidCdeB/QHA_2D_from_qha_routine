#

# First run this command, which will generate xx* files:
csplit -z  calcite_II_temperat.out  /"FINAL OPTIMIZED"/ {*}
#exit

# Edit the names for the FILES, as the ones that come as a result of:
# grep "EL            :" xx*

FILES="
xx01
xx02
xx03
xx04
xx05
"

for i in ${FILES}; do
VOLUME=`grep -A4 "FINAL OPTIMIZED GEOMETRY - DIMENSIONALITY " ${i} | grep "PRIMITIVE CELL" | awk '{print $8}'`
mv ${i} ${VOLUME}_TD.out

done

# Remove the excess of xx* files:
rm -Rf xx*

# Now we pass all these VOLUME_TD.out to the `QHA_steping_stone_qha_outputs.py` program:
