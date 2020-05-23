#!/bin/bash

thedataset=`echo $1 | sed -e 's/[-]/HYPHEN/g'`
thedataset=`echo $thedataset | sed -e 's/\//SLASH/g'`
thedataset=`echo $thedataset | sed -e 's/\_/UNDERSCORE/g'`

therequest=$1
therequest=`echo $therequest | sed -e 's/\///g'`
therequest=`echo $therequest | sed -e 's/-/\_/g'`
therequest=`echo $therequest | sed -e 's/USER//g'`
therequest=`echo $therequest | cut -c1-99`






cp crab_MINIAOD_template_Forthomme.py crab_template_MINIAOD_temp_Forthomme.py

sed -ie "s/THEDATASET/$thedataset/g" crab_template_MINIAOD_temp_Forthomme.py
sed -ie 's/HYPHEN/-/g' crab_template_MINIAOD_temp_Forthomme.py
sed -ie 's/SLASH/\//g' crab_template_MINIAOD_temp_Forthomme.py
sed -ie 's/UNDERSCORE/\_/g' crab_template_MINIAOD_temp_Forthomme.py


sed -ie "s/REQUESTNAME/$therequest/g" crab_template_MINIAOD_temp_Forthomme.py

crab submit crab_template_MINIAOD_temp_Forthomme.py 
rm  crab_template_MINIAOD_temp_Forthomme.py