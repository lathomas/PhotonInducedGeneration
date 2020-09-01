#!/bin/bash
#thedataset=$1
#therequestname=$1
thelhename=$1

thelhenamesimple=$1
thelhenamesimple=`echo $thelhenamesimple | sed -e 's/-//g' | sed -e 's/_//g'`



cp crab_LHEGENSIM_Forthomme.py crab_template_temp.py


sed -ie "s/THEREQUESTNAME/$thelhenamesimple/g" crab_template_temp.py
sed -ie "s/LHENAME/$thelhenamesimple/g" crab_template_temp.py


cp MakeLHEGENSIMinonestep_forcrab.py theconfig.py 
sed -ie "s/LHENAME/$thelhename/g" theconfig.py


cp theconfig.py  theconfigbu.py

crab submit crab_template_temp.py 
rm theconfig.py crab_template_temp.py