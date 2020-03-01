import os
import json
import math

REF_JSON = 'GC19_t3/lab_GC19_pseudotrue.json' 
EST_JSON = 'GC19_t3/GC19t3_intflow2020_sim1_10.json'

#REF_JSON = 'GC20_KICT_t3/500_sel_results_t.json' 
#EST_JSON = 'GC20_KICT_t3/500_sel_results_t_GC20_sim1_10.json'
PI = math.pi

with open(REF_JSON) as json_file:
    json_data_ref = json.load(json_file)

with open(EST_JSON) as json_file:
    json_data_est = json.load(json_file)

i = 0
score_final = 0
for clip_ref in json_data_ref['track3_results']:
    clip_est = json_data_est['track3_results'][i]
    #print(clip_ref['id'])

    if (clip_ref['angle'] >= 0 and clip_est['angle'] >= 0) or \
       (clip_ref['angle'] < 0 and clip_est['angle'] < 0):
        score = pow((clip_ref['angle'] - clip_est['angle'])/180.0*PI,2)
    else:
        score = pow(PI,2)

    print(score)
    score_final += score

    i+=1

score_final /= i

print('----Final Score!----')
print(score_final)