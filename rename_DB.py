import os
import json



with open('500_sel_results.json') as json_file:
    json_data = json.load(json_file)
    i = 0
    for clip in json_data['track3_results']:
       print(clip['id'])
       if os.path.isfile('500_sel/'+clip['id']+'.wav'):
           os.rename('500_sel/'+clip['id']+'.wav','500_sel/t3_audio_'+str(i).zfill(5)+'.wav')

       clip['id'] = i
       clip['angle'] = int(clip['angle'])
       i+=1

with open('500_sel_results_t.json', "w") as json_file:
    json.dump(json_data, json_file, indent=4)
    